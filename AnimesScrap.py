import urllib
from urllib.request import Request
import json

def BuscarSite(url):
    return urllib.request.urlopen(Request(url=url,headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"})).read()

def SplitarInicioFim(value,inicio,fim,qnt):
    return value.decode("utf-8").split(inicio)[qnt].split(fim)[0]

def EnviarDiscord(Token,Channel,Msg):
    return urllib.request.urlopen(Request(url=f"https://discordapp.com/api/v6/channels/{Channel}/messages",headers={"authorization":Token,"content-type":"application/json","user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"},data='{"content":"```md\\n[SuperAnimes](Lançamentos)\\nMsg```"}'.replace("Msg",Msg).encode("utf-8"),method="POST"))

def GetLastMessageId(Token,Channel):
    return json.loads(urllib.request.urlopen(Request(url=f"https://discordapp.com/api/v6/channels/{Channel}",headers={"authorization":Token,"content-type":"application/json","user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"},data=''.encode("utf-8"),method="GET")).read())["last_message_id"]

def DeleteMsgById(Token,Channel,Id):
    return urllib.request.urlopen(Request(url=f"https://discordapp.com/api/v6/channels/{Channel}/messages/{Id}",
                                          headers={"authorization": Token, "content-type": "application/json",
                                                   "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"},
                                          data=''.encode("utf-8"), method="DELETE"))

Site = BuscarSite("https://www.superanimes.biz/feed/atom")
Animes = []

for x in range(16):
    if("Ep" in SplitarInicioFim(Site,'<title type="html"><![CDATA[',']',x)):
        Animes.append(f"#--- {x} ---#"+SplitarInicioFim(Site,'<title type="html"><![CDATA[',']',x))
print(Animes)


#Infos
Channel = 811708968388395009 #Canal que sera enviado a mensagem
Token = ""#Discord token


try:
    DeleteMsgById(Token,Channel,GetLastMessageId(Token,Channel))
except:
    pass
EnviarDiscord(Token,Channel,str(Animes).replace(",","\\n").replace("'","").replace("[","").replace("]","").replace(" #","#"))
