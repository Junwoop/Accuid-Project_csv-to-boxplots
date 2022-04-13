import pandas as pd
import numpy as np
import seaborn as sb
import matplotlib.pyplot as plt
from os import listdir

def Accuid_boxplot(csv):
    wb=pd.read_csv(csv)
    # drop unnecessary columns for proper melting
    wb=wb.drop([wb.columns[0],wb.columns[3],wb.columns[4]],axis=1)
    dd=pd.melt(wb,id_vars=["Sample1","Sample2"])
    logval=[] #for new column in dataframe
    for cell in dd['value']:
        if cell !=0:
            logval.append(np.log10(cell)) #apply log for y axis scaling
        else:
            logval.append(0)
    logval=pd.DataFrame(logval,columns=["newval"]) #convert list to dataframe and assign name
    newd=pd.concat([dd,logval],axis=1) #append logscaled value

    #seaborn boxplot: omit outliers and add title from CSV names
    sb.boxplot(x="variable",y="newval",data=newd,showfliers=False).set_title(csv[:-4])
    plt.savefig('%s.png'%csv[:-4])#switch to plt.savefig() to save fig directly
    plt.clf()#pyplot does not clear former plot, so clear it manually


path='C:/Users/dnalink-20200810/PycharmProjects/pythonProject2' #directory
csvs=[]
for f in listdir(path):
    if '.csv' in f:
        Accuid_boxplot(f)
