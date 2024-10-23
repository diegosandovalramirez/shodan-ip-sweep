import shodan
import argparse
import time
import sys

# Replace 'YOUR_API_KEY' with your actual Shodan API key
API_KEY = 'YOURKEY'
api = shodan.Shodan(API_KEY)

def sweep_ips(ip_list):
    results = {}
    
    for ip in ip_list:
        try:
            # Lookup the IP address
            data = api.host(ip)
            results[ip] = {
                'ports': data['ports'],
                'cves': data.get('vulns', [])
            }
        except shodan.APIError as e:
            print(f"Error retrieving data for {ip}: {e}")
    
    return results

def load_ip_list(file_path):
    with open(file_path, 'r') as file:
        # Read lines and strip whitespace
        return [line.strip() for line in file if line.strip()]

def trabajando():
    print("Trabajando... ( ´(ｴ)ˋ )")
    for _ in range(5):  # Adjust the number of dots as needed
        sys.stdout.write('.')
        sys.stdout.flush()
        time.sleep(0.5)  # Adjust the delay as needed
    print()  # New line after the working message


if __name__ == "__main__":
    # Set up command line argument parsing
    parser = argparse.ArgumentParser(description='Sweep a list of IPs for open ports and CVEs using Shodan.')
    parser.add_argument('file_path', help='Path to the text file containing the IP addresses.')
    args = parser.parse_args()
    
    # Load IPs from the provided file path
    ip_list = load_ip_list(args.file_path)
    trabajando() 
    open_ports_and_cves = sweep_ips(ip_list)
    
    # Print results
    for ip, info in open_ports_and_cves.items():
        print(f"IP: {ip}")
        print(f"Open Ports: {info['ports']}")
        print(f"CVEs: {info['cves'] if info['cves'] else 'None'}")
        print("-" * 40)
