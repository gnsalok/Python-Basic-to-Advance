
#Histogram 

import matplotlib.pyplot as plt

fig=plt.figure("Histogram")

ax = fig.add_subplot(1,1,1)

ax.hist([10,20,25,35,45,55,60,80,70,90,90,100],bins=8,facecolor="brown", normed=True)

plt.title("Distribution")
plt.xlabel("Range")
plt.ylabel("Amount")
plt.show()
