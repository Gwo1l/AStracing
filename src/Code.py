import subprocess
import re
import os
import sys
from urllib.request import urlopen
import requests
from prettytable import PrettyTable



def get_ip_info(ip_address):
    url = f"http://ip-api.com/json/{ip_address}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        AS = data.get('as', 'пусто')
        country = data.get('country', 'пусто')
        provider = data.get('org', 'пусто')
        return {'Country': country, 'AS': AS, 'Provider': provider}
    else:

        return None


def print_addresses_info(ip_adresses_list):
    for ip_address in ip_adresses_list:
        ip_info = get_ip_info(ip_address)
        if ip_info:
            print("Инфа об IP-адресе", ip_address, '\n',
                  "Страна:", ip_info['Country'], '\n',
                  "AS:", ip_info['AS'], '\n',
                  "Провайдер:", ip_info['Provider'], '\n',
                  "================================")
        else:
            print("Нет инфы об IP-адресе", ip_address)


def tracert(name):
    command = "tracert " + str(name)
    obj = os.popen(command)
    com_output = obj.read()
    ips = re.compile("\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}").findall(com_output)
    return ips[1:]


domain_name = str(input())
list_of_addresses = tracert(domain_name)
print_addresses_info(list_of_addresses)

