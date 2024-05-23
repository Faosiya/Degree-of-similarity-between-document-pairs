#!/usr/bin/env python
# coding: utf-8

# Question 4
# 
# #Created another notebook to house my similarity function that will be used to solve Question 4 by importing it as a module

# In[6]:


import math


# In[7]:


def dot(vec1, vec2):
    total = 0
    for i in range(len(vec1)):
        total += vec1[i] * vec2[i]
    return total

def my_cosine_similarity(vec1, vec2):
    numerator = dot(vec1, vec2)
    denominator = math.sqrt(dot(vec1, vec1) * dot(vec2, vec2))

    if math.isnan(numerator) or math.isnan(denominator) or denominator == 0:
        return 0  # Return 0 for undefined or zero denominator

    similarity_c = numerator / denominator
    return similarity_c


# In[8]:


# Function to calculate Jaccard similarity
def my_jaccard_similarity(doc1, doc2):
    # Convert inputs into sets
    set_1 = set(doc1)
    set_2 = set(doc2)
    
    # Calculate intersection and union sizes
    intersection = len(set_1.intersection(set_2))
    union = len(set_1.union(set_2))
    
    # Calculate Jaccard similarity coefficient
    similarity_j = intersection / union if union != 0 else 0
    
    # Return the Jaccard similarity coefficient
    return similarity_j


# In[9]:


# Define a function to compute all document similarities using cosine similarity
def all_sims_cosine(data):
    sims_c = []

    for i in range(len(data)):
        row_sims = []
        for j in range(len(data)):
            row_sims.append(my_cosine_similarity(data[i], data[j]))
        sims_c.append(row_sims)
    
    return sims_c


# In[10]:


# Define a function to compute all document similarities using Jaccard similarity
def all_sims_jacc(data):
    sims_j = []

    for i in range(len(data)):
        row_sims = []
        for j in range(len(data)):
            row_sims.append(my_jaccard_similarity(data[i], data[j]))
        sims_j.append(row_sims)
    
    return sims_j


# In[11]:


# Define a function to compute all document similarities using Jaccard similarity
def all_sims_cosine(data):
    sims_j = []

    for i in range(len(data)):
        row_sims = []
        for j in range(len(data)):
            row_sims.append(my_cosine_similarity(data[i], data[j]))
        sims_j.append(row_sims)
    
    return sims_j

