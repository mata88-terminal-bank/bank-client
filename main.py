import socket
from constants import ADDRESS, FORMAT, SIZE

def send_request(request):
    """ Staring a TCP socket. """
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    """ Connecting to the server. """
    client.connect(ADDRESS)

    """ Sending the request to the server. """
    client.send(request.encode(FORMAT))
    msg = client.recv(SIZE).decode(FORMAT)
    print(f"[SERVER]: {msg}")

    """ Closing the connection from the server. """
    client.close()

def main():
    print("WELCOME TO THE TERMINAL BANK!")
    print("Type 'exit' at any point to exit")
    print("REQ:")
    request = input()

    while request != "exit":
        send_request(request)

        print("REQ:")
        request = input()

if __name__ == "__main__":
    main()

