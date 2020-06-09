# -*- coding: UTF-8 -*-
import json
import requests
import csv
import math

genrePoi = "公园"
region = "武昌区"
AKkey = 
pageNum = 0
url = "http://api.map.baidu.com/place/v2/search?query={}&region={}&output=json&ak={}&page_size=20&page_num={}".format(genrePoi,region,AKkey,pageNum)
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
    }
response = requests.get(url, timeout = 10, headers = headers)
itemNum = json.loads(response.text)["total"]    #获取项目个数
pageNum = math.ceil(itemNum/20)     #获取网站页数
path = "E:/code/python/poi_test" + '/{}.csv'.format(region+"_"+genrePoi)

#输出poi到csv文件
with open(path, "w+", newline= "") as csvFile:#创建csv文件
    writer = csv.writer(csvFile)
    head = ["名称","纬度","经度","地址","省份","城市","区县"]
    writer.writerow(head)   #写入表头
    for i in range(pageNum):
        newUrl = "http://api.map.baidu.com/place/v2/search?query={}&region={}&output=json&ak={}&page_size=20&page_num={}".format(genrePoi,region,AKkey,i)
        newResponse = requests.get(newUrl, timeout = 10, headers = headers)
        results = json.loads(newResponse.text)["results"]
        for r in results:
            name = r["name"]            #获取poi相关信息
            lat = r["location"]["lat"]
            lng = r["location"]["lng"]
            address = r["address"]
            province = r["province"]
            city = r["city"]
            area = r["area"]
            writer.writerow([name, lat, lng, address, province, city, area])    #把poi信息写入表每一行



