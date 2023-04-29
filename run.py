import subprocess
import random
import time

alpha = 1
beta = 1.5


if __name__ == '__main__':
    # Start 10 separate processes running register.py at the same time
    processes = []
    for i in range(2):
        
        # using the weibullvariate() method
        t = random.weibullvariate(alpha, beta)
        time.sleep(t)
        
        processes.append(subprocess.Popen(['python', 'register.py']))

    # Wait for all the processes to finish
    for p in processes:
        p.wait()
