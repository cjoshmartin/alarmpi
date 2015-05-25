#!/usr/bin/env python

import feedparser
import ConfigParser
Config=ConfigParser.ConfigParser()
try:
  Config.read('alarm.config')
except:
  raise Exception('Sorry, Failed reading alarm.config file.')

try: 
    rss = feedparser.parse('http://feeds.bbci.co.uk/news/world/rss.xml')
    #rss = feedparser.parse('http://createfeed.fivefilters.org/extract.php?url=twitter.com%2Ffivefilters%2F&item=.original-tweet&item_url=a.tweet-timestamp&item_desc=.content&item_title=0&strip=.stream-item-footer%2C.username%2C.js-short-timestamp')


#for entry in rss.entries[:4]:
#    print entry['title']
#    print entry['description']
#    
#print rss.entries[0]['title']
#print rss.entries[0]['description']
#print rss.entries[1]['title']
#print rss.entries[1]['description']
#print rss.entries[2]['title']
#print rss.entries[2]['description']
#print rss.entries[3]['title']
#print rss.entries[3]['description']

    newsfeed = rss.entries[0]['title'] + '.  ' + rss.entries[0]['description'] + '.  ' + rss.entries[1]['title'] + '.  ' + rss.entries[1]['description'] + '.  ' + rss.entries[2]['title'] + '.  ' + rss.entries[2]['description'] + '.  ' + rss.entries[3]['title'] + '.  ' + rss.entries[3]['description'] + '.  ' 

# print newsfeed
    newsfeed = newsfeed.encode('utf-8')

# Today's news from BBC
    news = 'And now, The latest stories from the World section of the BBC News.  ' + newsfeed
   #news = 'And now, Test tweets...  ' + newsfeed 

except rss.bozo:
    news = 'Failed to reach BBC News'

if Config.get('main','debug') == str(1):
  print news
