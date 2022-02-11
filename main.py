import plotly.figure_factory as ff
import statistics
import random
import pandas as pd
import csv

df=pd.read_csv('Data.csv')
data=df['temp'].tolist()
#mean=statistics.mean(data)
#fig=ff.create_distplot([data],['temp'],show_hist=False)
#fig.show()

#sd=statistics.stdev(data)
#print('Mean of the data is:', mean)
#print('Standard Deviation of the data is:', sd)

#data_set=[]
#for i in range(0,100):
 #   random_index=random.randint(0,len(data))
  #  value=data[random_index]
   # data_set.append(value)

#sampleMean=statistics.mean(data_set)
#sampleStandardDeviation=statistics.stdev(data_set)
#print('Mean of sample data is:', sampleMean)
#print('Standard Deviation of sample data is:', sampleStandardDeviation)

dataSet=[]
for i in range(0,10000):
    random_index=random.randint(0,len(data))
    value=data[random_index]
    dataSet.append(value)

sampleMean2=statistics.mean(dataSet)
sampleStandardDeviation2=statistics.stdev(dataSet)
#print('Mean of sample data is:', sampleMean2)
#print('Standard Deviation of sample data is:', sampleStandardDeviation2)

def set(counter):
    dataSet=[]
    for i in range(0,counter):
        random_index=random.randint(0,len(data)-1)
        value=data[random_index]
        dataSet.append(value)
    mean=statistics.mean(dataSet)
    return mean

def plot(mean_list):
    df=mean_list
    fig=ff.create_distplot([df],['temp'],show_hist=False)
    fig.show()

def setup():
    mean_list=[]
    for i in range(0,1000):
        set_of_means=set(100)
        mean_list.append(set_of_means)
    plot(mean_list)

setup()