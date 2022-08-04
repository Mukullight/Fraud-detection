import numpy as np
import pickle
import pandas as pd
#from flasgger import Swagger
import streamlit as st 

from PIL import Image

pickle_in = open('/content/classifier.pkl', "rb")
classifier = pickle.load(pickle_in)

def welcome():
    return "Welcome All"

#@app.route('/predict',methods=["Get"])
def predict_note_authentication(step,amount,oldbalanceOrg,newbalanceOrig,oldbalanceDest,newbalanceDest,var):
    
    """Let's check for transaction 
    This is using docstrings for specifications.
    ---
    parameters:  
      - name:step 
        in: query
        type: number
        required: true
      - name:amount 
        in: query
        type: number
        required: true
      - name: oldbalanceOrg
        in: query
        type: number
        required: true
      - name: newbalanceOrig
        in: query
        type: number
        required: true
      - name: oldbalanceDest
        in: query
        type: number
        required: true
      - name:newbalanceDest
        in: query
        type: number
        required: true
      - name:var
        in: query
        type: number
        required: true
    responses:
        200:
            description: The output values
        
    """
   
    prediction=classifier.predict([[step,amount,type1,oldbalanceOrg,newbalanceOrig,oldbalanceDest,newbalanceDest,var]])
    print(prediction)
    return prediction



def main():
    st.title("fruad detector")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Fruad detector Machine Learning App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    step = st.text_input("step","Type Here")
    amount = st.text_input("amount","Type Here")
    type1 = st.text_input("type","Type Here")
    oldbalanceOrg = st.text_input("oldbalanceOrg","Type Here")
    newbalanceOrig = st.text_input("newbalanceOrig","Type Here")
    oldbalanceDest = st.text_input("oldbalanceDest","Type Here")
    newbalanceDest = st.text_input("newbalanceDest","Type Here")
    var = abs(abs(newbalanceOrig-oldbalanceOrg)+abs(newbalanceDest-oldbalanceDest)-amount)
    result=""
    if st.button("Predict"):
        result=predict_note_authentication(step,amount,type1,oldbalanceOrg,newbalanceOrig,oldbalanceDest,newbalanceDest,var)
    st.success('The model prediction is {}'.format(result))
    if st.button("About"):
        st.text("Lets Learn Together")

if __name__=='__main__':
    main()
