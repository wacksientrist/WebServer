from http.server import BaseHTTPRequestHandler, CGIHTTPRequestHandler, HTTPServer
import socketserver
from urllib.parse import urlparse
from time import sleep as sleep
import os
sleep(10)
hostName = "10.38.94.206"
serverPort = 8080
#os.system('sudo raspi-gpio set 25 op')
#os.system('sudo raspi-gpio set 24 op')
#os.system('sudo raspi-gpio set 23 op')

Coffee = 0
Light = 0
Money = 0

class MyServer(BaseHTTPRequestHandler):
    def Check(self):
        if Coffee == 0:
            self.wfile.write(bytes('<button id="coffee" style="background-color:Green;"/> <a href="http://10.38.94.206:8080/CoffeeOn"/>Click For Coffee!</button>', "utf-8"))
            print("Coffee: OFF")
        elif Coffee == 1:
            self.wfile.write(bytes('<button id="coffee" style="background-color:Yellow;"/> <a href="http://10.38.94.206:8080/CoffeeOff"/>Click No Coffee!</button>', "utf-8"))
            print("Coffee: ON")
        if Light == 0:
            self.wfile.write(bytes('<button id="coffee" style="background-color:Green;"/> <a href="http://10.38.94.206:8080/LightOn"/>Click For Light!</button>', "utf-8"))
            print("Light: OFF")
        elif Light == 1:
            self.wfile.write(bytes('<button id="coffee" style="background-color:Yellow;"/> <a href="http://10.38.94.206:8080/LightOff"/>Click No Light!</button>', "utf-8"))
            print("Light: ON")
        if Money == 0:
            self.wfile.write(bytes('<button id="coffee" style="background-color:Green;"/> <a href="http://10.38.94.206:8080/MoneyOn"/>Click For Money!</button>', "utf-8"))
            print("Money: OFF")
        elif Money == 1:
            self.wfile.write(bytes('<button id="coffee" style="background-color:Yellow;"/> <a href="http://10.38.94.206:8080/MoneyOff"/>Click No Money!</button>', "utf-8"))
            print("Money: ON")

    def do_GET(self):
        if self.path == '/'+'CoffeeOn':
            Coffee = 1
            
            #os.system('sudo raspi-gpio set 25 dh')
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(bytes("<html><head><title>I Dont Want Coffee!</title></head>", "utf-8"))
            self.wfile.write(bytes("<body>", "utf-8"))
                
            self.wfile.write(bytes("</body></html>", "utf-8"))
        if self.path == '/'+'CoffeeOff':
            Coffee = 0
            #os.system('sudo raspi-gpio set 25 dl')
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(bytes("<html><head><title>I Want Coffee!</title></head>", "utf-8"))
            self.wfile.write(bytes("<body>", "utf-8"))

            self.Check()

            self.wfile.write(bytes("</body></html>", "utf-8"))
        if self.path == '/'+'LightOn':
            Light = 1
            #os.system('sudo raspi-gpio set 24 dh')
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(bytes("<html><head><title>I Dont Want Coffee!</title></head>", "utf-8"))
            self.wfile.write(bytes("<body>", "utf-8"))
                                 
            self.Check()

            self.wfile.write(bytes("</body></html>", "utf-8"))
        if self.path == '/'+'LightOff':
            Light = 0
            #os.system('sudo raspi-gpio set 24 dl')
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(bytes("<html><head><title>I Dont Want Coffee!</title></head>", "utf-8"))
            self.wfile.write(bytes("<body>", "utf-8"))
                                 
            self.Check()

            self.wfile.write(bytes("</body></html>", "utf-8"))
        if self.path == '/'+'MoneyOn':
            Money = 1
            #os.system('sudo raspi-gpio set 23 dh')
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(bytes("<html><head><title>I Dont Want Coffee!</title></head>", "utf-8"))
            self.wfile.write(bytes("<body>", "utf-8"))

            self.Check()

            self.wfile.write(bytes("</body></html>", "utf-8"))                  
            
        if self.path == '/'+'MoneyOff':
            Money = 0
            #os.system('sudo raspi-gpio set 23 dl')
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(bytes("<html><head><title>I Dont Want Coffee!</title></head>", "utf-8"))
            self.wfile.write(bytes("<body>", "utf-8"))

            self.wfile.write(bytes("</body></html>", "utf-8"))
        if self.path == '/'+'BannanaOn':
            #os.system('sudo raspi-gpio set 25 dh')
            #os.system('sudo raspi-gpio set 24 dh')
            #os.system('sudo raspi-gpio set 23 dh')
            print("Bannana: ON")
        if self.path == '/'+'BannanaOff':
            #os.system('sudo raspi-gpio set 25 dl')
            #os.system('sudo raspi-gpio set 24 dl')
            #os.system('sudo raspi-gpio set 23 dl')
            print("Bannana: OFF")
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(bytes("<html><head><title>I Want Coffee</title></head>", "utf-8"))
            self.wfile.write(bytes("<body>", "utf-8"))
            self.wfile.write(bytes('<button id="coffee" style="background-color:Green;"/> <a href="http://10.38.94.206:8080/CoffeeOn"/>Click For Coffee!</button>', "utf-8"))
            self.wfile.write(bytes('<button id="coffee" style="background-color:Green;"/> <a href="http://10.38.94.206:8080/LightOn"/>Click For Light!</button>', "utf-8"))
            self.wfile.write(bytes('<button id="coffee" style="background-color:Green;"/> <a href="http://10.38.94.206:8080/MoneyOn"/>Click For Money!</button>', "utf-8"))
            self.wfile.write(bytes("</body></html>", "utf-8"))
        
webServer = HTTPServer((hostName, serverPort), MyServer)
print("Server started http://%s:%s" % (hostName, serverPort))
webServer.serve_forever()

if KeyboardInterrupt == True:
    webServer.shutdown()
