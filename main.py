import requests
import re
import gspread
from values import Default
from headers_and_params import *
from bs4 import BeautifulSoup
import time


def update_and_share(dic: dict):
	# count variable for google api limitation
	cnt=0

	# Authorization from google
	gc = gspread.service_account('authorize.json')

	# create a new sheet with product category and current time stamp
	sh = gc.create(f'{Default.product_name}-{Default.time_now}_product_links')
	worksheet = sh.sheet1
	headers = list(dic.keys())

	# updated the headers 
	worksheet.update_cell(1, 1,headers[0])
	worksheet.update_cell(1, 2,headers[1])
	values = list(dic.values())

	# now fill the cells with product links and image links
	for col in range(1,len(values)+1):
		for row in range(2,len(values[col-1])+2):
			cnt+=1
			worksheet.update_cell(row, col,values[col-1][row-2])
			if cnt%55==0:
				time.sleep(60)

	# we share the created sheet with desired email address
	sh.share(Default.email, perm_type='user', role='writer')


def filter_lst(lst: list):

	# we request the facebook ad library api 
	response = requests.post(url=Default.url,params=params,data=data,headers=headers)
	# using regular expression we are getting the required URL
	
	links = re.findall('link_url":"(.*?)"',response.text)
	# now we transform the url in standard form 
	for url in links:
		url = str(url).replace('\\','').strip()
		if (url not in lst) and (url.count('/')>3):
			lst.append(url)
	# we return the result list of links generated
	return lst[:2]


def filter_images_from_link(url: str):
	# this function will generate a list that contains all images from give url
	response = requests.get(url,headers=default_headers)
	# if the url is invalid we return empty list
	if response.status_code!=200:
		return []
	soup = BeautifulSoup(response.text,'lxml')
	images_lst = [x.get('src') for x in soup.find_all('img') if x.get('src')]
	# we exclude all unecessary images mostly belong to this category
	
	new_lst = [url for url in images_lst if not ([x for x in Default.exclude if x in url])]
	# for some image source https is missing so we add them
	filtered_lst = [f'https:{url}' if 'https' not in url else url for url in new_lst]
	# we return result list
	return filtered_lst


def product_image_search(lst: list):
	result=[]
	# go through each url and search for the product images
	for url in lst:
		try:
			new_lst = filter_images_from_link(url)
			if new_lst==[]:
				continue
			result.extend(new_lst)
		except requests.exceptions.InvalidSchema:
			pass
	# return images list of all product links
	return result




if __name__=="__main__":
	products_links = filter_lst([])
	image_lst = product_image_search(products_links)
	updated_sheet = {
		'product_links' : products_links,
		'image_links': image_lst
	}
	update_and_share(updated_sheet)


