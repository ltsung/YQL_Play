#!/usr/bin/python

import yql
import urllib2
import simplejson

#
#  Python-YQL scraping one of my Flickr photosets
#  
#  Author: Lauren Tsung
#          ltsung@yahoo-inc.com
#  Date:   3 July 2011
#  
  
url = "http://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20flickr.photosets.photos%20where%20photoset_id%3D'72157625114818289'&format=json&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys&callback="

result = urllib2.urlopen(url).read()

data = simplejson.loads(result)

total_photos = len(data['query']['results']['photo'])

for i in range (0, total_photos):
	print data['query']['results']['photo'][i]['title'] 
