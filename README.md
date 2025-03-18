# PortHunter - A Multithreaded Port Scanner

PortHunter is a lightweight, multithreaded port scanner built using Python and Tkinter for a graphical user interface. This tool allows users to scan a target IP address for open ports efficiently using multithreading.

## Features
- **Multithreaded scanning** for faster results
- **Customizable port range selection** (1-1024, 1-65535, or a custom range)
- **User-friendly GUI** built with Tkinter
- **Real-time scan progress updates**
- **Displays open ports and alerts the user**

## Technologies Used
- **Python** for core logic
- **Tkinter** for the graphical user interface
- **Sockets** for network communication
- **Threading** for concurrent scanning

## Installation
To run PortHunter on your system, follow these steps:

1. Clone the repository:
   ```sh
   git clone https://github.com/your-username/PortHunter.git
   cd PortHunter
   ```
2. Install dependencies (if required):
   ```sh
   pip install tk
   ```
3. Run the script:
   ```sh
   python port_scanner.py
   ```

## Usage
1. Open the application.
2. Enter the **target IP address**.
3. Choose a port range:
   - **1-1024** (Common well-known ports)
   - **1-65535** (Full range)
   - **Custom range** (Enter start and end ports manually)
4. Click **Start Scan** and wait for results.
5. Open ports will be displayed in the output box.

## Screenshot
<img src="https://github.com/LaxmikantDhawade786/PortHunter/blob/main/images/Screenshot%202025-03-18%20211444.png?raw=true" alt="Sample Image">

<img src="https://github.com/LaxmikantDhawade786/PortHunter/blob/main/images/Screenshot%202025-03-18%20211429.png?raw=true" alt="Sample Image">

<img src="https://github.com/LaxmikantDhawade786/PortHunter/blob/main/images/Screenshot%202025-03-18%20211418.png?raw=true" alt="Sample Image">

<img src="https://github.com/LaxmikantDhawade786/PortHunter/blob/main/images/Screenshot_2025-03-05_07_28_22.png?raw=true" alt="Sample Image"> 


## How It Works
- The program creates a **socket connection** to each port on the target system.
- Uses **multithreading** with `ThreadPoolExecutor` to scan multiple ports simultaneously, improving speed.
- If a connection is successful, the port is marked **OPEN**.
- Results are displayed in the GUI and summarized at the end of the scan.

## Disclaimer
This tool is for **educational and ethical purposes only**. Scanning networks without permission may be illegal.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author
Developed by **Laxmikant Dhawade**


