import requests	
from pymsgbox import alert
from bs4 import BeautifulSoup
from config import *
headers={'User=Agent':'Mozilla/5.0'}
from datetime import datetime
from time import sleep

q='https://www.like4like.org/api/login.php'
q2='https://www.like4like.org/api/get-user-info.php'
q3='https://www.like4like.org/user/weekly-bonus.php'
CW=1
if CW:print('Name Credits Pos')
ins=0
if 	True:
	print('-'*50)
	ins+=1
	print(str(datetime.now().time())[:8])
	for u in [0,1,2]:
		u=ulogin[u]
		s=requests.Session()
		s.headers.update(headers)
		data={
		'?':	'',
		'password':	pwd,
		'recaptcha':	'',
		'username':	u,
		}
		r=s.post(q,data=data)
		if CW:
			r=s.get(q2,headers=headers)
			rd=r.json()['data']
			print(u,rd.get('credits','Rubs'),rd.get('weeklyPosition','Rubs'))
			# if rd.get('credits'):requests.get('https://bit.ly/myBOTi2')
		else:
			r=s.get(q3,headers=headers)
			print(r.text,file=open('z','w'))
			s=BeautifulSoup(r.text,'lxml')
			print(u)
			for i in (s.select('.rounded-corners.width-300.f-right tr')[-2:]):
				for j in (i.select('td')[2::2]):
					print((j.text).replace('\xa0',' '),end=' ')
				print()
	# sleep(5*60)
alert(3,timeout=5000)