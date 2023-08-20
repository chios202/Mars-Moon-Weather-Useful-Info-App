import socket
from ScraperRealTime import RealTime, Scraping

class  UnexpectedValue(Exception):
    pass 

class SocketServer:


    def __init__(self,ip,port):
        self.ip = ip
        self.port = port
        self.server_socket = socket.socket()


    def configureServer(self):
        self.server_socket.bind((self.ip, self.port))
        self.server_socket.listen(4)

    def sendDataToClient(self):

        while True:
            socket,adress = self.server_socket.accept()
            data = socket.recv(1024).decode()
            if (data == "1"):
                scraper = Scraping(RealTime("https://moon.nasa.gov/", "profile"))
                socket.send(bytes(scraper.getLRO(), "utf-8"))
            elif (data == "2"):
                scraper = Scraping(RealTime("https://solarsystem.nasa.gov/planets/mars/overview/", "profile2"))
                socket.send(bytes(scraper.getDistanceFromSun(), "utf-8"))
            else:
                raise UnexpectedValue


            print(f"Succesfully connected and sent data to {adress}")



if __name__ == "__main__":
    server = SocketServer("192.168.1.3", 1234)
    try:
        server.configureServer()
        server.sendDataToClient()
    except UnexpectedValue:
        pass
    



