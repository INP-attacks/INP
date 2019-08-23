# XML IP Address Spaces
import os
import time
import socket
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from threading import Thread

def createIPAddressesFile():

    XML_PATH = r"C:\Temp\INP\INP.xml"
    ADDRESSES_PATH = r"C:\Temp\INP\ipAddresses.txt"

    # Add RFC1918 addresses
    rfc1918 = "192.168.0.0/16^&172.16.0.0/12^&10.0.0.0/8"
    os.system("echo {0} > {1}".format(rfc1918, ADDRESSES_PATH))

    # Look at machine IP addresses
    os.system("for /F \"tokens=1,2,3 delims= \" %a in ('netsh interface ipv4 show addresses ^| findstr \"Prefix:\"')"
              r" do echo|set /p=XXX%c >> {0}".format(ADDRESSES_PATH))

    # Check if there is already XML with configures IP spaces
    if (os.path.exists(XML_PATH) and os.path.isfile(XML_PATH)):
        fp = open(XML_PATH, "r")
        for cnt, line in enumerate(fp):
            line = line.replace("\t","")
            if line.startswith("<Network>"):
                line = line.replace("<Network>", "")
                line = line.replace("</Network>", "")
                line = line.replace("\n", "")
                os.system("echo XXX{0} >> {1}".format(line, ADDRESSES_PATH))

    fp.close()
    fp = open(ADDRESSES_PATH, "r")
    data = fp.read()
    fp.close()
    data = data.replace(" ", "")
    data = data.replace("XXX", "&")
    data = data.replace("\r", "")
    data = data.replace("\n", "")
    fp = open(ADDRESSES_PATH, "w")
    fp.write(data)
    fp.close()


def main():
    createIPAddressesFile()

main()

