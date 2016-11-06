__author__ = 'haydz'

#this is a major work in progress

"""
This project is focused on intelligence automation from Nmap scans.
IT currently does the following:

1) Fast Nmap Scan to find hosts up
2) TOP 1000 PORTS TCP scan
3) Scan for common web ports
4) Run Eye Witness on common web ports (in progress)
"""

"""
Yet to do:
5) Enum4linux
6) connect all various NSE scripts up
7) ftp scan - log in for anonymous, output success anonmyous logins
8 ) snmp scans - private, community strings
"""


#to add multi process
from multiprocessing import Process

#importing multi processing to support running multiple nmap comamnds (similar to multiple threads)
import multiprocessing
#import os for allowing OS interfacing, such as listinga  directory if needed
import os

#importing to allow the script to connect to input and out put pipes, such as out put from nmap scans
import subprocess
import time
#import nmap


###### FUNCTIONS BELOW #####
#this is the function that will run the multip processing - NEED TO CONFIRM IF THIS IS USED -- need to add this
def multProc(targetin, scanip, port):
    jobs = []
    p = multiprocessing.Process(target=targetin, args=(scanip, port))
    jobs.append(p)
    p.start()
    return


def hostsup_scans(list): # maybe change to starter scan
    print"####### Starting -sn scan for hosts up \n"
    #tcpNameScan = 'nmap_%s_' % address\
    #print "File name is: %s" %(list)
    TCPSCAN = 'nmap -vv -sN -iL %s -oA hostsup1_sn' % (list)
    #tcp_results = scan(TCPSCAN)
    #print tcp_results
    #tcp_results = subprocess.check_output(TCPSCAN, shell=True)
    print "####### Starting -F scan for hosts up \n"
    TCPSCAN2 = 'nmap -vv -F -iL %s -oA hostsup2_fast' % (list)
    tcp_results2 = subprocess.check_output(TCPSCAN2, shell=True)
    print "####### Starting common ports scan for hosts up \n"
    TCPSCAN3 = 'nmap -iL %s -sn -T4 -PE -PM -PP -PU53,69,123,161,500,514,520,1434 -PA21,22,23,25,53,80,389,443,513,636,8080,8443,3389,1433,3306,10000 -PS21,22,23,25,53,80,443,513,8080,8443,389,636,3389,3306,1433,10000 -n -r -vv -oA hostsup3_ports' % (list)
    #tcp_results3 = subprocess.check_output(TCPSCAN3, shell=True)

    #for line in lines:
    #    if ("against" in line) and not ("no-response" in line):
    #        print line
    print "Finished Hostup scans"
    
    #Parsing all hostup scans for Hosts that are UP
    grepHostsUp = 'cat hostsup*.gnmap | grep Up | cut -d " " -f2 | sort -u'
    grepHostsUpResults = subprocess.check_output(grepHostsUp, shell=True)
    lines = grepHostsUpResults.split("\n")
    #removing any list items that are blank
    lines = [x for x in lines if x]

    #writing all hosts up to a file
    allHostsUp = open('allhostsup.txt', 'a')
    for line in lines:
        line = line.strip()
        allHostsUp.write("%s\n" %line)
    allHostsUp.close()

    print "Lauching Webports scan"
    #launching not as multi process so we know when it finishes
    webports('allhostsup.txt')

    #lauching EyeWitness as a seperate process due to how long it takes
    p2 = Process(target=eyewitness, args=('webPorts_common.xml', 'webPorts_common'))
    p2.start()

    print "testing if running after process ran"
    total = 0
    IPListClean = []

    # for IP in lines:
    #     print "IP:", IP
    #     IPListClean.append(IPList[total].strip('\n'))
    #     total = total + 1
    # for IP in IPListClean:
    #     p = Process(target=quicknmapScan, args=(IP,))
    #     p.start()

# generic nmap scan top 1000 ports
def quicknmapScan(address):
    #print address
    serv_dict = {}
    #nm = nmap.PortScanner()
    print "####### Starting TOP 1000 PORTS TCP scan for ", address
    tcpNameScan = 'nmap_%s_quick' % address
    #top one thousand ports
    TCPSCAN = 'nmap -vv --top-ports 1000  %s -oA %s_quick' % (address, tcpNameScan)
    tcp_results = subprocess.check_output(TCPSCAN, shell=True)

    #fullName = "%s_quick.xml" % tcpNameScan
    print "Gathering ports and services for %s" % address

    lines = tcp_results.split("\n")



    for line in lines:
        ports = []
        line = line.strip()
        if ("tcp" in line) and ("open" in line) and not ("Discovered" in line):
            # print line
            while "  " in line:
                line = line.replace("  ", " ");
            linesplit = line.split(" ")

            service = linesplit[2] #grabs service
            #print "service is"
            #print service

            port = line.split(" ")[0]
            #print "port is"
            port = line.split("/")[0] #remove protocol from pEyort: 80/tcp
            #print port
            if service in serv_dict:
                ports = serv_dict[service]
            serv_dict[service] = ports
            # print test_dict['port']
            ports.append(port)

            qhp = open('quick_hosts_ports.txt', 'a')
            qhp.write("%s:%s:%s\n" % (address, port, service))
            qhp.close()

#TO TEST
def scan(command):
    launchresults = subprocess.check_output(command, shell=True)
    return launchresults

def parseScanResults(results,filename,address):
    #parser to find ports open during nmap scan
    #results passed from def scan(command) : launchresults
    print "Gathering ports and services for %s" % address
    #split end of lines in results and parse for tcp, open, and no discovered in line
    lines = results.split("\n")
    for line in lines:
        ports = []
        line = line.strip()
        if ("tcp" in line) and ("open" in line) and not ("Discovered" in line):
            # print line
            while "  " in line:
                line = line.replace("  ", " ");
            linesplit = line.split(" ")

            service = linesplit[2] #grabs service
            #print "service is"
            #print service

            port = line.split(" ")[0]
            #print "port is"
            port = line.split("/")[0] #remove protocol from pEyort: 80/tcp
            #print port
            # if service in serv_dict:
            #     ports = serv_dict[service]
            # serv_dict[service] = ports
            # print test_dict['port']
            ports.append(port)

            print "Writing contents to %s" % filename
            qhp = open(filename, 'a')
            qhp.write("%s:%s:%s\n" % (address, port, service))
            qhp.close()






def top2000(address):
    serv_dict = {}
    print"####### Starting top 2000 ports scan", address
    #STILL TO DO


def webports(filename):
    print "Starting Common web ports scan -quick Fast One"
    #USING THIS TO TEST PARSING SCAN RESULTS THEN SEND TO EYEWITNESS.
    webScan = 'nmap -p 80,443,8080,8443,981,1311,2480 -iL %s -oA webPorts_common' % filename

    webresults = scan(webScan)

    #print testresults
    #parseScanResults(testresults, 'webports.txt',address)
#NEED TO TROUBLESHOOT THIS,
# CANNOT RUN EYE WITNESS SCAN ON WEBPORTS ONCE FINISHED

def ftpPort(filename):
    print "Starting FTP scan, checks anonymous"
    #USING THIS TO TEST PARSING SCAN RESULTS THEN SEND TO EYEWITNESS.
    ftpScan = 'nmap -sV -Pn -vv -p %s %s --script=banner,ftp-anon --oA ftpPorts' -oA webPorts_common' % filename

    ftwresults = scan(ftpScan)



def eyewitness(filename, outputName): #expecting IP addrees list
    print "Starting Eye Witness scan"
    #this requires editing the Eyewitness.py to use /bin/phantomjs

    if os_version == 'Ubuntu':
        eyewitnessPath = '/pentest/intelligence-gathering/eyewitness/'
        command = '%sEyeWitness.py --headless  --prepend-https --no-prompt  -x %s -d %s' %(eyewitnessPath,filename, outputName)
        print  "Running EyeWitness with: ", command

        #delete dir
        scan('rm -rf %s' %outputName)
        scan(command)
        print "\n ==== EyeWitness web ports scan finished ===="
        print "Located in the %s Directory" % outputName




#NMAP ALL PORTS DETAILED SCAN


#


#this is the start of the script, taking the IP addresses from a text file called IP.txt

if __name__ == '__main__':
    # get OS Versionur
    os_ver_scan = scan('uname -a')
    os_version = ""
    #print os_ver
    #checking OS
    if "Ubuntu" in os_ver_scan:
        print "Ubuntu Operating System Identified"
        print "Using PTF file structure (/pentest/)"
        os_version = 'Ubuntu'
    # raw_input("TEST")
    else:
        print "Unknown operating system being used, some tools will not work"



    #TO DO:
# Add excluding own IP address
# ifconfig
# nmap 192.168.0.* --exclude 192.168.0.100

#further functionality
# https://hackertarget.com/7-nmap-nse-scripts-recon/


    #open file'
    textfile = 'IP.txt'
    f = open(textfile, 'r')
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

    p2 = Process(target=hostsup_scans, args=(textfile,))
    p2.start()

    #p3 = Process(target=scan, args=(launchresults,))

    #the below returns results from the scan function
    #test = 'nmap -F 192.168.1.*'
    #testresults = scan(test)
    #print 'launchresults: ', testresults




    #p3.start()


    #print IPListClean
    #Creates blank files ready to write into
    # Acts as a blank file, when script is restarted
    open('quick_hosts_ports.txt', 'w').close()
    open('allhostsup.txt', 'w').close()
    open('webports.txt', 'w').close()


    for IP in IPListClean:
        print"IPS ", IP
        #p = Process(target=webports, args=(IP,))
        #p = Process(target=quicknmapScan, args=(IP,))
        #p.start()


    #eyewitness('webports.txt')


        #p2 = Process(target=nmapScan, args=(IP,))
        #p2.start()
    f.close()



