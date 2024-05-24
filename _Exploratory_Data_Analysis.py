#!/usr/bin/env python
# coding: utf-8

#              Automobile Exploratory Data Analysis

# In[1]:


get_ipython().system('pip install pandas')


# In[2]:


get_ipython().system('pip install pandas-profiling')


# In[32]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# create a data frame for Automobile_price_data_raw csv file into dataframe
# In[33]:


data =pd.read_csv("C:/Users/ADMIN/Downloads/Automobile price data _Raw_.csv")


# In[34]:


data.head()


# In[35]:


data.tail()


# In[36]:


#Display Name of entitys or columns
data.shape


# In[37]:


#Display name of columns
data.columns


# In[38]:


# information about the data like data types ,columns, rows ,null values
data.info()


# In[39]:


# calculate the null value in a columns
data.isnull().sum()


# In[62]:


# describe the statistics of the data
data.describe()


# In[63]:


data.describe(include="object")


# In[64]:


# all unique values is normalized-losses column
data["normalized-losses"].unique()


# In[65]:


# replace the "?" with np.nan values by using replace function
data["normalized-losses"]=data["normalized-losses"].replace("?",np.NaN)


# In[66]:


data["normalized-losses"]


# In[67]:


# change the data type
data["normalized-losses"] =pd.to_numeric(data["normalized-losses"],errors="coerce")


# In[68]:


data["normalized-losses"]


# #here the datatype is change converting object into float64

# In[69]:


# calculate the mean ,mode,median of normalized-losses column
normalized_osses_summary ={"mean": data["normalized-losses"].mean(),"median" : data["normalized-losses"].median(),"mode" : data["normalized-losses"].mode()}
normalized_osses_summary


# In[70]:


# fill the nan value into mean value
data["normalized-losses"]=data["normalized-losses"].fillna(data["normalized-losses"].mean())


# In[71]:


data["normalized-losses"]


# In[72]:


data["bore"] =pd.to_numeric(data["bore"],errors="coerce")
data["bore"] = data["bore"].fillna(data["bore"].mean())
data["bore"]


# In[73]:


data["horsepower"] =pd.to_numeric(data["horsepower"],errors="coerce")
data["horsepower"] = data["horsepower"].fillna(data["horsepower"].mean())
data["horsepower"]


# In[74]:


data["stroke"] =pd.to_numeric(data["stroke"],errors="coerce")
data["stroke"] = data["stroke"].fillna(data["stroke"].mean())
data["stroke"]


# In[75]:


data["price"] =pd.to_numeric(data["price"],errors="coerce")
data["price"] = data["price"].fillna(data["price"].mean())
data["price"]


# In[76]:


data["wheel-base"] =pd.to_numeric(data["wheel-base"],errors="coerce")
data["wheel-base"] = data["wheel-base"].fillna(data["wheel-base"].mean())
data["wheel-base"]


# In[77]:


data.info()


# In[78]:


# save the clean data file to new csv file
cleaned_data =data.to_csv("C:/Users/ADMIN/Downloads/Automobile price data _Raw_.csv")

            1  Perform (EDA) Exploratory Data Analysis
# In[79]:


plt.figure(figsize=(6,4))
sns.boxplot(x='body-style',y='price' ,data=data,color='pink')
plt.title("Body Style Price")
plt.xlabel('body-style')
plt.ylabel('price')
plt.xticks(rotation=10)
plt.show()


# In[80]:


pip install PyQt5


# In[81]:


sns.barplot(x=data["num-of-cylinders"] ,y=data ["price"],data=data)
plt.title("price v\s cylinders")
plt.xlabel('number of cylinders')
plt.xticks(rotation=45)
plt.figure(figsize=(12,8))
plt.show()


# In[82]:


sns.scatterplot(x=data['height'],y=data['width'],color ='red')

   In this sccter plot show the corelation between height and width
# In[83]:


sns.lineplot(x=data['stroke'],y=data['horsepower'],color ='#9966cc')
plt.title(" Display the Stroke and Horsepower")


# In[84]:


plt.boxplot(x=data['stroke'])


# In[85]:


sns.countplot(y=data['make'],data=data,color='pink')
plt.title("Automobile per cars")
plt.tight_layout()
plt.show()


# In[86]:


plt.figure(figsize=(6,5))
sns.countplot(x='engine-type' , hue='symboling',data=data)
plt.xlabel('engine-type')
plt.ylabel('count')
plt.title('symboling distribution by engine-type')
plt.show()


# In[87]:


plt.figure(figsize=(6,5))
sns.barplot(x=data['engine-type'] , y =data['engine-size'], hue=data['num-of-cylinders'])
plt.xlabel('engine-type')
plt.ylabel('engine-size')
plt.title(' distribution of engine-type v\s engine-size')
plt.show()


# In[88]:


plt.figure(figsize=(8,4))
sns.barplot(x=data['engine-type'],y=data['price'] ,color='skyblue')
plt.xlabel('engine type')
plt.ylabel('price')
plt.title("engine type v/s price")
plt.show()


# In[89]:


plt.figure(figsize=(6,4))
sns.barplot(x=data['fuel-type'],y=data['make'] ,color='Green')
plt.show()


# In[90]:


plt.figure(figsize=(8,5))
sns.lineplot(x=data['horsepower'],y=data['city-mpg'])
plt.xlabel('horsepower')
plt.ylabel('city-mpg range')
plt.title('Horsepower by average city-mpg range')
plt.show()


# In[95]:


#correlation matrix

n_data= data.select_dtypes(include=["Int64","Float64"])
Correlation_matrix=n_data.corr().round(2)
Correlation_matrix


# In[96]:


plt.figure(figsize=(10,6))
sns.heatmap(Correlation_matrix ,annot=True)
plt.show()


# In[ ]:


cleaned_data 

