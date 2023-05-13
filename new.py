import numpy as np
import matplotlib.pyplot as plt
import pyshark


capture = pyshark.FileCapture("selenium_traffic.pcap")
i = 0
data = [0.0]*3000
time = [0.0]*3000

for packet in capture:
    
    time[i] = packet.sniff_time.timestamp()
    #print(time[i])
    i+=1
  
for j in range(1, i):
    data[j-1]=time[j]-time[j-1]
    
    
# Generate some data
#data = np.random.randint(0, 100, 1000)

# Plot the data
plt.hist(data)
plt.show()

# Fit a normal distribution to the data
mu, sigma = np.mean(data), np.std(data)

# Plot the normal distribution
x = np.linspace(min(data), max(data), 3000)
y = np.exp(-(x - mu)**2 / (2 * sigma**2)) / (sigma * np.sqrt(2 * np.pi))
plt.plot(x, y)
plt.show()

# Print the parameters of the normal distribution
print('Mean:', mu)
print('Standard deviation:', sigma)