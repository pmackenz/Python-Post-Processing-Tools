'''
Created on Jun 28, 2017

@author: Smit
'''
'''
Created on Jun 20, 2017

@author: Smit
'''
import numpy as np
import matplotlib.pyplot as plt2
from StressPlots import *

def InctoTime(inc):
    h=(inc)*0.25
    hr=int(h)
    m=(h-hr)*60
    min=int(m)
    
    if hr>=10:
        hour=str(hr)
    elif hr==0:
        hour='00'
    else:
        hour='0'+str(hr)

    if min>=10:
        minutes=str(min)
    elif min==0:
        minutes='00'
    else:
        minutes='0'+str(min)
    
    time1=hour+minutes
    time2=hour+':'+minutes
    return [time1,time2]

def FindMaxStress(file):
    f=open(file,'r')
    hdr = f.readline()
    stress=[]
    for line in f:
        items = line.rstrip('\n').split('\t')
        stress.append(float(items[6]))
    f.close()
    MaxStress=max(stress)
    return MaxStress
        
def GetTimeArray():
    time1_array=[]
    time2_array=[]
    for i in range(0,97):
        [time1,time2]=InctoTime(i)
        time1_array.append(time1)
        time2_array.append(time2)
    return [time1_array,time2_array]
    
def PlotStress(time,stress,dia):
        plt2.plot(time,stress, '--r', linewidth=2)
        plt2.xlim(0., 24.)
        plt2.xticks([0,6,12,18,24],["00:00","6:00","12:00","18:00","24:00"])
        titlestring="Peak Maximum Principal Stress for {} cm diameter Boulder".format(dia)
        fine_name="Peak_Stress_{}.pdf".format(dia)
        plt2.title(titlestring)
        plt2.xlabel('Time (hr)')
        plt2.ylabel('Peak Maximum Principal Stress')       
        plt2.grid(True,which='major',axis='both')
        plt2.grid(True,which='minor',axis='both')
        plt2.savefig('../data/{}'.format(fine_name))
        plt2.hold(False)
        plt2.cla()
        #plt.show()
        
def PlotAllStress(details):
    
    for line in details:
        time=line['time']
        stress=line['stress']
        dia=line['diameter']
        plt2.plot(time,stress, linewidth=2,label=dia)
        plt2.hold(True)
        
        
    plt2.xlim(0., 24.)
    plt2.xticks([0,6,12,18,24],["00:00","6:00","12:00","18:00","24:00"])
    titlestring="Maximum Principal Stress over Time"
    fine_name="Peak_Stress_AllBoulders.pdf"
    plt2.title(titlestring)
    plt2.legend(loc='best',labelspacing=0, fontsize=12,ncol=2)
    plt2.xlabel('Time (hr)')
    plt2.ylabel('Peak Maximum Principal Stress')       
    plt2.grid(True,which='major',axis='both')
    plt2.grid(True,which='minor',axis='both')
    plt2.savefig('../data/{}'.format(fine_name))
    plt2.hold(False)
    plt2.cla() 
    #plt.clf() >Try this  
        
    
    
    

[time1_array,time2_array]=GetTimeArray()

    
boulder_dia=[62]

details=[]
NetMaxStress_array=[]
for i in boulder_dia:
    k = 0
    hour_array = []
    MaxStress_inc_array = []
    count = 0
    for j in time1_array:
        count+=1
        if (i == 200) or (i == 300) or (i == 500):
            if count <= 2:
                continue
        
        filename="../data/{}_direction_.bak/{}_direction_{}.txt".format(i,i,j)
        MaxStress_inc=FindMaxStress(filename)
        hour_array.append(int(j)/100.0)
        MaxStress_inc_array.append(MaxStress_inc)
        #print j
    #PlotStress(hour_array, MaxStress_inc_array, i)
    details.append({'time':hour_array,'stress':MaxStress_inc_array,'diameter':i})
    NetMaxStress_array.append(max(MaxStress_inc_array))


PlotAllStress(details)   

StressPlots('test2.txt',100,'0000','00:00',20)
'''
count=0
for p in boulder_dia:
    r=0
    for q in time1_array:
        filename="../data/{}_direction_.bak/{}_direction_{}.txt".format(p,p,q)
        StressPlots(filename,i,j,time2_array[k],NetMaxStress_array[count])
        #StressPlots(filename,p,q,time2_array[r])
        r+=1
    count+=1
        
'''
        

        
        
