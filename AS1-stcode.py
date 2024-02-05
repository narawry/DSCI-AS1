import pandas as pd 
import streamlit as st 

df = pd.read_csv('sleep_health_lifestyle.csv')

st.title("Sleep, Health and Lifestyle")
st.subheader("Made by Nana")

st.dataframe(df)

average = df['Age'].mean()
st.write("The average age is:", average)

high = df['Stress Level'].max() # Get the highest stress level with .max()
highest = df.loc[df['Stress Level'] == high]
st.write(high)