# This program is a voice assistant to be used with Spotify Web Player
# More features coming soon
# Sushruta Shankar, 2020

import speech_recognition as sr # version 3.8.1
import getpass 
from selenium import webdriver
import time

rec = sr.Recognizer()
mic = sr.Microphone()

# get Spotify username and password
username = input("Hello! Please enter your Spotify username: ")
password = getpass.getpass(prompt = "... and password: ", stream = None)


# get request from user via speech input (try tts instead of printing)
with mic as source:
    print("Adjusting for ambient noise...")
    rec.adjust_for_ambient_noise(source)
    print("Okay, say the name of a song you'd like to listen to: ")
    speech_in = rec.listen(source)

song = rec.recognize_google(speech_in)

print("Okay, playing", song)

# open Spotify Web Player
driver = webdriver.Chrome()
driver.get('https://open.spotify.com/')

# log in to Spotify
log_in = driver.find_element_by_xpath('//*[@id="main"]/div/div[2]/div[1]/header/div[4]/button[2]')
log_in.click()
time.sleep(4)

ubox = driver.find_element_by_xpath('//*[@id="login-username"]')
ubox.send_keys(username)
pbox = driver.find_element_by_xpath('//*[@id="login-password"]')
pbox.send_keys(password)

log_in2 = driver.find_element_by_xpath('//*[@id="login-button"]')
log_in2.click()
time.sleep(4)

# paste song into search bar
search_button = driver.find_element_by_xpath('//*[@id="main"]/div/div[2]/div[2]/nav/ul/li[2]/a')
search_button.click()
search_bar = driver.find_element_by_xpath('//*[@id="main"]/div/div[2]/div[1]/header/div[3]/div/div/input')
search_bar.send_keys(song)
time.sleep(4)

# play song
result = driver.find_element_by_xpath('//*[@id="searchPage"]/div/div/section[1]/div/div[2]/div/div/div/div[4]')
result.click()
