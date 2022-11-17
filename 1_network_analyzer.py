import pyshark
import time
import calendar

print('developed and maintained by SIDHARTH RASHWANA')

try : 
	# define interface
	networkInterface = "eth0"
	# gmt stores current gmtime
	gmt = time.gmtime()
	#print("gmt:-", gmt)
	# timestamp
	timestamp = calendar.timegm(gmt)
	#time before capturing traffic
	from_time = time.asctime(time.localtime(time.time()))
	#port specific traffic :
	#capture = pyshark.LiveCapture(interface='eth0', output_file='/home/darth6/Projects/Web Based Traffic Analyzer/NetBytes/capture/'+str(timestamp)+'.pcap',bpf_filter='tcp port 80 or tcp port 443 or udp port 80 or tcp port 443')
	capture = pyshark.LiveCapture(interface='eth0', output_file='/home/darth6/Projects/Web Based Traffic Analyzer/NetBytes/capture/'+str(timestamp)+'.pcap')
	capture.sniff()
except KeyboardInterrupt:
    print('interrupted by keyboard...Exiting!!!')
	#time till traffic was captured
    to_time = time.asctime(time.localtime(time.time()))
    print("Network traffic was captured : From  ",from_time, "To ",to_time)
    print("summary of pkts. captured",capture)
