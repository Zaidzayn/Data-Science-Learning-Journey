import threading

import time

def print_numbers():
    for i in range(5):
        time.sleep(2)
        # Simulate a time-consuming task
        print(f"Number: {i}")
        
def print_letters():
    for letter in 'abcde':
        time.sleep(2)
        print(f"Letter: {letter}")


##Create Two Threads
t1=threading.Thread(target=print_numbers)
t2=threading.Thread(target=print_letters)
# Start the threads
t1.start()
t2.start()
# Wait for both threads to complete
t1.join()
t2.join()
finished_time=time.time()
print(f"Finished at {finished_time} seconds")
print("Both threads have finished execution.")
# This code demonstrates how to run two functions concurrently using threads.

        
                