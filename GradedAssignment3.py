#Importing liberaries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import streamlit as st

## Setting page configuration 
st.set_page_config(layout='wide')

### Dashboard Title and subheader
st.title('Olympic History Dashboard')
st.subheader('Created By Shahzaib Ahmed')

#### Reading Filtered Dataset into Python

data=pd.read_csv(r'D:\Filtered_csv')

##### Country drop down
all_countries=data['Team'].unique()
selection=st.selectbox('Select The Country', all_countries)
subset=data[data['Team']==selection]
st.dataframe(subset)

###### Creating Metrics
col1,col2,col3,col4=st.columns(4)
col1.metric('**TOTAL PARTICIPANTS**', '269,731', '')
col2.metric('**GOLD MEDALS**', '13,369', '')
col3.metric('**SILVER MEDALS**', '13,108', '')
col4.metric('**BRONZE MEDALS**', '13,295', '')

####### Defining columns
col1,col2,col3=st.columns(3)

with col1:
    st.header('Medals In Line Chart')
    chart_data= pd.DataFrame(
    np.random.rand(20,3),
    columns=['SILVER','BRONZE','GOLD'])

    st.line_chart(chart_data) 


with col2:
    medal_count=data['Medal'].value_counts()
    st.header('Medals Count')
    st.set_option('deprecation.showPyplotGlobalUse', False)
    plt.rcParams['figure.figsize']=[12,6]
    colors=['green','yellow','blue']
    fig=plt.bar(x=medal_count.index, height=medal_count.values, color=colors)
    
    plt.title('medal_count')
    plt.xlabel('Medals')
    plt.ylabel('medal_count')
    st.pyplot()
    
    
with col3:
    top_five_sports= data.groupby('Sport')['Medal'].value_counts().sort_values(ascending=False)
    st.header('Medals Received in each Sports Top 5')
    new = pd.DataFrame(top_five_sports)
    new.head(5)
    st.table(new.head(5))


col1,col2,col3=st.columns(3)

######## Defining columns    
with col1:
    plt.rcParams['figure.figsize']=[15,13]
    data['Team'].value_counts()
    country_winner=data[data.Team.isin(['United States','France','Great Britain','Italy','Germany'])]
    st.header('Medals won by Countries **Top 5** ')
    Top_five=country_winner.groupby(['Team'])['Medal'].value_counts().unstack().fillna(0)
    fig=Top_five.plot(kind='bar',stacked=True,color=['#17D7A0','#FF5403','#8E05C2'])
    st.pyplot()
    
with col2:
    st.header('Age distribution of the athletes')
    top_10_countries=data.Team.value_counts().sort_values(ascending=False).head(10)
    plt.figure(figsize=(15,14))
    plt.title ('')
    plt.xlabel('Age')
    plt.ylabel('Number Of articipants')
    plt.hist(data.Age, bins=np.arange(10,80,20), color='orange',edgecolor='white');
    st.pyplot()
    

with col3:
    plt.figure(figsize=(15,2.7))
    data.groupby('Sex')['Medal'].count().sort_values(ascending=False).plot(kind='pie',autopct='%0.05f%%')
    st.header('Medal By Gender')
    st.pyplot()

































































    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    














