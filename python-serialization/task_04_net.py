#!/usr/bin/python3
import socket
# The socket library is used for network communication.
import json
# The json library is used for serializing and deserializing data.


# Function to start the server
def start_server(host='localhost', port=65432):
    # Create a TCP/IP socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # Bind the socket to the address and port
        s.bind((host, port))
        # Listen for incoming connections
        s.listen()
        print(f"Server listening on {host}:{port}")

        while True:
            # Wait for a connection
            conn, addr = s.accept()
            with conn:
                print(f"Connected by {addr}")
                # Receive the data in small chunks
                data = conn.recv(1024)
                if data:
                    # Deserialize the data from JSON format
                    received_dict = json.loads(data.decode('utf-8'))
                    print("Received Dictionary from Client:")
                    print(received_dict)
                    break


# Function to send data from the client to the server
def send_data(data, host='localhost', port=65432):
    # Create a TCP/IP socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # Connect to the server
        s.connect((host, port))
        # Serialize the data to JSON format
        serialized_data = json.dumps(data).encode('utf-8')
        # Send the serialized data
        s.sendall(serialized_data)
        print(f"Sent data: {data}")


if __name__ == "__main__":
    import threading
    # The threading library is used to run the server in a separate thread.
    import time
    # The time library is used to pause the main thread for a moment.

    # Start the server in a separate thread
    server_thread = threading.Thread(target=start_server)
    server_thread.start()

    # Give the server some time to start listening
    time.sleep(1)

    # Sample dictionary to send
    sample_dict = {'name': 'Alice', 'age': 30, 'city': 'Paris'}
    # Send the sample dictionary to the server
    send_data(sample_dict)

    # Ensure the server thread ends
    server_thread.join()
