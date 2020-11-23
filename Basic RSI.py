

from iqoptionapi.stable_api import IQ_Option
from talib.abstract import *
import numpy as np

API = IQ_Option("demosaha2537@outlook.com","shwchr15")
API.connect()


#get data
data = API.edsg_get_over_candles(1,1000,"EURUSD",1)


#get close data in Array
ip = {"close":np.array([])}
for i in data:
   data_close = i["close"]
   ip["close"]=np.append(ip["close"],data_close)
close = ip["close"]


#
timeperiod = 2
while True:
    data_rsi = RSI(close, timeperiod=timeperiod)

    # count RSI
    rs1 = 0
    rs2 = 0
    for i in data_rsi:
        if i > 70:
            rs1 = rs1 + 1
        if i > 71:
            rs2 = rs2 + 1
    #win point  
    if  rs1 > 10 and rs2 == 0:
        break
    elif timeperiod > 50:
        break
    else:
        timeperiod = timeperiod + 1

print("WIN :",rs1,"timeperiod :",timeperiod)





