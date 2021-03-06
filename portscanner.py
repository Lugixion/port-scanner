import socket
import sys

def get_valid_anser():
    while True:
        answer = input("Type A to a range of ports or B to check a specific one")
        if answer in "AB":
            return answer
        print("Invalid input")

answer = get_valid_anser()

if answer == "A":

    remoteServer    = input("Enter a remote host to scan: ")
    remoteServerIP  = socket.gethostbyname(remoteServer)


    print("-" * 60)
    print("Please wait, scanning remote host", remoteServerIP)
    print("-" * 60)

    x = int(input("Port to start checking on: "))
    y = int(input("Port to check to: "))

    def get_valid_ask():
        while True:
            answer = input("Do you want to print closed ports? Y/N")
            if answer in "YN":
                return answer
            print("Invalid input")

    ask = get_valid_ask()

    def get_valid_exportopen():
        while True:
            answer = input("Do you want to export open ports to a txt file? Y/N")
            if answer in "YN":
                return answer
            print("Invalid input")

    exportopen = get_valid_exportopen()

    def get_valid_exportclosed():
        while True:
            answer = input("Do you want to export closed ports to a txt file? Y/N")
            if answer in "YN":
                return answer
            print("Invalid input")

    exportclosed = get_valid_exportclosed()

    if exportopen == "Y" or exportclosed == "Y":
        f = open("ports.txt", "w")

    try:
        for port in range(x,y+1):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex((remoteServerIP, port))
            if result == 0:
                print("Port {}: 	 Open".format(port))
                if exportopen == "Y":
                    f.write("Port {}: 	 Open".format(port) + '\n')
            else:
                if ask == "Y":
                    print("Port {}: 	 Closed".format(port))
                if exportclosed == "Y":
                    f.write("Port {}: 	 Closed".format(port) + '\n')
            sock.close()


    except KeyboardInterrupt:
        prin("You pressed Ctrl+C")
        sys.exit()

    except socket.gaierror:
        print('Hostname could not be resolved. Exiting')
        sys.exit()

    except socket.error:
        print("Couldn't connect to server")
        sys.exit()



    print('Scanning Completed ')

else:

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(5)

    host2 = raw_input("Please enter the IP you want to scan: ")
    port2 = int(input("Please enter the port you want to scan: "))


    def portScanner(port2):
        if s.connect_ex((host2, port2)):
            print("The port is closed")
        else:
            print("The port is open")

    portScanner(port2)
