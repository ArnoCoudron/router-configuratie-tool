my_routers = [
{"Hostname":"Router 1", "MGMT_IP_Adres":"10.10.10.1", "Banner":"",
"username":"ehbadmin", "Password":"Test123"},
{"Hostname":"Router 2", "MGMT_IP_Adres":"10.10.10.2", "Banner":"",
"username":"ehbroot", "Password":"Test456"},
{"Hostname":"Router 3", "MGMT_IP_Adres":"10.10.10.3", "Banner":"",
"username":"ehbadmin", "Password":"Test789"},
{"Hostname":"Router 4", "MGMT_IP_Adres":"10.10.10.4", "Banner":"",
"username":"ehbroot", "Password":"Test0973"}
{"Hostname":"Router 5", "MGMT_IP_Adres":"10.10.10.5", "Banner":"",
 "username":"ehbadmin", "Password":"Test999"}
]

def connect_to_router(router):
    my_IP_adres = input("geef een ID-adres in: ")

    for router in my_routers:
        if router["MGMT_IP_Adres"] == my_IP_adres:
            my_username = input("Geef een username: ")
            my_password = input("geef een password: ")

            if router["username"] == my_username and router["Password"] == my_password:
                return my_IP_adres
            else:
                print("FOUT")
                return False

    print("Geen connectie gemaakt")
    return False

def overview_router():
    for rout in my_routers:
        print("Hostname: " + rout["Hostname"])
        print("MGMT_IP_Adres: " + rout["MGMT_IP_Adres"])
        print("Banner: " + rout["Banner"])
        print()


def stop_program():
    print("Programma sluit af binnen 3 2 1 ...")
    exit()


def configure_hostname():
    return input("geef een hostname: ")

def configure_banner():
    return input("Geef een banner: ")



while True:
    print("1 - Connecteren op een router")
    print("2 - Overzicht routers")
    print("3 - Script stoppen")
    keuze1 = input("Maak een keuze 1/2/3 : ")
    print()

    if keuze1 == "1":
        my_connect_router = connect_to_router(my_routers)
        if my_connect_router:
            print("JE HEBT CONNECTIE")
            while True:
                print()
                print("1 - Configureren van de hostname")
                print("2 - Configureren van de banner")
                print("3 - Verbreek de connectie met de router")
                keuze2 = input("Maak een keuze 1/2/3: ")
                print()

                if keuze2 == "1":
                    my_hostname = configure_hostname()
                    for router in my_routers:
                        if router["MGMT_IP_Adres"] == my_connect_router:
                            router["Hostname"] = my_hostname


                if keuze2 == "2":
                    my_banner = configure_banner()
                    for router in my_routers:
                        if router["MGMT_IP_Adres"] == my_connect_router:
                            router["Banner"] = my_banner


                if keuze2 == "3":
                    print("connectie word verbroken")
                    break



    if keuze1 == "2":
        overview_router()

    if keuze1 == "3":
        stop_program()
