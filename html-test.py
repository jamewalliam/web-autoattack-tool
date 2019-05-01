#!/usr/bin/env python
#coding:utf8

file = open("urls.txt","r")
for line in file:
    content = line[0:-1]
    if content.endswith("html"):
        continue
    if content.endswith("htm"):
        continue
    if ".php" in content or ".asp" in content:
        print content