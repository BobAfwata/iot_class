import serial
import tkinter as tk
from tkinter import ttk
import json
import threading

# Set up serial connection (change the port to your Arduino's port)
serial_port = 'COM47'  # Example for Linux. For Windows it could be 'COM3', 'COM4', etc.
baud_rate = 9600  # Set to match the baud rate of your Arduino

ser = serial.Serial(serial_port, baud_rate)

def read_serial():
    while True:
        if ser.in_waiting > 0:
            try:
                line = ser.readline().decode('utf-8').strip()
                data = json.loads(line)
                update_display(data)
            except (json.JSONDecodeError, ValueError) as e:
                print(f"Error reading or parsing line: {line}. Error: {e}")

def update_display(data):
    temperature_var.set(f"Temperature: {data['temperature']} °C")
    humidity_var.set(f"Humidity: {data['humidity']} %")
    light_var.set(f"Light: {data['light']} lx")
    sound_var.set(f"Sound: {data['sound']} dB")

def start_serial_thread():
    thread = threading.Thread(target=read_serial)
    thread.daemon = True
    thread.start()

# Set up the Tkinter GUI
root = tk.Tk()
root.title("Sensor Data Display")

temperature_var = tk.StringVar()
humidity_var = tk.StringVar()
light_var = tk.StringVar()
sound_var = tk.StringVar()

ttk.Label(root, textvariable=temperature_var, font=('Helvetica', 16)).pack(pady=10)
ttk.Label(root, textvariable=humidity_var, font=('Helvetica', 16)).pack(pady=10)
ttk.Label(root, textvariable=light_var, font=('Helvetica', 16)).pack(pady=10)
ttk.Label(root, textvariable=sound_var, font=('Helvetica', 16)).pack(pady=10)

# Initialize variables with default values
temperature_var.set("Temperature: N/A")
humidity_var.set("Humidity: N/A")
light_var.set("Light: N/A")
sound_var.set("Sound: N/A")

# Start the serial reading thread
start_serial_thread()

# Start the Tkinter main loop
root.mainloop()
