import socket

# Server settings
pi_ip_address =
pc_ip_address =

# next create a socket object
s = socket.socket()

# reserve a port on your computer
port = 12345

# Next bind to the port
s.bind(('ADRESSE_ORDINATEUR', port))

# put the socket into listening mode
s.listen(5)

actionOpcode = 0
data = None

VECT_FORCE_UPDATE_OPCODE = 2

#faut call ca dans un autre thread
def start_server():
    running = True
    while running:

        # Establish connection with client.
        c, addr = s.accept()
        print ('Got connection from', addr )
	#thread call of handle client
        thread = threading.Thread(target = handleClient , args = (client,) )
        thread.start()

    # Close the connection with the client
    c.close()


def handleClient(client):
    running = True

    while running:
	#on arrete de handle le client
        if actionOpcode  == -1:
            break

        #on attend une autre commande du serveur
        if actionOpcode  == 0 :
            time.sleep(10)
            continue

        #on arrete handle l'action VECT_FORCE_UPDATE_OPCODE
        if actionOpcode  == VECT_FORCE_UPDATE_OPCODE  :
            client.send(bytes( str(VECT_FORCE_UPDATE_OPCODE), 'utf8'))
            data = struct.pack( '<10f' , *data)
            action = 0
