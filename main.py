import sipfullproxy

def startProxy():
    sipfullproxy.logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s',filename='proxy.log',level=sipfullproxy.logging.INFO,datefmt='%H:%M:%S')
    sipfullproxy.logging.info(sipfullproxy.time.strftime("%a, %d %b %Y %H:%M:%S ", sipfullproxy.time.localtime()))
    hostname = sipfullproxy.socket.gethostname()
    sipfullproxy.logging.info(hostname)
    ipaddress = sipfullproxy.sys.argv[1]
    sipfullproxy.logging.info(ipaddress)
    sipfullproxy.recordroute = "Record-Route: <sip:%s:%d;lr>" % (ipaddress, sipfullproxy.PORT)
    sipfullproxy.topvia = "Via: SIP/2.0/UDP %s:%d" % (ipaddress,sipfullproxy.PORT)
    server = sipfullproxy.socketserver.UDPServer((sipfullproxy.HOST, sipfullproxy.PORT), sipfullproxy.UDPHandler)
    server.serve_forever()

if __name__ == "__main__":    
    startProxy()