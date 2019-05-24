from smart import *
import subprocess
from PIL import Image
from pymsgbox import alert
from time import sleep
from datetime import datetime
dn=lambda :(str(datetime.now().time()).split('.')[0])
import traceback,os,sys
import requests
sys.path.append(r'D:\1.Manoj\4.Study\4.Codes\99.Z\Sel\L4L')
# import zc
# import zrc
import os
from config import *
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from selenium.webdriver.common.by import By
class SessionRemote(webdriver.Remote):
	def start_session(self, desired_capabilities, browser_profile=None):
		self.w3c = True

print(dn())

	
a=r'C:\Windows\Temp\selp.txt'
a=(open(a). read());exec(a)
a=r'C:\Windows\Temp\sel{}.txt'.format(selp)
a=(open(a).read());exec(a)

bes=b.execute_script
bfc=b.find_element_by_css_selector
bfcs=b.find_elements_by_css_selector
bfx=b.find_element_by_xpath
bfxs=b.find_elements_by_xpath



def sp(r):
	try:
		return subprocess.check_output(r,shell=True)
	except Exception as e:
		print(e)
def mem(s=0):
	a=subprocess.Popen('typeperf  "\Memory\Available Bytes" -sc 1',shell=True,stdout=subprocess.PIPE)
	a=(float(a.stdout.readlines()[2].split(b'"')[-2]))
	a=(int((1-a/1024**3/3.86)*100));
	k=a>90
	if (k):sleep(60)
	return a if s else k

print('Fid',fid)
print('Selp',selp)


def kill(a=1):
	print(mem(1))
	q='taskkill -pid %s /f'%(fid,)
	print(sp(q))
	if a:alert2('Terminator')

tidma=496153443
tidme=369189676

def alert2(x,e=1,a=-1,tg=1):
	global flag;flag=1;
	print(x)
	if x=='Bonus':
		for i in range(2):
			try:
				captcha();start(ci,0);k=0;return
			except Exception as ex:
				print(ex)
				traceback.print_exc()
				sleep(2)
	if x.startswith('Slow'):kill();return
	if x=='Terminator':
		sleep(60)
		print('Terminated')
		alert2('Terminated')
		print(dn())
		# subprocess.Popen(r'D:\1.Manoj\2.Soft-war\2.Batch-files\sel.bat {} '.format(selp),)#creationflags=8)
		sleep(2)
		# exit()
	if x=='Total Finish':
		kill(0),
		alert2('Terminated2')
		s=[1,3]
		# subprocess.Popen(r'D:\1.Manoj\2.Soft-war\2.Batch-files\sel.bat {} '.format(s[(selp)<2]),creationflags=8)
		sleep(2)
		# exit()
	if tg:z=stg(x)
	if a:alert(x+' '+dn(),timeout=a*1000 if a!=-1 else None)
	if e:exit()

def stm():
	try:
		b.switch_to.window(b.window_handles[0])
		b.switch_to.default_content()
	except  SessionNotCreatedException as e:
		print(e);exit()



def captcha():
	ack()
	sleep(2)
	bes("$('#result')[0].style.backgroundColor='#000'")
	for i in range(3):
		if bes('var elem = document.querySelector("#result img"); return elem && elem.complete && typeof elem.naturalWidth != "undefined" && elem.naturalWidth > 0'):break
		print('Loading')
	im='zc.png'
	b.save_screenshot(im)
	im = Image.open(im)
	x,y=83.5,336.60000610351562
	# x,y=8,8.75
	im=im.crop((x,y,x+460,y+94))
	im.save('zc2.png')
	v=zc.cp(im)
	print('cp',v)
	# bes('counter=0')
	bes(bfcs('area')[v[0]-1].get_attribute('onclick'))
	# b.switch_to_defauslt_content()
	sleep(2)
	# m=bfc('#earnwebsitecaptcha').text
	# if not 'error' in m:b.close()
	m=bfcs('.red')[0].text
	print('won',m)


def ack():
	try:
		pass
		v='message_clicked_on_dnevni_bonusi_'
		z=bfcs(f'#{v}')
		if z:bes(f"document.querySelector('#{v} [type=submit]').click()");print('acked');sleep(5)
		v='message_clicked_on_antibot'
		z=bfcs(f'#{v}')
		if z:bes(f"document.querySelector('#{v} [type=submit]').click()");print('acked');sleep(5)
	except Exception as e:
		alert2(str(e),e=0)
def login():
	er=None
	for i in range(3):
		try:
			stm()
			try:
				if  bfc("#earned-credits"):return
			except Exception as e:
				pass
			u='https://www.like4like.org/login/'
			if u not in b.current_url:b.get(u);sleep(2)
			bes("document.querySelector('#username').value='{}'".format(ulogin[selp-1]))
			bes(f"document.querySelector('#password').value='{pwd}'")
			if not len(bfcs('#g-recaptcha_text.hidden')): zrc.rebreakcaptcha(b).solve(1);b.switch_to.default_content();sleep(2)
			bes("LoginFunctions()")
			sleep(3)
			z=bfc('#h1')
			if z.text!='Login':alert2(z.text)
			for i in range(3):
				try:
					WebDriverWait(b, delay+5).until(EC.presence_of_element_located((By.CSS_SELECTOR,'#earned-credits')))
				except (NoSuchElementException,TimeoutException) as e:
					print ("ecredits@l",e,"e")
					traceback.print_exc()
					sleep(3)
			print('Logged In')
			ack()
			break
		except Exception as e:
			print(e)
			traceback.print_exc()
			er=str(e)
	else:alert2(er)

def bot():
	sleep(3)
	for i in range(3):
		try:
			a=b.execute_script("return document.querySelector('#task-style').innerHTML")
			if not a :return
			ii=0
			for i in a.split('.profile_view_img_'):
				if 'antibot-' in i:
					z=i.split()[0]
					ii+=1
					bes("$('[class$=profile_view_img_{}]').parent().remove()".format(z))
					print('Total Bot ',ii)
			break
		except (AttributeError,JavascriptException) as e:
			a=bcheck();
			if not a:traceback.print_exc()
			sleep(5)

def report():
	try:
		bes("$('table [class=cursor]').remove()")
	except JavascriptException as e:
		bcheck()

def bcheck():
	c='bonus-page' in b.current_url
	if c:alert2('Bonus');
	return c
k2=0
def load(k=None,g=None,cnt=None):
	global k2
	if cnt and k==k2:print(k,k2);
	# alert2('Banner {}  {}'.format(k,lolok[g]),a=2,e=0,tg=None);
	lolo[lolok[g]]='';
	start((g+1)%len(lolo));
	return
	k2=k
	for i in range(5):
		try:
			bfc('#load-more-links').click()
			break
		except NoSuchElementException as e:
			b.switch_to.window(b.window_handles[0])
			b.refresh()
		except ElementNotInteractableException as e:
			print("wait for load-more-link")
			sleep(1)
	try:
		WebDriverWait(b, delay).until(EC.invisibility_of_element_located((By.CSS_SELECTOR,"[src='https://www.like4like.org/img/loading/loading-blue-square.gif']")))
	except (KeyError,NoSuchElementException,TimeoutException) as e:
			print ("Loading link")
			sleep(1)
	except Exception as e:
		print(e)

	sleep(3) #boting
	bcheck()
	bot()
	report()
	z=bfcs('[id^=task] a')
	return z,len(z)


def start(iki,uz=1):
	global flag,ld,z,ci,k2,tfc,cc
	ci=iki
	if uz and iki==zozs:
		tfc+=1
		print('-'*50)
		if tfc==2:print(len(lolo));alert2('Total Finish')
	rz=lolok[iki]
	cr=lolo.get(rz)
	if not cr:
		start((iki+1)%len(lolo));return
	print('@'*50)
	print(rz)
	flag=0
	ack()
	if cr not in b.current_url:
		b.get(cr);sleep(2)
	# start2();return
	bot()
	while 1:
		try:


			for i in b.window_handles[2:]:
				b.switch_to.window(i)
				b.close()
			b.switch_to.window(b.window_handles[0])
			if z:
				try:
					WebDriverWait(b, delay).until(EC.presence_of_element_located((By.CSS_SELECTOR,'[src="https://www.like4like.org/img/icon/report-a-problem.png"]')))
				except (NoSuchElementException,TimeoutException) as e:
					print ("loading took too much time!-try again l4l")
					if mem():alert2("Slow l4l")
					sleep(1)
			for i in range(3):
				try:
					WebDriverWait(b, delay).until(EC.presence_of_element_located((By.CSS_SELECTOR,'#earned-credits')))
				except (NoSuchElementException,TimeoutException) as e:
					print ("ecredits",e,"e")
					traceback.print_exc()
					sleep(3)
					login()
			ec=bes("return document.querySelector('#earned-credits').innerHTML")
			print('^',ec)
			report()
			z=bfcs('[id^=task] a')
			if len(z)<2:
				z,cc=load(ec,iki,cc)
				if not z or len(z)<2:
					alert2('Task Finished {}'.format(lolok[iki]),a=0,e=0,tg=0)
					k2=0
					start((iki+1)%len(lolo))
					return
			a=z[1].click()
			b.switch_to.window(b.window_handles[-1])

			for i in range(3):
				try:
					if rz.startswith('fb'):
						WebDriverWait(b, delay).until(EC.presence_of_element_located((By.ID,'header')))
					elif rz.startswith('yt'):
						WebDriverWait(b, delay).until(EC.presence_of_element_located((By.ID,'header')))
					elif rz.startswith('tw'):
						WebDriverWait(b, delay).until(EC.presence_of_element_located((By.XPATH,'//div[starts-with(.,"Follow")]')))
					else:
						sleep(1)
					break
				except (NoSuchElementException,TimeoutException) as e:
					print ("loading took too much time!-try again {}".format(lolok[iki]))
					if mem():alert2("Slow {}".format(lolok[iki]))

					sleep(1)
			for i in range(1):
				try:
					if rz=='fb_follow':
						s=bfxs('//a[text()="Follow"]/..')
						if not s:s=bfxs('//span[text()="Follow"]/..')
						s=s[0]
					elif rz=='fb_like':
						try:
							s=bfx('//span[text()="Like"]/..')
						except Exception as e:
							s=bfx('//span/button[text()="Like"]/..')
					elif rz=='yt_sub': s=bfx('//paper-button')
					elif rz=='yt_like': s=bfc('#top-level-buttons a')
					elif rz=='tw_follow':s=bfxs('//div[text()="Follow"]/..');s=s[0]
					elif rz=='ins_follow':s=bfx('//button[text()="Follow"]/..')
					elif rz=='gp_shr':s=bfx('//button[text()="Follow"]/..')
					if s:s.click()
					if rz.startswith('ins'):sleep(1)
					print('Click',end=' ')
					break
				except Exception as e:
					# print('159 ',e)
					sleep(1)


			sleep(2)
			if 'like4like.org' not in b.current_url: b.close()
		except NoSuchWindowException as e:
			b.switch_to.window(b.window_handles[0])
			b.refresh()
			print('nsw')
			traceback.print_exc()
		except SessionNotCreatedException as e:
			print(e)
			exit()
		except Exception as e:
			traceback.print_exc()
			print('-'*50)
			alert2(str(e),e=0)
			print(iki)



def start2():
	s=1
	if s:
		z=bfcs('.bluish')
		if len(z):
			z[0].click()
			bfcs('.earn-website-target')[0].click()
			bes("$('.bluish')[0].remove()")
			s=0
		else:bes('proveri2()')

	if not s:
		b.switch_to.window(b.window_handles[-1])
		sleep(18)
		b.switch_to_default_content()
		v=bfc('#earnwebsitecaptcha iframe')
		b.switch_to_frame(v)
		captcha()
lolo={
'fb_follow'		:'https://www.like4like.org/user/earn-facebook-subscribes.php',	
'fb_like'		:'https://www.like4like.org/free-facebook-likes.php'	,
'tw_follow'		:'https://www.like4like.org/free-twitter-followers.php',
# 'yt_sub'		:'https://www.like4like.org/user/earn-youtube-subscribe.php',
# 'yt_like'		:'https://www.like4like.org/user/earn-youtube.php',
# 'ins_follow'	:'https://www.like4like.org/free-instagram-followers-likes-and-comments-exchange.php',
# 'gp_shr'		:'https://www.like4like.org/user/earn-google.php',
# 'site'		:'http://www.like4like.org/user/earn-sites.php',
}
lolok=list(lolo.keys())
try:
	stm()
except Exception as e:
	print(e)
	exit()
if selp==1:
	# lolo[lolok[3]]=''
	pass
elif selp==2:
	# alert2('Total Finish')
	# lolo[lolok[1]]=''
	pass
elif selp==3:
	# lolo[lolok[1]]=''
	pass

delay=5;
login()
cc=ci=flag=z=None
tfc=0

if __name__ == '__main__':
	zozs=0

	# captcha()
	start(zozs,0)

alert2('Finished')


