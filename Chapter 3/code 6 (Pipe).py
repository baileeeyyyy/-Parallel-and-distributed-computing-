import multiprocessing
import time

def sender(conn):
    """Function to send data through the pipe."""
    for i in range(5):
        message = f"Message {i}"
        conn.send(message)  # Send data through the pipe
        print(f"Sender: Sent {message}")
        time.sleep(1)
    conn.send("END")  # Indicate the end of communication
    conn.close()  # Close the sending end of the pipe

def receiver(conn):
    """Function to receive data from the pipe."""
    while True:
        message = conn.recv()  # Receive data from the pipe
        if message == "END":
            print("Receiver: End of communication.")
            break
        print(f"Receiver: Received {message}")

if __name__ == "__main__":
    # Create a Pipe
    parent_conn, child_conn = multiprocessing.Pipe()

    # Create sender and receiver processes
    sender_process = multiprocessing.Process(target=sender, args=(parent_conn,))
    receiver_process = multiprocessing.Process(target=receiver, args=(child_conn,))

    # Start the processes
    sender_process.start()
    receiver_process.start()

    # Wait for the processes to finish
    sender_process.join()
    receiver_process.join()

    print("Communication complete.")

