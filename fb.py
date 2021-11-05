# -*- coding: utf-8 -*-
import requests, re, os, time

banner=(
"""  \x1b[1;92m github : github.com/xerafero\n   \x1b[1;96m______     ______     __          
  / __/ /    /_  __/__  / /_____ ___ 
 / _// _ \    / / / _ \/  '_/ -_) _ \\
/_/ /_.__/   /_/  \___/_/\_\\__/_//_/\x1b[1;93m  python2 & python3
                                     """)

def main():
	os.system(
		'clear'
	)
	print (
		banner
	)
	try:
		_cookie=raw_input(
			'\x1b[1;93m(+) cookie :\x1b[1;92m '
		)
	except:
		_cookie=input(
			'\x1b[1;93m(+) cookie :\x1b[1;92m '
		)
	head={
		'Host':'business.facebook.com',
			'cache-control':'max-age=0',
		'upgrade-insecure-requests':'1',
			'user-agent':'Mozilla/5.0 (Linux; Android 6.0.1; Redmi 4A Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.92 Mobile Safari/537.36',
		'accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
			'content-type' : 'text/html; charset=utf-8',
		'accept-encoding':'gzip, deflate',
			'accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
		'cookie': _cookie
	}
	try:
		_r=requests.get("https://business.facebook.com/creatorstudio/home", headers=head)
		_p=re.search(
			'{"accessToken":"(EAA\w+)', _r.text
		)
		_h=_p.group(
			1
		)
		if 'EAA' in _h:
			exit(
				'\x1b[1;93m(+) Token :\x1b[1;92m '+_h
			)
	except AttributeError:
		print(
			'\x1b[1;91m(×) cookie salah !'
		)
		time.sleep(
			3
		),main(
		)
	
main()
