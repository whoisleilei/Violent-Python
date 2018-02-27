import socket
def retBanner(ip,port):
	try:
		socket.setdefaulttimeout(2)
		s = socket.socket()
		s.connect((ip,port))
		banner = s.recv(1024)
		return banner
	except:
		return

def checkVulns(banner):
	if "FreeFloat Ftp Server" in banner:
		print "[+] FreeFloat Ftp Server is vulnerable."
	elif "3Com 3CDaemon FTP Server" in banner:
		print "[+] 3Com 3CDaemon FTP Server is vulnerable."
	elif "Ability Server" in banner:
		print "[+] Ability FTP Server is vulnerable."
	elif "Sami FTP Server" in banner:
		print "[+] Sami FTP Server is in vulnerable."
	else:
		print "[-] FTP Server is not vulnerable."
	return

def checkVulns_f(banner):
	f = open("list.txt",'r')
	for line in f.readlines():
		if line.strip('\n') in banner:
			print "[+] Server is vulnerable: " + banner.strip('\n')

def main():
	portList = [21,22,25,80,110,443]
	for x in range(22,255):
		ip = '79.96.118.' + str(x)
		for port in portList:
			banner = retBanner(ip,port)
			if banner:
				print '[+]' + ip + ':' + banner
				checkVulns_f(banner)

if __name__ == '__main__':
	main()