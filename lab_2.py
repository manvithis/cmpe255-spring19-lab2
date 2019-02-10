
# coding: utf-8

# In[3]:


import numpy as np
num_friends=[100, 49, 41, 40, 25, 10, 5, 4, 7, 20, 60]
mean=np.mean(num_friends)
print("mean={}".format(mean))
median=np.median(num_friends)
print("median={}".format(median))


# In[5]:


from matplotlib import pyplot as plt
import math as mt
def normal_pdf(x, mu=0, sigma=1):
    y=(x-mu)**2
    z=2*sigma**2
    w=mt.exp(-(y/z))
    q=mt.sqrt(2*mt.pi*sigma**2)
    s=w/q
    return s
xs = [x / 10.0 for x in range(-50, 50)]
plt.plot(xs, [normal_pdf(x, sigma=1) for x in xs], '-', label='mu=0,sigma=1')
plt.plot(xs, [normal_pdf(x, sigma=2) for x in xs], '-', label='mu=0,sigma=2')
plt.plot(xs, [normal_pdf(x, sigma=0.5) for x in xs], '-', label='mu=0,sigma=0.5')
plt.plot(xs, [normal_pdf(x, sigma=-1) for x in xs], '-', label='mu=0,sigma=-1')
plt.legend()
plt.show()

