import pyshark
import numpy as np
import matplotlib.pyplot as plt

capture = pyshark.FileCapture("selenium_traffic.pcap")
#capture = pyshark.FileCapture("real_traffic.pcap")
#capture = pyshark.FileCapture("2.pcap")
i = 0
interarrival = [0.0]*3000
time = [0.0]*3000

for packet in capture:
    
    time[i] = packet.sniff_time.timestamp()
    #print(time[i])
    i+=1
  
for j in range(1, i):
    interarrival[j-1]=time[j]-time[j-1]
    #print(interarrival[j-1])

#print("******")
#print(i)
 
#x = np.arange(0, 3000)
#y = interarrival
 
# plotting
#plt.title("Line graph")
#plt.xlabel("X axis")
#plt.ylabel("Y axis")
#plt.plot(x, y, color ="blue")
#plt.show()



hist, bin_edges = np.histogram(interarrival)

print(hist)
print(bin_edges)

plt.hist(interarrival, bins='auto')
plt.show()