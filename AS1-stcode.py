import pandas as pd 
import streamlit as st 
import seaborn as sns 
import matplotlib.pyplot as plt 

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
                                    ['Bar', 'Histogram', 'Scatter', 'Line', 'Area'])
    
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
            st.bar_chart(bar_graph)

        # 2nd Visualization
        elif visual_type == 'Histogram':
            st.subheader('Histogram')
            hist_att = st.selectbox('Choose an attribute:', 
                                   ['Age', 'CGPA', 'Semester_Credit_Load'])
    
            if hist_att == 'Age':
                fig, ax = plt.subplots()
                sns.histplot(filteredbygender[hist_att], kde=False, bins=[5,10,15,20,25,30,35,40], ax=ax)
                st.pyplot(fig)
            elif hist_att == 'CGPA':
                fig, ax = plt.subplots()
                sns.histplot(filteredbygender[hist_att], kde=False, bins=[2.5,3.0,3.5,4.0], ax=ax)
                st.pyplot(fig)
            else:
                fig, ax = plt.subplots()
                sns.histplot(filteredbygender[hist_att], kde=False, bins=[15,20,25,30], ax=ax)
                st.pyplot(fig)

        # 3rd Visualization
        elif visual_type == 'Scatter':
            st.subheader('Scatter Plot')
            x_axis = st.selectbox('Choose an attribute for x axis:', 
                              ['Age', 'CGPA', 'Stress_Level', 'Depression_Score', 
                               'Anxiety_Score', 'Financial_Stress', 'Semester_Credit_Load'], index=0)
            y_axis = st.selectbox('Choose an attribute for y axis:', 
                              ['Age', 'CGPA', 'Stress_Level', 'Depression_Score', 
                              'Anxiety_Score', 'Financial_Stress', 'Semester_Credit_Load'], index=1)

            sns.set_style('darkgrid')
            markers = {"Male": "X", "Female": "o"}
            fig, ax = plt.subplots()
            ax = sns.scatterplot(data=filteredbygender, x=x_axis, y=y_axis, markers=markers)
            plt.xlabel(x_axis)
            plt.ylabel(y_axis)
            plt.title("Scatter Plot")
            st.pyplot(fig)

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


    # Second Dashboard
    if dash_no == 'Second Dashboard':
        visual_type2 = st.selectbox('Select A Visualization:', 
                                 ['Bar', 'Histogram', 'Scatter', 'Line'])
    
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
            selected_column = st.selectbox('Choose an attribute:', 
                                       ['Age', 'CGPA', 'Stress_Level', 'Depression_Score', 
                                        'Anxiety_Score', 'Financial_Stress', 'Semester_Credit_Load'])
            st.write(sns.histplot(filteredbygender[selected_column], kde=True))
            st.pyplot()

        # 3rd Visualization
        elif visual_type2 == 'Scatter':
            st.subheader('Scatter Plot')
            x_axis = st.selectbox('Choose any attribute for x axis:', 
                              ['Age', 'CGPA', 'Stress_Level', 'Depression_Score', 
                               'Anxiety_Score', 'Financial_Stress', 'Semester_Credit_Load'], index=0)
            y_axis = st.selectbox('Choose any attribute for y axis:', 
                              ['Age', 'CGPA', 'Stress_Level', 'Depression_Score', 
                              'Anxiety_Score', 'Financial_Stress', 'Semester_Credit_Load'], index=1)

            sns.set_style('darkgrid')
            markers = {"Male": "X", "Female": "o"}
            fig, ax = plt.subplots()
            ax = sns.scatterplot(data=filteredbygender, x=x_axis, y=y_axis, markers=markers)
            plt.xlabel(x_axis)
            plt.ylabel(y_axis)
            plt.title("Scatter Plot")
            st.pyplot(fig)

        # 4th Visualization
        elif visual_type2 == 'Line':
            st.subheader('Line Chart')
