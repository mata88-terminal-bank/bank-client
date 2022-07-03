import socket
from constants import ADDRESS, FORMAT, SIZE

# Sends the requests inputted in the terminal through socket
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

