#shadow:

import matplotlib.pyplot as plt

plt.title('mobile sales')
mobile_sales=['samsung','vivo','oppo','lenovo']
sales_march=[35,20,40,15]
plt.pie(sales_march,labels=mobile_sales,startangle=90,shadow='true')
plt.show()
