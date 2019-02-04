# Finding the Address using python
# done by @Sri_Programmer
# python v3.7.2

__author__ = 'Sri Manikanta Palakollu'

# Imports

import requests
import bs4
import json

def getIpAddress():
    req = requests.get('http://checkip.dyndns.com/')    # Ipaddress providing url
    soup_obj = bs4.BeautifulSoup(req.text,'lxml')
    res = soup_obj.select('body')[0]
    res = res.text
    return res[20:]

IP = getIpAddress()

address_url = 'http://ipinfo.io/' + IP + '/json'

res = requests.get(address_url)
soup_obj = bs4.BeautifulSoup(res.text,'lxml')
data = soup_obj.select('p')[0]
data = data.text
data = json.loads(data) # Parse the JSON Data

# Passing information into variables

IPAddress = data['ip']
City = data['city']
Region = data['region']
Country = data['country']
Location = data['loc']
Postal = data['postal']
Organisation = data['org']

print('IPAddress is: ',IPAddress)
print('City: ',City)
print('Region: ',Region)
print('Country: ',Country)
print('Location: ',Location)
print('Postal: ', Postal)
print('Organisation: ',Organisation)

