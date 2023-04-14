import argparse
import colorama
from colorama import Fore, Back, Style
from scapy.all import *
from threading import Thread
from faker import Faker

colorama.init(autoreset=True)

def send_beacon(ssid, mac, infinite=True):
	dot11 = Dot11(type=0, subtype=8, addr1="ff:ff:ff:ff:ff:ff", addr2=mac, addr3=mac)
	beacon = Dot11Beacon()
	essid = Dot11Elt(ID="SSID", info=ssid, len=len(ssid))
	frame = RadioTap()/dot11/beacon/essid
	if infite:
		sendp(frame, inter=0.1, loop=1, iface=iface, verbose=1)
	else:
		sendp(frame, iface=iface, verbose=1)


argument_parser = argparse.ArgumentParser(description='')
argument_parser.add_argument('-i', help='')
args = argument_parser.parse_args()

faker = Faker()
ssid_mac = [(faker.name(), faker.mac_address())]

for ssid, mac in ssid_mac:
	send_beacon(ssid, mac)
