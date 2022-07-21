
#------------- import necessary modules -----------------
import csv
import numpy as np


#=================================================================================
#given a file this function returns a matrix with the numerical data in columns 
# and lines format. 

#ignore should be set to 0. This version is still not suited to read headers
#=================================================================================
def readmatrix(filename,ignore=0):

#--------------- Calculate number of files and columns in the file ---------------
    with open(filename) as file:
        for nlines, line in enumerate(file): #enumerates the lines starting from 0
            pass
        num_lines=nlines+1-ignore

    with open(filename) as file:
        reader=csv.reader(file, delimiter='\t', skipinitialspace=True) 
        #we setted tab as delimiter between numbers
        first_row = next(reader)
        num_cols = len(first_row)

    print('The file', filename ,'has ',num_lines,' lines and ',num_cols,' columns')

    data=np.zeros((num_lines,num_cols))


    file=open(filename, 'r')
    data=[line.split() for line in file]

    if ignore>0:
        header=data[0:ignore]
        print(header)
        data=data[ignore:num_lines][:]
        data=np.array(data)
        data=data.astype(float)

    if ignore==0:
        print('does this file have no header?')
        data=data[ignore:num_lines][:]
        data=np.array(data)
        #print(type(data))
        #print(data)
        data=data.astype(float)

    file.close()
    return data

#================================================================================
