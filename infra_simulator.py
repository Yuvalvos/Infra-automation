import json
import os
import logging
from src.machine import Machine

os.makedirs('logs', exist_ok=True)

logging.basicConfig(
    filename='logs/provisioning.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def get_user_input():
    machines = []
    valid_os = {
        'linux': 'Linux',
        'windows': 'Windows',
        'mac': 'Mac'
    }
    
    while True:
        name = input("Enter machine name (or 'done' to finish): ")
        if name.lower() == 'done':
            break
    
        if not name:
            logging.error("name cannot be empty")
            continue
        while True:
            os_input = input("Enter OS (Linux, Windows, Mac): ").lower()
            if os_input in valid_os:
                os_type = valid_os[os_input]
                break
            else:
                print("Invalid OS. Please enter Linux, Windows, or Mac.")
                logging.error(f"Invalid OS: {os_input}")
    
        while True:
            user_input = input("Enter CPU cores (must be a whole number > 0): ")
            if not user_input.isdigit():
                print("Invalid input. Please enter a whole number.")
                logging.error(f"Invalid CPU input: not a number - {user_input}")
                continue
            
            cpu = int(user_input)
            if cpu <= 0:
                print("CPU must be bigger than 0.")
                logging.error(f"Invalid CPU input: number not positive - {cpu}")
                continue
            break  
        
        while True:
            user_input = input("Enter RAM in GB (must be a whole number > 0): ")
            if not user_input.isdigit():
                print("Invalid input. Please enter a whole number.")
                logging.error(f"Invalid RAM input: not a number - {user_input}")
                continue
            
            ram = int(user_input)
            if ram <= 0:
                print("RAM must be bigger than 0.")
                logging.error(f"Invalid RAM input: number not positive - {ram}")
                continue
            break
        machine = Machine(name, os_type.lower(), cpu, ram)
        machines.append(machine.to_dict())
    return machines

def save_to_json(machines):
    os.makedirs("configs", exist_ok=True)
    with open("configs/instances.json", "w") as f:
        json.dump(machines, f, indent=4)
    logging.info("Machines saved to configs/instances.json")
import subprocess

def run_setup_script():
    try:
        subprocess.run(["bash", "scripts/setup_nginx.sh"], check=True)
        logging.info("Nginx setup script executed successfully")
    except subprocess.CalledProcessError as e:
        logging.error(f"Error executing setup script: {e}")
        raise
if __name__ == "__main__":
    logging.info("provisioning started")
    machines = get_user_input()
    save_to_json(machines)
    run_setup_script()
    logging.info("provisioning completed") 
