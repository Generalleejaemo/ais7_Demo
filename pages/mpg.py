import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import koreanize_matplotlib
import seaborn as sns
import plotly.express as px

st.set_page_config(
    page_title="ais 자동차 연비 App",
    page_icon="🚗",
    layout="wide",)

st.markdown("# 난 본문 MPG 🚗")
st.sidebar.markdown("# 난 사이드 MPG 🚗")

url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/mpg.csv"
@st.cache
def load_data():
    data= pd.read_csv(url)
    return data

data_load_state = st.text('Lading data')
data = load_data()
data_load_state.text("Done ! (using st.cache)")

st.write("""
### 자동차 연비
""")

mpg = sns.load_dataset("mpg")

st.sidebar.header('User Input Features')
selected_year = st.sidebar.selectbox('Year',
   list(reversed(range(mpg.model_year.min(),mpg.model_year.max())))
   )

# Sidebar - origin
sorted_unique_origin = sorted(mpg.origin.unique())
selected_origin = st.sidebar.multiselect('origin', sorted_unique_origin, sorted_unique_origin)


if selected_year > 0 :
   mpg = mpg[mpg.model_year == selected_year]

if len(selected_origin) > 0:
   mpg = mpg[mpg.origin.isin(selected_origin)]

st.dataframe(mpg)

st.line_chart(mpg["mpg"])

st.bar_chart(mpg["mpg"])

fig, ax = plt.subplots()
sns.barplot(data=mpg, x="origin", y="mpg", ci=None).set_title("origin 별 자동차 연비")
st.pyplot(fig)

fig, ax = plt.subplots(figsize=(10, 3))
sns.countplot(data=data, x="origin").set_title("지역별 자동차 연비 데이터 수")
st.pyplot(fig)

pxh = px.histogram(data, x="origin", title="지역별 자동차 연비 데이터 수")
st.plotly_chart(pxh)

lmp = sns.lmplot(data=data, x="mpg", y="weight",hue="origin").set_title("")
st.pyplot(lmp)
