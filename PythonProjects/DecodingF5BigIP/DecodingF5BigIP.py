


import struct

import sys




def decode(cookie_value):

    (host, port, end) = cookie_value.split('.')
    (ip1, ip2, ip3, ip4) = [i for i in struct.pack("<I", int(host))]

    p = [i for i in struct.pack("<I", int(port))]
    port = p[0] * 256 + p[1]
    print(" IP : Port --> %+3s.%+3s.%+3s.%+3s:%+5s" % (ip1, ip2, ip3, ip4, port))












if __name__ == '__main__':


    # cookie_value = sys.argv[1]
    cookie_value = "110536896.20480.0000"

    if(len(cookie_value.split('.')) != 3 ):
        print("Please input the correct bigIP")
    else:
        decode(cookie_value)

