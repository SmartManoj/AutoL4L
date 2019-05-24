from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from time import sleep
from pymsgbox import *
import traceback
import requests
import io
import random
import time
import os
import sys
from functools import reduce
# Speech Recognition Imports
from pydub import AudioSegment
import speech_recognition as sr

# Selenium
from selenium.common.exceptions import NoSuchElementException




# Randomization Related
MIN_RAND        = 0.64
MAX_RAND        = 1.27
LONG_MIN_RAND   = 4.78
LONG_MAX_RAND   = 6.1
NUMBER_OF_ITERATIONS = 5
RECAPTCHA_PAGE_URL = "https://www.google.com/recaptcha/api2/demo"

HOUNDIFY_CLIENT_ID = "IzKsCJiiW8nSTZHdTFg0PA=="
HOUNDIFY_CLIENT_KEY = "zLdwMYSaHud27N_V4Y7m_I78sM90ftEVy0p3A041dIkF-kJ8rp1hQJ-sPLPZu5svzPS8SG1LNXCO2rzsPoTItA=="
WIT_AI_KEY="JI5SZWSOEPZQRIZVUDDXNQ7TRYNKYQKS"


DIGITS_DICT = {
				"zero": "0",
				"one": "1",
				"two": "2",
				"three": "3",
				"four": "4",
				"five": "5",
				"six": "6",
				"seven": "7",
				"eight": "8",
				"nine": "9",
				"to": "2",
				"for": "4",
				"sex": "6",
				}

class rebreakcaptcha(object):
	def __init__(self,b):
		self.driver = b
		
	def is_exists_by_xpath(self, xpath):
		try:
			self.driver.find_element_by_xpath(xpath)
		except NoSuchElementException:
			return False
		return True
		
	def get_recaptcha_challenge(self):
		for _ in range(10):
			self.driver.switch_to.default_content()
			# self.b.get(RECAPTCHA_PAGE_URL)
			# Navigate to a ReCaptcha page
			# time.sleep(random.uniform(MIN_RAND, MAX_RAND))
			
			# Get all the iframes on the page
			iframes = self.driver.find_elements_by_css_selector("iframe[src^='https://www.google.com/recaptcha/api2/anchor']")
			# Switch focus to ReCaptcha iframe
			self.driver.switch_to_frame(iframes[0])
			# time.sleep(random.uniform(MIN_RAND, MAX_RAND))
			
			# Verify ReCaptcha checkbox is present
			if not self.is_exists_by_xpath('//div[@class="recaptcha-checkbox-checkmark" and @role="presentation"]'):
				print("[{0}] No element in the frame!!".format(self.current_iteration))
				continue
			
			# Click on ReCaptcha checkbox
			self.driver.find_element_by_xpath('//div[@class="recaptcha-checkbox-checkmark" and @role="presentation"]').click()
			sleep(3)
			# time.sleep(random.uniform(LONG_MIN_RAND, LONG_MAX_RAND))		
			# Check if the ReCaptcha has no challenge
			if self.is_exists_by_xpath('//span[@aria-checked="true"]'):
				print("[{0}] ReCaptcha has no challenge.".format(self.current_iteration))
				return False
			else:
				return True
			
	def get_audio_challenge(self, iframes):
		# Switch to the last iframe (the new one)
		self.driver.switch_to_frame(iframes[-1])
		
		# Check if the audio challenge button is present
		if not self.is_exists_by_xpath('//button[@id="recaptcha-audio-button"]'):
			print("[{0}] No element of audio challenge!!".format(self.current_iteration))
			return False
		if not self.is_exists_by_xpath('//button[@id="recaptcha-audio-button"][@style="display: none;"]'):
			print("[{0}] Clicking on audio challenge".format(self.current_iteration))
			# Click on the audio challenge button
			self.driver.find_element_by_xpath('//button[@id="recaptcha-audio-button"]').click()
			# time.sleep(random.uniform(LONG_MIN_RAND, LONG_MAX_RAND))
			sleep(3)
		else:
			print('Already opened')
	
	def get_challenge_audio(self, url):
		request = requests.get(url,headers={'User-Agent':'Mozilla/5.0'})
		audio_file = io.BytesIO(request.content)
		
		# Convert the audio to a compatible format in memory
		converted_audio = io.BytesIO()
		sound = AudioSegment.from_mp3(audio_file)
		sound.export(converted_audio, format="wav")
		converted_audio.seek(0)
		
		return converted_audio
		
		
	def string_to_digits(self, recognized_string):
		print (''.join([DIGITS_DICT.get(word, "|{}|".format(word)) for word in recognized_string.split(" ")]))
		return ''.join([DIGITS_DICT.get(word, "") for word in recognized_string.split(" ")])
	
	def speech_to_text(self, audio_source):
		# Initialize a new recognizer with the audio in memory as source
		recognizer = sr.Recognizer()
		with sr.AudioFile(audio_source) as source:
			audio = recognizer.record(source) # read the entire audio file

		audio_output = ""
		# recognize speech using Google Speech Recognition
		try:
			audio_output = recognizer.recognize_google(audio)
			print("[{0}] Google Speech Recognition: ".format(self.current_iteration) + audio_output)
			if any(character.isalpha() for character in audio_output):audio_output = ""
				
		except sr.UnknownValueError as e:
			print("[{0}] Google Speech Recognition could not understand audio".format(self.current_iteration))
			audio_output = ""

		except sr.RequestError as e:
			print("[{0}] Could not request results from Google Speech Recognition service; {1}".format(self.current_iteration).format(e))
			audio_output = ""
		try:
			if audio_output=='':
				print("[{0}] Fallback to Houndify!".format(self.current_iteration))
				if _ :
					audio_output = self.string_to_digits(recognizer.recognize_houndify(audio, client_id=HOUNDIFY_CLIENT_ID, client_key=HOUNDIFY_CLIENT_KEY))
				else:
					print('Witty')
					audio_output = self.string_to_digits(recognizer.recognize_wit(audio, key=WIT_AI_KEY))
				print("[{0}] Houndify: ".format(self.current_iteration) + audio_output)
		except sr.UnknownValueError:
			print("Houndify could not understand audio")
		except sr.RequestError as e:
			print("Could not request results from Houndify service; {0}".format(e))			

		return audio_output

	def solve_audio_challenge(self):
		# Verify audio challenge download button is present
		if not self.is_exists_by_xpath('//a[@class="rc-audiochallenge-tdownload-link"]') and \
				not self.is_exists_by_xpath('//div[@class="rc-text-challenge"]'):
			print("[{0}] No element in audio challenge download link!!".format(self.current_iteration))
			return False
		

		# If text challenge - reload the challenge
		for i in range(5):
			if not self.is_exists_by_xpath('//div[@class="rc-text-challenge"]'):break
			print("[{0}] Got a text challenge! Reloading!".format(self.current_iteration))

			self.driver.find_element_by_id('recaptcha-reload-button').click()
			# time.sleep(random.uniform(MIN_RAND, MAX_RAND))
			sleep(1)

		for i in range(3):
			try:
				# Download the 
				# Get the audio challenge URI from the download link
				print('Gotcha')
				download_object = self.driver.find_element_by_xpath('//a[@class="rc-audiochallenge-tdownload-link"]')
				download_link = download_object.get_attribute('href')
				
				# Get the challenge audio to send to Google
				converted_audio = self.get_challenge_audio(download_link)
				audio_output = self.speech_to_text(converted_audio)
				if not audio_output:raise
				break
			except:
				self.driver.find_element_by_id('recaptcha-reload-button').click()
				# time.sleep(random.uniform(MIN_RAND, MAX_RAND))
				audio_output=''
				sleep(2)
			
		# Send the audio to Google Speech Recognition API and get the output
		

		# Enter the audio challenge solution
		self.driver.find_element_by_id('audio-response').send_keys(audio_output)
		# time.sleep(random.uniform(LONG_MIN_RAND, LONG_MAX_RAND))
		time.sleep(random.uniform(MIN_RAND, MAX_RAND))

		# Click on verify
		self.driver.find_element_by_id('recaptcha-verify-button').click()
		# time.sleep(random.uniform(LONG_MIN_RAND, LONG_MAX_RAND))
		time.sleep(random.uniform(MIN_RAND, MAX_RAND))
		
		return True
			
	def solve(self, current_iteration):
		self.current_iteration = current_iteration + 1
		
		# Get a ReCaptcha Challenge
		if not self.get_recaptcha_challenge():return True
		
		# Switch to page's main frame
		self.driver.switch_to.default_content()
				
		# Get all the iframes on the page again- there is a new one with a challenge
		iframes = self.driver.find_elements_by_css_selector("iframe[title^='recaptcha']")
		
		# Get audio challenge
		self.get_audio_challenge(iframes)
		# Solve the audio challenge
		if not self.solve_audio_challenge():
			return False
		sleep(2)
		
		# Check if there is another audio challenge and solve it too
		for _ in range(10):
			if not (self.is_exists_by_xpath('//div[@class="rc-audiochallenge-error-message"]') and \
				self.is_exists_by_xpath('//div[contains(text(), "Multiple correct solutions required")]') ):break
			print("[{0}] Need to solve more. Let's do this!".format(self.current_iteration))
			self.solve_audio_challenge()
			sleep(2)
			# Switch to the ReCaptcha iframe to verify it is solved
			self.driver.switch_to.default_content()	
			
			self.driver.switch_to_frame(iframes[0])
			
			return self.get_recaptcha_challenge()



		return self.is_exists_by_xpath('//span[@aria-checked="true"]')


