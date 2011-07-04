import yql

#
#  Python-YQL scraping one of my Flickr photosets
#  
#  Author: Lauren Tsung
#          ltsung@yahoo-inc.com
#  Date:   3 July 2011
#  
  
y = yql.Public()
query = 'use "http://www.datatables.org/flickr/flickr.photosets.getPhotos.xml" as flickr.photosets.getPhotos; select * from flickr.photosets.getPhotos where photoset_id="72157625114818289"'
result = y.execute(query)
print result