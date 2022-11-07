import pymysql
db = pymysql.connect(host='database-2.cxx3vliix7rd.us-east-1.rds.amazonaws.com',user='admin',password='adminadmin')
cursor = db.cursor()
cursor.execute("use ACQ")
print(cursor.fetchone())
cursor.execute("select Value,timeOfProbe from ACQ.historian where ID_Location = 2 AND timeOfProbe > '2022-10-13 00:00:00'")
data = cursor.fetchall()
print(data[1][0])
tab = []
ox = []
i= 0
for x in range(len(data)):
    if data[x][0] < 60:
        tab.append(data[x][0])
        ox.append(data[x][1])
        i+=1
cursor.execute("select Value,timeOfProbe from ACQ.historian where ID_Location = 3 AND timeOfProbe > '2022-10-13 00:00:00' AND timeOfProbe < '2022-10-14 00:00:00'")
data = cursor.fetchall()
print(data[1][0])
tab2 = []
ox2 = []
i= 0
for x in range(len(data)):
    if data[x][0] < 60:
        tab2.append(data[x][0])
        ox2.append(data[x][1])
        i+=1
cursor.execute("select Value,timeOfProbe from ACQ.historian where ID_Location = 1 AND timeOfProbe > '2022-10-13 00:00:00'")
data = cursor.fetchall()
print(data[1][0])
tab3 = []
ox3 = []
i= 0
for x in range(len(data)):
    if data[x][0] < 60:
        tab3.append(data[x][0])
        ox3.append(data[x][1])
        i+=1
import matplotlib.pyplot as plt
import numpy as np
# make data
#x = np.linspace(0,i,i)
x = ox
y = tab

# plot
fig, ax = plt.subplots()

ax.plot(x, y, '--bo',label='Outside')
ax.plot(ox2, tab2, '--go',label='Inside1')
ax.plot(ox3, tab3, '--ro',label='Inside2')
ax.legend()
#plt.xlim([0, 30])
#ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
#       ylim=(0, 8), yticks=np.arange(1, 8))

plt.show()