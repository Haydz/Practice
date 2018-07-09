import csv
import requests
import time

print(' This code use a csv of IP addresses as an INPUT file, then run queries through the Robtex API. \n'
      'It currently Pulls: PASSIVE DNS, ACTIVE DNS and WHOIS \n \n ')


#Use for when testing
#test_ipaddress = ['199.19.54.1', '177.128.44.166']

# array to hold ips from input file
test_ipaddress = []
# dict to hold results and ip addresses
blacklist_dict = {}
#robtex API
url = "https://freeapi.robtex.com/ipquery/"

# Collect and parse firs

with open('C:\\Users\haydn.johnson\PycharmProjects\PointsClass\ipstest.csv') as csv_file:
    csv_data = list(csv.DictReader(csv_file))
    #print(csv_data[0])
    for x in csv_data:
       #print(x['IP address'])
        test_ipaddress.append(x['IP address'])

ip_dict = {}


#example of how to access a nested dictionary
#people = {'127.001': {'name': 'John', 'age': '27', 'sex': 'Male'},
 #         '122': {'name': 'Marie', 'age': '22', 'sex': 'Female'}}
#print(people['122'])

#Flag for what way the dictionary should be created
array_created = False
for ip in test_ipaddress:

    # running through up ip addresses for website - assuming JSON format
    page = requests.get(url + ip).json()
    print('======================Checking Robtex for: ', ip, ' ======================')
    #print(page) - to get JSON format


    #Checks if Passive DNS has anything
    if 'pas' in page:
        #    print('Passive DNS History' , page['pash'])
        pas = page['pas']
        if not pas:
            print('Nothing in PAS, leaving blank')
            pas = 'NA'
        else:
            pas2 = pas[0]
            #print(pas2)
            pas = pas2['o']

    #Checks if Active DNS has anything
    if 'acth' in page:
        #    print('Active DNS History, page', page['acth'])
        acth = page['acth']
        if not acth:
            print('Nothing in ACTH, leaving Blank')
            acth = 'NA'
    #gathering whois information
    whois = page['whoisdesc']
    if array_created is False:
        print("creating dict for first dict: ", ip)
        #ip_dict = {ip: {'Passive DNS History': pash, 'Active DNS History': acth, 'Whois': whois}}
        ip_dict = {ip:{'Passive DNS History': pas,'Active DNS History': acth, 'Whois': whois}}
        array_created = True
    else:
        print('Creating extra dictionary for', ip)

        ip_dict[ip] = {'Passive DNS History': pas,'Active DNS History': acth, 'Whois': whois}

    #creating space to look nicer
    print('\n')
    #to reduce throttling
    time.sleep(1)


#Print IP_DICT to confirm everything is ok
print('full Dictionary for comparision')
print(ip_dict)

#Field names for Header and to match with ip_dict items
fields = ['IP', 'Passive DNS History', 'Active DNS History', 'Whois']


with open('robtextresults.csv','w', newline='') as writing_csv:
    w = csv.writer(writing_csv)
    w.writerow(i for i in fields)
    w = csv.DictWriter(writing_csv, fields)
    #writing values into dictionary
    for key, val in sorted(ip_dict.items()):
        row = {'IP': key}
        row.update(val)
        w.writerow(row)
print('CSV Writing Complete')
