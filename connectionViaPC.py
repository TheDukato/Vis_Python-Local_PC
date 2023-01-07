import pymysql
import matplotlib.pyplot as plt

f = open("conf.txt", "r")
strin = f.readlines()

db = pymysql.connect(host=strin[0][0:-1],user=strin[1][0:-1],password=strin[2][0:-1])
cursor = db.cursor()

cursor.execute("use ACQ")
print(cursor.fetchone())

ID_Loc = input("Enter ID_Location: ")

cursor.execute("select Value,timeOfProbe from ACQ.historian where ID_Location = "+ID_Loc+" ORDER BY timeOfProbe desc LIMIT 100")
data = cursor.fetchall()

tab = []
ox = []
i = 0
for x in range(len(data)):
    if data[x][0] < 60:
        tab.append(data[x][0])
        ox.append(data[x][1])
        i+=1

x = ox
y = tab

fig, ax = plt.subplots()

ax.plot(x, y, '--bo',label='Outside')
ax.legend()

plt.show()