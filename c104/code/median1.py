from collections import Counter
import csv

with open("SOCR-heightWeight.csv",newline='') as f:
    reader=csv.reader(f)
    file_data=list(reader)

file_data.pop(0)

new_data=[]
for i in new_data:
    n_mun=file_data[i][1]
    new_data.append(float(reader))

    n=len(new_data)
    new_data.sort()

    if n%2==0:

        median1=float(new_data[n//2])
        median2=float(new_data[n//2-1])
        #median3=float(new_data[n//])

        median =(median1+median2)/2

    else:
        median=new_data[n//2]


print("median is "+str(median))




    

