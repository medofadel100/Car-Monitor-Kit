import http.client
import json

conn = http.client.HTTPSConnection("fcm.googleapis.com")
payload = json.dumps({
  "to": "/topics/egypark",
  "priority": "high",
  "notification": {
    "title": "Emergency Alert2222222222!", # <- change title
    "body": "body" # <- change body
  },
  "data": {
    "your_custom_data": "data"
  }
})
headers = {
  'Authorization': 'key=AAAAaQIyZmI:APA91bE6G5hFhno9VH58jwGWxeHybAZ_S3n6aN3gzLVMc9fgD5QO8oXIRAOfYL7z5y_5UpKXuo4I1lSzLalCj8-WguN_cArXLdSXtz1dWIoaKMeMOEjodhYfFKdzMHC0-UXbWz0PpJ-d',
  'Content-Type': 'application/json'
}
conn.request("POST", "/fcm/send", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
