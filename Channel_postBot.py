#This code was written by Pycomet
#This program collects post from telegram channel 
#and forwards the messages to the specified whatsapp Group

from telethon import TelegramClient, sync, events
from telethon.tl.types import InputPeerChannel
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import sys


# Input your api details here
api_id = '' # API ID
api_hash = '' # API HASH
phone_number = '' # Phone number


#This part of the code handles opening of Whatsapp on a new Chrome Window
print ("NOTE: Please do not alter anything on the opened chrome window except scanning the QRcode")

driver = webdriver.Chrome('./chromedriver')
driver.get("https://web.whatsapp.com/")
wait = WebDriverWait(driver, 600000000000000000) # Wait time is almost limitless

target = '' # The name of the targeted group on Whatsapp


#This part handles the telethon Connection
client = TelegramClient('Comet01', api_id, api_hash)
client.start()
print ("This program just started! All new posts would be sent to" + target)


chat = InputPeerChannel(channel_id=channel_id, access_hash=channel_access_hash) # Input channel id and access_hash

x_arg = '//span[contains(@title,' + target + ')]'
group_title = wait.until(EC.presence_of_element_located((By.XPATH, x_arg)))
group_title.click()


@client.on(events.NewMessage(chat, incoming=True)) # For every new message posted to the telegram channel
def my_event_handler(event):
    msg = event.message.message
    print(msg) # print the message to console
    message = driver.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')[0] # Message Box
    message.send_keys(str(msg))
    sendbutton = driver.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button')[0] # Send button
    sendbutton.click()

client.add_event_handler(my_event_handler)
client.run_until_disconnected()




