from pnio_dcp import DCP

LOCAL_IP = "172.21.0.167"
MENU = """
==== PROFINET DCP TOOL ====
1 - DCP Identify All
2 - DCP Set Name Station
q - quit
"""

dcp = DCP(LOCAL_IP)

def main():
    while True:
        print(MENU)
        choice = input("profinet_tool> ").strip()

        if choice == "1":
            identify_all()
        elif choice == "2":
            mac = input("profinet_tool> insert mac address (aa:bb:cc:dd:ee:ff): ")
            new_name = input("profinet_tool> insert new station name: ")
            new_station_name(mac, new_name)
        elif choice == "q":
            print("Exiting")
            break
    return 0

def new_station_name(mac, new_name):
    try:
        response = dcp.set_name_of_station(mac, new_name, store_permanent=False)
        print("DCP_set_station_name response:")
        print(response)
    except Exception as e:
        print(f"profinet_tool> ERROR: {e}")
    
def identify_all():
    print("Sending DCP Identify All and listening for 7s...")
    devs = dcp.identify_all(timeout=1)
    
    print(f"Found {len(devs)} devices.")

    for dev in devs:
        print(dev)


if __name__ == "__main__":
    main()

