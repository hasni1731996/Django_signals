import urllib2

from twilio.rest import Client

account_sid = 'AC2e57b7668825e995be6264b2775eb274' # Found on Twilio Console Dashboard
auth_token = '51da85b1fedff0a98d87639183b824ac' # Found on Twilio Console Dashboard

myPhone = '' # Phone number you used to verify your Twilio account
# TwilioNumber = '' # Phone number given to you by Twilio
# #
# # client = Client(account_sid, auth_token)
# #
# # message=client.messages.create(
# #   to='+923013018173',
# #   from_='+16025368995',
# #   body='I set a text message from Python! ' + u'\U0001f680')
# # print message.status
###############################TWILIO ENDS CODE HERE####################
#import urllib.request
from six.moves import urllib
from six.moves.urllib.parse import urlencode
def sendSMS(apikey, numbers, sender, message):
    url ='https://api.txtlocal.com/send/?'
    params = {'apikey': apikey, 'numbers': numbers, 'message': message, 'sender': sender}
    data = urlencode(params)
    data = data.encode('Big5')
    req = urllib2.Request(url, data)
    response = urllib2.urlopen(req)
    return (response.read(), response.code)


resp, code = sendSMS('5BxrE8v7suo-ww4OHpymlYZ6X9VupvXTiykhHYmeCf', '+923013018173',
                     'Jims Autos', 'Test with an ampersan')
print (resp)