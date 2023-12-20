import socket
from _pydatetime import datetime

target =input("Enter target ip : ")

def port_scan(target):
    try:
        ip = socket.gethostbyname(target)

        print(f"Sacnning the target {target}.")
        print("Time started : ",datetime.now())

        for port in range(20,3306):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((ip, port))
            if result == 0:
                print("port {} : open".format(port))
                sock.close()
    except socket.gaierror:
        print("Hostname could not be resolved")
    except socket.error:
        print("Could not connect to the server")


port_scan(target)