import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()
browser.get('https://gabrielecirulli.github.io/2048/')
Elementohtml = browser.find_element_by_class_name('grid-container')


for i in range(0, 99):
    direction = random.randint(1, 4)
    if direction == 1:
        Elementohtml.send_keys(Keys.UP)
    elif direction == 2:  
        Elementohtml.send_keys(Keys.RIGHT) 
    elif direction == 3:
        Elementohtml.send_keys(Keys.DOWN) 
    else:
        Elementohtml.send_keys(Keys.LEFT) 
