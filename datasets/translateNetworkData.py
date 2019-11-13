import csv
import time
import math

'''
This script takes the network data from the los Alamos dataset (use download.sh to get it)
and strips out the src and dest devices for each transmission and sorts them into hourly txt files
to be read in later.

'''

start = time.time()
files = {}
day = 2 # Hard coded for netflow-day-2
for i in range(0, 24):
    name = "day-"+str(day)+"_hour-"+str(i)+".txt"
    f = open(name, "w")
    files[i] = f

finalData = []
csvFile = open('netflow_day-02')



fieldNames = ["Time", "Duration", "SrcDevice", "DstDevice", "Protocol", "SrcPort", "DstPort", "SrcPackets", "DstPackets", "SrcBytes", "DstBytes"]

dictionaries = csv.DictReader(csvFile, fieldnames=fieldNames)

for row in dictionaries:
    # Why do we use the magic number 6?
    if  row['Protocol'] == '6':
        row["Time"] = math.floor(int(row["Time"]) % 3600*24*(day - 1)/3600)
        singleLine = str(row["SrcDevice"]) +","+ str(row["DstDevice"])+ "\n"
        # This will include repeats, when we read these back in we need to remove repeats
        files[row["Time"]].write(singleLine)



for f in range(0,24):
    files[f].close()

end = time.time()
print("Elpased time (m): " + str((end - start)/60))




