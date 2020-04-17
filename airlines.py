import pandas as pd
import datetime
import matplotlib.pyplot as plt
import numpy as np

alaska=pd.read_csv("ALK.csv")
spirit=pd.read_csv("SAVE.csv")
delta=pd.read_csv("DAL.csv")
sw=pd.read_csv("LUV.csv")

alaska.Date=alaska.Date.map(lambda x: datetime.datetime.strptime(x,'%Y-%m-%d'))
spirit.Date=spirit.Date.map(lambda x: datetime.datetime.strptime(x,'%Y-%m-%d'))
delta.Date=delta.Date.map(lambda x: datetime.datetime.strptime(x,'%Y-%m-%d'))
sw.Date=sw.Date.map(lambda x: datetime.datetime.strptime(x,'%Y-%m-%d'))


plt.style.use('default')
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)

ax1.plot(alaska.Date,alaska.Open)
plt.setp( ax1.xaxis.get_majorticklabels(), rotation=25 )
ax1.set_ylabel("Price")
ax1.set_title("Alaska Airlines")


ax2.plot(spirit.Date,spirit.Open)
plt.setp( ax2.xaxis.get_majorticklabels(), rotation=25 )
ax2.set_ylabel("Price")
ax2.set_title("Spirit Airlines")


ax3.plot(delta.Date,delta.Open)
plt.setp( ax3.xaxis.get_majorticklabels(), rotation=25 )
ax3.set_ylabel("Price")
ax3.set_title("Delta Air Lines")


ax4.plot(sw.Date,sw.Open)
plt.setp( ax4.xaxis.get_majorticklabels(), rotation=25 )
ax4.set_ylabel("Price")
ax4.set_title("Southwest Airlines")

fig.tight_layout(pad=1.0)





from datetime import timedelta

#Alaska
n=len(alaska.Date)-1
addons=[]

addons.append(alaska.Date[n])
addons.append(alaska.Date[n]+timedelta(days=3))
addons.append(alaska.Date[n]+timedelta(days=30))
addons.append(alaska.Date[n]+timedelta(days=90))
addons.append(alaska.Date[n]+timedelta(days=180))
addons.append(alaska.Date[n]+timedelta(days=270))


values=np.asarray([0,1.12,3.65,5.1,6.82,7.9]+alaska.Open[n])
addons=np.asarray(addons)

temp=pd.DataFrame(values,index=addons,columns=["Open"])

alaska=alaska[["Date","Open"]]
alaska=alaska.set_index("Date")


vol1=np.std((alaska["Open"]-alaska["Open"].shift(1))/alaska["Open"].shift(1)[0:220])
vol2=np.std((alaska["Open"]-alaska["Open"].shift(1))/alaska["Open"].shift(1))
vol=0.5*vol1+0.5*vol2 #short run + long run volatility

band=vol*np.sqrt([0,3,30,90,180,270])
upper=values*(1+band/2)
lower=values*(1-band/3)

temp_up=pd.DataFrame(upper,index=addons)
temp_down=pd.DataFrame(lower,index=addons)


fig, ax = plt.subplots()
ax.plot(alaska.resample('h').interpolate('quadratic'))
ax.plot(temp.resample('h').interpolate('quadratic'),alpha=0.7,color="green")
ax.plot(temp_up.resample('h').interpolate('quadratic'),color="orange")
ax.plot(temp_down.resample('h').interpolate('quadratic'),color="orange")
ax.fill_between(np.asarray(temp_up.resample('h').interpolate('quadratic').index).flatten(),np.asarray(temp_up.resample('h').interpolate('quadratic').values).flatten(),
                np.asarray(temp_down.resample('h').interpolate('quadratic').values).flatten(),color="orange",alpha=0.2)

plt.setp( ax.xaxis.get_majorticklabels(), rotation=25 )
ax.set_ylabel("Price")
ax.set_title("Alaska Airlines Stock Price Forecast based on Call options")












