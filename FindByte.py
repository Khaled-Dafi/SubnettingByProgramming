def get_ip_address_bytes(ip_address):
  """Returns the number of bytes in an IP address."""
  octets = ip_address.split(".")
  return len(octets)

def main():
  ip_address = input("Enter the IP address: ")
  number_of_bytes = get_ip_address_bytes(ip_address)
  print(f"The number of bytes in the IP address {ip_address} is {number_of_bytes}")

if __name__ == "__main__":
  main()
