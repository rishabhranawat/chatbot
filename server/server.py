"""
The server will accept requests and send back responses -

The server interacts via a client that is either web based, sms based or command line based.


how to run:

python server.py

new tab

python client.py --debug (launches a shell)

OR

python client.py --web (launches a web interface)

OR

python client.py --sms (launches a psuedo sms application, working over twilio messages)

By 
Eric Schles
"""


from app import app
app.run()
