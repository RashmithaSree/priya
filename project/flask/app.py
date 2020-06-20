# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 13:25:15 2020

@author: HP
"""
from flask import Flask, render_template , request
app = Flask(__name__)
import pickle
model=pickle.load(open('flightmodel.pkl','rb'))
scaler=pickle.load(open('flightscaler.pkl','rb'))
@app.route('/')
def helloworld():     
    return render_template("index.html")

@app.route('/predict',methods = ['POST'])
def loginfunc():
    dt = request.form["dt"]
    crsdt = request.form["crsdt"]
    at = request.form["at"]
    crsat = request.form["crsat"]
    O = request.form["O"]
    De = request.form["De"]
    Di = request.form["Di"]
    if(O == "IAD"):
        a1,a2,a3,a4,a5,a6 = 1,0,0,0,0,0
    if(O == "IND"):
        a1,a2,a3,a4,a5,a6 = 0,1,0,0,0,0
    if(O == "ISP"):
        a1,a2,a3,a4,a5,a6 = 0,0,1,0,0,0
    if(O == "JAN"):
        a1,a2,a3,a4,a5,a6 = 0,0,0,1,0,0
    if(O == "JAX"):
        a1,a2,a3,a4,a5,a6 = 0,0,0,0,1,0
    if(O == "LAS"):
        a1,a2,a3,a4,a5,a6 = 0,0,0,0,0,1
        
        #write these in the same ascending order ABQ,ALB,AMA,AUS,BDL,BHM,BNA,BWI,FLL,HOU,IND,JAX,LAS,MCO,MDX,PBI,PHL,PHX,RSW,TPA
    if(De == "ABQ"):
        s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12,s13,s14,s15,s16,s17,s18,s19,s20 = 1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0          
    if(De == "ALB"):
        s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12,s13,s14,s15,s16,s17,s18,s19,s20 = 0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0          
    if(De == "AMA"):
        s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12,s13,s14,s15,s16,s17,s18,s19,s20 = 0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0          
    if(De == "AUS"):
        s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12,s13,s14,s15,s16,s17,s18,s19,s20 = 0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0          
    if(De == "BDL"):
        s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12,s13,s14,s15,s16,s17,s18,s19,s20 = 0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0          
    if(De == "BHM"):
        s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12,s13,s14,s15,s16,s17,s18,s19,s20 = 0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0          
    if(De == "BNA"):
        s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12,s13,s14,s15,s16,s17,s18,s19,s20 = 0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0          
    if(De == "BWI"):
        s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12,s13,s14,s15,s16,s17,s18,s19,s20 = 0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0          
    if(De == "FLL"):
        s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12,s13,s14,s15,s16,s17,s18,s19,s20 = 0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0          
    if(De == "HOU"):
        s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12,s13,s14,s15,s16,s17,s18,s19,s20 = 0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0          
    if(De == "IND"):
        s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12,s13,s14,s15,s16,s17,s18,s19,s20 = 0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0          
    if(De == "JAX"):
        s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12,s13,s14,s15,s16,s17,s18,s19,s20 = 0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0          
    if(De == "LAS"):
        s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12,s13,s14,s15,s16,s17,s18,s19,s20 = 0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0          
    if(De == "MCO"):
        s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12,s13,s14,s15,s16,s17,s18,s19,s20 = 0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0          
    if(De == "MDX"):
        s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12,s13,s14,s15,s16,s17,s18,s19,s20 = 0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0          
    if(De == "PBI"):
        s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12,s13,s14,s15,s16,s17,s18,s19,s20 = 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0          
    if(De == "PHL"):
        s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12,s13,s14,s15,s16,s17,s18,s19,s20 = 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0          
    if(De == "PHX"):
        s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12,s13,s14,s15,s16,s17,s18,s19,s20 = 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0          
    if(De == "RSW"):
        s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12,s13,s14,s15,s16,s17,s18,s19,s20 = 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0          
    if(De == "TPA"):
        s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12,s13,s14,s15,s16,s17,s18,s19,s20 = 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1          
    d=[[s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12,s13,s14,s15,s16,s17,s18,s19,s20,a1,a2,a3,a4,a5,a6,int(dt),int(crsdt),int(at),int(crsat),int(Di)]]
    h=model.predict(scaler.transform(d))
    if(h==0):
        Stroutput="Your Flight is Delay!"
    elif (h==1):
        Stroutput="Yor flight is arriving!"
    return render_template("index.html",r=Stroutput)

if __name__=='__main__' :
    app.run(debug=True)

