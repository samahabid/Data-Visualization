#!/usr/bin/env python
# coding: utf-8

# **This notebook is an exercise in the [Data Visualization](https://www.kaggle.com/learn/data-visualization) course.  You can reference the tutorial at [this link](https://www.kaggle.com/alexisbcook/bar-charts-and-heatmaps).**
# 
# ---
# 

# In this exercise, you will use your new knowledge to propose a solution to a real-world scenario.  To succeed, you will need to import data into Python, answer questions using the data, and generate **bar charts** and **heatmaps** to understand patterns in the data.
# 
# ## Scenario
# 
# You've recently decided to create your very own video game!  As an avid reader of [IGN Game Reviews](https://www.ign.com/reviews/games), you hear about all of the most recent game releases, along with the ranking they've received from experts, ranging from 0 (_Disaster_) to 10 (_Masterpiece_).
# 
# ![ex2_ign](https://i.imgur.com/Oh06Fu1.png)
# 
# You're interested in using [IGN reviews](https://www.ign.com/reviews/games) to guide the design of your upcoming game.  Thankfully, someone has summarized the rankings in a really useful CSV file that you can use to guide your analysis.
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


# The questions below will give you feedback on your work. Run the following cell to set up our feedback system.

# In[2]:


# Set up code checking
import os
if not os.path.exists("../input/ign_scores.csv"):
    os.symlink("../input/data-for-datavis/ign_scores.csv", "../input/ign_scores.csv") 
from learntools.core import binder
binder.bind(globals())
from learntools.data_viz_to_coder.ex3 import *
print("Setup Complete")


# ## Step 1: Load the data
# 
# Read the IGN data file into `ign_data`.  Use the `"Platform"` column to label the rows.

# In[5]:


# Path of the file to read
ign_filepath = "../input/ign_scores.csv"

# Fill in the line below to read the file into a variable ign_data
ign_data = pd.read_csv(ign_filepath, index_col="Platform")

# Run the line below with no changes to check that you've loaded the data correctly
step_1.check()


# In[4]:


# Lines below will give you a hint or solution code
#step_1.hint()
#step_1.solution()


# ## Step 2: Review the data
# 
# Use a Python command to print the entire dataset.

# In[8]:


# Print the data
ign_data


# The dataset that you've just printed shows the average score, by platform and genre.  Use the data to answer the questions below.

# In[10]:


# Fill in the line below: What is the highest average score received by PC games,
# for any genre?
high_score =7.759930

# Fill in the line below: On the Playstation Vita platform, which genre has the 
# lowest average score? Please provide the name of the column, and put your answer 
# in single quotes (e.g., 'Action', 'Adventure', 'Fighting', etc.)
worst_genre = 'Simulation'

# Check your answers
step_2.check()


# In[9]:


# Lines below will give you a hint or solution code
#step_2.hint()
#step_2.solution()


# ## Step 3: Which platform is best?
# 
# Since you can remember, your favorite video game has been [**Mario Kart Wii**](https://www.ign.com/games/mario-kart-wii), a racing game released for the Wii platform in 2008.  And, IGN agrees with you that it is a great game -- their rating for this game is a whopping 8.9!  Inspired by the success of this game, you're considering creating your very own racing game for the Wii platform.
# 
# #### Part A
# 
# Create a bar chart that shows the average score for **racing** games, for each platform.  Your chart should have one bar for each platform. 

# In[13]:


# Bar chart showing average score for racing games by platform
plt.figure(figsize=(9, 5))
sns.barplot(x=ign_data['Racing'], y=ign_data.index)
plt.xlabel("")
plt.title("Average Score for Racing Games, by Platform")
step_3.a.check()


# In[14]:


# Lines below will give you a hint or solution code
#step_3.a.hint()
#step_3.a.solution_plot()


# #### Part B
# 
# Based on the bar chart, do you expect a racing game for the **Wii** platform to receive a high rating?  If not, what gaming platform seems to be the best alternative?

# In[17]:


#no,Xbox One
#step_3.b.hint()


# In[16]:


# Check your answer (Run this code cell to receive credit!)
step_3.b.solution()


# ## Step 4: All possible combinations!
# 
# Eventually, you decide against creating a racing game for Wii, but you're still committed to creating your own video game!  Since your gaming interests are pretty broad (_... you generally love most video games_), you decide to use the IGN data to inform your new choice of genre and platform.
# 
# #### Part A
# 
# Use the data to create a heatmap of average score by genre and platform.  

# In[20]:


# Heatmap showing average game score by platform and genre
plt.figure(figsize=(10,10))
sns.heatmap(ign_data, annot=True)
plt.xlabel("Genre")
plt.title("Average Game Score, by Platform and Genre")

# Check your answer
step_4.a.check()


# In[19]:


# Lines below will give you a hint or solution code
#step_4.a.hint()
#step_4.a.solution_plot()


# #### Part B
# 
# Which combination of genre and platform receives the highest average ratings?  Which combination receives the lowest average rankings?

# In[ ]:


#Simulation games for Playstation 4,Shooting and Fighting games for Game Boy Colo
#step_4.b.hint()


# In[21]:


# Check your answer (Run this code cell to receive credit!)
step_4.b.solution()


# # Keep going
# 
# Move on to learn all about **[scatter plots](https://www.kaggle.com/alexisbcook/scatter-plots)**!

# ---
# 
# 
# 
# 
# *Have questions or comments? Visit the [course discussion forum](https://www.kaggle.com/learn/data-visualization/discussion) to chat with other learners.*
