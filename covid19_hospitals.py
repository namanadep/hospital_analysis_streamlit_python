import requests
import json
import streamlit as st 
from pandas.io.json import json_normalize
import pandas as pd 

#Get hospital information
url='https://api.rootnet.in/covid19-in/stats/hospitals'
client=requests.get(url)
data=client.content
data=json.loads(data)

#Display summary of beds
st.title('Covid-19 Hospital Information')
st.subheader("Summary of beds across all the states")
totalBeds=data['data']['summary']['totalBeds']
totalHospitals=data['data']['summary']['totalHospitals']
urbanhospital=data['data']['summary']['urbanHospitals']
urbanbeds=data['data']['summary']['urbanBeds']
ruralhospitals=data['data']['summary']['ruralHospitals']
ruralbeds=data['data']['summary']['ruralBeds']

hosp='''## Total Hospitals ```  %d``` '''%totalHospitals
beds='''## Total beds ```  %d``` '''%totalBeds
urbanhosp='''## Urban Hospitals ```  %d``` '''%urbanhospital
urbanbed='''## Urban beds ```  %d``` '''%urbanbeds
ruralhosp='''## Rural Hospitals ```  %d``` '''%ruralhospitals
ruralbed='''## Rural beds ```  %d``` '''%ruralbeds

st.markdown(hosp)
st.markdown(beds)
st.markdown(urbanhosp)
st.markdown(urbanbed)
st.markdown(ruralhosp)
st.markdown(ruralbed)


#Display region wise information of hospitals
st.subheader("Beds available for selected state")
df=json_normalize(data['data']['regional'])
locations=df['state'].tolist()
choice=st.selectbox('Choose Location',locations)
df=df.drop(['asOn'],axis=1)
df.rename(columns = {'state':'State','ruralHospitals':'Rural Hospitals','ruralBeds':'Rural Beds','urbanHospitals':'Urban Hospitals','urbanBeds':'Urban Beds','totalHospitals':'Total Hospitals','totalBeds':'Total Beds'}, inplace = True)
value=df.loc[df['State']==choice]
st.table(value)

#Display information about all the hospitals
st.subheader("Beds available for all the states")
st.table(df)


