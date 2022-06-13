#!/usr/bin/env python
# coding: utf-8

# **This notebook is an exercise in the [Data Visualization](https://www.kaggle.com/learn/data-visualization) course.  You can reference the tutorial at [this link](https://www.kaggle.com/alexisbcook/distributions).**
# 
# ---
# 

# In this exercise, you will use your new knowledge to propose a solution to a real-world scenario.  To succeed, you will need to import data into Python, answer questions using the data, and generate **histograms** and **density plots** to understand patterns in the data.
# 
# ## Scenario
# 
# You'll work with a real-world dataset containing information collected from microscopic images of breast cancer tumors, similar to the image below.
# 
# ![ex4_cancer_image](https://i.imgur.com/qUESsJe.png)
# 
# Each tumor has been labeled as either [**benign**](https://en.wikipedia.org/wiki/Benign_tumor) (_noncancerous_) or **malignant** (_cancerous_).
# 
# To learn more about how this kind of data is used to create intelligent algorithms to classify tumors in medical settings, **watch the short video [at this link](https://www.youtube.com/watch?v=9Mz84cwVmS0)**.

# 
# 
# ## Setup
# 
# Run the next cell to import and configure the Python libraries that you need to complete the exercise.

# In[2]:


import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns
print("Setup Complete")


# The questions below will give you feedback on your work. Run the following cell to set up our feedback system.

# In[3]:


# Set up code checking
get_ipython().system('pip install -U -t /kaggle/working/ git+https://github.com/Kaggle/learntools.git@master')
from learntools.core import binder
binder.bind(globals())
from learntools.data_viz_to_coder.ex5 import *
print("Setup Complete")


# ## Step 1: Load the data
# 
# In this step, you will load the data.
# - Load the data file into a DataFrame called `cancer_data`.  
# - The corresponding filepath is `cancer_filepath`.  
# - Use the `"Id"` column to label the rows.

# In[5]:


# Path of the files to read
cancer_filepath = "../input/cancer.csv"

# Fill in the line below to read the file into a variable cancer_data
cancer_data = pd.read_csv(cancer_filepath, index_col="Id")

# Run the line below with no changes to check that you've loaded the data correctly
step_1.check()


# In[6]:


# Lines below will give you a hint or solution code
#step_1.hint()
#step_1.solution()


# ## Step 2: Review the data
# 
# Use a Python command to print the first 5 rows of the data.

# In[7]:


# Print the first five rows of the data
cancer_data.head()


# In the dataset, each row corresponds to a different image.  The dataset has 31 different columns, corresponding to:
# - 1 column (`'Diagnosis'`) that classifies tumors as either benign (which appears in the dataset as **`B`**) or malignant (__`M`__), and
# - 30 columns containing different measurements collected from the images.
# 
# Use the first 5 rows of the data to answer the questions below.

# In[9]:


# Fill in the line below: In the first five rows of the data, what is the
# largest value for 'Perimeter (mean)'?
max_perim = 87.46

# Fill in the line below: What is the value for 'Radius (mean)' for the tumor with Id 8510824?
mean_radius = 9.504

# Check your answers
step_2.check()


# In[10]:


# Lines below will give you a hint or solution code
#step_2.hint()
#step_2.solution()


# ## Step 3: Investigating differences

# #### Part A
# 
# Use the code cell below to create two histograms that show the distribution in values for `'Area (mean)'`, separately for both benign and malignant tumors.  (_To permit easy comparison, create a single figure containing both histograms in the code cell below._)

# In[12]:


# Histograms for benign and maligant tumors
sns.histplot(data=cancer_data, x='Area (mean)', hue='Diagnosis')

# Check your answer
step_3.a.check()


# In[13]:


# Lines below will give you a hint or solution code
#step_3.a.hint()
#step_3.a.solution_plot()


# #### Part B
# 
# A researcher approaches you for help with identifying how the `'Area (mean)'` column can be used to understand the difference between benign and malignant tumors.  Based on the histograms above, 
# - Do malignant tumors have higher or lower values for `'Area (mean)'` (relative to benign tumors), on average?
# - Which tumor type seems to have a larger range of potential values?

# In[14]:


step_3.b.hint()


# In[15]:


# Check your answer (Run this code cell to receive credit!)
step_3.b.solution()


# ## Step 4: A very useful column
# 
# #### Part A
# 
# Use the code cell below to create two KDE plots that show the distribution in values for `'Radius (worst)'`, separately for both benign and malignant tumors.  (_To permit easy comparison, create a single figure containing both KDE plots in the code cell below._)

# In[17]:


# KDE plots for benign and malignant tumors
sns.kdeplot(data=cancer_data, x='Radius (worst)', hue='Diagnosis', shade=True)

# Check your answer
step_4.a.check()


# In[18]:


# Lines below will give you a hint or solution code
#step_4.a.hint()
#step_4.a.solution_plot()


# #### Part B
# 
# A hospital has recently started using an algorithm that can diagnose tumors with high accuracy.  Given a tumor with a value for `'Radius (worst)'` of 25, do you think the algorithm is more likely to classify the tumor as benign or malignant?

# In[19]:


step_4.b.hint()


# In[20]:


# Check your answer (Run this code cell to receive credit!)
step_4.b.solution()


# ## Keep going
# 
# Review all that you've learned and explore how to further customize your plots in the **[next tutorial](https://www.kaggle.com/alexisbcook/choosing-plot-types-and-custom-styles)**!

# ---
# 
# 
# 
# 
# *Have questions or comments? Visit the [course discussion forum](https://www.kaggle.com/learn/data-visualization/discussion) to chat with other learners.*
