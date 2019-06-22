#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os; os.chdir('..')
import multiprocessing
from prev_ob_models.Birgiolas2020.fitting import *


# In[2]:


import sys
cell_id = sys.argv[1] if len(sys.argv) > 1 and sys.argv[1].isdigit() else 5
print(cell_id)


# In[3]:


fitter = CellFitter(cell_type="gc", fitting_model_class="prev_ob_models.Birgiolas2020.isolated_cells.GC"+str(cell_id))


# In[ ]:


fitter.clear_cache()
fitter.fit(multiprocessing.cpu_count()*1.5, 15)

