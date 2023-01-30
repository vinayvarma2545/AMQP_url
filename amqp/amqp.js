  // Converts an Azure Connection String like this:
  //     Endpoint=sb://example.servicebus.windows.net/;SharedAccessKeyName=example-key;SharedAccessKey=Random/Chars/Need/Encoding=;EntityPath=example-entity
  // to one accepted by the RabbitMQ Shovel Plugin:
  //     amqps://example-key:Random%2FChars%2FNeed%2FEncoding@example.servicebus.windows.net:5671/?sasl=plain
  function convertString(par1) {
    
    var conn_string = par1
    var kv = conn_string.split(';');
    var hash = {}
    for (var i = 0; i < kv.length; i++) {

      var kv_temp = kv[i].split(/=(.+)/);
      hash[kv_temp[0]] = kv_temp[1];
    }

    var url = new URL(hash['Endpoint']);
    var host = url.pathname.slice(2, url.pathname.length - 1);

    var amqp_conn = amqps//%(SharedAccessKeyName)s:%(SharedAccessKey)s@%(host)s:5671/?sasl=plain
    return amqp_conn
  }

  console.log(convertString('Endpoint=sb://adx-eg-paeventsdatacluster.servicebus.windows.net/;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey=2Idt5WG9Gy2kK/lepblOg8raFwJ3Nl63IKWdDww9O1U='))