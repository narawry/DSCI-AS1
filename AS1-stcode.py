import pandas as pd 
import streamlit as st 
import seaborn as sns 
import matplotlib.pyplot as plt 
import plotly.express as px 

df = pd.read_csv('students_mental_health.csv')

st.title("Students' Mental Health")

# Sidebar
st.sidebar.title('Home')
first_page = st.sidebar.radio('Click to view:', ('Introduction', 'Data Overview', 'Dashboards'))

if first_page == 'Introduction':
    st.image('https://s3-prod.adage.com/s3fs-public/20230519_OPIN_MentalHealth_3x2.jpg', caption='test', use_column_width=True)
    st.write('add caption')
    
if first_page == 'Data Overview':    
    st.subheader('Data Overview')
    st.write(df.head(10))

if first_page == 'Dashboards':
    dash_no = st.sidebar.selectbox('Select a dashboard:', ['First Dashboard', 'Second Dashboard'])

    # First Dashboard
    if dash_no == 'First Dashboard':
        visual_type = st.selectbox('Select A Visualization:', 
                                    ['Bar', 'Histogram', 'Scatter', 'Line', 'Area', 'Pie'])
    
        # Using st.radio to divide gender
        gender_rad = st.radio('Gender', ['Male', 'Female'])
        filteredbygender = df.loc[df['Gender'] == gender_rad]

        # 1st Visualization
        if visual_type == 'Bar':
            st.subheader('Bar Graph')
            bar_att = st.selectbox('Choose an attribute:', 
                                       ['Age', 'Course', 'Stress_Level', 'Depression_Score', 'Anxiety_Score', 
                                        'Sleep_Quality', 'Physical_Activity', 'Diet_Quality', 'Social_Support', 
                                        'Relationship_Status', 'Substance_Use', 'Extracurricular_Involvement', 
                                        'Financial_Stress'])
            bar_graph = filteredbygender[bar_att].value_counts()

            fig = px.bar(x=bar_graph.index, y=bar_graph.values, labels={'x': bar_att, 'y': 'Count'}, template='plotly_dark')
            fig.update_layout(title="Bar Graph", xaxis_title=bar_att, yaxis_title="Count", height=600, width=800)
            st.plotly_chart(fig)

        # 2nd Visualization
        elif visual_type == 'Histogram':
            st.subheader('Histogram')
            hist_att = st.selectbox('Choose an attribute:', 
                                   ['Age', 'CGPA', 'Semester_Credit_Load'])
    
            fig = px.histogram(filteredbygender, x=hist_att, template='plotly_dark')
            fig.update_layout(title="Histogram", xaxis_title=hist_att, yaxis_title="Count")
            fig.update_traces(marker=dict(line=dict(width=1, color='White')))
            st.plotly_chart(fig)

        # 3rd Visualization
        elif visual_type == 'Scatter':
            st.subheader('Scatter Plot')
            x_axis = st.selectbox('Choose an attribute for x axis:', 
                              ['Age', 'CGPA', 'Stress_Level', 'Depression_Score', 
                               'Anxiety_Score', 'Financial_Stress', 'Semester_Credit_Load'], index=0)
            y_axis = st.selectbox('Choose an attribute for y axis:', 
                              ['Age', 'CGPA', 'Stress_Level', 'Depression_Score', 
                              'Anxiety_Score', 'Financial_Stress', 'Semester_Credit_Load'], index=1)

            fig = px.scatter(filteredbygender, x=x_axis, y=y_axis, color='Gender', template='plotly_dark')
            fig.update_layout(title="Scatter Plot", xaxis_title=x_axis, yaxis_title=y_axis, height=600, width=800)
            st.plotly_chart(fig)

        # 4th Visualization
        elif visual_type == 'Line':
            st.subheader('Line Chart')
            line_att = st.selectbox('Choose an attribute:', 
                                       ['Age', 'Course', 'Stress_Level', 'Depression_Score', 'Anxiety_Score', 
                                        'Sleep_Quality', 'Physical_Activity', 'Diet_Quality', 'Social_Support', 
                                        'Relationship_Status', 'Substance_Use', 'Extracurricular_Involvement', 
                                        'Financial_Stress'])
            line_chart = filteredbygender[line_att].value_counts()
            st.line_chart(line_chart)

        # 5th Visualization
        elif visual_type == 'Area':
            st.subheader('Area Chart')
            area_att = st.selectbox('Choose an attribute:', 
                                       ['Age', 'Course', 'Stress_Level', 'Depression_Score', 'Anxiety_Score', 
                                        'Sleep_Quality', 'Physical_Activity', 'Diet_Quality', 'Social_Support', 
                                        'Relationship_Status', 'Substance_Use', 'Extracurricular_Involvement', 
                                        'Financial_Stress'])
            area_chart = filteredbygender[area_att].value_counts()
            st.area_chart(area_chart)

        # 6th Visualization
        elif visual_type == 'Pie':
            st.subheader('Pie Chart')
            pie_att = st.selectbox('Choose an attribute:', 
                           ['Course', 'Sleep_Quality', 'Physical_Activity', 'Diet_Quality', 'Social_Support', 
                            'Relationship_Status', 'Substance_Use', 'Counseling_Service_Use', 
                            'Chronic_Illness', 'Extracurricular_Involvement', 'Residence_Type'])
    
            pie_chart = filteredbygender[pie_att].value_counts().reset_index()
            pie_chart.columns = ['Labels', 'Values']

            fig = px.pie(pie_chart, values='Values', names='Labels', template='plotly_dark')
            fig.update_layout(height=650, width=850)
            st.plotly_chart(fig)


    # Second Dashboard
    if dash_no == 'Second Dashboard':
        visual_type2 = st.selectbox('Select A Visualization:', 
                                 ['Bar', 'Histogram', 'Scatter', 'Line', 'Area', 'Pie'])
    
        # Using st.radio to divide gender
        gender_rad = st.radio('Gender', ['Male', 'Female'])
        filteredbygender = df.loc[df['Gender'] == gender_rad]

        # 1st Visualization
        if visual_type2 == 'Bar':
            st.subheader('Bar Graph')
            selected_column = st.selectbox('Choose an attribute:', 
                                       ['Age', 'Course', 'Stress_Level', 'Depression_Score', 'Anxiety_Score', 
                                        'Sleep_Quality', 'Physical_Activity', 'Diet_Quality', 'Social_Support', 
                                        'Relationship_Status', 'Substance_Use', 'Extracurricular_Involvement', 
                                        'Financial_Stress'])
            bar_graph = filteredbygender[selected_column].value_counts()
            st.bar_chart(bar_graph)
    
        # 2nd Visualization
        elif visual_type2 == 'Histogram':
            st.subheader('Histogram')
            hist_att = st.selectbox('Choose an attribute:', 
                                   ['Age', 'CGPA', 'Semester_Credit_Load'])
            
            fig = px.histogram(filteredbygender, x=hist_att, template='plotly_dark')
            fig.update_layout(title="Histogram", xaxis_title=hist_att, yaxis_title="Count")
            fig.update_traces(marker=dict(line=dict(width=1, color='White')))
            st.plotly_chart(fig)

        # 3rd Visualization
        elif visual_type2 == 'Scatter':
            st.subheader('Scatter Plot')
            x_axis = st.selectbox('Choose any attribute for x axis:', 
                              ['Age', 'CGPA', 'Stress_Level', 'Depression_Score', 
                               'Anxiety_Score', 'Financial_Stress', 'Semester_Credit_Load'], index=0)
            y_axis = st.selectbox('Choose any attribute for y axis:', 
                              ['Age', 'CGPA', 'Stress_Level', 'Depression_Score', 
                              'Anxiety_Score', 'Financial_Stress', 'Semester_Credit_Load'], index=1)

            fig = px.scatter(filteredbygender, x=x_axis, y=y_axis, color='Gender', template='plotly_dark')
            fig.update_layout(title="Scatter Plot", xaxis_title=x_axis, yaxis_title=y_axis)
            st.plotly_chart(fig)

        # 4th Visualization
        elif visual_type2 == 'Line':
            st.subheader('Line Chart')
            line_att = st.selectbox('Choose an attribute:', 
                                       ['Age', 'Course', 'Stress_Level', 'Depression_Score', 'Anxiety_Score', 
                                        'Sleep_Quality', 'Physical_Activity', 'Diet_Quality', 'Social_Support', 
                                        'Relationship_Status', 'Substance_Use', 'Extracurricular_Involvement', 
                                        'Financial_Stress'])
            line_chart = filteredbygender[line_att].value_counts()
            st.line_chart(line_chart)

        # 5th Visualization
        elif visual_type2 == 'Area':
            st.subheader('Area Chart')
            area_att = st.selectbox('Choose an attribute:', 
                                       ['Age', 'Course', 'Stress_Level', 'Depression_Score', 'Anxiety_Score', 
                                        'Sleep_Quality', 'Physical_Activity', 'Diet_Quality', 'Social_Support', 
                                        'Relationship_Status', 'Substance_Use', 'Extracurricular_Involvement', 
                                        'Financial_Stress'])
            area_chart = filteredbygender[area_att].value_counts()
            st.area_chart(area_chart)

        # 6th Visualization
        elif visual_type == 'Pie':
            st.subheader('Pie Chart')
            pie_att = st.selectbox('Choose an attribute:', 
                           ['Course', 'Sleep_Quality', 'Physical_Activity', 'Diet_Quality', 'Social_Support', 
                            'Relationship_Status', 'Substance_Use', 'Counseling_Service_Use', 
                            'Chronic_Illness', 'Extracurricular_Involvement', 'Residence_Type'])
    
            pie_chart = filteredbygender[pie_att].value_counts().reset_index()
            pie_chart.columns = ['Labels', 'Values']

            fig = px.pie(pie_chart, values='Values', names='Labels', template='plotly_dark')
            fig.update_layout(height=650, width=850)
            st.plotly_chart(fig)
