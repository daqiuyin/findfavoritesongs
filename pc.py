# -*- coding: utf-8 -*-
from selenium import webdriver
import os
import sys
import csv
from time import sleep
chromedriver = os.path.join(sys.path[0],'chromedriver.exe')
os.environ["webdriver.chrome.driver"] = chromedriver
browser = webdriver.Chrome()
url ="http://music.163.com/#/discover/playlist"

with open(os.path.join(sys.path[0],'playlist.csv'),'w',newline='',encoding='utf-8') as csv_file:
    write = csv.writer(csv_file)
    write.writerow(['标题','播放次数','连接'])
    while url != 'javascript:void(0)':
        browser.get(url)
        sleep(3)
        browser.switch_to.frame("contentFrame")
        data = browser.find_element_by_id("m-pl-container").find_elements_by_tag_name("li")
        for i in range(len(data)):
            nb = data[i].find_element_by_class_name("nb").text
            if '万'in nb and int(nb.split('万')[0])>50:
                msk = data[i].find_element_by_css_selector("a.msk")
                write.writerow([msk.get_attribute('title'),nb,msk.get_attribute('href')])
            url = browser.find_element_by_css_selector('a.zbtn.znxt').get_attribute('href')




# @Time    : 2018/5/14 16:41
# @Auth    : DAQIUYIN
# @File    : pc.py
# @SoftWare: PyCharm Community Edition