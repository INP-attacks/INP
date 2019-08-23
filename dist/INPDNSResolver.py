import sys
import socket
import time

filePath = sys.argv[0]

try:
    with open(filePath, "rb") as f:
        data = f.read()
        f.close()
    ips = "&".join(socket.gethostbyname_ex(data)[2])
    data_to_write = "[START_RESP]" + ips + "[END_RESP]"
    with open(filePath, "wb") as f:
        f.write(data_to_write)
        f.close()
except:
    with open(filePath, "wb") as f:
        data_to_write = "[START_RESP][END_RESP]"
        f.write(data_to_write)
        f.close()
