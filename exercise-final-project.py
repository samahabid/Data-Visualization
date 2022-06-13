#!/usr/bin/env python
# coding: utf-8

# **This notebook is an exercise in the [Data Visualization](https://www.kaggle.com/learn/data-visualization) course.  You can reference the tutorial at [this link](https://www.kaggle.com/alexisbcook/final-project).**
# 
# ---
# 

# Now it's time for you to demonstrate your new skills with a project of your own!
# 
# In this exercise, you will work with a dataset of your choosing.  Once you've selected a dataset, you'll design and create your own plot to tell interesting stories behind the data!
# 
# ## Setup
# 
# Run the next cell to import and configure the Python libraries that you need to complete the exercise.

# In[1]:


import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns
print("Setup Complete")


# The questions below will give you feedback on your work. Run the following cell to set up the feedback system.

# In[2]:


# Set up code checking
from learntools.core import binder
binder.bind(globals())
from learntools.data_viz_to_coder.ex7 import *
print("Setup Complete")


# ## Step 1: Attach a dataset to the notebook
# 
# Begin by selecting a CSV dataset from [Kaggle Datasets](https://www.kaggle.com/datasets).  If you're unsure how to do this, please revisit the instructions in the previous tutorial.
# 
# Once you have selected a dataset, click on the **[+ Add data]** option in the top right corner.  This will generate a pop-up window that you can use to search for your chosen dataset.  
# 
# ![ex6_search_dataset](https://i.imgur.com/cIIWPUS.png)
# 
# Once you have found the dataset, click on the **[Add]** button to attach it to the notebook.  You can check that it was successful by looking at the **Data** dropdown menu to the right of the notebook -- look for an **input** folder containing a subfolder that matches the name of the dataset.
# 
# <center>
# <img src="https://i.imgur.com/nMYc1Nu.png" width=30%><br/>
# </center>
# 
# You can click on the carat to the left of the name of the dataset to double-check that it contains a CSV file.  For instance, the image below shows that the example dataset contains two CSV files: (1) **dc-wikia-data.csv**, and (2) **marvel-wikia-data.csv**.
# 
# <center>
# <img src="https://i.imgur.com/B4sJkVA.png" width=30%><br/>
# </center>
# 
# Once you've uploaded a dataset with a CSV file, run the code cell below **without changes** to receive credit for your work!

# In[3]:


# Check for a dataset with a CSV file
step_1.check()


# ## Step 2: Specify the filepath
# 
# Now that the dataset is attached to the notebook, you can find its filepath.  To do this, begin by clicking on the CSV file you'd like to use.  This will open the CSV file in a tab below the notebook.  You can find the filepath towards the top of this new tab.  
# 
# ![ex6_filepath](https://i.imgur.com/fgXQV47.png)
# 
# After you find the filepath corresponding to your dataset, fill it in as the value for `my_filepath` in the code cell below, and run the code cell to check that you've provided a valid filepath.  For instance, in the case of this example dataset, we would set
# ```
# my_filepath = "../input/fivethirtyeight-comic-characters-dataset/dc-wikia-data.csv"
# ```  
# Note that **you must enclose the filepath in quotation marks**; otherwise, the code will return an error.
# 
# Once you've entered the filepath, you can close the tab below the notebook by clicking on the **[X]** at the top of the tab.

# In[5]:


# Fill in the line below: Specify the path of the CSV file to read
my_filepath = '../input/data-set/cancer_b.csv'

# Check for a valid filepath to a CSV file in a dataset
step_2.check()


# ## Step 3: Load the data
# 
# Use the next code cell to load your data file into `my_data`.  Use the filepath that you specified in the previous step.

# In[6]:


# Fill in the line below: Read the file into a variable my_data
my_data = pd.read_csv(my_filepath, index_col="Id")

# Check that a dataset has been uploaded into my_data
step_3.check()


# **_After the code cell above is marked correct_**, run the code cell below without changes to view the first five rows of the data.

# In[7]:


# Print the first five rows of the data
my_data.head()


# ## Step 4: Visualize the data
# 
# Use the next code cell to create a figure that tells a story behind your dataset.  You can use any chart type (_line chart, bar chart, heatmap, etc_) of your choosing!

# In[8]:


# Create a plot
sns.histplot(data=my_data, x='Area (mean)', hue='Diagnosis')

# Check that a figure appears below
step_4.check()


# ## Keep going
# 
# Learn how to use your skills after completing the micro-course to create data visualizations in a **[final tutorial](https://www.kaggle.com/alexisbcook/creating-your-own-notebooks)**.

# ---
# 
# 
# 
# 
# *Have questions or comments? Visit the [course discussion forum](https://www.kaggle.com/learn/data-visualization/discussion) to chat with other learners.*
