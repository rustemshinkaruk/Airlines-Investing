import pandas as pd
import datetime
import matplotlib.pyplot as plt

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


