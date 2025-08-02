t
import streamlit as st
import numpy as np
import pandas as pd
import joblib

with open('final_model.joblib', 'rb') as file:
    model=joblib.load(file)

def prediction(input_list):

    pred = model.predict([input_list])[0]
    if pred==0:
        return 'Sitting on bed'
    elif pred==1:
        return 'Sitting on chair'
    elif pred==2:
        return 'Lying on bed'
    else:
        return 'Ambulating'

def main():
    st.title('ACTIVITY PREDICTION FROM SENSOR DATA')
    st.subheader('''This application will predict the ongoing activity on the basis of Sensor Data Provided. Fill the respective fields 
    to get prediction.''')
    st.image('image.png')

    rfid = st.selectbox('Enter the RFID Configuration settings', ['Config 1 (4 Sensors)', 'Config 2 (3 Sensors)'])
    rfid_e = (lambda x: 3 if x == 'Config 2 (3 Sensors)' else 4)(rfid)

    ant_ID = st.selectbox('Select the Antenna ID', [1,2,3,4])
    rssi = st.text_input('Enter the recieved signal strength indicator (RSSI)')

    accv =  st.text_input('Enter the vertical acceleration data from Sensor')
    accf =  st.text_input('Enter the frontal acceleration data from Sensor')
    accl =  st.text_input('Enter the lateral acceleration data from Sensor')

    input_data = [accf, accv, accl, ant_ID, rssi, rfid_e]

    if st.button('Predict'):
        response = prediction(in_data)
        st.success(response)

if __name__=='__main__':
    main()


