from re import sub
import numpy as np
import sympy as sp
from flask import Flask
from flask import request,render_template

app = Flask(__name__)

def convert_o(ma1):
    c = []
    x1 = []
    for i in list(ma1):
        if i.isdigit():
            x1.append(int(i))
            if len(x1) == 3:
                c.append(x1)
                x1 = []
        else:
            continue
    mat1 = np.array(c)
    return mat1

def convert_s(n,ma2):
    a = int(n)
    c = []
    x1 = []
    for i in list(ma2):
        if i.isdigit():
            x1.append(int(i))
            if len(x1) == 3:
                c.append(x1)
                x1 = []
        else:
            continue
    mat1 = np.array(c)
    return a,mat1


def convert(ma1,ma2):
    c = []
    x1 = []
    for i in list(ma1):
        if i.isdigit():
            x1.append(int(i))
            if len(x1) == 3:
                c.append(x1)
                x1 = []
        else:
            continue
    d = []
    x2 = []
    for i in list(ma2):
        if i.isdigit():
            x2.append(int(i))
            if len(x2) == 3:
                d.append(x2)
                x2 = []
        else:
            continue
    mat1 = np.array(c)
    mat2 = np.array(d)
    return mat1,mat2

@app.route('/add/<ma1>/<ma2>',methods =["GET","POST"])
def add(ma1 = None,ma2 = None):
    tup = convert(ma1,ma2)
    res = np.add(tup[0],tup[1])
    res1 = res.tolist()
    return render_template("index.html",data = res1)

@app.route('/sub/<ma1>/<ma2>',methods =["GET","POST"])
def subtract(ma1 = None,ma2 = None):
    tup = convert(ma1,ma2)
    res = np.subtract(tup[0],tup[1])
    res1 = res.tolist()
    return render_template("index.html",data = res1)

@app.route('/mmul/<ma1>/<ma2>',methods =["GET","POST"])
def m_mul(ma1,ma2):
    tup = convert(ma1,ma2)
    res = np.dot(tup[0],tup[1],out=None)
    res1 = res.tolist()
    return render_template("index.html",data = res1)

@app.route('/smul/<n>/<ma2>',methods =["GET","POST"])
def s_mul(n,ma2):
    tup = convert_s(n,ma2)
    res = np.multiply(tup[0],tup[1])
    res1 = res.tolist()
    return render_template("index.html",data = res1)

@app.route('/tr/<ma1>',methods =["GET","POST"])
def transpose_(ma1):
    mat1 = convert_o(ma1)
    res = mat1.transpose()
    res1 = res.tolist()
    return render_template("index.html",data = res1)

@app.route('/inv/<ma1>',methods =["GET","POST"])
def inverse(ma1):
    mat1 = convert_o(ma1)
    mat2 = np.linalg.inv(mat1)
    res = []
    for i in mat2:
        y = []
        for j in i:
            x = j.round(2)
            y.append(x)
        res.append(y)
    return render_template("index.html",data = res)

@app.route('/det/<ma1>',methods =["GET","POST"])
def det(ma1):
    mat1 = convert_o(ma1)
    res = np.linalg.det(mat1)
    res1 = res.tolist()
    return render_template("index.html",data = res1)

@app.route('/co/<ma1>',methods =["GET","POST"])
def cofactor(ma1):
    mat1 = convert_o(ma1)
    determinant = np.linalg.det(mat1)
    adjoint = np.linalg.inv(mat1)*determinant
    cofactor = adjoint.transpose()
    res1 = []
    for i in cofactor:
        y = []
        for j in i:
            x = j.round(2)
            y.append(x)
        res1.append(y)
    return render_template("index.html",data = res1)

@app.route('/ad/<ma1>',methods =["GET","POST"])
def adjoint(ma1):
    mat1 = convert_o(ma1)
    determinant = np.linalg.det(mat1)
    adjoint = np.linalg.inv(mat1)*determinant
    res1 = []
    for i in adjoint:
        y = []
        for j in i:
            x = j.round(2)
            y.append(x)
        res1.append(y)
    return render_template("index.html",data = res1)