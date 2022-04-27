#!/usr/bin/env python
# coding: utf-8

# # GAN Basics
# > Summarizing the foundational concepts relating to GANs
# 
# Author: Isaac Flath
# 

# ## Purpose
# 
# This blog is tagetted to people wanting a general intuition about GANs.  This is not going to cover how to code one or build one, but will talk about the most basic high level concepts to understand.
# 
# You do not need to understand GANs prior to reading this post.  I do assume that you generally are familiar with modeling.

# ## What is a GAN and what can it do?
# 
# A GAN is a Generative Adverserial Network.  They excel in creating data.  Let's take a look at a few examples:

# #### A GAN can enhance images
# 
# Google Brain did research to show how GANs can be used to enhance images.  The left super blurry unrecognizable pictures were given to a GAN.  The Middle column is what the GAN made when enhancing the image.  The right column is what the image should look like if the GAN was perfect.
# 
# ![Image Enhancement](my_icons/SuperEnhancement.jpg)

# #### A GAN can change image style
# 
# We can also transfer images from one style to another.  Whether that's changing video of a horse to a zerbra or combining photos with art, [this medium aricle](https://medium.com/@purnasaigudikandula/artistic-neural-style-transfer-with-pytorch-1543e08cc38f) shows a cool example!
# 
# ![Dog Style Transfer](my_icons/DogStyleTransfer.jpeg)

# #### A GAN can create new images
# 
# In the paper [Progressive Growing of GANs for Improved Quality, Stability, and Variation](https://arxiv.org/pdf/1710.10196.pdf), NVIDIA showed the capability of GANs to create realistic super resolution photos of people that do not exist.  These are fictional people made up by the GAN.
# 
# ![Super Resolution Images](my_icons/SuperResolution.png)
# 

# #### A GAN can help you draw
# 
# NVIDIA again shows a really cool video of how basic sketches cna be turned into realistic photos.  I can imagine how this could help people create art, visualize designs, and more!

# In[3]:


from IPython.display import YouTubeVideo

YouTubeVideo('p5U4NgVGAwg', width=800, height=400)


# #### A GAN can compose music
# 
# Another example is this song that was composed by AI.  The lyrics is a person, but the instrumentation is AI - a great example of Machine-Human collaboration.  You can see the GAN understood basic musical phrasing, hits, understood it can build to hits and go quiet for a couple beats before a large hit to add impact.  If I didn't know, I wouldn't have realized is was using AI

# In[4]:


from IPython.display import YouTubeVideo

YouTubeVideo('XUs6CznN8pw', width=800, height=400)


# ## How Does it Work?
# 
# This is more complex than your average Neural Network because it is relying on 2 (or more) Neural Networks training in conjunction.  You have 2 models with different roles:
# 
# The Critic is the quality gauge on the Generator while the generator is what's actually producing the data.  Let's look at a summary of each of those.
# 
# ![Critic Generator Summary](my_icons/CriticGenerator.png)

# #### How they train together
# 
# There is a big loop where they pass information back and forth an dlearn.  Here's generally how it works
# 
# ![GAN Training Loop](my_icons/GANTrainingLoop.png)

# ## First Challenges
# 
# 

# #### Co-learning
# 
# As these models learn together they need to be evenly match in terms of skill.  This can be especially challenging because the critic has a much easier job.  Think about it.  You paint a fake Monet and I will determine whether it's a real monet or a fake.  Who do you think will be more competent at their task?  Clearly painting the monet is the much harder job.
# 
# So what can we do about it?  The siimplest 2 appraoches are:
# 1. Set how many times the generator gets updated vs the critic.
# 1. Set the learning rates different for the generator vs the critic
# 
# 

# #### Mode Collapse
# 
# Mode collapse happens when the generator finds a weakness in the crtic and exploits it.  For example, the generator might do really well with golden retrievers - so rather than making all types of dogs is just learns to make lots of golden retrievors.
# 
# 

# ## Improvements & Tweaks
# 
# What I have covered above is simple data generation in an unsupervised manner.  There's several modification that can be made to let these GANs do fancier things - and Ill briefly touch on two of those here.
# 
# #### Conditional GANs
# 
# A conditional GAN is where you can tell it what kind of image you want.  For example if you are generating different dog breeds, you tell the gan you want a specific breed (ie Golden Retriever).  The way this works:
# 
# 1. The Generator is given a specific class to generate data for.
# 1. The Critic determins whether is is real or fake data for that class.  For example rather than "Predict if this is a real dog or not" it's "Predict if this is a real golden retriever or not".  In order to fool the critic, the generator now has to not just create a dog - but the right species of dog.  The generator could predict a perfect image of a pitbull, but it woul dbe easy for the critic to determine that it's a not a real golden retriever as pitbulls look completely different!
# 
# #### Controllable GANs
# 
# A Controllable GAN allows you to control different aspects of the image.  For example, I want to be able to take an image and tell it to generate the same image but add a beard.  Or generate the same image but make the person look older.  
# 
# A bit of background and how it's accomplished:  A generator creates data from random noise vectors.  These random noise vectors can be thought of as random seeds in a sense.  If I give the generator the exact same vector of random numbers, it will generate the exact same data.  So those random number translate to output features in the data, so you can figure out how they map and then tweak away! 
# 
# Now, there's a lot of execution details and challenges to making this happen that I am not covering in this post, but feel free to reach out if you're interested and I can do a follow up post on the details on how to actually accomplish this.
# 
# Here's an example of what Photoshop is working on when it comes to controllable GANs.

# In[6]:


from IPython.display import YouTubeVideo

YouTubeVideo('iJs_nqu8P08', width=800, height=400)


# In[ ]:




