#!/usr/bin/python

import yql
import urllib2
import simplejson

#
#  Python-YQL scraping my unique tumblr post tags
#  
#  Author: Lauren Tsung
#          ltsung@yahoo-inc.com
#  Date:   4 July 2011
#  

url = "http://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20tumblr.posts%20where%20username%3D'ltsung'&format=json&diagnostics=true&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys&callback="

result = urllib2.urlopen(url).read()

data = simplejson.loads(result)

total_posts = len(data['query']['results']['posts']['post'])

unique_tags = []

for i in range (0, total_posts):
	tag = data['query']['results']['posts']['post'][i]['tag']
	
	if tag not in set(unique_tags):
		unique_tags.append(data['query']['results']['posts']['post'][i]['tag'])
	
print unique_tags

