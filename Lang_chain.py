#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("basic langchain integration")


# In[2]:


import os
os.environ["GROQ_API_KEY"] = ""



# In[4]:


import os
print(os.getenv("GROQ_API_KEY"))


# In[5]:


from langchain_groq import ChatGroq

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0.7
)

response = llm.invoke("Say hello in one sentence.")
print(response.content)



# In[9]:


text =" suggest me work out plan for 1 week 1hr per day"
response = llm.invoke(text)
print(response.content)


# In[ ]:




