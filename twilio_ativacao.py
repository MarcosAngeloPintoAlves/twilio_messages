#!/usr/bin/env python
# coding: utf-8

# In[1]:


from twilio.rest import Client
import pandas as pd
sm_id = []
numeros = pd.read_csv('datasets/numeros.csv')
numeros.head()


# In[2]:


num_conv = numeros['numeros']
num_conv


# In[5]:


#formatando o número para whatsapp
num = []
for j in range(len(num_conv)):
    num.append("whatsapp:+55"+str(num_conv[j]))
num


# In[3]:


#formatando o número para sms
num_sms = []
for j in range(len(num_conv)):
    num_sms.append("+55"+str(num_conv[j]))
num_sms


# In[6]:


#Mandando mensagens por meio do WhatsApp

account_sid = "your_twilio_acc_sid"
auth_token  = "your_twilio_auth_token"

client = Client(account_sid, auth_token)

for i in range(len(num)):
    message = client.messages.create(
             from_='whatsapp:+your_twilio_number',
             body='Olá, bom dia! Para prosseguirmos com o seu atendimento entre em contato pelo e-mail: time@contasimples.com. \nObrigado pela preferência!',
             to=num[i]
         )

    print(message.sid)
    sm_id.append(message.sid)


# In[4]:


#Mandando mensagens por meio de SMS

account_sid = "your_twilio_acc_sid"
auth_token  = "your_twilio_auth_token"

client = Client(account_sid, auth_token)

for i in range(len(num_sms)):
    message = client.messages.create(
        to=num_sms[i], 
        from_="+your_twilio_number",
        body="Olá, bom dia! Para prosseguirmos com o seu atendimento entre em contato pelo e-mail: time@contasimples.com. Obrigado pela preferência!")
    print(message.sid)
    sm_id.append(message.sid)


# In[ ]:




