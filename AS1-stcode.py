import pandas as pd 
import streamlit as st 
import seaborn as sns 
import matplotlib.pyplot as plt 

df = pd.read_csv('sleep_health_lifestyle.csv')

progress_bar = st.sidebar.progress(0)
status_text = st.sidebar.empty()

st.title("Dashboard Application")
st.subheader("Sleep, Health and Lifestyle")

st.write(df.head(3))

# with st.form('Gender'):
    # Gender = st.selectbox('Gender', ['Male', 'Female'])
    # my_submit_button = st.form_submit_button()

selected_x_var = st.selectbox('Choose any attribute for x axis:', ['Age', 'Sleep Duration', 'Quality of Sleep', 'Physical Activity Level', 'Stress Level'])
selected_y_var = st.selectbox('Choose any attribute for y axis:', ['Age', 'Sleep Duration', 'Quality of Sleep', 'Physical Activity Level', 'Stress Level'])

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