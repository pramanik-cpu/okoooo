import csv
from os import X_OK

with open("SOCR-heightWeight.csv",newline='') as f:
    reader=csv.reader(f)
    file_data=list(reader)

file_data.pop(0)

new_data=[]
for i in range(len(reader)):
    n_num=file_data[i][1]
    new_data.append(float(n_num))


n=len(new_data)
total=0
for i in new_data:
     total += i

mean= total/n
print("mean in"+str(mean))