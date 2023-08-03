import ipaddress

def get_subnet_mask(ip_address):
  """Returns the subnet mask of an IPv4 address."""
  network = ipaddress.ip_network(ip_address)
  subnet_mask = network.netmask
  return subnet_mask

def main():
  ip_address = input("Enter the IP address: ")
  subnet_mask = get_subnet_mask(ip_address)
  print(f"The subnet mask of {ip_address} is {subnet_mask}")

if __name__ == "__main__":
  main()
