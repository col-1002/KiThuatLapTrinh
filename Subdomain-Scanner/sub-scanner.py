import requests
import sys

list_domain = sys.argv[1]

def domain_scanner(domain_name,sub_domnames):

	print('-----------Scanner Started-----------'+"\n")
		
	for subdomain in sub_domnames:
		url = f"http://{subdomain}.{domain_name}"
		try:
			requests.get(url)
			print(f'[+] {url}')
		except requests.ConnectionError:
			pass
			
	print("\n"+'---------Scanning Finished---------')

if __name__ == '__main__':
	
	dom_name = input("Enter the Domain Name:")
	
	with open(list_domain,'r') as file:
		name = file.read()
		sub_dom = name.splitlines()
		
	domain_scanner(dom_name,sub_dom)
