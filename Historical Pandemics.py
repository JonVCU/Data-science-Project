#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df = pd.read_csv("Historical Panademics #.csv")


# In[3]:


#With many people around the world having already experieced life under a pandemic, A group of historians approach a data scientist to help them build an exhibit on the entire history of epidemics. 


# In[4]:


#I as the head of the project want to first retrieve a dataset of historical pandemics from human history and create graph to present the data in a viewer friendly way for a exhib.


# In[5]:


df.dtypes


# In[6]:


df.columns


# In[7]:


df.shape


# In[8]:


df.index


# In[9]:


df.describe()


# In[10]:


df.head(5)
df.tail(4)


# In[11]:


df.groupby(by=("Epidemics/pandemics")).sum()
#Used a groupby here because I want to find the sum so I can rank which epidemic/pandemics was the dealiest in order. As well as match the rank of each epidemics with date in a later groupby. 


# In[12]:


df.groupby(by=("Location")).sum()
#The reason why I groupby the locations for the sum here is because I wanted to see which regions were heavily affected.


# In[13]:


df.groupby(by=("Date")).sum()
#Here what I did was groupy to see which dates were the dealiest in the history of panademics to use for a latter graph.


# In[14]:


import plotly.express as px
fig = px.pie(df, values='Rank', names='Epidemics/pandemics')
fig.show()


# In[15]:


#I wanted to show a pie chart first because I believe that it would be the best viewing experienece for a visitor to an exhibit. 
#For my first pie chart, I wanted to display which were the worst epidemics/pandemics in history by rank. 


# In[16]:


import plotly.express as px
fig = px.pie(df, values='Rank', names='Disease')
fig.show()


# In[17]:


#For my second pie chart, I wanted to display the percentage of which type of diseases affected humans the most in all of history. 


# In[18]:


import plotly.express as px
fig = px.scatter(df, y="Death toll", x="Disease")
fig.show()


# In[19]:


import plotly.express as px
fig = px.scatter(df, y="Death toll", x="Epidemics/pandemics", )
fig.show()


# In[20]:


import plotly.express as px
fig = px.scatter(df, x="Rank", y="Death toll")
fig.show()


# In[21]:


import plotly.express as px
fig = px.scatter(x=df["Epidemics/pandemics"], y=df["Death toll"])
fig.show()
#I chose to use a scatter plot here because I wanted to rank which were the deadliest epidemics/pandemics by death toll (The deadliest is the Black Death).(In python 1 is replaced with 0 therefore that is why the graph is going in descending order)


# In[22]:


import plotly.express as px
fig = px.scatter(x=df["Disease"], y=df["Death toll"])
fig.show()


# In[23]:


fig = px.histogram(df, x= ["Epidemics/pandemics","Location"],  barmode="overlay")

fig.show()


# In[24]:


fig = px.histogram(df, x= ["Regional population lost","Location"],  barmode="overlay")
fig.show()
#The reason I wanted to use a histogram here is to note which regions had the greatest population lost and which locations were affected the most. As you can see on the x axis, it is displaying the percentage of the locations and it's lost in population.


# In[25]:


fig = px.histogram(df, x= ["Global population lost","Location"],  barmode="overlay")
fig.show()
#Here I am using a histogram to display the global population lost. On the left you can see the perceantages of the global population according to it's location on the right in red. Since I already did regionals, doing global was my next direction. Since the raw data has millions of numbers, that is why it is only showing percentage.  


# In[26]:


import plotly.express as px

fig = px.histogram(df, x="Rank", y="Epidemics/pandemics")
fig.update_layout(bargap=0.5)
fig.show()


# In[27]:


import plotly.express as px

fig = px.histogram(df, x="Rank", y="Disease")
fig.update_layout(bargap=0)
fig.show()


# In[28]:


import plotly.express as px
fig = px.scatter(df, x="Rank", y="Death toll", color="Location")
fig.show()


# In[29]:


import plotly.express as px
fig = px.scatter(df, x="Disease", y="Death toll", color="Location")
fig.show()


# In[30]:


#The historians wanted one interactive graph so they can use as an touch-screen display. For this graph, you can see which disease greatly affected a specific country. For example, the bubonic plague killed 1.25 million in southern Italy and 2 million in Persia. Vistors at the exhibit can touch and view whatever location they want.  


# In[ ]:





# In[ ]:




