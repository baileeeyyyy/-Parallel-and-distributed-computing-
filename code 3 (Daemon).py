#DaemonChapter  - 3: Process Based Parallelism

import multiprocessing
import time

def foo():
    print('Starting function')
    for i in range(0, 10):
        time.sleep(1)
        print(f"{i} -> {name}")
    print('Finished function')

if __name__ == '__main__':
    p = multiprocessing.Process(target=foo)

    print('Process before execution:', p, p.is_alive())
    p.start()

    print('Process running:', p, p.is_alive())
    p.terminate()

    print('Process terminated:', p, p.is_alive())
    p.join()

    print('Process joined:', p, p.is_alive())
    print('Process exit code:', p.exitcode)