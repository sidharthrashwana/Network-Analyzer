import requests
import mysql.connector
print('developed and maintained by SIDHARTH RASHWANA')
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="NetBytes"
)
mycursor = mydb.cursor()
print(mycursor)

"""  
def get_ip():
    response = requests.get('https://api64.ipify.org?format=json').json()
    return response["ip"]
"""

def source_location():
	mycursor.execute("SELECT source_ip FROM flow")
	myresult = mycursor.fetchall()
	sip=[]
	sipr=[]
	print('SOURCE IP ADDRESS:\n')
	for src in myresult:
		if src[0] != None:
			ip_address=src[0]
			if ip_address not in sip:
				sip.append(ip_address)
				response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()
				location_data = {"ip": ip_address,"city": response.get("city"),"region": response.get("region"),"country": response.get("country_name")}
				print(location_data)
				sipr.append(location_data)
	print(sipr)	
			
def destination_location():
	mycursor.execute("SELECT destination_ip FROM flow")
	myresult = mycursor.fetchall()
	dip=[]
	dipr=[]
	print('DESTINATION IP ADDRESS:\n')
	for dst in myresult:
		if dst[0] != None:
			ip_address=dst[0]
			if ip_address not in dip:
				dip.append(ip_address)
				response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()
				location_data = {"ip": ip_address,"city": response.get("city"),"region": response.get("region"),"country": response.get("country_name")}
				print(location_data)
				dipr.append(location_data)
	print(dipr)	
source_location()
destination_location()
