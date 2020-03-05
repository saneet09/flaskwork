from flask import Flask, render_template, request
import json
import os
import sys
import numpy as np 

app = Flask(__name__)

@app.route("/task1")
def task1():
    product_json=[]
    with open("E:/flask/netaporter_gb.json",encoding="utf8") as fp:
        for product in fp.readlines():
            product_json.append(json.loads(product))
    a=52383
    offer=[]
    regular=[]
    arr=[]
    ids=[]
    for i in range(52383):
        offer.append(product_json[i]["price"]["offer_price"]["value"])
        regular.append(product_json[i]["price"]["regular_price"]["value"])
    for i in range(len(regular)):
        diff=regular[i]-offer[i]
        div=diff/regular[i]
        discount=div*100
        if(discount>5):
            arr.append(i)
    for i in range(len(arr)):
        ids.append(product_json[arr[i]]['_id']['$oid'])
                

    return render_template("result.html",prediction=ids) 

@app.route("/task2")
def task2():
    product_json=[]
    with open("E:/flask/netaporter_gb.json",encoding="utf8") as fp:
        for product in fp.readlines():
            product_json.append(json.loads(product))
    a=52383
    offer=[]
    regular=[]
    arr=[]
    ids=[]
    for i in range(52383):
        offer.append(product_json[i]["price"]["offer_price"]["value"])
        regular.append(product_json[i]["price"]["regular_price"]["value"])
    for i in range(len(regular)):
        diff=regular[i]-offer[i]
        div=diff/regular[i]
        discount=div*100
        if(discount>5):
            arr.append(i)
    for i in range(len(arr)):
        if(product_json[arr[i]]['brand']['name']=="balenciaga"):
            ids.append(product_json[arr[i]]['_id']['$oid'])
    return render_template("task2.html",prediction=ids) 

@app.route("/task3")
def task3():
    product_json=[]
    with open("E:/flask/netaporter_gb.json",encoding="utf8") as fp:
        for product in fp.readlines():
            product_json.append(json.loads(product))
    a=52383
    index=[]
    offer=[]
    regular=[]
    discounts=[]
    ids=[]
    for i in range(52383):  
        if(product_json[i]['brand']['name']=="gucci"):
            offer.append(product_json[i]["price"]["offer_price"]["value"])
            regular.append(product_json[i]["price"]["regular_price"]["value"])
    for i in range(len(regular)):
        diff=regular[i]-offer[i]
        div=diff/regular[i]
        discount=div*100
        discounts.append(discount)
    length=len(discounts)
    total=0
    for i in range(length):
        total =total+discounts[i]
    avgdiscount=total/length
    return render_template("task3.html",prediction=avgdiscount,totals=length)

@app.route("/task4")
def task4():
    product_json=[]
    with open("E:/flask/netaporter_gb.json",encoding="utf8") as fp:
        for product in fp.readlines():
            product_json.append(json.loads(product))
    a=52383
    index=[]
    discounts=[]
    listbrand=[]
    ids=[]
    brand=[]
    for i in range(52383):
        brand.append(product_json[i]['brand']['name'])      
    brandarr = np.array(brand)  
    uniquebrand=np.unique(brandarr)
    leng=len(uniquebrand)
    j=0
    for j in range(leng):
        offer=[]
        regular=[]
        for i in range(52383):
            if(product_json[i]['brand']['name']==uniquebrand[j]):
                offer.append(product_json[i]["price"]["offer_price"]["value"])
                regular.append(product_json[i]["price"]["regular_price"]["value"])  
        for i in range(len(regular)):
            diff=regular[i]-offer[i]
            div=diff/regular[i]
            discount=div*100
            discounts.append(discount)
        length=len(discounts)
        total=0
        for i in range(length):
            total =total+discounts[i]
            avgdiscount=total/length        
        if(avgdiscount>10):
            listbrand.append(uniquebrand[j])
    t=len(listbrand)        
    return render_template("task4.html",prediction=listbrand,totals=t)

@app.route("/task5")
def task5():
    product_json=[]
    with open("E:/flask/netaporter_gb.json",encoding="utf8") as fp:
        for product in fp.readlines():
            product_json.append(json.loads(product))
    value=0
    ids=[]
    for i in range(52383):
        if 'similar_products' in product_json[i]:
            if(product_json[i]['price']['basket_price']['value']>product_json[i]['similar_products']['meta']['max_price']['basket']):
                ids.append(product_json[i]['_id']['$oid']) 
    return render_template("task5.html",prediction=ids)

@app.route("/task6")
def task6():
    product_json=[]
    with open("E:/flask/netaporter_gb.json",encoding="utf8") as fp:
        for product in fp.readlines():
            product_json.append(json.loads(product))
    value=0
    ids=[]
    for i in range(52383):
        if 'similar_products' in product_json[i]:
            if(product_json[i]['price']['basket_price']['value']>product_json[i]['similar_products']['meta']['max_price']['basket']):
                if(product_json[i]['brand']['name']=="balenciaga"):
                    ids.append(product_json[i]['_id']['$oid'])        
    return render_template("task6.html",prediction=ids)

@app.route("/task7")
def task7():
    product_json=[]
    with open("E:/flask/netaporter_gb.json",encoding="utf8") as fp:
        for product in fp.readlines():
            product_json.append(json.loads(product))
    a=52383
    offer=[]
    regular=[]
    arr=[]
    ids=[]
    for i in range(52383):
        if(product_json[i]['website_id']['$oid']=='5d0cc7b68a66a100014acdb0'):
            offer.append(product_json[i]["price"]["offer_price"]["value"])
            regular.append(product_json[i]["price"]["regular_price"]["value"])
    for i in range(len(regular)):
        diff=offer[i]-regular[i]
        div=diff/offer[i]
        discount=div*100
        if(discount>10):
            arr.append(i)
    for i in range(len(arr)):
        ids.append(product_json[arr[i]]['_id']['$oid'])        

    return render_template("task7.html",prediction=ids) 


    
if __name__ == "__main__":
    app.run(debug=True)