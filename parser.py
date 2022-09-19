import urllib.request
from urllib.request import urlretrieve
import os.path
from os import path

def main():
    weburl = urllib.request.urlopen("https://s3.amazonaws.com/tcmg476/http_access_log")
    resultcode = print("result code: " + str(weburl.getcode()))
    
    if path.isfile('logfile.txt') == False:
        print('downloading log file...')
        url = 'https://s3.amazonaws.com/tcmg476/http_access_log'
        urllib.request.urlretrieve (url, 'logfile.txt')
        print('done')
    else: print('this file is already present on your workstation')
    
with open(r"logfile.txt", 'r') as fp:
    lines = len(fp.readlines())
    print('Total number of logs in file between Oct 1994 and Oct 1995:', lines)
    
#now to find # of logs in first 6 months

    
if __name__ == "__main__":
    main()
