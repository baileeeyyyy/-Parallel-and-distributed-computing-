import multiprocessing
import random
import time

class Producer(multiprocessing.Process):
    def __init__(self, queue):
        super().__init__()  # Use super() for better inheritance handling
        self.queue = queue

    def run(self):
        for _ in range(10):  # Use underscore for unused loop variable
            item = random.randint(0, 256)
            self.queue.put(item)
            print(f"Process Producer: Item {item} appended to queue {self.name} (size: {self.queue.qsize()})")
            time.sleep(1)

class Consumer(multiprocessing.Process):
    def __init__(self, queue):
        super().__init__()
        self.queue = queue

    def run(self):
        while True:
            if self.queue.empty():
                print("The queue is empty")
                break
            else:
                item = self.queue.get()
                print(f"Process Consumer: Item {item} popped from queue {self.name}")
                time.sleep(1)
                break  # Exit the loop after consuming an item

if __name__ == '__main__':
    queue = multiprocessing.Queue()
    process_producer = Producer(queue)
    process_consumer = Consumer(queue)

    process_producer.start()
    process_consumer.start()

    process_producer.join()
    process_consumer.join()