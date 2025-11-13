def cardf(i,task,sq,opta,optb):
    t=task.loc[i]
    x0=sq
    x1=opta.loc[t]
    x2=optb.loc[t]
    return squeeze(array(x0)),array(x1),array(x2)

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


datapath='C:\\Users\\n_1ho\\Documents\\biodiversity_model_final_kelvin\\cmdstanpy\\data2'
name=datapath+'\\bio_dce_attrib_diff_final.xlsx'

choice30=findex(pd.read_excel(name,sheet_name='biodiversity choice'))
sq=findex(pd.read_excel(name,sheet_name='status quo'))
opta=findex(pd.read_excel(name,sheet_name='option A'))
optb=findex(pd.read_excel(name,sheet_name='option B'))
locat=findex(pd.read_excel(name,sheet_name='biodiversity location pref'))
reason=findex(pd.read_excel(name,sheet_name='biodiversity location reason'))
attend=findex(pd.read_excel(name,sheet_name='attribute attendance'))
socio=findex(pd.read_excel(name,sheet_name='sociodemographic'))

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

#status quo
sq_=sq
sq_.loc[1]=[0,0,0,0,0,0]

opta_['tax1']=-opta['tax1']/100/5
optb_['tax2']=-optb['tax2']/100/5

df1=opta_.max()-opta_.min()
df1['tax1']=1

df2=optb_.max()-optb_.min()
df2['tax2']=1

opta_=opta_/df1
optb_=optb_/df2

sq_=frame(array(sq_.loc[1])/df1).T

y30=choice30['choice']
card30=choice30['card shown']
id30=choice30['ID']


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




