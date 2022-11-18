# Network-Analyzer

A software designed to capture packets passing through an interface and store on DB for later analysis.

Step 1 : Download XAMPP for ubuntu from :
    
    https://www.apachefriends.org/download.html
    
Step 2: Run phpmyadmin and apache server :

![image](https://user-images.githubusercontent.com/43272058/202472017-97f1a3bd-8d08-445c-9caa-d20294f54213.png)

Step 3:Navigate to :
    
    http://localhost/phpmyadmin
    
Step 4 : Create DB as NetByte and import sql file:

![image](https://user-images.githubusercontent.com/43272058/202472438-4232e240-8f3c-45e8-a334-fc9b3a9f1024.png)


Step 5 : Run the scripts :
    
    5.1 To capture the traffic :
    
      python3 1_network_analyzer.py
      
    5.2 To store packets onto database :
      
      python3 2_store.py
      
    5.3 To find location of ip addresses : 
    
      python3 3_coordinates.py
      

Note: Change the location of pcap file in 1_network_analyzer.py and 2_store.py.There is a video added with project folder which demonstrate the project working.
