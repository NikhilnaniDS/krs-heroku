import flask
from flask import Flask,render_template, request

import pickle
from sklearn.linear_model import LinearRegression

app=Flask(__name__)



@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict',methods=['POST'])


def predict():
    if request.method=='POST':
        a=request.form['a']
        b=request.form['b']
        c=request.form['c']
        d=request.form['d']
        e=request.form['e']
        f=request.form['f']

        arr=[[a,b,c,d,e,f]]
        

        model=pickle.load(open('krs.pkl','rb'))
        model.LinearRegression()
        prediction=model.predict(arr)
        return render_template('home.html', prediction_text="water availability is {}".format(prediction))

if __name__== '__main__':
    app.run(debug=True)