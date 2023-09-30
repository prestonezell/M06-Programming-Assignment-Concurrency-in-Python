import multiprocessing
import time
import random
from datetime import datetime

def print_time_and_wait(process_num):
    wait_time = random.random()
    time.sleep(wait_time)
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
    print(f"Process {process_num}: Current time is {current_time}")
    
if __name__ == "__main__":
    processes = []
    for i in range(3):
        process = multiprocessing.Process(target=print_time_and_wait, args=(i,))
        processes.append(process)
        process.start()