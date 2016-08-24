import socket
import struct
import textwrap
import string

def main():
    #conn = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3)) #ntoh makes sure its compatibale, big/small endian converting byte order
    conn = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3)) #ntoh makes sure its compatibale, big/small endian converting byte order
    while True:
        raw_data, addr = conn.recvfrom(65536)
        dest_mac, src_mac, eth_proto, data = ethernet_frame(raw_data)
        print ('\nEthernet Frame: ')
        print('Destination: {}, Source: {}, Protocol: {}'.format(dest_mac, src_mac , eth_proto))






def ethernet_frame(data):
    #passing in 1 and zeros, and protocol
    dest_mac, src_mac, proto = struct.unpack('! 6s 6s H', data[:14]) #6 bytes for dest & src, H for 14
    return get_mac_addr(dest_mac),get_mac_addr(src_mac), socket.htons(proto), data[14:]  #htons converts to convert endian

#return properly formatted mac address (AA:AA:AA:AA:AA:AA_
def get_mac_addr(bytes_addr):
    bytes_str = '{:02X}'.format(*bytes_addr)
    return ':'.join(bytes_str).upper()


main()
