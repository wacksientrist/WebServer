from http.server import BaseHTTPRequestHandler, CGIHTTPRequestHandler, HTTPServer
import time
import os
time.sleep(10)
hostName = "172.20.10.5"
serverPort = 8080
os.system('sudo raspi-gpio set 25 op')
os.system('sudo raspi-gpio set 24 op')
os.system('sudo raspi-gpio set 23 op')
class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        Coffee = 0
        Light = 0
        Money = 0
        if self.path == '/'+'CoffeeOn':
            Coffee = 1
            
            os.system('sudo raspi-gpio set 25 dh')
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(bytes("<html><head><title>I Dont Want Coffee!</title></head>", "utf-8"))
            self.wfile.write(bytes("<body>", "utf-8"))
            
            if Coffee == 0:
                self.wfile.write(bytes('<button id="coffee" style="background-color:Green;"/> <a href="http://172.20.10.5:8080/CoffeeOn"/>Click For Light!</button>', "utf-8"))
            elif Coffee == 1:
                self.wfile.write(bytes('<button id="coffee" style="background-color:Yellow;"/> <a href="http://172.20.10.5:8080/CoffeeOff"/>Click For Light!</button>', "utf-8")
            if Light == 0:
                self.wfile.write(bytes('<button id="coffee" style="background-color:Green;"/> <a href="http://172.20.10.5:8080/LightOn"/>Click For Light!</button>', "utf-8"))
            elif Light == 1:
                self.wfile.write(bytes('<button id="coffee" style="background-color:Yellow;"/> <a href="http://172.20.10.5:8080/LightOff"/>Click For Light!</button>', "utf-8"))
            if Money == 0:
                self.wfile.write(bytes('<button id="coffee" style="background-color:Green;"/> <a href="http://172.20.10.5:8080/MoneyOn"/>Click For Light!</button>', "utf-8"))
            elif Money == 1:
                self.wfile.write(bytes('<button id="coffee" style="background-color:Yellow;"/> <a href="http://172.20.10.5:8080/MoneyOff"/>Click For Light!</button>', "utf-8")

                
            self.wfile.write(bytes("</body></html>", "utf-8"))
        if self.path == '/'+'CoffeeOff':
            Coffee = 0
            os.system('sudo raspi-gpio set 25 dl')
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(bytes("<html><head><title>I Want Coffee!</title></head>", "utf-8"))
            self.wfile.write(bytes("<body>", "utf-8"))
                                 
            if Coffee == 0:
                self.wfile.write(bytes('<button id="coffee" style="background-color:Green;"/> <a href="http://172.20.10.5:8080/CoffeeOn"/>Click For Light!</button>', "utf-8"))
            elif Coffee == 1:
                self.wfile.write(bytes('<button id="coffee" style="background-color:Yellow;"/> <a href="http://172.20.10.5:8080/CoffeeOff"/>Click For Light!</button>', "utf-8")
            if Light == 0:
                self.wfile.write(bytes('<button id="coffee" style="background-color:Green;"/> <a href="http://172.20.10.5:8080/LightOn"/>Click For Light!</button>', "utf-8"))
            elif Light == 1:
                self.wfile.write(bytes('<button id="coffee" style="background-color:Yellow;"/> <a href="http://172.20.10.5:8080/LightOff"/>Click For Light!</button>', "utf-8"))
            if Money == 0:
                self.wfile.write(bytes('<button id="coffee" style="background-color:Green;"/> <a href="http://172.20.10.5:8080/MoneyOn"/>Click For Light!</button>', "utf-8"))
            elif Money == 1:
                self.wfile.write(bytes('<button id="coffee" style="background-color:Yellow;"/> <a href="http://172.20.10.5:8080/MoneyOff"/>Click For Light!</button>', "utf-8")

            self.wfile.write(bytes("</body></html>", "utf-8"))
        if self.path == '/'+'LightOn':
            Light == 1
            os.system('sudo raspi-gpio set 24 dh')
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(bytes("<html><head><title>I Dont Want Coffee!</title></head>", "utf-8"))
            self.wfile.write(bytes("<body>", "utf-8"))
                                 
            if Coffee == 0:
                self.wfile.write(bytes('<button id="coffee" style="background-color:Green;"/> <a href="http://172.20.10.5:8080/CoffeeOn"/>Click For Light!</button>', "utf-8"))
            elif Coffee == 1:
                self.wfile.write(bytes('<button id="coffee" style="background-color:Yellow;"/> <a href="http://172.20.10.5:8080/CoffeeOff"/>Click For Light!</button>', "utf-8")
            if Light == 0:
                self.wfile.write(bytes('<button id="coffee" style="background-color:Green;"/> <a href="http://172.20.10.5:8080/LightOn"/>Click For Light!</button>', "utf-8"))
            elif Light == 1:
                self.wfile.write(bytes('<button id="coffee" style="background-color:Yellow;"/> <a href="http://172.20.10.5:8080/LightOff"/>Click For Light!</button>', "utf-8"))
            if Money == 0:
                self.wfile.write(bytes('<button id="coffee" style="background-color:Green;"/> <a href="http://172.20.10.5:8080/MoneyOn"/>Click For Light!</button>', "utf-8"))
            elif Money == 1:
                self.wfile.write(bytes('<button id="coffee" style="background-color:Yellow;"/> <a href="http://172.20.10.5:8080/MoneyOff"/>Click For Light!</button>', "utf-8")

            self.wfile.write(bytes("</body></html>", "utf-8"))
        if self.path == '/'+'LightOff':
            Light = 0
            os.system('sudo raspi-gpio set 24 dl')
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(bytes("<html><head><title>I Dont Want Coffee!</title></head>", "utf-8"))
            self.wfile.write(bytes("<body>", "utf-8"))
                                 
            if Coffee == 0:
                self.wfile.write(bytes('<button id="coffee" style="background-color:Green;"/> <a href="http://172.20.10.5:8080/CoffeeOn"/>Click For Light!</button>', "utf-8"))
            elif Coffee == 1:
                self.wfile.write(bytes('<button id="coffee" style="background-color:Yellow;"/> <a href="http://172.20.10.5:8080/CoffeeOff"/>Click For Light!</button>', "utf-8")
            if Light == 0:
                self.wfile.write(bytes('<button id="coffee" style="background-color:Green;"/> <a href="http://172.20.10.5:8080/LightOn"/>Click For Light!</button>', "utf-8"))
            elif Light == 1:
                self.wfile.write(bytes('<button id="coffee" style="background-color:Yellow;"/> <a href="http://172.20.10.5:8080/LightOff"/>Click For Light!</button>', "utf-8"))
            if Money == 0:
                self.wfile.write(bytes('<button id="coffee" style="background-color:Green;"/> <a href="http://172.20.10.5:8080/MoneyOn"/>Click For Light!</button>', "utf-8"))
            elif Money == 1:
                self.wfile.write(bytes('<button id="coffee" style="background-color:Yellow;"/> <a href="http://172.20.10.5:8080/MoneyOff"/>Click For Light!</button>', "utf-8")

            self.wfile.write(bytes("</body></html>", "utf-8"))
        if self.path == '/'+'MoneyOn':
            Money = 1
            os.system('sudo raspi-gpio set 23 dh')
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(bytes("<html><head><title>I Dont Want Coffee!</title></head>", "utf-8"))
            self.wfile.write(bytes("<body>", "utf-8"))
            if Coffee == 0:
                self.wfile.write(bytes('<button id="coffee" style="background-color:Green;"/> <a href="http://172.20.10.5:8080/CoffeeOn"/>Click For Light!</button>', "utf-8"))
            elif Coffee == 1:
                self.wfile.write(bytes('<button id="coffee" style="background-color:Yellow;"/> <a href="http://172.20.10.5:8080/CoffeeOff"/>Click For Light!</button>', "utf-8")
            if Light == 0:
                self.wfile.write(bytes('<button id="coffee" style="background-color:Green;"/> <a href="http://172.20.10.5:8080/LightOn"/>Click For Light!</button>', "utf-8"))
            elif Light == 1:
                self.wfile.write(bytes('<button id="coffee" style="background-color:Yellow;"/> <a href="http://172.20.10.5:8080/LightOff"/>Click For Light!</button>', "utf-8"))
            if Money == 0:
                self.wfile.write(bytes('<button id="coffee" style="background-color:Green;"/> <a href="http://172.20.10.5:8080/MoneyOn"/>Click For Light!</button>', "utf-8"))
            elif Money == 1:
                self.wfile.write(bytes('<button id="coffee" style="background-color:Yellow;"/> <a href="http://172.20.10.5:8080/MoneyOff"/>Click For Light!</button>', "utf-8")

            self.wfile.write(bytes("</body></html>", "utf-8"))                  
            
        if self.path == '/'+'MoneyOff':
            Money = 0
            os.system('sudo raspi-gpio set 23 dl')
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(bytes("<html><head><title>I Dont Want Coffee!</title></head>", "utf-8"))
            self.wfile.write(bytes("<body>", "utf-8"))
            if Coffee == 0:
                self.wfile.write(bytes('<button id="coffee" style="background-color:Green;"/> <a href="http://172.20.10.5:8080/CoffeeOn"/>Click For Light!</button>', "utf-8"))
            elif Coffee == 1:
                self.wfile.write(bytes('<button id="coffee" style="background-color:Yellow;"/> <a href="http://172.20.10.5:8080/CoffeeOff"/>Click For Light!</button>', "utf-8")
            if Light == 0:
                self.wfile.write(bytes('<button id="coffee" style="background-color:Green;"/> <a href="http://172.20.10.5:8080/LightOn"/>Click For Light!</button>', "utf-8"))
            elif Light == 1:
                self.wfile.write(bytes('<button id="coffee" style="background-color:Yellow;"/> <a href="http://172.20.10.5:8080/LightOff"/>Click For Light!</button>', "utf-8"))
            if Money == 0:
                self.wfile.write(bytes('<button id="coffee" style="background-color:Green;"/> <a href="http://172.20.10.5:8080/MoneyOn"/>Click For Light!</button>', "utf-8"))
            elif Money == 1:
                self.wfile.write(bytes('<button id="coffee" style="background-color:Yellow;"/> <a href="http://172.20.10.5:8080/MoneyOff"/>Click For Light!</button>', "utf-8")

            self.wfile.write(bytes("</body></html>", "utf-8"))
        if self.path == '/'+'BannanaOn':
            os.system('sudo raspi-gpio set 25 dh')
            os.system('sudo raspi-gpio set 24 dh')
            os.system('sudo raspi-gpio set 23 dh')
        if self.path == '/'+'BannanaOff':
            os.system('sudo raspi-gpio set 25 dl')
            os.system('sudo raspi-gpio set 24 dl')
            os.system('sudo raspi-gpio set 23 dl')
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(bytes("<html><head><title>I Want Coffee</title></head>", "utf-8"))
            self.wfile.write(bytes("<body>", "utf-8"))
            self.wfile.write(bytes('<button id="coffee" style="background-color:Green;"/> <a href="http://172.20.10.5:8080/CoffeeOn"/>Click For Coffee!</button>', "utf-8"))
            self.wfile.write(bytes('<button id="coffee" style="background-color:Green;"/> <a href="http://172.20.10.5:8080/LightOn"/>Click For Light!</button>', "utf-8"))
            self.wfile.write(bytes('<button id="coffee" style="background-color:Green;"/> <a href="http://172.20.10.5:8080/MoneyOn"/>Click For Money!</button>', "utf-8"))
            self.wfile.write(bytes("</body></html>", "utf-8"))
webServer = HTTPServer((hostName, serverPort), MyServer)
print("Server started http://%s:%s" % (hostName, serverPort))
webServer.serve_forever()

if KeyboardInterrupt == True:
    webServer.shutdown()
