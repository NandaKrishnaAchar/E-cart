import urllib.request
from flask import Flask, request, redirect, jsonify,render_template
from werkzeug.utils import secure_filename
import numpy as np
import os
import pandas as pd
import json

data=pd.read_csv('product.csv')
r = json.load(open("Rules.txt"))

def suggest_item(pid):
    pro_name=data.iloc[pid,1]
    try:
        pr={pro_name:r[pro_name]}
    except:
        return {pro_name:['NO PRODUCTS']}
    return pr

app = Flask(__name__)

@app.route('/details/', methods=['POST'])

def addOne():

    data = request.get_json()
    print("heloo",data)
    print(data['phn'])

    d=suggest_item(int(data['rfid']))
    r=list(d.values())[0]
    k=list(d.keys())[0]
    print(r,k)

    r_one=""
    r_two=""
    r_three=""


    try:
        r_one=r[0]
        r_two=r[1]
        r_three=r[2]

    except:
        if(r_one=='NO PRODUCTS'):
            r_one=""
        print(r_one,r_two,r_three)
    

    return jsonify({'name' : k,'price':'10000','r_one':r_one,'t_one':'TAG_One','p_one':'Price_One','r_two':r_two,'t_two':'TAG_two','p_two':'Price_two','r_three':r_three,'t_three':'TAG_three','p_three':'Price_three'})



"""
def addOne():
    data = request.get_json()
    print("heloo",data)
    print(data['phn'])
    return jsonify({'name' : 'Product_0','price':'10000','r_one':'Product_One_Name','t_one':'TAG_One','p_one':'Price_One','r_two':'Product_Two_Name','t_two':'TAG_two','p_two':'Price_two','r_three':'Product_three_Name','t_three':'TAG_three','p_three':'Price_three'})

"""
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=80,debug=True)
