import os
import sys

join=os.path.join
drs=os.getcwd().split('\\')
direc=''
for i in drs[:-1]:
    direc+=i+'\\'

outpath=join(direc,'output')
codepath=join(direc,'code')
datapath=join(direc,'data2')

print('The route directory: direc:',direc)
print('Will get code from: codepath:',codepath)
print('Will send code to: outpath:',outpath)
print('If data is needed it will look in: datapath: ', datapath) 

dr=codepath
sys.path.append(dr)