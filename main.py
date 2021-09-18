import os
from twilio.rest import Client

account_sid = os.environ['account_sid']
auth_token = os.environ['auth_token']
to_whatsapp_no = os.environ['to_whatsapp_no']

client = Client(account_sid, auth_token)

message = client.messages.create(
                              body='Yay! Push event triggered in master branch',
                              from_='whatsapp:'+from_whatsapp_no,
                              to='whatsapp:'+to_whatsapp_no
                          )

print("Message ID:",message.sid)
