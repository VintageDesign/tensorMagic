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
day = 2
hours = 12
for i in range(0, hours):
    for j in range(0, 60):
        name = "day-"+str(day)+"_hour-"+str(i+9) + "_minute-" + str(j) + ".txt"
        f = open(name, "w")
        files[i*60 + j] = f

finalData = []
csvFile = open('originals/netflow_day-0'+str(day))



fieldNames = ["Time", "Duration", "SrcDevice", "DstDevice", "Protocol", "SrcPort", "DstPort", "SrcPackets", "DstPackets", "SrcBytes", "DstBytes"]

dictionaries = csv.DictReader(csvFile, fieldnames=fieldNames)

for row in dictionaries:
    # Why do we use the magic number 6?
    if  row['Protocol'] == '6':
        row["Time"] = (math.floor(int(row["Time"]) / 60 ) -540 )% (hours * 60)
        singleLine = str(row["SrcDevice"]) +","+ str(row["DstDevice"])+ "\n"
        # This will include repeats, when we read these back in we need to remove repeats
        try:
            files[row["Time"]].write(singleLine)
        except KeyError:
            if row["Time"] > hours*60:
                break
            else:
                print("Missed at", row["Time"])
                pass



for i in range(0, hours):
    for j in range(0, 60):
        files[i*60 + j].close()

end = time.time()
print("Elpased time (m): " + str((end - start)/60))




