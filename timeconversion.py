from datetime import datetime
from pytz import timezone

import csv

hour = raw_input("Please enter the hour in UTC (24hr): ")
minute = raw_input("Please enter the minute in UTC: ")
print "you entered", hour+':'+minute

fmt = "%Y-%m-%d %H:%M:%S %Z%z"
timezonelist = [timezone('UTC'),timezone('US/Central')]

utc_time = timezonelist[0].localize(datetime(2016, 7, 18, int(hour), int(minute), 0))
central_time = utc_time.astimezone(timezonelist[1])
print utc_time.strftime(fmt)
print central_time.strftime(fmt)
print 
print


with open("time.txt") as file: 
    reader = csv.reader(file, delimiter=' ')
    for row in reader:
    	if(int(row[3]) > 0 and int(row[3]) < 5):
	        utc_time = timezonelist[0].localize(datetime(
	       									int(row[2]), int(row[1]), int(row[0]), int(row[3]), int(row[4]), 0))
	        central_time = utc_time.astimezone(timezonelist[1])
	        print central_time.strftime(fmt)
