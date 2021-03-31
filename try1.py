
from flask import Flask ,render_template , url_for, json, jsonify, request,make_response
from collections import Counter
import pyrebase
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from matplotlib import pyplot
from pandas.plotting import autocorrelation_plot
from pandas import read_csv
from pandas import datetime
from pandas import DataFrame
from statsmodels.tsa.arima_model import ARIMA
from matplotlib import pyplot
#from statsmodels.tsa.arima_model import ARIMA
from sklearn.metrics import mean_squared_error

app = Flask(__name__) 
app.debug = True
config = {
    "apiKey": "AIzaSyD7227U0LJPyf2IkRNh1_wELS7dPJg-UjE",
    "authDomain": "milksales-f5dfa.firebaseapp.com",
    "databaseURL": "https://milksales-f5dfa.firebaseio.com",
    "projectId": "milksales-f5dfa",
    "storageBucket": "milksales-f5dfa.appspot.com",
    "messagingSenderId": "657029337030",
    "appId": "1:657029337030:web:8ce2bd7e94f5335d172cc7",
    "measurementId": "G-N4DV004NMJ"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()
a =(db.child("customers").get().val())
cust = list(a.keys())
datekey = (a.values())
datelist = []
for eachcust in list(datekey):
    #print(eachcust)
    datelist= list(eachcust.keys())
    break
datelist = datelist[:-1]

#print(len(datekey))
#print(list(datekey)[0])
totalbuffalomilk = 0
totalbuffalomilkeve = 0
totalcowmilk = 0
totalcowmilkeve = 0

indbuffalomilk = []
indbuffalomilkeve = []
indcowmilk = []
indcowmilkeve = []
for eachcust in list(datekey):
    buffalomilk = 0
    buffalomilkeve = 0
    cowmilk = 0
    cowmilkeve = 0
   # for eachdate in eachcust:
      #  print(eachcust.values())
    #print(eachcust.values())
    a = eachcust.values()
    for eachdate in a:
        #print(eachdate)
        
        for key in eachdate.keys():
            if key != 'date' and eachdate[key]!=None:
                st = eachdate[key].replace('`','')
                #print(st)
                if st == '':
                    st = 0
                if key == 'buffalomilk' :
                  #  print(eachdate[key])
                    buffalomilk+=float(st)
                elif key == 'buffalomilkeve':
                    buffalomilkeve+=float(st)
                elif key == 'cowmilk':
                    cowmilk+=float(st)
                elif key == 'cowmilkeve':
                    cowmilkeve+=float(st)
                    
   # print(buffalomilk)
    indbuffalomilk.append(buffalomilk)
    indbuffalomilkeve.append(buffalomilkeve)
    indcowmilk.append(cowmilk)
    indcowmilkeve.append(cowmilkeve)
    totalbuffalomilk+=buffalomilk
    totalbuffalomilkeve+=buffalomilkeve
    totalcowmilk+=cowmilk
    totalcowmilkeve+=cowmilkeve
#********************************************************************************************************************
#********************************************************************************************************************
#********************************************************************************************************************
#*******************************************  initial opening Of LOGIN   ********************************************
#********************************************************************************************************************
#********************************************************************************************************************
#********************************************************************************************************************
@app.route('/') 
def login(): 
    return render_template('login.html')

@app.route('/login.html') 
def loginn(): 
    return render_template('login.html')

@app.route('/page1.html') 
def pagee1():
    a112123 =(db.child("customers").get().val())
    cust112123 = list(a112123.keys())
    cuscus = cust112123
    return render_template('page1.html',cuscus=cuscus)

@app.route('/page3.html',methods = ["POST","GET"]) 
def login133():
    a12123 =(db.child("customers").get().val())
    cust12123 = list(a12123.keys())
    contri=[0,0,0]
    return render_template('page3.html',cuscus=cust12123,contri=contri)

@app.route('/page4.html',methods = ["POST","GET"]) 
def login144():
    a112123 =(db.child("customers").get().val())
    cust112123 = list(a112123.keys())
    cuscus = cust112123
    tt1=[0,0]
    return render_template('page4.html',cuscus=cuscus ,tt1=tt1)
#********************************************************************************************************************
#********************************************************************************************************************
#********************************************************************************************************************
#*******************************************  VALIDATION Of LOGIN   *************************************************
#********************************************************************************************************************
#********************************************************************************************************************
#********************************************************************************************************************
@app.route('/page1',methods = ["POST","GET"]) 
def loginval(): 
    if request.method == "POST":
        userid = request.form['u_name']
        pass1 = request.form['u_password']
        use = db.child("validation").get()
        u1=use.val().values()
        useri = list(u1)[1]
        pas = list(u1)[0]
        a112123 =(db.child("customers").get().val())
        cust112123 = list(a112123.keys())
        cuscus = cust112123
        #print(userid,useri )
        if useri == userid and pas == pass1:
            return render_template('page1.html',cuscus=cuscus)

#********************************************************************************************************************
#********************************************************************************************************************
#********************************************************************************************************************
#*******************************************  INSERTION OF DATA   ***************************************************
#********************************************************************************************************************
#********************************************************************************************************************
#********************************************************************************************************************
@app.route('/pa1',methods = ["POST","GET"]) 
def insertionn(): 
    if request.method == "POST":
        date = request.form['entryDate']
        sess = request.form['session']
        cmilk = request.form['cowMilk']
        bmilk = request.form['buffaloMilk']
        name = request.form['customerName']
        if(sess == "morning"):
            db.child('customers').child(name).child(date).update({"cowmilk":cmilk})
            db.child('customers').child(name).child(date).update({"buffalomilk":bmilk})
            # db.child('customers').child(name).child(date).update({"cowmilkeve":""})
            # db.child('customers').child(name).child(date).update({"buffalomilkeve":""})
        if(sess == "evening"):
            # db.child('customers').child(name).child(date).update({"cowmilk":""})
            # db.child('customers').child(name).child(date).update({"buffalomilk":""})
            db.child('customers').child(name).child(date).update({"cowmilkeve":cmilk})
            db.child('customers').child(name).child(date).update({"buffalomilkeve":bmilk})
        # print(date,sess,cmilk,bmilk,name)
        a112123 =(db.child("customers").get().val())
        cust112123 = list(a112123.keys())
        cuscus = cust112123
        return render_template("page1.html", cuscus=cuscus)        
#********************************************************************************************************************
#********************************************************************************************************************
#********************************************************************************************************************
#*******************************************  customer analysis   *************************************************
#********************************************************************************************************************
#********************************************************************************************************************
#********************************************************************************************************************  

@app.route('/pa3',methods = ["POST","GET"]) 
def custdetails(): 
    #cust
    if request.method == "POST":
        name = request.form['customernames']
        index = cust.index(name)
        #print(index)
        contribuffmilk = (indbuffalomilk[index]+indbuffalomilkeve[index])/(totalbuffalomilk+totalbuffalomilkeve)*100

        contricowmilk = (indcowmilk[index]+indcowmilkeve[index])/(totalcowmilk+totalcowmilkeve)*100
        contri = {}
        
        # print(contribuffmilk)
        # print(contricowmilk)
        toto = totalbuffalomilk+totalbuffalomilkeve+totalcowmilk+totalcowmilkeve
        indcon = []
        for i in range(0,len(indbuffalomilk)):
            a111 = 0
            a111 = indbuffalomilk[i] + indbuffalomilkeve[i] + indcowmilk[i] + indcowmilkeve[i]
            b111 = ((a111/toto)*100) 
            indcon.append(b111)
        #print(indcon)
        #print(toto)
        from collections import Counter
        contr = {}
        #contrcow = {}
        for key in cust: 
            for value in indcon: 
                contr[key] = value 
                indcon.remove(value) 
                break  
        #print(contr)

        concus = []
        conval = []
        finalcon = {}
        k = Counter(contr) 
        high = k.most_common(len(cust))
        #print(high)
        for i in high: 
            concus.append(i[0])
            conval.append(i[1])
        for key in concus: 
            for value in conval: 
                finalcon[key] = value 
                conval.remove(value) 
                break
        #print(finalcon)
        rank=1
        for i in range(0,len(finalcon)):
            if(name == concus[i]):
                break
            else:
                rank = rank + 1
        #print(rank)
        a12123 =(db.child("customers").get().val())
        cust12123 = list(a12123.keys())

        contri =[contribuffmilk, contricowmilk, rank ]
        print(contri)
        a112123 =(db.child("customers").get().val())
        cust112123 = list(a112123.keys())
        cuscus = cust112123
        return render_template('page3.html', contri=contri, cuscus=cuscus)
    else:
        return request.method
#********************************************************************************************************************
#********************************************************************************************************************
#********************************************************************************************************************
#*******************************************  overall analysis    *************************************************
#********************************************************************************************************************
#********************************************************************************************************************
#********************************************************************************************************************
@app.route('/page2.html') 
def overall_analysis(): 
    contribuff=[]
    contricow=[]
    for na in cust:
        index = cust.index(na)
        contribuffmilk = (indbuffalomilk[index]+indbuffalomilkeve[index])/(totalbuffalomilk+totalbuffalomilkeve)*100
        contribuff.append(contribuffmilk)
        contricowmilk = (indcowmilk[index]+indcowmilkeve[index])/(totalcowmilk+totalcowmilkeve)*100
        contricow.append(contricowmilk)
    # print(contribuff)
    # print(contricow)

    from collections import Counter
    contrbuff = {}
    contrcow = {}
    for key in cust: 
        for value in contribuff: 
            contrbuff[key] = value 
            contribuff.remove(value) 
            break  
    # print(contrbuff)

    for key in cust: 
        for value in contricow: 
            contrcow[key] = value 
            contricow.remove(value) 
            break  
    # print(contrcow)
    #---------------------------------------------------------------------------top10buffalo--------------------------------------------------------------------------------------
    top10buffcus = []
    top10buffval = []
    top10buff = {}
    k = Counter(contrbuff) 
    high = k.most_common(10)
    #print(high)
    for i in high: 
        top10buffcus.append(i[0])
        top10buffval.append(i[1])
    for key in top10buffcus: 
        for value in top10buffval: 
            top10buff[key] = value 
            top10buffval.remove(value) 
            break
    #-------------------------------------------------------------------------------------top10cow--------------------------------------
    top10cowcus = []
    top10cowval = []
    top10cow = {}
    k = Counter(contrcow) 
    high = k.most_common(10)
    #print(high)
    for i in high: 
        top10cowcus.append(i[0])
        top10cowval.append(i[1])
    for key in top10cowcus: 
        for value in top10cowval: 
            top10cow[key] = value 
            top10cowval.remove(value) 
            break
    top10 = {}
    top10['top10buff']=top10buff
    top10['top10cow']=top10cow
    #top10['buffmilkcontribution']=contrbuff
    #top10['cowmilkcontribution']=contrcow

    #----------------------------------------------------------------------------------prediction--------------------------------------
    cowmilk = []
    buffalomilk = []
    for eachdate in datelist:
        bmdatewise = 0
        cmdatewise = 0
        for eachcust in list(datekey):
        # print(eachcust[eachdate])
            dic = eachcust[eachdate]
            
            dbm = dic['buffalomilk'].replace('`','')
            dbme = dic['buffalomilkeve'].replace('`','')
            dcm = dic['cowmilk'].replace('`','')
            dcme = dic['cowmilkeve'].replace('`','')
            if dbm =='' :
                #print("hkn")
                dbm = 0
            if dbme == '':
            #  print("hgfgh")
                dbme =0
            if dcm =='':
                dcm=0
            if dcme=='':
                dcme=0

            bmdatewise += float(dbm) + float(dbme)
            cmdatewise += float(dcm) + float(dcme)
            
        buffalomilk.append(bmdatewise)
        cowmilk.append(cmdatewise)
            
            

    dicc1 = {'date':datelist,'buffalomilk':buffalomilk}
    dicc2 = {'date':datelist,'cowmilk':cowmilk}
    dicc3 = {'date':datelist,'buffalomilk':buffalomilk,'cowmilk':cowmilk}
    data = pd.DataFrame(dicc1)
    data1 = pd.DataFrame(dicc2)
    df3 = pd.DataFrame(dicc3)
    data['date'] = pd.to_datetime(data['date'])
    data.set_index('date',inplace = True)
    data1['date'] = pd.to_datetime(data1['date'])
    data1.set_index('date',inplace = True)
    data.head()
    series = data
    model = ARIMA(series, order=(3,1,0))
    model_fit = model.fit(disp=0)
  
    residuals = DataFrame(model_fit.resid)
  



    X = series.values
    size = int(len(X) * 0.66)
    train, test = X[0:size], X[size:len(X)]
    history = [x for x in train]
    predictions = list()
    for t in range(len(test)):
        model = ARIMA(history, order=(3,1,0))
        model_fit = model.fit(disp=0)
        output = model_fit.forecast()
        yhat = output[0]
        predictions.append(yhat)
        obs = test[t]
        history.append(obs)
    #	print('predicted=%f, expected=%f' % (yhat, obs))
    error = mean_squared_error(test, predictions)
    #print('Test MSE: %.3f' % error)
    # plot
    #pyplot.plot(test)
    #pyplot.plot(predictions, color='red')
    #pyplot.show()

    # split the dataset

    series = data
    split_point = len(series) - 7
    dataset, validation = series[0:split_point], series[split_point:]
    #print('Dataset %d, Validation %d' % (len(dataset), len(validation)))
  

    forecast = model_fit.forecast(steps=5)[0]


    series1 = data1
    #print(series1.head())
    # series1.plot()
    # pyplot.show()

  

    model1 = ARIMA(series1, order=(3,1,0))
    model_fit1 = model1.fit(disp=0)
    #print(model_fit1.summary())
    # plot residual errors
    residuals1 = DataFrame(model_fit1.resid)
    #residuals1.plot()
    #pyplot.show()
    #residuals1.plot(kind='kde')
    #pyplot.show()
    #print(residuals1.describe())

    X1 = series1.values
    size1 = int(len(X1) * 0.66)
    train1, test1 = X1[0:size1], X1[size:len(X1)]
    history1 = [x1 for x1 in train1]
    predictions1 = list()
    for s in range(len(test1)):
        model1 = ARIMA(history1, order=(3,1,0))
        model_fit1 = model1.fit(disp=0)
        output1 = model_fit1.forecast()
        yhat1 = output1[0]
        predictions1.append(yhat1)
        obs1 = test1[s]
        history1.append(obs1)

    error1 = mean_squared_error(test1, predictions1)
   
    series1 = data1
    split_point1 = len(series1) - 7
    dataset1, validation1 = series1[0:split_point1], series[split_point1:]



    forecast1 = model_fit1.forecast(steps=5)[0]
    fc = []
    fc.insert(0,forecast.tolist())
    fc.insert(1,forecast1.tolist())
    
    overallfinl = [fc,dicc1,dicc2]
    # print(overallfinl)
    return render_template('page2.html', overallfinl=json.dumps(overallfinl), top10buff=json.dumps(top10buff), top10cow=json.dumps(top10cow));
#********************************************************************************************************************
#********************************************************************************************************************
#********************************************************************************************************************
#*******************************************  CALCULATION OF CUSTOMER AMOUNT  ***************************************
#********************************************************************************************************************
#********************************************************************************************************************
#********************************************************************************************************************
@app.route('/pa4',methods = ["POST","GET"]) 
def cal():
    if request.method == "POST":
        cuname = request.form['customer']
        fdate = request.form['fromDate']
        tdate = request.form['todate']    
        #cust
        #datelist
        a11 =(db.child("customers").get())
        b11 = a11.val()
        c11 = b11[cuname]
        vl = list(c11.values())
        dl = list(c11.keys())
        fdateindex = dl.index(fdate)
        tdateindex = dl.index(tdate)
        req_list = list(c11.values())[fdateindex:tdateindex+1]
        #bfms=0
        #coms=0
        ttbm=0
        ttcm=0
        for i in range(0,len(req_list)):
            k = req_list[i]['buffalomilk']
            l =  req_list[i]['buffalomilkeve']
            m =  req_list[i]['cowmilk']
            n =  req_list[i]['cowmilkeve']
            k.replace('`','')
            if k=='':
                k='0.0'
            #print(k)
            l.replace('`','')
            if l=='':
                l='0.0'
            #print(l)
            m.replace('`','')
            if m=='':
                m='0.0'
            #print(m)
            n.replace('`','')
            if n=='':
                n='0.0'
            #print(n)
            ttbm += float(k)+float(l)
            #print("ttbm",ttbm)
            ttcm += float(m)+float(n)
        # tt = [ttcm,ttbm]
        # tt['total cow milk']=ttcm
        # tt['total buff milk']=ttbm
        
        a1212 =(db.child("customers").get().val())
        cust1212 = list(a1212.keys())
        cuscus=cust1212
        # tt['customer names']=cust1212
        tt1 = [ttcm,ttbm]
        # print(tt1)
        return render_template('page4.html',tt1=tt1,cuscus=cuscus)



if __name__ == '__main__': 


	app.run() 
