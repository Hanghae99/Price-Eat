import requests
import json
from pymongo import MongoClient
import dbconfig
client = MongoClient(dbconfig.MONGODB_SETTING.values())
db = client.test

url = 'http://apis.data.go.kr/4640000/jeonjurestaurant/v1/getAllList?serviceKey=cvbuiI62JcgVFYZeKhNySkudFpfeTmn%2FbwXZWziaO%2Bov%2BQAPo14nlvnYMLGvr1jpjYUjxDGLSReE7qrIzStnkw%3D%3D&currPage=1&pageSize=100'

response = requests.get(url)

contents = response.text

json_ob = json.loads(contents)

shopList = json_ob['body']['shopList']

for i in shopList:
    name = i['infoList'][0]['name']
    address = i['infoList'][0]['lotAddr']
    food = i['infoList'][0]['menuList']
    dong_name = i['infoList'][0]['lotAddr'].split(" ")[3].split('동')[0] + '동'
    imgs = i['shopImageList']

    for img in imgs:
        img_url = img['path']


    c = []
    d = []
    for a in food:
        c.append(a['name'])
        d.append(a['price'])
        # if a['price'] == '없음':
        #     d.append('')
        # elif a['price'] == '별도표기':
        #     d.append(-1)
        # elif a['price'] == '싯가':
        #     d.append(-1)
        # elif '/' in a['price']:
        #     d.append(-1)
        # elif '추가' in a['price']:
        #     d.append(-1)
        # else:
        #     d.append(a['price'])

        menu = dict(zip(d, c))
    # print(menu)

    # print(menu)
    #
    # g = []
    #
    # for j in menu.items():
    #     g.append(j)
    # print(g)

    doc = {
        'name' : name,
        'address' : address,
        'dong_name' : dong_name,
        'img' : img_url,
        'menu' : menu
    }

    db.test.insert_one(doc)