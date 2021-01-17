import socket
from datetime import datetime



irc = socket.socket()
SERVER = 'irc.chat.twitch.tv'
PORT = 6667
BOT = 'TwitchBot'
PASS = 'oauth:xxxxxxxxxxxxxxxxxxxx'
who=str(input('from whom chat do you want to read?: '))
CHANNEL = who.lower()
irc.connect((SERVER, PORT))

irc.send(("PASS "+PASS+'\n'+
          "NICK "+BOT+'\n'+
          "JOIN #"+CHANNEL+'\n').encode('utf-8'))
def prfy(a):
    now = datetime.now()
    current_time = now.strftime('%H:%M:%S')
    
    a=a[1:]
    a=a.split('!')
    print('@'+a[0]+':')
    a=a[1].split(':')
    print(current_time,'-',a[1]+'\n')

def joinChat():
    Loading=True
    while Loading:
        readbuffer_join=irc.recv(2048)
        readbuffer_join=readbuffer_join.decode('utf-8')
        prfy(readbuffer_join)
        

joinChat()