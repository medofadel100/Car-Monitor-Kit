from onesignal import OneSignal, SegmentNotification

client = OneSignal("01ee2b88-5d21-4160-8d62-1bb8bf8c5827" , "Nzk5MWMxMGUtMWI4OS00OTI1LWJkNGYtNjkzZDUzYzMzYmM2")
notification_to_all_users = SegmentNotification(
    contents={
        "en": "Hello from OneSignal-Notifications"
    },
    included_segments=SegmentNotification.ALL
)
client.send(notification_to_all_users)