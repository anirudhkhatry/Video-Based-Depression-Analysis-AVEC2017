import pandas as pd



"""
minimum,
maximum,
mean, 
mode, 
median, 
range,
mean deviation, 
variance, 
standard deviation, 
skewness,
kurtosis
"""

#TODO add loop to go through each file


dat=pd.read_csv('471_CLNF_AUs.csv') 


minimum_val=dat.min(axis=0)
print(minimum_val)

maximum_val=dat.max(axis=0)
print(maximum_val)

mean_val=dat.mean(axis=0)
print(mean_val)

mode=dat.mode(axis=0)
mode=mode.iloc[0]
print(mode)

median=dat.median(axis=0)
print(median)

"""Range idk how to find """

mean_deviation=dat.mad(axis=0)
print(mean_deviation)


variance_val=dat.var(axis=0)
print(variance_val)

std_deviation=dat.std(axis=0)
print(std_deviation)

skew_val=dat.skew(axis=0)
print(skew_val)

kurtosis_val=dat.kurtosis(axis=0)
print(kurtosis_val)