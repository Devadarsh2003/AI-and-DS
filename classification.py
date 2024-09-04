import streamlit as st
import pandas as pd
from sklearn.datasets import load_iris 
from sklearn.ensemble import RandomForestClassifier

@st.cache_data
def load_data():
     iris = load_iris()
     df = pd.DataFrame(iris.data, columns = iris.feature_names) 
     df['species'] = iris.target
     return df, iris.target_names

data, target = load_data()

model = RandomForestClassifier()
model.fit(data.iloc[:,:-1], data['species'])

st.sidebar.title("input features")
sep_len = st.sidebar.slider("Sepal Length", float(data['sepal length (cm)'].min()), float(data['sepal length (cm)'].max()))
sep_wid = st.sidebar.slider("Sepal Width", float(data['sepal width (cm)'].min()), float(data['sepal width (cm)'].max()))
pet_len = st.sidebar.slider("Petal Length", float(data['petal length (cm)'].min()), float(data['petal length (cm)'].max()))
pet_wid = st.sidebar.slider("Petal Width", float(data['petal width (cm)'].min()), float(data['petal width (cm)'].max()))

input_data = [[sep_len, sep_wid, pet_len, pet_wid]]

prediction = model.predict(input_data)
pred_species = target[prediction[0]]

st.write("prediction")
st.write(f"{prediction} {pred_species}")