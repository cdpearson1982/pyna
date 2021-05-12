#!/usr/bin/env python3

import netifaces

def get_ip(interface):
    return (netifaces.ifaddresses(interface)[netifaces.AF_INET])[0]['addr']

def get_mac(interface):
    return (netifaces.ifaddresses(interface)[netifaces.AF_LINK])[0]['addr']

def main():
    print(netifaces.interfaces())
    for i in netifaces.interfaces():
        print('\n**************Details of Interface - ' + i + ' *********************')
        try:    
            print('MAC: ', end='')
            print(get_mac(i))
            print('IP: ', end='')
            print(get_ip(i))
        except:          
            print('Could not collect adapter information') 

if __name__ == "__main__":
    main()





