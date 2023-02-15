
##############################DATA CLEANING####################################
#Importing liberaries
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

## Reading Filtered Dataset into Python
data =pd.read_csv (r'C:\Users\TOSHIBA\Downloads\CDA Material\Python Assignments\csv files\athlete_events.csv')
data.head()

### Finding missing values
data.loc[data.duplicated()]

#### keeping first row lock
(data.drop_duplicates(keep='first', inplace=True))

##### Taking average missing values of variables 
data_null = data.isna().mean().round(4) * 100
data_null.sort_values(ascending=False).head(5)

###### unique values in medal column
data.Medal.unique()

####### using fillna method 
data['Medal'].fillna(' ', inplace=True)
data.head()


######## filling by average of event column in age-height-weight 
data.Age=data.Age.fillna(data.groupby('Event')['Age'].transform('mean'))

data.Height=data.Height.fillna(data.groupby('Event')['Height'].transform('mean'))

data.Weight=data.Weight.fillna(data.groupby('Event')['Weight'].transform('mean'))

data.Age=np.floor(data.Age)
data.info()

######### filling by average of Sex column in age-height-weight 
data.Age=data.Age.fillna(data.groupby('Sex')['Age'].transform('mean'))

data.Height=data.Height.fillna(data.groupby('Sex')['Height'].transform('mean'))

data.Weight=data.Weight.fillna(data.groupby('Sex')['Weight'].transform('mean'))

data.Age = np.floor(data.Age)
data.info()

########## Checking missing values again
data_null = data.isna().mean().round(4) * 100
data_null.sort_values(ascending=False).head(15)
data.shape

########### Exporting Data to csv
data.to_csv('Filtered_csv')

