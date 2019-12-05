
import struct




def main():
    print("staring")

    #839518730.47873.0000


    cookie_string = "1401452298.0.0000"


    (cookie_ip, cookie_port, end) = cookie_string.split('.')


    (ip1, ip2, ip3, ip4) = (i for i in struct.pack("<I", int(cookie_ip)))

    p = [i for i in struct.pack("<I", int(cookie_port))]

    serverport = p[0]*256 + p[1]





    server_ip = str(ip1) + "." + str(ip2) + "." + str(ip3) + "." + str(ip4)



    print("server_ip : %s ; server_port : %s "  %(server_ip, str(serverport)))





if __name__ == '__main__':
    main()

