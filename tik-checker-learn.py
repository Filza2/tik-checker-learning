import re
import requests 
user=input('user : ')
headers={
    'Host': 'livecounts.io',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'ar,en-US;q=0.7,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'Cache-Control': 'max-age=0',
    'Te': 'trailers',
    'Connection': 'close'
}
our_requests=requests.get(f"https://livecounts.io/tiktok-live-follower-counter/{user}",headers=headers)	

title=re.findall('<title>(.*?)</title>',our_requests.text)[0]	

if 'Unexpected Error' in title:
    print(f'Available : {user}  - {title}')

elif "success" not in our_requests.text:
    try:
        re.findall('"success":(.*?),',our_requests.text)[0]
        IN=True#if success in our request user will be unavailable , if success not in our request the user is available and here we check that , with if statement & try : except 
    except:
        IN=False

    print(f'Available : {user} - {IN}')

elif 'true' in re.findall('"success":(.*?),',our_requests.text)[0]:
    print(f'Not Available  : {user} ')			

else:
    print(f'Not Available  : {user} ')	
    
    
    
 #@TweakPY - @vv1ck
