# Telegram-Flood-Bot
A Telegram bot for sending out bulk messages, made in 2021.

## Run
The code is run on Python 3. If Python 3 is not your default interpreter (say Python 2.7), you will probably need `pip3 install`, and `python3` command to install the packages and run the .py file.

If the packages are not already installed, run the following code to install the packages:
- `pip install telethon`
- `pip install pysocks`

`python floodTemplate.py` to run the file: It was originally created on PyCharm, but can be put on a virtual machine, say Google Cloud for 24/7 access.

After first time running, ***.session*** file will be generated for each logged in phone number. Afterwards, verficiation for logging into that account is no longer required.

## Tailor made adjustments

The lines of codes highlighted with the followings are required to pay attention:

- `##### 0` Turn on or off the shuffling (Might be required to turn off shuffling recreate an authentic discussion)
- `##### 1` Type the name of the file which holds all the pre-set messages
- `##### 2` Type the name of the file which holds the deatils about the channel name to send the message to, phone number, etc.
- `user['channelName'] = 'testingChannel'` is for testing and debugging. Comment this line and uncomment the above line for actual implementation
- `proxy_file = 'proxy.csv'` Proxy file name too, can be adjusted.
- **API_ID** and **API_HASH** values are retrived from https://my.telegram.org.
- `#, proxy=getProxy(n))` The proxy feature is currently disabled. If you have bought proxies, can delete the `) #` in this line to re-use this feature. 
- `##### 3` Adjust when to launch the code. If the time scheudled is in the past, the code will run immediately. (Since the loading and logging into 50+ Telegram accounts can take up to mintues, this feature is required for pre-loading.)
- In the main function: `abc = input("Type anything to continue: ")` This line is for holding back sending messages after pre-logging in into accounts. Comment this line if wishes to automatically send messages in scheduled time.
- `await everything[0].send_message(everything[3], everything[2])` Can be commneted if only wish to join group instead of sending out messages in the first time.

## messages.csv

Can use Excel to type the messages and save as .csv format after completion. Each line represents one message. The delimiter is `|` since in a conversation, `,` is usually used.

Change the file name here and the file name in the code accordingly.

## phones.csv

Can use Excel to type the information and save as .csv format after completion. The delimiter is `,` as in normal csv file. The headings are **channelName**,**id**,**phone**,**msg_num**.

Change the file name here and the file name in the code accordingly.

## proxy.csv

Can use Excel to type the proxy information and save as .csv format after completion. The headings are **proxy_type**,**addr**,**port**,**username**,**password**. **socks5** is recommended for proxy type.

Change the file name here and the file name in the code accordingly.

