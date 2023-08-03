def calculate_subnet_mask(prefix_length):
    mask = [0, 0, 0, 0]
    for i in range(prefix_length):
        mask[i // 8] += 1 << (7 - i % 8)
    return ".".join(map(str, mask))

def main():
    network_class = input("Enter the class of IP address you want to use (A, B, or C): ").upper()
    
    if network_class == "A":
        prefix_length = 8
    elif network_class == "B":
        prefix_length = 16
    elif network_class == "C":
        prefix_length = 24
    else:
        print("Invalid class of IP address.")
        return
    
    num_networks = int(input("Enter the number of networks: "))
    num_hosts = int(input("Enter the number of hosts per network: "))

    # Calculate the subnet mask for the given prefix length
    subnet_mask = calculate_subnet_mask(prefix_length)

    # Calculate the number of hosts per network (excluding network address and broadcast address)
    usable_hosts_per_network = num_hosts - 2

    # Calculate the total number of hosts required (including all networks)
    total_hosts_required = num_networks * num_hosts

    # Calculate the number of bits required to accommodate the total hosts required
    bits_for_hosts = 0
    while 2**bits_for_hosts < total_hosts_required:
        bits_for_hosts += 1

    # Calculate the number of bits reserved for the network portion
    bits_for_network = prefix_length + bits_for_hosts

    # Calculate the subnet mask for the network portion
    subnet_mask_network = calculate_subnet_mask(bits_for_network)

    print("\nSubnet Mask for Network Portion:", subnet_mask_network)
    print("Subnet Mask for Host Portion:", subnet_mask)
    print("")

    network_address = "192.168.0.0"  # Replace this with your desired starting network address
    host_address = 1  # Replace this with your desired starting host address

    for i in range(num_networks):
        print(f"Network {i + 1}: {network_address}/{bits_for_network} (Usable Hosts: {usable_hosts_per_network})")
        for j in range(1, num_hosts + 1):
            print(f"  Host {j}: {network_address[:-1]}{host_address}")
            host_address += 1
        network_address_parts = network_address.split(".")
        network_address_parts[-1] = str(int(network_address_parts[-1]) + 2**bits_for_hosts)
        network_address = ".".join(network_address_parts)
        host_address = 1
        print("")

if __name__ == "__main__":
    main()
