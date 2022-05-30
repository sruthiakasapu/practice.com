#adding labels to pie-graph

import matplotlib.pyplot as plt

plt.title('mobile sales')

mobiles_labels=['samsung','vivo','oppo','lenovo']
sales_march=[55,20,10,15]
plt.pie(sales_march,labels=mobiles_labels)
plt.show()
