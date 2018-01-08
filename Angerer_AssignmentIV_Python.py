#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 00:30:20 2018

@author: Momo
"""

#unneccessary comment
#one more of those

import json

with open('precipitation.json') as file:
    precipitation=json.load(file)

#generate guinea pig
precip_sample=precipitation[:20]

#PART 1: Seattle - monthly rain buckets

#extract single station data:

#guinea pig run
precip_sample_cincinnati=[]
for item in precip_sample:
    if item["station"]=="GHCND:USW00093814":
        precip_sample_cincinnati.append(item.values())
print(precip_sample_cincinnati)

#real deal
precip_seattle=[]
for item in precipitation:
    if item["station"]=="GHCND:US1WAKG0038":
        precip_seattle.append(item)

#single month bucket:
precip_seattle_month01=[]
for item in precip_seattle:
    date=item["date"]
    if date[5:7]=="01":
        precip_seattle_month01.append(item["value"])
print(sum(precip_seattle_month01))

#list - monthly buckets:
sum_rainfall=[0,0,0,0,0,0,0,0,0,0,0,0]
for item in precip_seattle:
    rainfall=int(item["value"])
    date=item["date"]
    month=int(date[5:7])
    sum_rainfall[month-1]+=rainfall


       
        
    
   






