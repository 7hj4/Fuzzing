#usr/bin/python3 

import requests
import argparse
import os

# clean screen
os.system("cls")
os.system("clear")

logo = '''
        ###########################################

                tool Brute Force directory
                        y0usef 
        ###########################################
'''

print(logo)

# open session here connect 

session = requests.Session()

directory_list = open("directory_list.txt",'r')

def get_arags():
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--url' , dest ='url',help = 'url website')
    options = parser.parse_args()

    if not options.url:
        parser.error('[-] Please Enter url website , use --help for more')

    return options.url

for line in directory_list:
    url = session.get(get_arags()+ "/" + str(line),verify=False)
    remove = line.rstrip("\n")
    if url.status_code == 200:
        print("[+] site is status code 200 => " + get_arags() + "/" + str(remove))
    else:
        print(" [-] site is status code other => " + get_arags() + "/" + str(remove))
    
