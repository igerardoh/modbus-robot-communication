#!/usr/bin/env python
# coding: utf-8

# # MODBUS GETTING STARTED

# # 1. Connect Robot

# ### 1.1 Define parameters and establish connection
# Before establish the connection, please make sure your robot has remote and modbus enabled. Also make sure your robot is running in Auto Mode. 
# https://pymodbus.readthedocs.io/en/latest/source/library/pymodbus.client.html?highlight=ModbusTcpClient#pymodbus.client.sync.ModbusTcpClient

# In[20]:


from pymodbus.client.sync import ModbusTcpClient

# Define device/robot parameters
SERVER_IP = '192.168.132.173' # TMrobot
SERVER_PORT = 502
DEVICE_ID = 1

# Establish TCP connection
print('Trying to establish connection.....')
client = ModbusTcpClient(host=SERVER_IP, port=SERVER_PORT)

if client.connect():
    print("Connection to Robot %s:%d established succesfully" % (SERVER_IP, SERVER_PORT))
else:
    print("[Error] Fail to connect to modbus slave %s:%d." % (SERVER_IP, SERVER_PORT))
    exit()


# # 2. Trigger Events (Write Data)

# ### 2.1 Change Current Project

# In[22]:


def str2hex(string):
    _hex = list(int(string[0+i:2+i].encode("utf-8").hex(),16) for i in range(0, len(string), 2))
    return _hex

# Define Parameters
ADDRESS_START  = 7701 
MESSAGE = 'pointspose' # as HEX=[0x706F, 0x696E, 0x7473, 0x706F, 0x7365]

modbus_change_project = client.write_registers(address=ADDRESS_START, values=str2hex(MESSAGE)+[0,23600])  # append suffix '/0'
print("Project file succesfully changed")


# ### 2.2 Play/Pause Current Project
# If the project is stopped or paused at the moment you run these lines of codes, then the project will be played. If the project is already being played, then these lines of codes will pause it.

# In[15]:


# Define Parameters
ADDRESS_START  = 7104

modbus_play = client.write_coil(address=ADDRESS_START, value=1)

print("Play/Pause command sent successfully")


# ### 2.3 Change Project Speed

# In[5]:


# Define Parameters
ADDRESS_START  = 7101
ROBOT_SPEED = 25

modbus_change_speed = client.write_register(address=ADDRESS_START, value=ROBOT_SPEED)

print("Robot speed succesfully changed")


# # 3. GET INFO (Read Data)

# ## 3.1 Robot Status

# ### 3.1.1 Is there an Error?

# In[8]:


ADDRESS_START = 7201

modbus_isError = client.read_discrete_inputs(address=ADDRESS_START, count=1)
print(modbus_isError.bits[0])


# ### 3.1.2 Is Project Running?

# In[12]:


ADDRESS_START = 7202

modbus_isPlay = client.read_discrete_inputs(address=ADDRESS_START, count=1)
print(modbus_isPlay.bits[0])


# In[ ]:




