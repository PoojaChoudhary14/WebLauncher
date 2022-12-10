from sys import *
import webbrowser
import re
from urllib.request import urlopen

def is_connected():
    try:
        urlopen('https://www.google.com/',timeout=1)
        return True
    except Exception as err:
        return False

def Find(String):
    url=re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',String)
    print(url)
    return url

def WebLauncher(path):
    with open(path) as fp:
        print(fp)
        for line in fp:
            print(line)
            url=Find(line)
            print(url)
            for str in url:
                webbrowser.open(str,new=2)

def main():
    print("Application name:"+argv[0])

    if(len(argv)!=2):
        print("Error : Invalid number of arguments")
        exit()

    if(argv[1]=='-H' or argv[1]=='-h'):
        print("This script is used to open URl which are written in one file")
        exit()

    if(argv[1]=='-u' or argv[1]=='-U'):
        print("usage: ApplicatonName Name_Of_File")

    try:
        connected=is_connected()

        if connected:
            WebLauncher(argv[1])

        else:
            print("Unable to connect to internet...")

    except ValueError:
        print("Error: Invalid datatype of input")

    except Exception as E:
        print("Error: Invalid input", E)


if __name__=="__main__":
    main()
        
