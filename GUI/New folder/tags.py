import tkinter as tk
import tkinter.font as tkFont
import serial.tools.list_ports
from PIL import Image, ImageTk
import os
import  vlc
import time
import requests
import json
from firebase import firebase


serialObj = serial.Serial()
#serialObj.port = "/dev/ttyACM0"
serialObj.port = "/dev/ttyACM0"
serialObj.baudrate = 9600
serialObj.open()

text = ""
root = tk.Tk()


width=800
height=480
screenwidth = root.winfo_screenwidth()
screenheight = root.winfo_screenheight()
alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
root.geometry(alignstr)
root.resizable(width=False, height=False)



def checkSerialPort():
    if serialObj.isOpen() and serialObj.in_waiting:
        recentPacket = serialObj.readline()
        recentPacketString = recentPacket.decode('utf').rstrip('\n')
        
        firebase = firebase.FirebaseApplication('https://car-monitor-kit-default-rtdb.firebaseio.com/', None)
        tempp = firebase.put("/", "/temp", temp)
        psii = firebase.put("/", "/wbl", psi) 
        
        temp=0
        psi=0
        del temp
        del psi
        temp,psi,wtemp,Door = recentPacketString.split(':')
        tempp = firebase.put("/", "/temp", temp)
        psii = firebase.put("/", "/wbl", psi) 
        
        image1 = Image.open("car-interface.jpg")
        test = ImageTk.PhotoImage(image1)

        label1 = tk.Label(image=test)
        label1.image = test
        label1.place(x=0, y=0)
        
        
        GLabel_1=tk.Label(root)
        ft = tkFont.Font(family='Times',size=30)
        GLabel_1["font"] = ft
        GLabel_1["bg"] = "#3d4548"
        GLabel_1["justify"] = "center"
        GLabel_1["text"] = "Car Monitor Kit"
        GLabel_1.place(x=5,y=10,width=790,height=40)

        GLabel_16=tk.Label(root)
        ft = tkFont.Font(family='Times',size=20)
        GLabel_16["font"] = ft
        GLabel_16["bg"] = "#3d4548"
        GLabel_16["justify"] = "center"
        GLabel_16["text"] = "Speed = 80 km/h" # speed
        GLabel_16.place(x=530,y=417,width=200,height=25)

        GLabel_54=tk.Label(root)
        ft = tkFont.Font(family='Times',size=20)
        GLabel_54["font"] = ft
        GLabel_54["bg"] = "#3d4548"
        GLabel_54["justify"] = "center"
        GLabel_54["text"] ="temp = " + temp + " c"# temp
        GLabel_54.place(x=70,y=417,width=200,height=25)
        

        GLabel_823=tk.Label(root)
        ft = tkFont.Font(family='Times',size=20)
        GLabel_823["font"] = ft
        GLabel_823["bg"] = "#485156"
        GLabel_823["justify"] = "center"
        GLabel_823["text"] = psi +" psi" # wfl
        GLabel_823.place(x=100,y=150,width=70,height=25)

        GLabel_103=tk.Label(root)
        ft = tkFont.Font(family='Times',size=20)
        GLabel_103["font"] = ft
        GLabel_103["bg"] = "#424c4e"
        GLabel_103["justify"] = "center"
        GLabel_103["text"] = "35"
        GLabel_103.place(x=100,y=300,width=70,height=25)

        GLabel_31=tk.Label(root)
        ft = tkFont.Font(family='Times',size=20)
        GLabel_31["font"] = ft
        GLabel_31["bg"] = "#485156"
        GLabel_31["justify"] = "center"
        GLabel_31["text"] = "35"
        GLabel_31.place(x=630,y=150,width=70,height=25)

        GLabel_615=tk.Label(root)
        ft = tkFont.Font(family='Times',size=20)
        GLabel_615["font"] = ft
        GLabel_615["bg"] = "#424c4e"
        GLabel_615["justify"] = "center"
        GLabel_615["text"] = "35"
        GLabel_615.place(x=630,y=300,width=70,height=25)
        
        if (int(temp) >= 40):
            
            url = "https://fcm.googleapis.com/fcm/send"

            payload = json.dumps({
            "to": "/topics/all",
            "priority": "high",
            "notification": {
                "title": "Emergency Alert!",
                "body": "temperature is high please stop and check cooling system"
            },
            "data": {
                "your_custom_data": "data"
            }
            })
            headers = {
            'Authorization': 'key=AAAAiCzukI8:APA91bGr50xiGAzGjMgiMYxdx2ntg0hhaxoX6DSrxtT4gZHm9brbi4D-1ed0fGeRMm7-miHHv6djfFypSbENbtOAQT8cN4bSPhDY7m1x0b3m9GMiAqUTqOsXVv4qF877jD3Y7VC_vjq-',
            'Content-Type': 'application/json'
            }

            response = requests.request("POST", url, headers=headers, data=payload)

            print(response.text)
            p = vlc.MediaPlayer("temp.mp3")
            p.play()
            time.sleep(10)
            p.stop()
            
        del temp
        recentPacket = serialObj.readline()
        recentPacketString = recentPacket.decode('utf').rstrip('\n')
        temp,psi,wtemp,Door = recentPacketString.split(':')
        print("uhim")
        if (int(psi) >= 35):
            url = "https://fcm.googleapis.com/fcm/send"

            payload = json.dumps({
            "to": "/topics/all",
            "priority": "high",
            "notification": {
                "title": "Emergency Alert!",
                "body": "The tire pressure is High, please stop and check the tires"
            },
            "data": {
                "your_custom_data": "data"
            }
            })
            headers = {
            'Authorization': 'key=AAAAiCzukI8:APA91bGr50xiGAzGjMgiMYxdx2ntg0hhaxoX6DSrxtT4gZHm9brbi4D-1ed0fGeRMm7-miHHv6djfFypSbENbtOAQT8cN4bSPhDY7m1x0b3m9GMiAqUTqOsXVv4qF877jD3Y7VC_vjq-',
            'Content-Type': 'application/json'
            }

            response = requests.request("POST", url, headers=headers, data=payload)

            print(response.text)
            p = vlc.MediaPlayer("tire_high.mp3")
            p.play()
            time.sleep(30)
            p.stop()
            
        if (int(psi) <= 13):
            url = "https://fcm.googleapis.com/fcm/send"

            payload = json.dumps({
            "to": "/topics/all",
            "priority": "high",
            "notification": {
                "title": "Emergency Alert!",
                "body": "The tire pressure is LOW, please stop and check the tires"
            },
            "data": {
                "your_custom_data": "data"
            }
            })
            headers = {
            'Authorization': 'key=AAAAiCzukI8:APA91bGr50xiGAzGjMgiMYxdx2ntg0hhaxoX6DSrxtT4gZHm9brbi4D-1ed0fGeRMm7-miHHv6djfFypSbENbtOAQT8cN4bSPhDY7m1x0b3m9GMiAqUTqOsXVv4qF877jD3Y7VC_vjq-',
            'Content-Type': 'application/json'
            }

            response = requests.request("POST", url, headers=headers, data=payload)

            print(response.text)
            p = vlc.MediaPlayer("tire_low.mp3")
            p.play()
            time.sleep(10)
            p.stop()
            
        del psi




while True:
    root.update()
    checkSerialPort()

