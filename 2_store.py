import pyshark
from termcolor import colored,cprint
import os
import time
import sys
#find oldest file in directory
import mysql.connector
from datetime import datetime
import pytz
ist = pytz.timezone("Asia/Kolkata")
#all time zones print : zones = pytz.all_timezones
#https://thepacketgeek.com/pyshark/intro-to-pyshark/#:~:text=PyShark%20is%20a%20wrapper%20for,new%20tool%3A%20Cloud%2DPcap.
print('developed and maintained by SIDHARTH RASHWANA')
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="NetBytes"
)
mycursor = mydb.cursor()
print(mycursor)

path='/home/darth6/Projects/Web Based Traffic Analyzer/NetBytes/capture'
fullpath="find '%s' -type f  | sort | head -n 1"%(path)
oldestFile = os.popen(fullpath).read()
output = str(oldestFile)
oldestFile = output.splitlines()
print("Resultant prefix", str(oldestFile))
oldestFile=str(oldestFile[0])
print("oldest captured file: "+oldestFile)
  
#read the oldest captured file
capture = pyshark.FileCapture(oldestFile)

#read pkts.
pkt_count=0
for pkt in capture:
	time.sleep(2)
	print(len(capture))
	pkt_count+=1
	pkt_timestamp=pkt.sniff_timestamp
	timestamp=float(pkt_timestamp)        
	#timestamp = datetime.fromtimestamp(timestamp)
	#print(timestamp)
	date = datetime.fromtimestamp(timestamp, ist)
	print("IST:", date)
	print(colored(('packet no.',pkt_count,'scanning pkt : ',pkt),'green'))
	################OTHERS###################
	if ('TCP' not in str(pkt) and 'UDP' not in str(pkt)):
		print('TCP or UDP are not present',pkt)
		pkt=str(pkt)
		new_str = pkt.replace('"', '')
		pkt=new_str.replace("'",'')
		query=("INSERT INTO flow (record,packet) VALUES ('%s','%s')")%(pkt_count,pkt)
		print(query)
		cursor = mydb.cursor()
		cursor.execute(query)
		# accept the changes
		mydb.commit()
		print(colored((pkt_count, "Record inserted."),'green'))
	else:
		try:
			tcp = pkt['TCP']
			if tcp:
			    print(tcp)
			    print(colored(("transport layer"),'red'))
			    print(colored(("TCP source port:",tcp.srcport),'blue'))
			    print(colored(("TCP destination port :",tcp.dstport),'blue'))
			    try:
			        eth = pkt['ETH']
			        if eth:
			            print(colored(("DataLink layer"),'red'))
			            print(colored(("source MAC address :",eth.src),'green'))
			            print(colored(("destination MAC address :",eth.dst),'green'))
			            mySql_insert_query = "INSERT INTO flow (record,source_port,destination_port,source_MAC,destination_MAC) VALUES ('%s','%s','%s','%s','%s')"%(pkt_count,tcp.srcport,tcp.dstport,eth.src,eth.dst)
			            cursor = mydb.cursor()
			            cursor.execute(mySql_insert_query)
			            mydb.commit()
			            print(pkt_count, "Record inserted.")
			            cursor.close()
			    except:
			        pass
			    try:
			        ipv4 = pkt['IP']
			        if ipv4:
			            print(colored(("Network layer"),'red'))
			            print(colored(("source ip address :",ipv4.src),'green'))
			            print(colored(("destination ip address :",ipv4.dst),'green'))
			            pkt=str(pkt)
			            try :
			                #remove strings from packet
			                new_str = pkt.replace('"', '')
			                pkt=new_str.replace("'",'')
			                query=("UPDATE flow SET source_ip='%s',destination_ip='%s',protocol='TCP',packet=\"%s\" WHERE record='%s'")%(ipv4.src,ipv4.dst,pkt,pkt_count)
			                print(query)   
			                cursor = mydb.cursor()
			                cursor.execute(query)
			                mydb.commit()
			                print(pkt_count, "Record updated.")
			                cursor.close()
			            except Exception as e:
			                print(colored(('Error! not able to update TCP pkt. with IPv4 Code: {c}, Message, {m}'.format(c = type(e).__name__, m = str(e))),'red'))
			    except:
			        pass
			    try:
			        ipv6 = pkt['IPV6']
			        if ipv6:
			            print(colored(("Network layer"),'red'))
			            print(colored(("source ip address :",ipv6.src),'green'))
			            print(colored(("destination ip address :",ipv6.dst),'green'))
			            pkt=str(pkt)
			            try:
			                new_str = pkt.replace('"', '')
			                pkt=new_str.replace("'",'')
			                query=("UPDATE flow SET source_ip='%s',destination_ip='%s',protocol='TCP',packet=\"%s\" WHERE record='%s'")%(ipv6.src,ipv6.dst,pkt,pkt_count)
			                print(query)
			                cursor = mydb.cursor()
			                cursor.execute(query)
			                mydb.commit()
			                print(pkt_count, "Record updated.")
			                cursor.close()
			            except Exception as e:
			                print(colored(('Error! not able to update TCP pkt. with IPv6 Code: {c}, Message, {m}'.format(c = type(e).__name__, m = str(e))),'red'))
			    except:
			        pass
		except:
			pass
		try:
			udp = pkt['UDP']
			if udp:
			    print(udp)
			    print(colored(("transport layer"),'red'))
			    print(colored(("UDP source port:",udp.srcport),'blue'))
			    print(colored(("UDP destination port :",udp.dstport),'blue'))
			    try:
			        eth = pkt['ETH']
			        if eth:
			            print(colored(("DataLink layer"),'red'))
			            print(colored(("source MAC address :",eth.src),'green'))
			            print(colored(("destination MAC address :",eth.dst),'green'))
			            mySql_insert_query = "INSERT INTO flow (record,source_port,destination_port,source_MAC,destination_MAC) VALUES ('%s','%s','%s','%s','%s')"%(pkt_count,udp.srcport,udp.dstport,eth.src,eth.dst)
			            cursor = mydb.cursor()
			            cursor.execute(mySql_insert_query)
			            mydb.commit()
			            print(pkt_count, "Record inserted.")
			            cursor.close()
			    except:
			        pass
			    try:
			        ipv4 = pkt['IP']
			        if ipv4:
			            try:
			                print(colored(("Network layer"),'red'))
			                print(colored(("source ip address :",ipv4.src),'green'))
			                print(colored(("destination ip address :",ipv4.dst),'green'))
			                pkt=str(pkt)
			                new_str = pkt.replace('"', '')
			                pkt=new_str.replace("'",'')
			                query=("UPDATE flow SET source_ip='%s',destination_ip='%s',protocol='UDP',packet=\"%s\" WHERE record='%s'")%(ipv4.src,ipv4.dst,pkt,pkt_count)
			                print(query)
			                cursor = mydb.cursor()
			                cursor.execute(query)
			                mydb.commit()
			                print(pkt_count, "Record updated.")
			                cursor.close()
			            except Exception as e:
			                print(colored(('Error! not able to update UDP pkt. with IPv6 Code: {c}, Message, {m}'.format(c = type(e).__name__, m = str(e))),'red'))
			    except:
			        pass
			    try:
			        ipv6 = pkt['IPV6']
			        if ipv6:
			            try:
			                print(colored(("Network layer"),'red'))
			                print(colored(("source ip address :",ipv6.src),'green'))
			                print(colored(("destination ip address :",ipv6.dst),'green'))
			                pkt=str(pkt)
			                new_str = pkt.replace('"', '')
			                pkt=new_str.replace("'",'')
			                query=("UPDATE flow SET source_ip='%s',destination_ip='%s',protocol='UDP',packet=\"%s\" WHERE record='%s'")%(ipv6.src,ipv6.dst,pkt,pkt_count)
			                print(query)
			                cursor = mydb.cursor()
			                cursor.execute(query)
			                mydb.commit()
			                print(pkt_count, "Record updated.")
			                cursor.close()
			            except Exception as e:
			                print(colored(('Error! not able to update UDP pkt. with IPv6 Code: {c}, Message, {m}'.format(c = type(e).__name__, m = str(e))),'red'))
			    except:
			        pass
		except:
			pass
		statement='pkt. scanned : %s'%(pkt_count)
		text = colored(statement, 'red', attrs=['reverse', 'blink'])
		print(text)
