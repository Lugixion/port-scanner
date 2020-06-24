import socket
import sys

print("Type A to a range of ports or B to check a specific one")
answer = raw_input()
if answer == "A":

    remoteServer    = raw_input("Enter a remote host to scan: ")
    remoteServerIP  = socket.gethostbyname(remoteServer)


    print "-" * 60
    print "Please wait, scanning remote host", remoteServerIP
    print "-" * 60

    x = int(input("Port to start checking on: "))
    y = int(input("Port to check to: "))
    print("Do you want to print closed ports?")
    ask = raw_input()

    try:
        for port in range(x,y+1):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex((remoteServerIP, port))
            if result == 0:
                print "Port {}: 	 Open".format(port)
            else:
                if ask == "Y":
                    print "Port {}: 	 Closed".format(port)
            sock.close()

    except KeyboardInterrupt:
        print "You pressed Ctrl+C"
        sys.exit()

    except socket.gaierror:
        print 'Hostname could not be resolved. Exiting'
        sys.exit()

    except socket.error:
        print "Couldn't connect to server"
        sys.exit()



    print 'Scanning Completed '

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
