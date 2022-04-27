#!/usr/bin/env python
# coding: utf-8

# # Practical Chatbots
# 
# > Improving Business Processes Using ML-Based Chatbots
# 
# - toc: true
# - badges: true
# - comments: true
# - author: Isaac Flath
# - categories: [NLP, Deep Learning]

# I developed a process and app for creating and deploying chatbots for support and question answering purposes for Novetta.  This solution focused on practicality including minimizing the dataset needed, minimizing training/retraining needed, eliminating the need to retrain if policies change, and empowering domain experts to expand and improve the responses of without requiring a ML engineer for every tweak.
# 
# This approach was built on the sentence transformer (siamese BERT) architecture and the core machine learning technology was semantic similarity.  I built it using dash, but any deployment method could be used (slack bot, email bot, web app, etc.)
# 
# To read the blog post [click here](https://www.novetta.com/2021/06/chatbots/)
# 
