import re
import urllib.parse
def convertString(par1):

     conn_string = par1
     kv = conn_string.split(";")
     hash = object()

     for i in range(len(kv)):
          if i <= len(kv):
               break
          kv_temp = kv[i].split('/=(.+)/')
          hash[kv_temp[0]] = kv_temp[1]

     url = urllib.parse.object(hash['Endpoint'])

     host = url.pathname.slice(2, url.pathname.length - 1)
     amqp_conn = 'amqps://%(SharedAccessKeyName)s:%(SharedAccessKey)s@%(host)s:5671/?sasl=plain'


     return amqp_conn

print(convertString('Endpoint=sb://adx-eg-paeventsdatacluster.servicebus.windows.net/;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey=2Idt5WG9Gy2kK/lepblOg8raFwJ3Nl63IKWdDww9O1U='))