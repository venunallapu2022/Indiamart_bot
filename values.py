import requests
import re
from datetime import datetime

class Default():
	# Enter the Product name we want 
	product_name = 'Furniture'

	# facebook ad library api
	url='https://www.facebook.com/ads/library/async/search_ads/'


	# Enter the min_date we need to see 
	min_date =  '2023-05-18' #yyyy-mm-dd

	# exclude these images from collection
	exclude = ['svg','gif','logo','facebook','whatsapp','demo','icon','data']

	# Enter the max_date we need to see 
	max_date =  '2023-05-18' #yyyy-mm-dd

	# email to share the output sheet
	email = 'varvic13@gmail.com'

	# timestamp to get execution time
	time_now = datetime.now().strftime('%y-%m-%d-%H-%M-%S')

	#to generate facebook token
	def generate_token():
		# url for generating token url
		token_url='https://www.facebook.com/ads/library/'
		#params for token url
		params = {
			'active_status': 'all',
			'ad_type': 'all',
			'country': 'IN',
			'q': 'Learning%20toy',
			'search_type': 'keyword_unordered',
			'media_type': 'all'
		}
		# headers for token url
		headers = {
			'Cookie': 'datr=hM74Y_9MCndDkhCrgfODlLjG; sb=u_U3ZOa0Z-1AdFEIWDIaVFdH; locale=en_GB; c_user=100092591290023; xs=40%3A9-gZ7hijTnzDzw%3A2%3A1683702505%3A-1%3A-1%3A%3AAcXi766Qw8HaHXLi1nGy44X_vief_nZKCZZhmG8DBQ; fr=0Eum7uDafvD6HBoCe.AWVVRNkpIKhzdbMe1EGjg1Iz4_g.BkXGXF.uz.AAA.0.0.BkXGXF.AWXpiWQApus; dpr=0.75; usida=eyJ2ZXIiOjEsImlkIjoiQXJ1b3FrbzE5d3N5MnYiLCJ0aW1lIjoxNjg0MTI5NDE2fQ%3D%3D; wd=1030x1342',
			'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
		}
		response = requests.get(token_url,params=params,headers=headers)
		fb_token = re.findall('"token":"(.*?)"\}',response.text)[0]
		return fb_token