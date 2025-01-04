#Spawn a Process – Chapter 3: Process Based Parallelism
import multiprocessing
import time

def myFunc():
    name = multiprocessing.current_process().name
    print(f'Starting process name : {name}')
    time.sleep(3)
    print(f'Exiting process name : {name}')

if __name__ == '__main__':
    process_with_name = multiprocessing.Process(
        name='myFunc Process',
        target=myFunc
    )

    # process with name daemon = True

    process_with_default_name = multiprocessing.Process(
        target=myFunc
    )

    process_with_name.start()
    process_with_default_name.start()

    process_with_name.join()
    process_with_default_name.join()