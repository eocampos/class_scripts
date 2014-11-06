
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  6 11:33:11 2014

Generates random data and plots histogram of it

@author: EOCampos
"""
import numpy as np
import matplotlib.pyplot as plt

random_numbers = np.random.normal(0,1,1000)

plt.hist(random_numbers, 100)
plt.show()
