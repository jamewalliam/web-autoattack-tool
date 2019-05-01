#!/usr/bin/env python
#coding:utf8

import requests
from bs4 import BeautifulSoup
import sys

# config-start
keyword = "inurl:.asp?id="
# config-end

url = "http://www.baidu.com/s?wd=" + keyword
response = requests.get(url)
content = response.content
status_code = response.status_code
soup = BeautifulSoup(content, "html.parser")
links = soup.findAll("a")
for link in links:
    try:
        dstURL = link['href']
        if (dstURL.startswith("http://") or dstURL.startswith("https://")) and dstURL.startswith("http://www.baidu.com/link?url=") :
            result_url = requests.get(dstURL).url
            print result_url
    except Exception as e:
        continue