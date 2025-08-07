
# Infra Automation Project 

This project simulates the provisioning of virtual machines using Python and Bash.
It receives input from the user, validates it, saves the configuration to a JSON file, logs all operations,
and simulates infrastructure setup using a Bash script.

---

## 📁 Project Structure

```
infra-automation/
├── configs/
│   └── instances.json        # Saved machine configurations
├── logs/
│   └── provisioning.log      # Full log of the process
├── scripts/
│   └── setup_nginx.sh        # Bash script to simulate provisioning
├── src/
│   └── machine.py            # Machine class definition
├── infra_simulator.py        # Main Python script
└── README.md                 # This file
```

---

## 🚀 How to Run

1. Make sure you are in the root directory of the project.
2. Run the simulator:

```bash
python3 infra_simulator.py
```

3. Follow the instructions to enter machine details:
   - Machine name
   - Operating system (Linux, Windows, Mac)
   - CPU cores
   - RAM in GB

---

## 🧠 Input Example

```
Enter machine name (or 'done' to finish): web1
Enter OS (Linux, Windows, Mac): LiNuX
Enter CPU cores (e.g., 2): 2
Enter RAM in GB (e.g., 4): 4
```

---

## 📄 Output

✅ Saved machine configurations to: `configs/instances.json`  
✅ Log created at: `logs/provisioning.log`  
✅ Simulated setup using: `scripts/setup_nginx.sh`

---

## ⚙️ Technologies Used

- Python 3
- Bash scripting
- JSON


---

## 👨‍💻 Author

Yuval Vos 
