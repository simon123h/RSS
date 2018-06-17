import feedparser
import os
import pdb
from yattag import Doc, indent
from lxml import html
import requests

rss = "http://www.ynet.co.il/Integration/StoryRss2.xml"


d = feedparser.parse(rss)

#Title of Service
print d['feed']['title']


##Basic HTML template
##doc,tag,text= Doc().tagtext()
##doc.asis('<DOCTYPE html>')

##Loop to create HTML
##with tag ('html', dir = "rtl"):
##    with tag ('body'):
##        with tag ('h1', style= "font-family:sans-serif;"):
##            text (d.feed.title) ##Main title for RSS
##        for item in range (len(d.entries)): ##Loop over articles in RSS feed
##            with tag ('h2', style= "font-family:sans-serif;"): #Article title
##                with tag ('a', href=d.entries[item].link): #Add link
##                    text (d.entries[item].title)
##            with tag ('p', style= "font-family:sans-serif; font-weight:bold;"): ##Article description
##                text (d.entries[item].description)
##            with tag('div', id='photo-container'): #Get picture
##                links=dict(d.entries[item])
##                imageLink=str(links['links'][1]['href'])
##                doc.stag('img', src=imageLink, width="150px", klass="photo") #Input pic in html
##            with tag ('p', style = 'font-family:sans-serif;'): ##Article text
##                page=requests.get(d.entries[item].link)
##                tree = html.fromstring(page.content)
##                textbody = tree.xpath("//section[@class='article__entry h-group']/p[@class='t-body-text']") ##//section[@class='article__entry h-group']/p/child::text()
##                for item in textbody:
##                    raw_text="'{0}'".format(item.text_content().encode('iso-8859-1','replace'))
##                    utf_text = raw_text.decode('UTF-8', 'ignore')
##                    text(utf_text)
##                    doc.stag('br') #Add linebreaks between paragraphs
##                    doc.stag('br')
##                    #pdb.set_trace()
##
##
##html_str=doc.getvalue().encode('UTF-8', 'ignore')
##
##Html_file= open("TheMarker.html","w")
##Html_file.write(html_str)
##Html_file.close()
##
##
##os.startfile(Html_file.name, 'open')

#print "DONE"
