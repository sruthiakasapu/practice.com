#colors:

import matplotlib.pyplot as plt

plt.title('mobile sales')
mobile_sales=['samsung','vivo','oppo','lenovo']
mobile_colors=['red','green','blue','black']
sales_march=[35,20,40,15]
plt.pie(sales_march,labels=mobile_sales,startangle=90,colors=mobile_colors)
plt.show()
