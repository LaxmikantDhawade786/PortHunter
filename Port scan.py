import socket  # Used for network connections to scan ports
import threading  # Enables concurrent execution of scanning tasks
import tkinter as tk  # GUI library for building the user interface
from tkinter import scrolledtext, messagebox  # For text display and alerts
from concurrent.futures import ThreadPoolExecutor  # For efficient multi-threaded execution

def scan_port(target, port, output_text, open_ports):
    """Attempt to connect to a specified port on the target IP."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:  # Create a TCP socket
        s.settimeout(1)  # Set timeout for response
        try:
            result = s.connect_ex((target, port))  # Attempt connection
            if result == 0:
                output_text.insert(tk.END, f'Port {port}: OPEN\n')
                output_text.see(tk.END)
                open_ports.append(port)
        except Exception as e:
            output_text.insert(tk.END, f'Error scanning port {port}: {e}\n')

def port_scan(target, start_port, end_port, output_text, status_label):
    """Scan a range of ports on the target IP using multithreading."""
    output_text.delete(1.0, tk.END)
    output_text.insert(tk.END, f'Scanning target: {target} (Ports {start_port}-{end_port})\n')
    status_label.config(text=f"Scanning {target} (Ports {start_port}-{end_port})", fg="yellow")
    open_ports = []
    
    # Using ThreadPoolExecutor for multi-threaded execution
    with ThreadPoolExecutor(max_workers=100) as executor:
        futures = [executor.submit(scan_port, target, port, output_text, open_ports) for port in range(start_port, end_port + 1)]
        for _ in futures:
            pass
    
    if open_ports:
        messagebox.showinfo("Scan Complete", f"Scanning finished! Open ports: {sorted(open_ports)}")
        output_text.insert(tk.END, f'Open ports: {sorted(open_ports)}\n')
    else:
        messagebox.showinfo("Scan Complete", "Scanning finished! No open ports found.")
        output_text.insert(tk.END, 'No open ports found.\n')
    
    status_label.config(text="Scan Complete", fg="green")

def start_scan():
    """Starts the scanning process in a new thread."""
    target = ip_entry.get().strip()
    option = scan_option.get()
    
    if not target:
        messagebox.showerror("Error", "Please enter a valid IP address.")
        return
    
    if option == "1-1024":
        start_port, end_port = 1, 1024
    elif option == "1-65535":
        start_port, end_port = 1, 65535
    else:
        try:
            start_port = int(custom_start_entry.get().strip())
            end_port = int(custom_end_entry.get().strip())
            if start_port < 1 or end_port > 65535 or start_port > end_port:
                raise ValueError
        except ValueError:
            messagebox.showerror("Error", "Invalid port range. Use values between 1 and 65535.")
            return
    
    # Running port scan in a separate thread to keep the GUI responsive
    threading.Thread(target=port_scan, args=(target, start_port, end_port, output_text, status_label), daemon=True).start()

# GUI setup
root = tk.Tk()
root.title("PortHunter by Laxmikant Dhawade")
root.geometry("700x550")
root.configure(bg="#2c3e50")
root.resizable(False, False)

# Title Label
tk.Label(root, text="PortHunter", font=("Arial", 24, "bold"), fg="#f1c40f", bg="#2c3e50").pack(pady=10)

# Status Label
status_label = tk.Label(root, text="Waiting for input...", font=("Arial", 14), bg="#2c3e50", fg="white")
status_label.pack(pady=5)

# IP Entry
tk.Label(root, text="Enter Target IP:", font=("Arial", 14), bg="#2c3e50", fg="white").pack()
ip_entry = tk.Entry(root, width=30, font=("Arial", 14))
ip_entry.pack(pady=5)

# Scan Options
scan_option = tk.StringVar(value="1-1024")
tk.Label(root, text="Select Scan Range:", font=("Arial", 14), bg="#2c3e50", fg="white").pack()
tk.Radiobutton(root, text="Ports 1-1024", variable=scan_option, value="1-1024", font=("Arial", 12), bg="#2c3e50", fg="white").pack()
tk.Radiobutton(root, text="Ports 1-65535", variable=scan_option, value="1-65535", font=("Arial", 12), bg="#2c3e50", fg="white").pack()
tk.Radiobutton(root, text="Custom Range", variable=scan_option, value="custom", font=("Arial", 12), bg="#2c3e50", fg="white").pack()

# Custom Port Entries
custom_frame = tk.Frame(root, bg="#2c3e50")
tk.Label(custom_frame, text="Start:", font=("Arial", 12), bg="#2c3e50", fg="white").pack(side=tk.LEFT)
custom_start_entry = tk.Entry(custom_frame, width=6, font=("Arial", 12))
custom_start_entry.pack(side=tk.LEFT, padx=5)
tk.Label(custom_frame, text="End:", font=("Arial", 12), bg="#2c3e50", fg="white").pack(side=tk.LEFT)
custom_end_entry = tk.Entry(custom_frame, width=6, font=("Arial", 12))
custom_end_entry.pack(side=tk.LEFT, padx=5)
custom_frame.pack(pady=5)

# Scan Button
scan_button = tk.Button(root, text="Start Scan", command=start_scan, bg="#27ae60", fg="white", font=("Arial", 14, "bold"), padx=10, pady=5)
scan_button.pack(pady=10)

# Output Box
output_text = scrolledtext.ScrolledText(root, width=75, height=10, font=("Arial", 12), bg="#ecf0f1", fg="#2c3e50")
output_text.pack(pady=5)

# Run GUI
root.mainloop()
