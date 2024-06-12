import os
import shutil

# def update_dns(val):
#   os.remove("/etc/resolv.conf")
#   f = open("/etc/resolv.conf","x")
#   f.close()
#   f = open("/etc/resolv.conf","w")
#   print(dns_dict[val])
#   f.write(dns_dict[val])
#   f.close()

def update_dns(val):
  if os.path.exists("/etc/resolv.conf"):
    shutil.copyfile("/etc/resolv.conf","/etc/resolv.confbackup")
    os.remove("/etc/resolv.conf")
    f = open("/etc/resolv.conf","x")
    f.close()
    f = open("/etc/resolv.conf","w")
    print(dns_dict[val])
    f.write(dns_dict[val])
    f.close()


design = """
$$$$$$$\  $$\   $$\  $$$$$$\         $$$$$$\  $$\   $$\  $$$$$$\  $$\   $$\  $$$$$$\  $$$$$$$$\ $$$$$$$\  
$$  __$$\ $$$\  $$ |$$  __$$\       $$  __$$\ $$ |  $$ |$$  __$$\ $$$\  $$ |$$  __$$\ $$  _____|$$  __$$\ 
$$ |  $$ |$$$$\ $$ |$$ /  \__|      $$ /  \__|$$ |  $$ |$$ /  $$ |$$$$\ $$ |$$ /  \__|$$ |      $$ |  $$ |
$$ |  $$ |$$ $$\$$ |\$$$$$$\        $$ |      $$$$$$$$ |$$$$$$$$ |$$ $$\$$ |$$ |$$$$\ $$$$$\    $$$$$$$  |
$$ |  $$ |$$ \$$$$ | \____$$\       $$ |      $$  __$$ |$$  __$$ |$$ \$$$$ |$$ |\_$$ |$$  __|   $$  __$$< 
$$ |  $$ |$$ |\$$$ |$$\   $$ |      $$ |  $$\ $$ |  $$ |$$ |  $$ |$$ |\$$$ |$$ |  $$ |$$ |      $$ |  $$ |
$$$$$$$  |$$ | \$$ |\$$$$$$  |      \$$$$$$  |$$ |  $$ |$$ |  $$ |$$ | \$$ |\$$$$$$  |$$$$$$$$\ $$ |  $$ |
\_______/ \__|  \__| \______/        \______/ \__|  \__|\__|  \__|\__|  \__| \______/ \________|\__|  \__|"""
print(design,"\n")
print("DNS Provider        Primary DNS     Secondary DNS")
print("1. Google           8.8.8.8         8.8.4.4")
print("2. Control D        76.76.2.0       76.76.10.0")
print("3. Quad9            9.9.9.914       9.112.112.112")
print("4. OpenDNS Home     208.67.222.222  208.67.220.220")
print("5. Cloudflare       1.1.1.1         1.0.0.1")
print("6. AdGuard DNS\t    94.140.14.14    94.140.15.15")
print("7. CleanBrowsing    185.228.168.9   185.228.169.9")
print("8. Alternate DNS    76.76.19.19     76.223.122.150")

val = input("Enter your choice of dns:")

dns_dict = {
  "1":"nameserver  8.8.8.8\nnameserver  8.8.4.4",
  "2":"nameserver  76.76.2.0\nnameserver 76.76.10.0",
  "3":"nameserver  9.9.9.914\nnameserver 9.112.112.112",
  "4":"nameserver  208.67.222.222\nnameserver  208.67.220.220",
  "5":"nameserver  1.1.1.1\nnameserver 1.0.0.1",
  "6":"nameserver  94.140.14.14\nnameserver  94.140.15.15",
  "7":"nameserver  185.228.168.9\nnameserver 185.228.169.9",
  "8":"nameserver  76.76.19.19\nnameserver 76.223.122.150"
}

match val:
  case "1":
    print("google dns is updated")
    update_dns(val)
  case "2":
    print("control d is updated")
    update_dns(val)
  case "3":
    print("Quad9 is updated")
    update_dns(val)
  case "4":
    print("OpenDNS Home is updated")
    update_dns(val)
  case "5":
    print("Cloudflare is updated")
    update_dns(val)
  case "6":
    print("Adguard DNS is updated")
    update_dns(val)
  case "7":
    print("CLean Browsing is updated")
    update_dns(val)
  case "8":
    print("Alternate DNS is updated")
    update_dns(val)


