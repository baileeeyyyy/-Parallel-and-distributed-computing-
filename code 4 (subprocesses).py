import multiprocessing
import random
import time

class producer(multiprocessing.Process):
    def __init__(self, queue):
        multiprocessing.Process.__init__(self)
        self.queue = queue

    def run(self):
        for i in range(10):
            item = random.randint(0, 256)
            self.queue.put(item)
            print(f"Process Producer: item {item} appended to queue {self.name} size {self.queue.qsize()}")
            time.sleep(1)
            print(f"The size of queue is {self.queue.qsize()}")

class consumer(multiprocessing.Process):
    def __init__(self, queue):
        multiprocessing.Process.__init__(self)
        self.queue = queue

    def run(self):
        while True:
            if self.queue.empty():
                print("The queue is empty")
                break
            else:
                item = self.queue.get()
                print(f"Process Consumer: item {item} removed from queue")
                time.sleep(2)

if __name__ == "__main__":
    queue = multiprocessing.Queue()  # Shared queue

    # Create producer and consumer processes
    producer_process = producer(queue)
    consumer_process = consumer(queue)

    # Start the processes
    producer_process.start()
    consumer_process.start()

    # Wait for processes to complete
    producer_process.join()
    consumer_process.join()

    print("Processing complete.")
