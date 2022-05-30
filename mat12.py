#startangle

import matplotlib.pyplot as plt
import numpy as np

plt.title('mobile sales')

mobiles_labels=['samsung','vivo','oppo','lenovo']
sales_march=[55,20,10,15]
plt.pie(sales_march,labels=mobiles_labels,startangle=90)
plt.show()
