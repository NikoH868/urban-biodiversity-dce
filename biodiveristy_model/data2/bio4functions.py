from bio1prepare import *
def wtp1f(z,df1):
    c1='WTP in annual tax for a 1% increase in bumblebees'
    c2='WTP in annual tax for a 1% increase in house sparrows'
    c3='WTP in annual tax for a 1% increase in holly blue butterflies'
    c4='WTP in annual tax for a 1% increase in hedgehogs'
    c5='WTP in annual tax for a 1% increase in pipistrelle bats'

    labwtp=[c1,c2,c3,c4,c5]
    wtpsummary=cc([frame(z['beta_mu']).mean(),frame(z['beta_mu']).median(),frame(z['beta_mu']).std(),
                     frame(z['beta_mu']).quantile([.05,.95]).T])
    wtpsummary.columns=['mean','median','stdv','5%','95%']
    wtpsummary.index=labwtp
    
    wtpsummary.iloc[0]=100*wtpsummary.loc[c1]/df1.iloc[0]
    wtpsummary.iloc[1]=100*wtpsummary.loc[c2]/df1.iloc[1]
    wtpsummary.iloc[2]=100*wtpsummary.loc[c3]/df1.iloc[2]
    wtpsummary.iloc[3]=100*wtpsummary.loc[c4]/df1.iloc[3]
    wtpsummary.iloc[4]=100*wtpsummary.loc[c5]/df1.iloc[4]
    wtpsummary1=wtpsummary
    
    c1='WTP in annual tax for a 60% increase in bumblebees'
    c2='WTP in annual tax for a 60% increase in house sparrows'
    c3='WTP in annual tax for a 60% increase in holly blue butterflies'
    c4='WTP in annual tax for a 60% increase in hedgehogs'
    c5='WTP in annual tax for a 60% increase in pipistrelle bats'

    labwtp=[c1,c2,c3,c4,c5]
    wtpsummary=cc([frame(z['beta_mu']).mean(),frame(z['beta_mu']).median(),frame(z['beta_mu']).std(),
                           frame(z['beta_mu']).quantile([.05,.95]).T])
    wtpsummary.columns=['mean','median','stdv','5%','95%']
    wtpsummary.index=labwtp
    
    wtpsummary.iloc[0]=100*wtpsummary.loc[c1]
    wtpsummary.iloc[1]=100*wtpsummary.loc[c2]
    wtpsummary.iloc[2]=100*wtpsummary.loc[c3]
    wtpsummary.iloc[3]=100*wtpsummary.loc[c4]
    wtpsummary.iloc[4]=100*wtpsummary.loc[c5]
    wtpsummary2=wtpsummary
    
    wtp_sq=-100*cc([frame(z['theta_mu']).mean(),-frame(z['theta_std']).mean()]).T
    wtp_sq.columns=['WTP in annual tax to avoid the status quo']
    wtp_sq=wtp_sq.T
    wtp_sq.columns=[['mean','std of mean']]
    
    return wtpsummary1,wtpsummary2,wtp_sq 

#These are the mean plots for the WTP for the difference between the miniumn and maximum levels of the attributes

def plot_wtp_means(z):
    pltsize(8, 15)
    fig, ax = plt.subplots(2, 3)
    
    # Plot for bumblebees
    data0 = frame(100 * z['beta_mu'])[0]
    data0.plot(title='Mean WTP bumblebees', ax=ax[0, 0], kind='hist', bins=100, grid=True)
    mean0 = data0.mean()
    ax[0, 0].axvline(x=mean0, color='black', linestyle='--', linewidth=1.5)
    ax[0, 0].text(mean0, ax[0, 0].get_ylim()[1] * 0.9, f'Mean: {mean0:.2f}', color='black', ha='center')
    ax[0, 0].set_xlim(-20, 30)  # Adjust x-axis to show negative values

    # Plot for house sparrows
    data1 = frame(100 * z['beta_mu'])[1]
    data1.plot(title='Mean WTP house sparrows', ax=ax[0, 1], kind='hist', bins=100, grid=True)
    mean1 = data1.mean()
    ax[0, 1].axvline(x=mean1, color='black', linestyle='--', linewidth=1.5)
    ax[0, 1].text(mean1, ax[0, 1].get_ylim()[1] * 0.9, f'Mean: {mean1:.2f}', color='black', ha='center')
    ax[0, 1].set_xlim(-20, 30)  # Adjust x-axis to show negative values

    # Plot for holly blue butterflies
    data2 = frame(100 * z['beta_mu'])[2]
    data2.plot(title='Mean WTP holly blue butterflies', ax=ax[0, 2], kind='hist', bins=100, grid=True)
    mean2 = data2.mean()
    ax[0, 2].axvline(x=mean2, color='black', linestyle='--', linewidth=1.5)
    ax[0, 2].text(mean2, ax[0, 2].get_ylim()[1] * 0.9, f'Mean: {mean2:.2f}', color='black', ha='center')
    ax[0, 2].set_xlim(-20, 30)  # Adjust x-axis to show negative values

    # Plot for hedgehogs
    data3 = frame(100 * z['beta_mu'])[3]
    data3.plot(title='Mean WTP hedgehogs', ax=ax[1, 0], kind='hist', bins=100, grid=True)
    mean3 = data3.mean()
    ax[1, 0].axvline(x=mean3, color='black', linestyle='--', linewidth=1.5)
    ax[1, 0].text(mean3, ax[1, 0].get_ylim()[1] * 0.9, f'Mean: {mean3:.2f}', color='black', ha='center')
    ax[1, 0].set_xlim(-20, 30)  # Adjust x-axis to show negative values

    # Plot for pipistrelle bats
    data4 = frame(100 * z['beta_mu'])[4]
    data4.plot(title='Mean WTP pipistrelle bats', ax=ax[1, 1], kind='hist', bins=100, grid=True)
    mean4 = data4.mean()
    ax[1, 1].axvline(x=mean4, color='black', linestyle='--', linewidth=1.5)
    ax[1, 1].text(mean4, ax[1, 1].get_ylim()[1] * 0.9, f'Mean: {mean4:.2f}', color='black', ha='center')
    ax[1, 1].set_xlim(-20, 30)  # Adjust x-axis to show negative values

    plt.tight_layout()
    plt.show()

def plot_wtp_stdv(z):
    pltsize(8,15)
    fig,ax=plt.subplots(2,3)
    frame(z['beta_std'])[0].plot(title='STDV WTP bumblebees',ax=ax[0,0],kind='hist',bins=100,grid=True)
    frame(z['beta_std'])[1].plot(title='STDV WTP house sparrows',ax=ax[0,1],kind='hist',bins=100,grid=True)
    frame(z['beta_std'])[2].plot(title='STDV WTP holly blue butterflies',ax=ax[0,2],kind='hist',bins=100,grid=True)
    frame(z['beta_std'])[3].plot(title='STDV WTP hedgehogs',ax=ax[1,0],kind='hist',bins=100,grid=True)
    frame(z['beta_std'])[4].plot(title='STDV WTP pipistrelle bats',ax=ax[1,1],kind='hist',bins=100,grid=True)
    return

def iwtpf(z,df1):
#Calculating the individuals willingness to pay
    wtpi0=[]
    wtpi1=[]
    i=1
    for i in range(shape(z['beta'])[1]):
        wtpi0=wtpi0+[100*squeeze(array(meanc(z['beta'][:,i,:])))/array(df1.iloc[0:5])]
        wtpi1=wtpi1+[100*squeeze(array(meanc(z['beta'][:,i,:])))]
    
    wtpi0=frame(wtpi0)
    wtpi1=frame(wtpi1)
    wtpi0.columns=['bumblebees','house sparrows','holly blue butterflies','hedgehogs','pipistrelle bats']
    wtpi1.columns=['bumblebees','house sparrows','holly blue butterflies','hedgehogs','pipistrelle bats']
    return findex(wtpi0),findex(wtpi1)

def plotiwtp(wtpi):
    #These are the individual plots for the WTP for the difference between the miniumn and maximum levels of the attributes
    fig,ax=plt.subplots(2,3)
    wtpi['bumblebees'].plot(kind='hist',grid=True,ax=ax[0,0],bins=100,title='bumblebees')
    wtpi['house sparrows'].plot(kind='hist',grid=True,ax=ax[0,1],bins=100,title='house sparrows')
    wtpi['holly blue butterflies'].plot(kind='hist',grid=True,ax=ax[0,2],bins=100,title='holly blue butterflies')
    wtpi['hedgehogs'].plot(kind='hist',grid=True,ax=ax[1,0],bins=100,title='hedgehogs')
    wtpi['pipistrelle bats'].plot(kind='hist',grid=True,ax=ax[1,1],bins=100,title='pipistrelle bats')
    return

#This function computes the WTP for each of the options 2 and 3 (non sq) EXCLUDING the status quo effect for the choces they were offered
#i is the respondent
def wtpforx(i,z,ids,y,X1,X2):
    coeff=frame(z['beta'][:,i-1,:]).mean()
    s=ids==i
    x1i=X1[s]
    x2i=X2[s]
    yi=twodma(y[s])
    wtp1=twodma(array(frame(x1i)[[1,2,3,4,5,6,7,8]]).dot(coeff))
    p1=twodma(array(frame(x1i)[[0]]))
    wtp2=twodma(array(frame(x2i)[[1,2,3,4,5,6,7,8]]).dot(coeff)) 
    p2=twodma(array(frame(x2i)[[0]]))
    prem1=wtp1+p1
    prem2=wtp2+p2
    w=100*findex(cc([wtp1,wtp2,-p1,-p2,prem1,prem2,yi/100]))
    w.columns=['wtp2','wtp3','tax2','tax3','premium2','premium3','choice30']
    w1=w.loc[1:8]
    w1['choice30']=array
    sq=-findex(z['theta']).loc[i].mean()*100
    sq=['wtp to avoid sq',sq]
    return w1,sq
