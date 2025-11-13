def cardf(i,task,sq,opta,optb):
    t=task.loc[i]
    x0=sq
    x1=opta.loc[t]
    x2=optb.loc[t]
    return squeeze(array(x0)),array(x1),array(x2)

import numpy as np
from shortercuts import findex,rows,squeeze,array,ones,zeros,frame,pd

def recode(df,y,old,new):
    dfs=df.copy()
    for i in dfs.index:
        k=0
        for j in old:
            if dfs.loc[i,y]==j:
                dfs.loc[i,y]=new[k]
            k=k+1
    if type(dfs.loc[i,y])==float:
        dfs[y]=dfs[y].astype(float)
    if type(dfs.loc[i,y])==int:
        dfs[y]=dfs[y].astype(int)    
    return dfs  


datapath='C:\\Users\\n_1ho\\Documents\\biodiversity_model_final_kelvin\\cmdstanpy\\datamerged'
name=datapath+'\\bio_dce_1_2_merged_dist.xlsx'

choice30=findex(pd.read_excel(name,sheet_name='biodiversity choice1'))
choice30AD=findex(pd.read_excel(name,sheet_name='biodiversity choice2'))
sq=findex(pd.read_excel(name,sheet_name='status quo'))
opta=findex(pd.read_excel(name,sheet_name='option A1'))
optb=findex(pd.read_excel(name,sheet_name='option B1'))
optaAD=findex(pd.read_excel(name,sheet_name='option A2'))
optbAD=findex(pd.read_excel(name,sheet_name='option B2'))
socio1=findex(pd.read_excel(name,sheet_name='sociodemographic1'))
socio2=findex(pd.read_excel(name,sheet_name='sociodemographic2'))

#DCE1
opta_=recode(opta,'bees1',['60% inc','45% inc','35% inc','25% inc','15% inc','10% inc','498 sightings'],[60,45,35,25,15,10,0])
opta_=recode(opta_,'sparrows1',['60% inc','45% inc','35% inc','25% inc','15% inc','10% inc','667 sightings'],[60,45,35,25,15,10,0])
opta_=recode(opta_,'butterflies1',['60% inc','45% inc','35% inc','25% inc','15% inc','10% inc','326 sightings'],[60,45,35,25,15,10,0])
opta_=recode(opta_,'hedgehogs1',['60% inc','45% inc','35% inc','25% inc','15% inc','10% inc','222 sightings'],[60,45,35,25,15,10,0])
opta_=recode(opta_,'bats1',['60% inc','45% inc','35% inc','25% inc','15% inc','10% inc','514 sightings'],[60,45,35,25,15,10,0])


optb_=recode(optb,'bees2',['60% inc','45% inc','35% inc','25% inc','15% inc','10% inc','498 sightings'],[60,45,35,25,15,10,0])
optb_=recode(optb_,'sparrows2',['60% inc','45% inc','35% inc','25% inc','15% inc','10% inc','667 sightings'],[60,45,35,25,15,10,0])
optb_=recode(optb_,'butterflies2',['60% inc','45% inc','35% inc','25% inc','15% inc','10% inc','326 sightings'],[60,45,35,25,15,10,0])
optb_=recode(optb_,'hedgehogs2',['60% inc','45% inc','35% inc','25% inc','15% inc','10% inc','222 sightings'],[60,45,35,25,15,10,0])
optb_=recode(optb_,'bats2',['60% inc','45% inc','35% inc','25% inc','15% inc','10% inc','514 sightings'],[60,45,35,25,15,10,0])

#DCE2
optaAD_=recode(optaAD,'bees1',['60% inc','45% inc','35% inc','25% inc','15% inc','10% inc','498 sightings'],[60,45,35,25,15,10,0])
optaAD_=recode(optaAD_,'sparrows1',['60% inc','45% inc','35% inc','25% inc','15% inc','10% inc','667 sightings'],[60,45,35,25,15,10,0])
optaAD_=recode(optaAD_,'butterflies1',['60% inc','45% inc','35% inc','25% inc','15% inc','10% inc','326 sightings'],[60,45,35,25,15,10,0])
optaAD_=recode(optaAD_,'hedgehogs1',['60% inc','45% inc','35% inc','25% inc','15% inc','10% inc','222 sightings'],[60,45,35,25,15,10,0])
optaAD_=recode(optaAD_,'bats1',['60% inc','45% inc','35% inc','25% inc','15% inc','10% inc','514 sightings'],[60,45,35,25,15,10,0])


optbAD_=recode(optbAD,'bees2',['60% inc','45% inc','35% inc','25% inc','15% inc','10% inc','498 sightings'],[60,45,35,25,15,10,0])
optbAD_=recode(optbAD_,'sparrows2',['60% inc','45% inc','35% inc','25% inc','15% inc','10% inc','667 sightings'],[60,45,35,25,15,10,0])
optbAD_=recode(optbAD_,'butterflies2',['60% inc','45% inc','35% inc','25% inc','15% inc','10% inc','326 sightings'],[60,45,35,25,15,10,0])
optbAD_=recode(optbAD_,'hedgehogs2',['60% inc','45% inc','35% inc','25% inc','15% inc','10% inc','222 sightings'],[60,45,35,25,15,10,0])
optbAD_=recode(optbAD_,'bats2',['60% inc','45% inc','35% inc','25% inc','15% inc','10% inc','514 sightings'],[60,45,35,25,15,10,0])

#status quo
sq_=sq
sq_.loc[1]=[0,0,0,0,0,0]

opta_['tax1']=-opta['tax1']/100/5
optb_['tax2']=-optb['tax2']/100/5
optaAD_['tax1']=-optaAD['tax1']/100/5
optbAD_['tax2']=-optbAD['tax2']/100/5

df1=opta_.max()-opta_.min()
df1['tax1']=1

df2=optb_.max()-optb_.min()
df2['tax2']=1

opta_=opta_/df1
optb_=optb_/df2

df1=optaAD_.max()-optaAD_.min()
df1['tax1']=1

df2=optbAD_.max()-optbAD_.min()
df2['tax2']=1

optaAD_=optaAD_/df1
optbAD_=optbAD_/df2

sq_ = frame(array(sq_.loc[1]) / df1).T


y30=choice30['choice']
card30=choice30['card shown']
id30=choice30['ID']
y30AD=choice30AD['choice']
card30AD=choice30AD['card shown']
id30AD=choice30AD['ID']

#build design matrices DCE1
X0=[]
X1=[]
X2=[]

for i in range(1,rows(y30)+1):
    #print(i,task[i])
    x0,x1,x2=cardf(i,card30,sq_,opta_,optb_)
    X0=X0+[x0]
    X1=X1+[x1]
    X2=X2+[x2]
X0=findex(X0)
X1=findex(X1)
X2=findex(X2)
X0['sq']=ones(rows(X0))
X1['sq']=zeros(rows(X1))
X2['sq']=zeros(rows(X2))
X0_30=X0[[5,0,1,2,3,4,'sq']].astype(float)
X1_30=X1[[5,0,1,2,3,4,'sq']].astype(float)
X2_30=X2[[5,0,1,2,3,4,'sq']].astype(float)

#Build design matrices DCE2
X0=[]
X1=[]
X2=[]

for i in range(1,rows(y30AD)+1):
    #print(i,task[i])
    x0,x1,x2=cardf(i,card30AD,sq_,optaAD_,optbAD_)
    X0=X0+[x0]
    X1=X1+[x1]
    X2=X2+[x2]
X0=findex(X0)
X1=findex(X1)
X2=findex(X2)
X0['sq']=ones(rows(X0))
X1['sq']=zeros(rows(X1))
X2['sq']=zeros(rows(X2))
X0_30AD=X0[[5,0,1,2,3,4,'sq']].astype(float)
X1_30AD=X1[[5,0,1,2,3,4,'sq']].astype(float)
X2_30AD=X2[[5,0,1,2,3,4,'sq']].astype(float)

# Combine and return for use in jupyter notebook
X0_all = pd.concat([X0_30, X0_30AD], ignore_index=True)
X1_all = pd.concat([X1_30, X1_30AD], ignore_index=True)
X2_all = pd.concat([X2_30, X2_30AD], ignore_index=True)

# Combine sociodemographic data
socio = pd.concat([socio1, socio2], ignore_index=True)

X = np.stack([X0_all.values, X1_all.values, X2_all.values], axis=1)
y = np.concatenate([y30, y30AD]) + 1
id_all = np.concatenate([id30, id30AD])
