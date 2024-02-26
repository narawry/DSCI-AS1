import pandas as pd 
import streamlit as st 
import seaborn as sns 
import matplotlib.pyplot as plt 
import plotly.express as px 

df = pd.read_csv('students_mental_health.csv')

st.title("Students' Mental Health")

# Sidebar
st.sidebar.title('Home')
first_page = st.sidebar.radio('Click to view:', ('Data Overview', 'Dashboards'))
   
if first_page == 'Data Overview': 
    st.image('https://s3-prod.adage.com/s3fs-public/20230519_OPIN_MentalHealth_3x2.jpg', use_column_width=True)
    st.write('This application offers clear and simple visualizations for users '
             'to utilize in order to review, explore and comprehend the state of the students mental health.')  
     
    st.subheader('Overview of The Dataset')
    st.write(df.head(11))

if first_page == 'Dashboards':
    dash_no = st.sidebar.selectbox('Select a dashboard:', ['First (Main) Dashboard', 'Second Dashboard'])

    # First (Main) Dashboard
    if dash_no == 'First (Main) Dashboard':
    
        # Using st.radio to divide gender
        gender_rad = st.radio('Select a Gender:', ['Male', 'Female'])
        filteredbygender = df.loc[df['Gender'] == gender_rad]

        # 1st Visualization (Bar)
        st.subheader('1 - Factors of Mental Health')
        bar_att1 = st.selectbox('Choose an attribute:', 
                                       ['Sleep_Quality', 'Substance_Use', 'Counseling_Service_Use'])
        bar_chart = filteredbygender[bar_att1].value_counts()

        # Selectbox to choose what to filter
        filter_att = st.selectbox('Choose an attribute to filter:', 
                                      ['Stress_Level', 'Depression_Score', 'Anxiety_Score', 'Financial_Stress'])
            
        # Slider for filtering
        min_value = filteredbygender[filter_att].min()
        max_value = filteredbygender[filter_att].max()
        filtslide = st.slider(label=f'Adjust the filter:', min_value=min_value, max_value=max_value)
           
        filtered_df = filteredbygender[(filteredbygender['Stress_Level'] >= filtslide) &
                                           (filteredbygender['Depression_Score'] >= filtslide) &
                                           (filteredbygender['Anxiety_Score'] >= filtslide) &
                                           (filteredbygender['Financial_Stress'] >= filtslide)]
            
        bar_chart = filtered_df[bar_att1].value_counts()

        fig = px.bar(x=bar_chart.index, y=bar_chart.values, color=bar_chart.index, labels={'x': bar_att1, 'y': filter_att}, template='plotly_dark')
        fig.update_layout(title="Correlation Between Mental Health Factors", xaxis_title=bar_att1, yaxis_title=filter_att, height=600, width=800)
        st.plotly_chart(fig)

        # 2nd Visualization (Bar)
        st.subheader('2 - Mental Health vs Courses')
        bar_att2 = st.radio('Choose an attribute:', ['Stress_Level', 'Depression_Score', 'Anxiety_Score'])
            
        bar_chart = filteredbygender.groupby(['Course', bar_att2]).size().reset_index(name='Count')

        fig = px.bar(bar_chart, x='Course', y='Count', color=bar_att2, labels={'x': 'Course', 'y': 'Count'}, template='plotly_dark')
        fig.update_layout(title=f"Count for each {bar_att2} in different courses", xaxis_title='Course', yaxis_title='Count', height=600, width=800)
        st.plotly_chart(fig)

        # 3rd Visualization (Bar)
        st.subheader('3 - Mental Health vs Relationship Status')
        bar_att3 = st.selectbox('Select an attribute:', ['Stress_Level', 'Depression_Score', 'Anxiety_Score'])
            
        bar_chart = filteredbygender.groupby(['Relationship_Status', bar_att3]).size().reset_index(name='Count')

        fig = px.bar(bar_chart, x='Relationship_Status', y='Count', color=bar_att3, labels={'x': 'Relationship Status', 'y': 'Count'}, template='plotly_dark')
        fig.update_layout(title=f"Count for each {bar_att3} in relationship status", xaxis_title='Relationship Status', yaxis_title='Count', height=600, width=800)
        st.plotly_chart(fig)

        # 4th Visualization (Area)
        st.subheader('4 - Mental Health vs Physical Activity')
        area_att = st.selectbox('Choose an attribute:', 
                                    ['Stress_Level', 'Depression_Score', 'Anxiety_Score'])

        area_cat = st.selectbox('Choose one:', ['Physical_Activity', 'Extracurricular_Involvement'])
        category = st.radio('Choose a Category:', ['Low', 'Moderate', 'High'])
    
        filtered_df = filteredbygender[filteredbygender[area_cat] == category]

        area_chart = filtered_df[area_att].value_counts()

        fig = px.area(x=area_chart.index, y=area_chart.values, labels={'x': area_att, 'y': 'Count'}, template='plotly_dark')
        fig.update_layout(title=f"Count for each {area_att} in {category} category", xaxis_title=area_att, yaxis_title='Count', height=600, width=800)
        st.plotly_chart(fig)

        # 5th Visualization (Area)
        st.subheader('5 - Role of Social Support')
        area_att = st.selectbox('Choose an attribute:', 
                                    ['Sleep_Quality', 'Diet_Quality'])
    
        socsup_cat = st.radio('Choose a Social Support Category:',
                                    ['Low', 'Moderate', 'High'])
    
        filtered_df = filteredbygender[filteredbygender['Social_Support'] == socsup_cat]
        area_chart = filtered_df[area_att].value_counts()

        fig = px.area(x=area_chart.index, y=area_chart.values, labels={'x': area_att, 'y': 'Count'}, template='plotly_dark')
        fig.update_layout(title=f"Count for each {area_att} with {socsup_cat} Support", xaxis_title=area_att, yaxis_title='Count', height=600, width=800)
        st.plotly_chart(fig)

        # 6th Visualization (Pie)
        st.subheader('6 - Illness on Mental Health')
        pie_att = st.selectbox('Pick an attribute:', 
                                    ['Stress_Level', 'Depression_Score', 'Anxiety_Score'])
            
        # Slider for filtering
        min_value = filteredbygender[pie_att].min()
        max_value = filteredbygender[pie_att].max()
        filtslide = st.slider(label=f'Adjust to filter:', min_value=min_value, max_value=max_value)
           
        filtered_df = filteredbygender[(filteredbygender['Stress_Level'] >= filtslide) &
                                           (filteredbygender['Depression_Score'] >= filtslide) &
                                           (filteredbygender['Anxiety_Score'] >= filtslide)]
            
        pie_cat = st.selectbox('Choose one:', ['Chronic_Illness', 'Family_History'])

        pie_yes = filtered_df[filtered_df[pie_cat] == 'Yes'][pie_att]
        pie_no = filtered_df[filtered_df[pie_cat] == 'No'][pie_att]

        yes_total = pie_yes.value_counts().values[0] if not pie_yes.empty else 0
        no_total = pie_no.value_counts().values[0] if not pie_no.empty else 0

        fig = px.pie(names=['Yes', 'No'], values=[yes_total, no_total],
                title=f"{pie_att} vs {pie_cat}", labels={'names': pie_cat, 'values': 'Count'}, template='plotly_dark')
        fig.update_layout(height=650, width=850)
        st.plotly_chart(fig)




    # Second Dashboard
    if dash_no == 'Second Dashboard':
    
        # Using st.radio to divide gender
        gender_rad = st.radio('Gender', ['Male', 'Female'])
        filteredbygender = df.loc[df['Gender'] == gender_rad]

        # 1st Visualization
        st.subheader('Bar Graph')
        bar_att = st.selectbox('Choose an attribute:', 
                               ['Stress_Level', 'Depression_Score', 'Anxiety_Score', 'Financial_Stress'])
            
        bar_chart = filteredbygender.groupby(['Age', bar_att]).size().reset_index(name='Count')

        fig = px.bar(bar_chart, x='Age', y='Count', color=bar_att, labels={'x': 'Age', 'y': 'Count'}, template='plotly_dark')
        fig.update_layout(xaxis_title='Age', yaxis_title='Count', height=600, width=800)
        st.plotly_chart(fig)
    
        # 2nd Visualization
        st.subheader('Histogram')
        hist_att = st.radio('Choose an attribute:', ['CGPA', 'Semester_Credit_Load'])
            
        fig = px.histogram(filteredbygender, x=hist_att, template='plotly_dark')
        fig.update_layout(xaxis_title=hist_att, yaxis_title="Count")
        fig.update_traces(marker=dict(line=dict(width=1, color='White')))
        st.plotly_chart(fig)

        # 3rd Visualization
        st.subheader('Scatter Plot')
        x_axis = st.selectbox('Choose an attribute for x axis:', 
                              ['Age', 'CGPA', 'Stress_Level', 'Depression_Score', 
                               'Anxiety_Score', 'Financial_Stress', 'Semester_Credit_Load'], index=0)
        y_axis = st.selectbox('Choose an attribute for y axis:', 
                              ['Age', 'CGPA', 'Stress_Level', 'Depression_Score', 
                              'Anxiety_Score', 'Financial_Stress', 'Semester_Credit_Load'], index=1)

        fig = px.scatter(filteredbygender, x=x_axis, y=y_axis, color='Gender', template='plotly_dark')
        fig.update_layout(xaxis_title=x_axis, yaxis_title=y_axis, height=600, width=800)
        st.plotly_chart(fig)

        # 4th Visualization
        st.subheader('Line Chart')
        line_att = st.radio('Choose an attribute:', 
                                       ['Sleep_Quality', 'Diet_Quality'])
       
        line_chart = filteredbygender.groupby(['Course', line_att]).size().reset_index(name='Count')
        
        fig = px.line(line_chart, x='Course', y='Count', color=line_att, labels={'x': 'Course', 'y': 'Count'}, template='plotly_dark')
        fig.update_layout(xaxis_title='Course', yaxis_title='Count', height=600, width=800)
        st.plotly_chart(fig)

        # 5th Visualization
        st.subheader('Area Chart')
        area_att = st.selectbox('Choose an attribute:', 
                                       ['Age', 'Course', 'Stress_Level', 'Depression_Score', 'Anxiety_Score', 
                                        'Sleep_Quality', 'Physical_Activity', 'Diet_Quality', 'Social_Support', 
                                        'Relationship_Status', 'Substance_Use', 'Extracurricular_Involvement', 
                                        'Financial_Stress'])
        area_chart = filteredbygender[area_att].value_counts()
        st.area_chart(area_chart)

        # 6th Visualization
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
