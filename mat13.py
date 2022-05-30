#explode:

import matplotlib.pyplot as plt

plt.title('mobile sales')
mobile_sales=['samsung','vivo','oppo','lenovo']
sales_march=[35,20,40,15]
explode=[0,0.2,0,0]
plt.pie(sales_march,labels=mobile_sales,startangle=90,explode=explode)
plt.show()
