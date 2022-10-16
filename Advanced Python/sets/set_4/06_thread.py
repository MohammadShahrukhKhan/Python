from threading import Thread, Event
import time
 
 
# It sends signals from one to another thread
bridge = Event()
 
 
def func():
    print('func() is started')
    """
    func will timeout after 3 seconds it will print a number starting from 1 and wait for 1 second 
    """
    x = 0
    while True:
        x += 1
        print(x)
        time.sleep(1)
 
        # Ensures whether the other thread sends the signals or not
        if bridge.is_set():
            break
 
 
if __name__ == '__main__':
    # Creating the main thread that executes the function
    main_thread= Thread(target=func)
 
    # We start the thread and will wait for 3 seconds then the code will continue to execute
    main_thread.start()
    main_thread.join(timeout=3)
 
    # sends the signal to stop other thread
    bridge.set()
 
    print("The function is timed out, you can continue performing your other task")
