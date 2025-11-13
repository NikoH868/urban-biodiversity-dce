import os
import pickle
import numpy as np
import matplotlib.pyplot as plt
from shortercuts import frame,shape,cols,rows,exp,meanc,sumc,maxc,minc,ln,twodma,twodmca,ones,cc,rc,squeeze,array,findex,zeros,sqrt,stdc,pd,np


def r_hat(sample,num_chains):
    num_samples=int(len(sample)/num_chains)
    samples=sample.reshape(num_chains,num_samples)
    # Assuming samples is a 2D array of shape (num_chains, num_samples)
    num_chains, num_samples = samples.shape
    
    # Calculate the within-chain variance
    W = np.mean(np.var(samples, axis=1, ddof=1))
    # Calculate the between-chain variance
    chain_means = np.mean(samples, axis=1)
    B = num_samples * np.var(chain_means, ddof=1)
    # Estimate the marginal posterior variance
    var_plus = ((num_samples ) / num_samples) * W + (1 / num_samples) * B
    # Calculate R-hat
    r_hat = np.sqrt(var_plus / W)
    return r_hat


def r_hat1(z,name,num_chains):
    rhats=[]
    shap=np.shape(z[name])
    print(shap)
    x=z[name]
    rhats+=[name,r_hat(x,num_chains)]
    return rhats

def r_hat2(z,name,num_chains):
    rhats=[]
    shap=np.shape(z[name])
    print(shap)
    for i in range(shap[1]):
            x=z[name][:,i]
            rhats+=[[name,i+1,r_hat(x,num_chains)]]
    return rhats

def r_hat3(z,name,num_chains):
    rhats=[]
    shap=np.shape(z[name])
    for i in range(shap[1]):
        for j in range(shap[2]):
            x=z[name][:,i,j]
            rhats+=[[name,i+1,j+1,r_hat(x,num_chains)]]
    return rhats

def delete_files_in_directory(directory_path):
   try:
     files = os.listdir(directory_path)
     for file in files:
       file_path = os.path.join(directory_path, file)
       if os.path.isfile(file_path):
         os.remove(file_path)
     print("All files deleted successfully.")
   except OSError:
     print("Error occurred while deleting files.")


def savemodel(sm,name):
    name=name+'.pkl'
    with open(name, 'wb') as f:
        pickle.dump(sm, f)
    return

def loadmodel(name):
    name=name+'.pkl'
    sm = pickle.load(open(name, 'rb'))
    return sm



#This is the WAIC information criteria for models and for comparison of models
def WAICf(f): #f here is (MCMC trials T, by Number of Data Points N)
    #f[:,n] is a T dimensional array
    #f[t,:] is a N dimensional array
    N=shape(f)[1] #The number of data points
    T=shape(f)[0] #The number of MCMC trials
    lppd=0
    mi=[]
    vlppd=[]
    maxloglik=maxc(sumc(f.T))     #Maximum of the log-likelihood encountered in the sample
    for i in range(N):
        wi=twodma(f[:,i])         #vector of logged densities for a data point
        lpdi=lmean(wi)            #the logged-Mean (across the mcmc draws) of the densities
        vlppd+=[lpdi]
        mi+=[meanc(wi)]         #list of Mean-logged densities for each data point by increment
    vlppd=twodma(squeeze(array(vlppd)))
    mi=twodma(squeeze(array(mi))) #list of Mean-logged densities  as a vector
    si=[]
    for i in range(N):
        wi=twodma(f[:,i])                 #vector of logged densities for a data point 
        S=rows(wi)                        #The number of MCMC samples
        si+=[sumc((wi-mi[i])**2)/(S-1)] #list of sum of squared deviations of wi from its mean for each data point
    si=twodma(squeeze(array(si)))         #si as an array
    elppdi=vlppd-si
    p_waic2=sumc(si)                 #This is the estimated variance of logged density for a point, pwaic type 2 (eq 13)
    p_waic1=2*sumc(vlppd)-2*sumc(mi) #This is the pwaic type 1
    elppd=sumc(vlppd)-p_waic2        #This needs to be maximised, it is called the elpd in the paper  
    waic=-2*elppd                    #This needs to be minimised   
    sewaic=2*(sqrt(N)*stdc(elppdi))
    out1=frame([float(waic),float(elppd),float(p_waic1),float(p_waic2),float(maxloglik),float(sewaic)])
    out1=out1.T
    out1.columns=['waic','elpd','p_waic1','p_waic2','maxloglik','se_waic']
    return out1,elppdi

def comparewaic(f1,f2):
    out1a,out2a=WAICf(f1)
    out1b,out2b=WAICf(f2)
    #This is the negativised eldp difference, a negative score indicates that the first model is preferred
    out=frame([float(-sumc(out2a-out2b)),float(sqrt(rows(out2a))*stdc(out2a-out2b))])
    out=out.T
    out.columns=['-elpd','se']
    print('A negative value favours the first model')
    return out

def lmean(z):
    T=rows(z)
    m=maxc(z)
    d=exp(z-m)
    return -ln(T)+m+ln(sumc(d))

def sortc(x,n=0,ascending=True):
    x=pd.DataFrame(x)
    z=twodma(x.sort_values(by=n,ascending=ascending))
    return(z)  
