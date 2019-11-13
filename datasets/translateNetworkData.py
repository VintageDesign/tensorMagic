import csv
import time
import math

print("Opening CSV File...")
start = time.time()
csvFile = open('xaa')
day = 2 # Hard coded for netflow-day-2
hour = 11 # we only want an hours worth of data cause RAM would fill up... probably will anyway

print("Translating Data...")


fieldNames = ["Time", "Duration", "SrcDevice", "DstDevice", "Protocol", "SrcPort", "DstPort", "SrcPackets", "DstPackets", "SrcBytes", "DstBytes"]

dictionaries = csv.DictReader(csvFile, fieldnames=fieldNames)
middleData = []
finalData = []

for row in dictionaries:
    if  row['Protocol'] == '6':
        row["Time"] = math.floor(int(row["Time"]) % 3600*24*(day - 1)/3600)
        middleData.append(row)


print("Outputting Final Data...")
f = open("Out.txt", "w+")
for row in middleData:
    if row["Time"] == hour:
        if row not in finalData:
            finalData.append(str(row["SrcDevice"]) + str(row["DstDevice"]) )
            f.write(str(row["SrcDevice"]) +","+ str(row["DstDevice"])+ "\n" )

f.close()
end = time.time()
print("Elpased time (m): " + str((end - start)/60))







