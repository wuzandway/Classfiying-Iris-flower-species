import streamlit as st
import pandas as pd
import joblib
from PIL import Image

#Loading Our final trained Knn model 
model= open("Knn_Classifier.pkl", "rb")
knn_clf=joblib.load(model)


st.title("Iris flower species Classification App")

#Loading images

setosa= Image.open('setosa.png')
cat= Image.open('cat.png')
virginica = Image.open('virginica.png')

st.sidebar.title("Features")

#Intializing
parameter_list=['萼片大小 (cm)','萼片寬度 (cm)','花瓣大小 (cm)','花瓣寬度 (cm)']
parameter_input_values=[]
parameter_default_values=['5.2','3.2','4.2','1.2']

values=[]

#Display
for parameter, parameter_df in zip(parameter_list, parameter_default_values):
	
	values= st.sidebar.slider(label=parameter, key=parameter,value=float(parameter_df), min_value=0.0, max_value=8.0, step=0.1)
	parameter_input_values.append(values)
	
input_variables=pd.DataFrame([parameter_input_values],columns=parameter_list,dtype=float)
st.write('\n\n')

if st.button("Click Here to Classify"):
	prediction = knn_clf.predict(input_variables)
	st.image(setosa) if prediction == 0 else st.image(cat)  if prediction == 1 else st.image(virginica) 
	


