import re
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter



match = r'/doWork/'
latency_data = re.compile(r'\d.\d\d\d')
filter_match = re.compile(match)


fd = open('/home/totallynottito/access_logs/all_logs.log')

def count_elements(data) ->dict :
    hist = {}
    for i in data :
        hist[i] = hist.get(i,0) + 1
    return hist


array = []
for line in fd:
    #print(str(line))
    
    filter = filter_match.search(str(line))
    if (filter) :
        found = latency_data.search(str(line))
        array.append(found[0])
        #print(filter)
    
    #found = latency_data.search(str(line))
    #array.append(found[0])
    
    #print(found[0])
    #if found[0][0] == 0 :
        #print(found)
        #array.append(float(found[0])

data = []
for n in range(len(array)) :
    if (int(array[n][0]) == 0) :
        data.append(float(array[n]))
    #print(int(array[n][0]))
#print(len(data))

pd.cut(data,1000)
counted = count_elements(data)

happy = pd.DataFrame.from_dict(counted, orient='index')


#happy = pd.DataFrame.from_dict(data, orient='index')
#print(type(happy))
plt.hist(happy)
plt.show()

"""
plot = np.array(counted)
times = np.array(data)
print(plot)
#print(type(counted))
fig, ax = plt.subplots(figsize = (10,7))
ax.hist(plot,bins = [0.000, 0.100, 0.200, 0.300, 0.400, 0.500, 0.600, 0.700, 0.800, 0.900])
plt.show()
"""
#print(times)
#recounted = Counter(data)

#if (recounted.items() == counted.items()) :
#    print('yay')

#print(counted)

#plt.hist(counted)


"""
np.set_printoptions(precision=3)
counted, bin_edges = np.histogram(data)

first_edge, last_edge = counted.min(),counted.max()
n_equal_bins = 10
bin_edges = np.linspace(start=first_edge, stop=last_edge,num=n_equal_bins + 1, endpoint=True)
bin_count = np.bincount(counted)
hist, _ = np.histogram(counted,range=(0,counted.max()+1))
np.array_equal(hist, bin_count)
dict(zip(np.unique(counted),bin_count[bin_count.nonzero()]))

np.histogram(counted,bins=10,range=(counted.min(),counted.max()),normed=None,weights=None,density=None)
"""

"""
size, scale = 1000,10
total = pd.Series(np.random.gamma(scale,size=size) ** 1.5)
total.plot.hist(grid=True,bins=20,rwidth=0.9,color='#607c8e')
plt.title('Latency Times: Sassassfrass Site')
plt.xlabel('Latency Time')
plt.ylabel('Counts')
plt.grid(axis='y', alpha=0.75)
"""

"""
n, bins, patches = plt.hist(x=data, bins='auto', color='#0504aa', alpha=0.7,rwidth=0.85)
plt.grid(axis='y',alpha=0.75)
plt.xlabel('Latency')
plt.ylabel('Frequency')
plt.title('Team Sassafrass')
plt.text(23,45,r'$\mu=15, b=3$')
maxfreq = counted.max()
plt.ylim(ymax=np.ceil(maxfreq/10) * 10 if maxfreq % 10 else maxfreq + 10)
"""



#print(bin_edges.size)
#print(data)