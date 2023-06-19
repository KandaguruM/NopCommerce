import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time



site = "https://demo.nopcommerce.com/"



def setup():
    driver = webdriver.Chrome()
    return driver


