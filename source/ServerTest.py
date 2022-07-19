# Not working code

import socket
import threading
import time
import struct

# Server settings
pi_ip_address = 0
pc_ip_address = 1

# next create a socket object
s = socket.socket()

# reserve a port on your computer
port = 12345

# Next bind to the port
s.bind(('computer_address', port))

# put the socket into listening mode
s.listen(5)

actionOpcode = 0
data = None

VECT_FORCE_UPDATE_OPCODE = 2


# Needs to be called in another thread


def start_server():
    running = True
    while running:
        # Establish connection with client.
        c, addr = s.accept()
        print('Got connection from', addr)
        # thread call of handle client
        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()

    # Close the connection with the client
    c.close()


def handle_client(client):
    running = True

    while running:
        # Stop handling the client
        if actionOpcode == -1:
            break

        # Wait for another command from server
        if actionOpcode == 0:
            time.sleep(10)
            continue

        # Stop handle the action VECT_FORCE_UPDATE_OPCODE
        if actionOpcode == VECT_FORCE_UPDATE_OPCODE:
            client.send(bytes(str(VECT_FORCE_UPDATE_OPCODE), 'utf8'))
            data = struct.pack('<10f', *data)
