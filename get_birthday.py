#!/usr/bin/python
import time
import ConfigParser

#print int(time.strftime("%m%d"))

Config=ConfigParser.ConfigParser()
try:
  Config.read('alarm.config')
except:
  raise Exception('Sorry, Failed reading alarm.config file.')

birthday = 'null'

if int(time.strftime("%m%d")) == 525 :
  birthday = 'Joshua, '
#if int(time.strftime("%m%d")) == 129 :
#  birthday = 'dummy'

print birthday

#put birthday here!

# reads out birthday
if birthday == 'null':
  birthday = ''
else:
  birthday = 'God!... ' + birthday + 'It\'s your Birthday...Your getting old!...  ' 

if Config.get('main','debug') == str(1):
  print birthday


