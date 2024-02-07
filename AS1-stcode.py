import pandas as pd 
import streamlit as st 
import seaborn as sns 
import matplotlib.pyplot as plt 

df = pd.read_csv('students_mental_health.csv')

progress_bar = st.sidebar.progress(0)
status_text = st.sidebar.empty()

st.title("Dashboard Application")
st.subheader("Students' Mental Health")

st.write(df.head(3))

# with st.form('Gender'):
    # Gender = st.selectbox('Gender', ['Male', 'Female'])
    # my_submit_button = st.form_submit_button()

selected_x_var = st.selectbox('Choose any attribute for x axis:', [])
selected_y_var = st.selectbox('Choose any attribute for y axis:', [])

gender_rad = st.radio('Gender', ['Male', 'Female']) 

filteredbygender = df.loc[df['Gender'] == gender_rad] # Create new 'dataframe'
st.write(gender_rad)

sns.set_style('darkgrid')
markers = {"male": "X", "female": "s"}

fig, ax = plt.subplots()
ax = sns.scatterplot(data=filteredbygender, x=selected_x_var, y=selected_y_var, markers=markers)

plt.xlabel(selected_x_var)
plt.ylabel(selected_y_var)
plt.title("Scatter Plot")
st.pyplot(fig)