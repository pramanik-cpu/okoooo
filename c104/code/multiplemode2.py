from _typeshed import ReadableBuffer
from collections import Counter
import csv
from os import read
from types import resolve_bases

with open("SOCR-heightWeight.csv",newline='') as f:
    reader= csv.reader(f)
    file_data=list(reader)

file_data.pop()

new_data=[]
for i in new_data:
    n_num=file_data[i][1]
    new_data.append(float(reader))

n=len(new_data)
data=Counter(new_data)
get_mode=dict(data)

mode=[]
mode1=[]
mode2=[]

for a,v in get_mode.items():
    a=float(a)
    if 50<a<70:
        if v==max(list(data.values())):
            mode.append(a)
    elif 60<a<70:
        if v==max(list(data.values())):
            mode1.append(a)
    elif 70<a<75:
        if v==max(list(data.values())):
            mode2.append(a)

if len(mode)>len(mode1) and len(mode2):
    print("modeis "+''.join(map(str,mode)))
elif len(mode1)>len(mode2) and len(mode):
    print("mode is"+''.join(map(str,mode1)))
elif len(mode1)>len(mode2) and len(mode):
    print("mode is"+''.join(map(str,mode1)))






