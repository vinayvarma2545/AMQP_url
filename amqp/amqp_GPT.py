import urllib.parse

def convert_string(par1):
    conn_string = par1
    kv = conn_string.split(';')
    hash = {}
    for i in range(len(kv)):
        kv_temp = kv[i].split('=')
        hash[kv_temp[0]] = kv_temp[1]
    
    url = urllib.parse.urlsplit(hash['Endpoint'])
    host = url.path[2:-1]
    
    amqp_conn = f'amqps://{urllib.parse.quote(hash["SharedAccessKeyName"])}:{urllib.parse.quote(hash["SharedAccessKey"])}@{host}:5671/?sasl=plain'
    return amqp_conn

print(convert_string('Endpoint=sb://adx-eg-paeventsdatacluster.servicebus.windows.net/;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey=2Idt5WG9Gy2kK/lepblOg8raFwJ3Nl63IKWdDww9O1U='))
