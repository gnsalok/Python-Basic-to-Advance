
#Histogram 

import matplotlib.pyplot as plt

fig=plt.figure("Histogram")

ax = fig.add_subplot(1,1,1)

ax.hist([10,20,25,35,45,55,60,80,70,90,90,100],bins=8,facecolor="black", normed=True)

plt.title("Distribution")
plt.xlabel("Range")
plt.ylabel("Amount")
plt.show()



#working with Box
fig2=plt.figure("Box-plot")
ax1=fig2.add_subplot(1,1,1)
ax1.boxplot([21,12,25,11,30,15,40,20])

plt.title("Box-plot")
plt.xlabel("Range")
plt.ylabel("Amount")
plt.show()