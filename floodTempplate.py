from telethon import TelegramClient, events #pip install telethon
from telethon.tl.functions.channels import JoinChannelRequest
import asyncio
import csv
from random import shuffle, randint
import sched
from datetime import datetime
import time as time_module
import socks #pip install pysocks

Shuffling = True    ##### 0. True if shuffle; False if not shuffle   #####

read_file = 'messages.csv'     ##### 1. Adjust message file name #####
msg_list = []

with open(read_file, encoding='UTF-8') as f:
    rows = csv.reader(f,delimiter="|",lineterminator="\n")
    for row in rows:
        msg_list.append(row[0])
if Shuffling == True: shuffle(msg_list)
print("msg_list:")
print(msg_list)

input_file = 'phones.csv'        ##### 2. Adjust phone file name #####
users = []
with open(input_file, encoding='UTF-8') as f:
    rows = csv.reader(f,delimiter=",",lineterminator="\n")
    next(rows, None)
    for row in rows:
        user = {}
        #user['channelName'] = row[0]         ### Uncomment this line, & comment the below for actual work
        user['channelName'] = 'testingChannel'    ### debugging & testing channel
        user['id'] = int(row[1])
        user['phone'] = row[2]
        user['msg_num'] = int(row[3])
        users.append(user)
shuffle(users)
print("users:")
print(users)


proxy_file = 'proxy.csv' ##### proxy file #####
proxies = []
with open(proxy_file, encoding='UTF-8') as f:
    rows = csv.reader(f,delimiter=",",lineterminator="\n")
    next(rows, None)
    for row in rows:
        proxy = {}
        proxy['proxy_type'] = row[0]
        proxy['addr'] = row[1]
        proxy['port'] = int(row[2])
        proxy['username'] = row[3]
        proxy['password'] = row[4]
        proxies.append(proxy)
len_users = len(users)
bound = []
division = len_users // len(proxies)
print("division", division)
for x in range(len(proxies)):
    pack_range = (x + 1) * division
    bound.append(pack_range)
bound.pop()
bound.append(len_users)
def getProxy(user_idx):
    if len_users < len(proxies): #proxy_no. > user_no.
        return proxies[user_idx]
    for i in bound:
        if user_idx < i:
            return proxies[bound.index(i)]

API_ID = ******** #E.g. 1234567
API_HASH = "********" #E.g. "string30624700string"
phones = []

itr = 0
for num in users:
    phones.append(users[itr]['phone'])
    itr+=1
print(phones)

clients = []
n = 0
for phone in phones:
    try:
        print(str(n+1) + ". Adding " + phone)
        a = TelegramClient(phone, api_id=API_ID, api_hash=API_HASH) #, proxy=getProxy(n)) ##### Proxy feature temporarily disabled
        a.start(phone)
        clients.append(a)
        print(phone + " has been added.")
    except:
        print(phone + " failed to be added. Probably got banned?")
    n += 1

########### Important Shuffling block ###########
client_phone_msg_channel = []
i = 0
m = 0
for phone in phones:
    try:
        for x in range(users[i]['msg_num']):
            everything = [clients[i],phone,msg_list[m],users[i]['channelName']]
            client_phone_msg_channel.append(everything)
            m+=1
        i+=1
    except:
        print("Msg list & users out of range...")
        break
if Shuffling == True: shuffle(client_phone_msg_channel)
###################### End ######################

########### Time block ###########
def myfunc(): print("Working at ", datetime.now())
scheduler = sched.scheduler(time_module.time, time_module.sleep)
t = time_module.strptime('2021-07-17 08:50:00', '%Y-%m-%d %H:%M:%S')        ##### 3. Adjust when launch #####
t = time_module.mktime(t)
scheduler_e = scheduler.enterabs(t, 1, myfunc, ())
print("Waiting at ", datetime.now())
scheduler.run()
print("Move on to main()")
############## End ###############

async def main():
    abc = input("Type anything to continue: ")   # Comment if already scheduled.
    for everything in client_phone_msg_channel:
        try:
            print(everything[1] + " is joining channel")
            await everything[0](JoinChannelRequest(everything[3]))
            print(everything[1] + " is sending" + '\"' + everything[2] + '\"')
            await everything[0].send_message(everything[3], everything[2])  ##### Comment this line, to just join group
            await asyncio.sleep(randint(1, 1))  ##### 4. Adjust random interval #####
        except:
            print(everything[1] + " cannot write message")

with clients[0]:
    clients[0].loop.run_until_complete(main())