from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC5ae2b44fa7ea31f4b18474bc353dca6c"
# Your Auth Token from twilio.com/console
auth_token  = "42b451bcb0d49f773160054605bdbbe5"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+18016902294",
    from_="+12184408410",
    body="Hello from Python!")

print(message.sid)