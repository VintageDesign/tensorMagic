import csv
import time
import math

start = time.time()
files = {}
day = 2 # Hard coded for netflow-day-2
hour = 11 # we only want an hours worth of data cause RAM would fill up... probably will anyway
for i in range(0, 24):
    name = "day-"+str(day)+"_hour-"+str(i)+".txt"
    f = open(name, "w")
    files[i] = f

finalData = []
csvFile = open('netflow_day-02')



fieldNames = ["Time", "Duration", "SrcDevice", "DstDevice", "Protocol", "SrcPort", "DstPort", "SrcPackets", "DstPackets", "SrcBytes", "DstBytes"]

dictionaries = csv.DictReader(csvFile, fieldnames=fieldNames)

for row in dictionaries:
    if  row['Protocol'] == '6':
        row["Time"] = math.floor(int(row["Time"]) % 3600*24*(day - 1)/3600)
        singleLine = str(row["SrcDevice"]) +","+ str(row["DstDevice"])+ "\n"
        # This will include repeats, when we read these back in we need to remove repeats
        files[row["Time"]].write(singleLine)



for f in range(0,24):
    files[f].close()

end = time.time()
print("Elpased time (m): " + str((end - start)/60))




