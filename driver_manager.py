from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import os
import sys

def create_driver():
	options = Options()
	options.add_argument('--headless')
	options.add_argument('--disable-gpu')  # Last I checked this was necessary.
	driver = webdriver.Chrome(chrome_options=options)
	return driver