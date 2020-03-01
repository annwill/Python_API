import requests
import json
park_msg=""
url='http://api.kcg.gov.tw/api/service/get/897e552a-2887-4f6f-a6ee-709f7fbe0ee3'
r=requests.get(url)
r.recodin='utf-8'
js=json.loads(r.text)
park=js['data'] #抓出所有park的value值

dist=input('請輸入查詢的區域 :')
print('查詢 {} 臨時停車所'.format(dist))
 
for item in park:
    if item['行政區']==dist:
        # print('地點: {}、小型停車位: {}、地址: {}'\
        #     .format(item['臨時停車處所'],item['可提供小型車停車位'],item['地址']))
        park_msg +='地點:'+ item['臨時停車處所'] +'、小型停車位: '+ item['可提供小型車停車位'] +'、地址: '+ item['地址']+'\n'

if park_msg =='':
    park_msg='查無資料'  
 
print( park_msg)
print('查詢結束')      