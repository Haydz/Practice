__author__ = 'haydz'

#this is a major work in progress

#This code runs a normal TOP 1000 ports scan and writes it to a file. You can then start using this
# it will then run a full TCP scan and run extra NMAP scripts based on the ports found
# working on adding dirbuster, smb enumeration and others that are not nmap related


#to add multi process


from multiprocessing import Process

#importing multi processing to support running multiple nmap comamnds (similar to multiple threads)
import multiprocessing
#import os for allowing OS interfacing, such as listinga  directory if needed
import os

#importing to allow the script to connect to input and out put pipes, such as out put from nmap scans
import subprocess
import time
import nmap


#this is the function that will run the multip processing - NEED TO CONFIRM IF THIS IS USED -- need to add this
def multProc(targetin, scanip, port):
    jobs = []
    p = multiprocessing.Process(target=targetin, args=(scanip, port))
    jobs.append(p)
    p.start()
    return


#in process dirbuster scan, this will run dirbuster on http ports found
#functionality to add: add for https ports and to output the dirs found to a file
def Dirbuster(address, port):
    print("## found HTTP port, DIRBUSTERING....")
    print "with", address, ':', port
    folders = ["/usr/share/dirb/wordlists", "/usr/share/dirb/wordlists/vulns"]
    found_lines = []
    print "ATTEMPTING TO BRUTE FORCE DIRECTORIES"
    for folder in folders:
        for files in os.listdir(folder):
            outputfile = ' -o ./backup%s_dirbuster_%s'  # % (address, files)
            DIRBUSTER_SCAN = 'dirb http://%s:80 %s/%s %s' % (address, folder, files, outputfile)

            try:
                results = subprocess.check_output(DIRBUSTER_SCAN, shell=True)
                resultarr = results.split("\n")
                for line in resultarr:
                    if "+" in line:
                        if line not in found_lines:
                            # print "found line"
                            found_lines.append(line)
                            # print 'wtf'
            except:
                pass

    try:
        if found_lines[0] != "":
            print '[*] Dirb found the following items...'
            for item in found_lines:
                print "   >>>>" + item
    except:
        print "INFO: No items found during dirb scan of " + address

        #need to place this into a text file



#this runs Nmap NSE scans on http ports
def HttpScan(address, port):
    print("## found HTTP port, enumerating....")
    print "with", address, ':', port

    scan_name = '%s_http' % address
    HTTPSCAN = 'nmap -sV -Pn -vv -p %s %s -script=http-vhosts,http-userdir-enum,http-apache-negotiation,' \
               'http-backup-finder,http-config-backup,http-default-accounts,http-email-harvest,http-methods,http-method-tamper,' \
               'http-passwd,http-robots.txt -oA %s' % (port, address, scan_name)

    results = subprocess.check_output(HTTPSCAN, shell=True)


    #this runs NSE scans on HTTPS ports
def HttpsScan(address, port):
    print("## found HTTPS port, enumerating....")
    print "with", address, ':', port

    scan_name = '%s_httpS' % address
    HTTPS_SCAN = 'nmap -sV -Pn -vv -p %s %s --script=banner,http-vhosts,http-userdir-enum,http-apache-negotiation,http-backup-finder,' \
                 'http-config-backup,http-default-accounts,http-email-harvest,http-methods,http-method-tamper,http-passwd,' \
                 'http-robots.txt,http-headers,http-errors.nse -oX %s' % (port, address, scan_name)
    results = subprocess.check_output(HTTPS_SCAN, shell=True)


#this runs FTP NSE scans on FTP ports
def FTP_Scan(address, port):
    print("## found FTP port, enumerating....")
    print "with", address, ':', port

    scan_name = '%s_FTP' % address
    FTP_SCAN = 'nmap -sV -Pn -vv -p %s %s --script=banner,ftp-anon -oX %s' % (port, address, scan_name)
    results = subprocess.check_output(FTP_SCAN, shell=True)


#this runs the available SSH NSE scripts
def SSH_Scan(address, port):
    print("## found SSH port, enumerating....")
    print "with", address, ':', port

    scan_name = '%s_SSH' % address
    SSH_SCAN = 'nmap -sV -Pn -vv -p %s %s --script=banner,ssh2-enum-algos -oX %s' % (port, address, scan_name)
    results = subprocess.check_output(SSH_SCAN, shell=True)


#this runs the NSE SMB scans
# as well as an nmblook up
def SMB_SCAN(address, port):
    print("## found SMB port, enumerating....")
    print "with", address, ':', port

    scan_name = '%s_SMB' % address
    SMB_SCAN = 'nmap -sV -Pn -vv -p 139,445 %s --script=smb-enum-shares,smb-enum-users,smb-os-discovery,smb-brute -oX %s' %(address, scan_name)

    results = subprocess.check_output(SMB_SCAN, shell=True)
    SMB_recon = 'nmblookup -A %s > nmblookup_%s' % (address,address)
    results = subprocess.check_output(SMB_recon, shell=True)
    # need to add DNS etc


# generic nmap scan top 1000 ports
def quicknmapScan(address):
    # print address
    serv_dict = {}
    #nm = nmap.PortScanner()
    print"####### Starting TOP 1000 PORTS TCP scan for ", address
    tcpNameScan = 'nmap_%s_quick' % address
    #top one thousand ports
    TCPSCAN = 'nmap -vv  %s -oA %s_quick' % (address, tcpNameScan)
    tcp_results = subprocess.check_output(TCPSCAN, shell=True)
    lines_results = tcp_results.split("\n")
    #print lines_results
    print 'Have %d bytes in output' % len(tcp_results)
    print type(tcp_results)


    print "Gathering ports and services"
    f = open(tcpNameScan, 'r')
    #linestri[p]
    for line in f:
        ports = []
        # print line
        # print "testing OPEN"
        if 'open' in line:
            # print line

            linesplit = line.split(" ")
            linesplit = line.split('"')

            # print linesplit
            port = linesplit[3]
            service = linesplit[11]

            serv_dict[service] = port


            # print test_dict['port']
            ports.append(port)
    f.close()
    print ports




#NMAP ALL PORTS DETAILED SCAN
def nmapScan(address):
    # print address
    serv_dict = {}
    print"####### Starting TCP ALL PORTS scan for ", address
    tcpNameScan = 'nmap_%s' % address
    #top one thousand ports
    TCPSCAN = 'nmap -vv -p 1-65535  %s -oX %s' % (address, tcpNameScan)
    tcp_results = subprocess.check_output(TCPSCAN, shell=True)

    lines_results = tcp_results.split("\n")
    print "####printing results for: ", address
    for line in lines_results:
        print line

    #this opens the file and strips the ports from it
    print "Gathering ports and services"
    f = open(tcpNameScan, 'r')
    #linestri[p]
    for line in f:
        ports = []
        # print line
        # print "testing OPEN"
        if 'open' in line:
            # print line

            linesplit = line.split(" ")
            linesplit = line.split('"')

            # print linesplit
            port = linesplit[3]
            service = linesplit[11]

            serv_dict[service] = port


            # print test_dict['port']
            ports.append(port)
    f.close()
    print ports

    #now search through list for services and ports
    #will use xml format, as the grep format is harder to splt
    print " Service Dictionary test"
    print serv_dict

    for key in serv_dict:

        # print key
        if (key == 'http') or (serv_dict[key] == 80):
            #nmap scan on port 80
            multProc(HttpScan, address, serv_dict[key])
            multProc(Dirbuster, address, serv_dict[key])
        #based on the port number aor service name it will run the relevant scan
        elif (key == 'https') or (key == 'ssl/http') or (key == 'microsoft-ds') or (serv_dict[key] == 443):
            #nmap scan on port 80
            multProc(HttpsScan, address, serv_dict[key])
        elif (serv_dict[key] == '21') or (key == 'ftp'):
            multProc(FTP_Scan, address, serv_dict[key])

        elif (serv_dict[key] == '22') or (key == 'ssh'):
            multProc(SSH_Scan, address, serv_dict[key])

        elif (serv_dict[key] == '139') or (serv_dict[key] == 445) or (key == 'smb'):
            multProc(SMB_SCAN, address, serv_dict[key])

#go through notes of oscp machines for the port numbres
# then we need to have a way to grep up and open ports and enumerate them

#


#this is the start of the script, taking the IP addresses from a text file called IP.txt

if __name__ == '__main__':

#TO DO:
# Add excluding own IP address
# ifconfig
# nmap 192.168.0.* --exclude 192.168.0.100

    #open file'
    f = open('IP.txt', 'r')
    print"IPs in File::"
    #
    #WList = f.read()
    print( "### this is the main recon file ####")
    IPList = []
    total = 0
    for IP in f:
        IPList.append(IP)

        total = total + 1


    print" Total Number of IPS: %s" % total
    IPListClean = []
    total = 0
    for IP in IPList:
        IPListClean.append(IPList[total].strip('\n'))
        total = total + 1

    # print IPListClean

    for IP in IPListClean:
        print"IPS ", IP
        p = Process(target=quicknmapScan, args=(IP,))
        p.start()

        #p2 = Process(target=nmapScan, args=(IP,))
        #p2.start()
    f.close()


