#Working with line

import matplotlib.pyplot as plt

fig=plt.figure("Line-Graph")
ax = fig.add_subplot(1,1,1)
ax.set_xlim([1,10])
ax.set_ylim([0,13])

ax.set_title('Line-Graph')
ax.set_xlabel('Qty.')
ax.set_ylabel('Amout')

ax.plot([1,2,4,7,8],[5,2,3,4,3],'r')

plt.show()