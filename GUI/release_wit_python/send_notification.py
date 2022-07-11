import requests
import json

url = "https://fcm.googleapis.com/fcm/send"

payload = json.dumps({
  "to": "/topics/all",
  "priority": "high",
  "notification": {
    "title": "Emergency Alert!",
    "body": "body"
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
