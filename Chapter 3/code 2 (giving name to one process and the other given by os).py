#DaemonChapter  - 3: Process Based Parallelism

import multiprocessing
import time

def foo():
    name = multiprocessing.current_process().name
    print(f"Starting {name}")
    if name == 'background_process':
        for i in range(0, 5):
            time.sleep(1)
            print(f"{i} -> {name}")
    else:
        for i in range(5, 10):
            time.sleep(1)
            print(f"{i} -> {name}")
    print(f"Exiting {name}")

if __name__ == '__main__':
    background_process = multiprocessing.Process(
        name='background_process',
        target=foo
    )
    background_process.daemon = True

    NO_background_process = multiprocessing.Process(
        name='NO background process',
        target=foo
    )
    NO_background_process.daemon = False

    background_process.start()
    NO_background_process.start()
