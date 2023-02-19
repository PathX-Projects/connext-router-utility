import os
from pathlib import Path
import json

if __name__ == "__main__":
    clr = lambda: os.system('clear') if os.name == 'posix' else os.system('cls')
    
    def cPrompt(input_msg):
        r = input(input_msg)
        c = input(f'Confirm "{r}"? (y/n): ')
        if c.lower() == 'y':
            return r
        else:
            return cPrompt("Try Again: " + input_msg)
    
    clr()
    print("Welcome to PathX's Connext Router Configuration Utility!\nThis script will accelerate the process of configuring your Connext Router.\nYou can use CTRL+C to exit the script at any time.")
    
    router_repo = Path(__file__).parent.parent.parent.joinpath('router-docker-compose')
    
    if not router_repo.exists():
        print("\nERROR: Could not locate the router's repository. Please ensure that this repository is located in the same parent folder as your router's repository.\n(E.g. ~/router-docker-compose and ~/connext-router-utility)")
        exit(1)
        
    print("\nTo begin, please select which network you'd like to set up on:\n1. Mainnet\n2. Testnet")
    network = input("Enter your choice (i.e. Testnet): ").strip().lower()
    
    resource_dir = Path(__file__).parent.joinpath('resources', network)
    
    print(f"\nBeginning router configuration on the {network}...")
    
    # Load necessary resources
    with open(resource_dir.joinpath('config.template.json')) as config_file:
        config = json.load(config_file)
    with open(resource_dir.joinpath('.env.template')) as env_file:
        env = env_file.read()
    with open(resource_dir.joinpath('chain-ids.json')) as chains_file:
        chains = json.load(chains_file)
    with open(resource_dir.joinpath('key.template.yaml')) as key_file:
        key = key_file.read()
        
    print("\nPlease head here to find the latest version of the router:\nhttps://github.com/connext/monorepo/pkgs/container/router-publisher/versions?filters%5Bversion_type%5D=tagged")
    
    version = cPrompt("\nEnter the version of the router you'd like to use: ")
        
    admin_token = cPrompt("\nYour Admin Token is used to authenticate requests made to the Router's REST API endpoint, and must be kept secret. "
                          "If your Router's API endpoint is left exposed to the public and your Admin Token is either compromised or vulnerable to brute forcing, someone could use your token perform unauthorized operations with your Router. "
                          "Enter a sufficiently complex token to protect against brute force attacks: ")

    config['server']['adminToken'] = admin_token
    
    print(f"\nYou will now be prompted to enter the comma-separated list of RPC providers you'd like to use for each {network} chain - E.g. https://mainnet.infura.io/v3/1234567890abcdef1234567890abcdef,https://mainnet.infura.io/v3/1234567890abcdef1234567890abcdef")
    for chain in chains:
        providers = cPrompt(f"\nPlease enter the comma-separated list of providers you'd like to use for {chain['name']}: ").strip(" ").split(',')
        if len(providers) == 0:
            print(f"No providers given - disabling {chain['name']} ({chain['id']})")
            config['chains'].pop(str(chain['id']))
        else:
            config['chains'][str(chain['id'])]['providers'] = providers
    
    private_key = cPrompt("\nEnter the private key of the wallet that you'd like to set and use as your Router. It is advisable that you create a fresh wallet for the router: ")
    
    print("\nWriting configuration files...")
    
    # ---- WRITE ENV FILE ----
    do = True
    f = router_repo.joinpath('.env')
    if f.exists():
        print("\nWARNING: A .env file already exists in the router's repository. This script will overwrite the existing file.")
        overwrite = input("Continue? (y/n): ")
        if overwrite.lower() != 'y':
            print("Skipping .env file...")
            do = False
    if do:
        with open(f, 'w') as env_file:
            env_file.write(env.format(version=version))
    
    # ---- WRITE CONFIG FILE ----
    do = True
    f = router_repo.joinpath('config.json')
    if f.exists():
        print("\nWARNING: A config.json file already exists in the router's repository. This script will overwrite the existing file.")
        overwrite = input("Continue? (y/n): ")
        if overwrite.lower() != 'y':
            print("Skipping config.json file...")
            do = False
    if do:
        with open(f, 'w') as config_file:
            json.dump(config, config_file, indent=2)
    
    # ---- WRITE KEY FILE ----
    do = True
    f = router_repo.joinpath('key.yaml')
    if f.exists():
        print("\nWARNING: A key.yaml file already exists in the router's repository. This script will overwrite the existing file.")
        overwrite = input("Continue? (y/n): ")
        if overwrite.lower() != 'y':
            print("Skipping key.yaml file...")
            do = False
    if do:
        with open(f, 'w') as key_file:
            key_file.write(key.format(private_key=private_key))
    
    print(f"\nYour router has been configured! If you need to modify these files, you can find them in the {router_repo} directory.\nYou can also reconfigure using the ~/connext-router-utility/configure.sh script.")