from values import Default


# default headers
default_headers = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
}

#params for facebook api url
params = {
	'q': Default.product_name,
	'session_id': 'ef7226b9-2210-4429-80f2-97230b4ad56e',
	'count': '100',
	'active_status': 'active',
	'ad_type': 'all',
	'countries[0]': 'IN',
	'start_date[min]': Default.min_date,
	'start_date[max]': Default.max_date,
	'media_type': 'all',
	'content_languages[0]': 'en',
	'sort_data[direction]': 'desc',
	'sort_data[mode]': 'relevancy_monthly_grouped',
	'search_type': 'keyword_unordered'
}


# form_data for facebook api url
data = {
	'__user': '100092591290023',
	'__a': '1',
	'__req': '4l',
	'__hs': '19488.BP:DEFAULT.2.0..0.0',
	'dpr': '1',
	'__ccg': 'EXCELLENT',
	'__rev': '1007472581',
	'__s': 'j6ewa4:qykzqz:05u0xv',
	'__hsi': '7231767180787420212',
	'__dyn': '7xeUmxa3-Q8zo5ObwKBWobVo9E4a2i5U4e1FxebzEdF8aUuxa1ZzES2S2q0_EtxG4o3Bw5VCyU4a0OE2WxO2O1Vwooa8465o-cw5Mx62G3i1ywa-2l0Fwwwi831wnFokwyx2cU2czXwrUcUjwVw9O79UbobEaUtws8nwhE2Lxiaw4JwJwSyES0gq0K-1bwzwqobU5G361pwr8',
	'__csr': '',
	'fb_dtsg': Default.generate_token(),
	'jazoest': '25256',
	'lsd': 'FqKqxi_SihZp4Mzq2uJuV6',
	'__spin_r': '1007472581',
	'__spin_b': 'trunk',
	'__spin_t': '1683777007',
	'__jssesw': '1'
}


#headers for facebook api url
headers={
	'Cookie': 'datr=hM74Y_9MCndDkhCrgfODlLjG; sb=u_U3ZOa0Z-1AdFEIWDIaVFdH; locale=en_GB; c_user=100092591290023; xs=40%3A9-gZ7hijTnzDzw%3A2%3A1683702505%3A-1%3A-1%3A%3AAcVdzIrv89i_bL2T8oXYZ-vHWJxPEW1Q6A_J05q9Nw; fr=0GaayUSSSZyp7VoSU.AWXSWAK8ZHljQ6CH7zzf6yQ3nCk.BkW5xg.uz.AAA.0.0.BkW5xg.AWW3BjBa7AQ; wd=660x1007',
	'Sec-Ch-Ua-Full-Version-List': '"Google Chrome";v="113.0.5672.93", "Chromium";v="113.0.5672.93", "Not-A.Brand";v="24.0.0.0"',
	'Sec-Ch-Ua-Mobile': '?0',
	'Sec-Ch-Ua-Platform': '"Windows"',
	'Sec-Ch-Ua-Platform-Version': '"10.0.0"',
	'Sec-Fetch-Dest': 'empty',
	'Sec-Fetch-Mode': 'cors',
	'Sec-Fetch-Site': 'same-origin',
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
	'Viewport-Width': '660',
	'X-Asbd-Id': '198387',
	'X-Fb-Lsd': 'FqKqxi_SihZp4Mzq2uJuV6'
}