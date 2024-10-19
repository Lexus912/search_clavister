import pandas as pd 
from bs4 import BeautifulSoup
ip4address_arry ={'ipv4address_name':[],
                  'ipv4address_ipv4':[],
                  'ipv4address_commentg':[]}

with open('config-Slave-20241014.bak', "r", encoding='utf8') as fh:
    file = fh.read()
# Read file to buffer
Bs_data = BeautifulSoup(file, "xml")
for ip4address in Bs_data.find_all('IP4Address'):
    try:
        ipv4address_name = ip4address.get('Name')
        ip4address_arry['ipv4address_name'].append(ipv4address_name)
        ipv4address_ipv4 = ip4address.get('Address')
        ip4address_arry['ipv4address_ipv4'].append(ipv4address_ipv4)
        ipv4address_commentg = ip4address('CommentGroup')
        ip4address_arry['ipv4address_commentg'].append(ipv4address_commentg)
        print(f'Name: {ipv4address_name}, Address: {ipv4address_ipv4}, CommentGroup: {ipv4address_commentg}')
    except Exception as e:
        print(f"Error proccesing IP4Address element: {e}")

DataFrame = pd.DataFrame(ipv4address_arry)
DataFrame.to_csv("ipv4address.csv")

fh.close()
