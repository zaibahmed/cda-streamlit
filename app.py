import pandas as pd

import streamlit as st



st.header('Billionaire')


#file =r'C:\Users\Haier\Downloads\shahzaib material\Billionaire.csv'
df = pd.read_csv('Billionaire.csv')




#find the most popular source of income
#group_by = df.groupby('Source')
#income = group_by['Source'].count()
#print('the most popular source of income',income.nlargest(1))
#sour=df.groupby('Source')['Name'].count().sort_values()
#st.bar_chart(sour)

#find count of billionaires by country.

#bill_count = df.groupby('Country')['Name'].count().sort_values()
#st.bar_chart(bill_count)
#print('The count of billionaires are',bill_count)





#find the cumulative wealth of billionaries belongings to us

#df1=df['NetWorth'].apply(lambda x: float(x.replace '$', '').replace())


#all_countries = df['Country'].unique()

#selection = st.selectbox('Select Country', all_countries)

#subset = df[df['Country'] == selection]
#st.dataframe(subset) 

#all_source = df['Source'].unique()

#selection = st.selectbox('Select Source', all_source)

#subset = df[df['Source']== selection ]
#st.dataframe(subset)





all_countries = sorted(df['Country'].unique())

col1 , col2 = st.columns(2)

selected_country = col1.selectbox('Select Your Country',all_countries)

subset_country = df[df['Country'] == selected_country]


sources = sorted(subset_country['Source'].unique())

#display on stream lit

selected_source = col1.multiselect('Select source of income',sources)
subset_source = subset_country[subset_country['Source'].isin(selected_source)]

#columns 2
main_string = '{} - Billionaires'.format(selected_country)
col2.header(main_string)
col2.table(subset_country)
col2.header('Source wise info')
col2.dataframe(subset_source)






























