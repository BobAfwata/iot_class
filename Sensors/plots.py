import serial
import json
import threading
import time
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Set up serial connection (change the port to your Arduino's port)
serial_port = 'COM47'  # Example for Linux. For Windows it could be 'COM3', 'COM4', etc.
baud_rate = 9600  # Set to match the baud rate of your Arduino

ser = serial.Serial(serial_port, baud_rate)

# Data lists to store sensor values
time_data = []
temperature_data = []
humidity_data = []
light_data = []
sound_data = []

start_time = time.time()

def read_serial():
    while True:
        if ser.in_waiting > 0:
            try:
                line = ser.readline().decode('utf-8').strip()
                data = json.loads(line)
                current_time = time.time() - start_time
                time_data.append(current_time)
                temperature_data.append(data['temperature'])
                humidity_data.append(data['humidity'])
                light_data.append(data['light'])
                sound_data.append(data['sound'])
                
                # Limit lists to the last 100 items for better performance
                if len(time_data) > 100:
                    time_data.pop(0)
                    temperature_data.pop(0)
                    humidity_data.pop(0)
                    light_data.pop(0)
                    sound_data.pop(0)
            except (json.JSONDecodeError, ValueError) as e:
                print(f"Error reading or parsing line: {line}. Error: {e}")

def start_serial_thread():
    thread = threading.Thread(target=read_serial)
    thread.daemon = True
    thread.start()

# Set up the matplotlib figure and axes
fig, axs = plt.subplots(4, 1, figsize=(10, 8))
fig.suptitle('Real-time Sensor Data')

# Define a function to update the plots
def update_plot(frame):
    axs[0].clear()
    axs[1].clear()
    axs[2].clear()
    axs[3].clear()
    
    axs[0].plot(time_data, temperature_data, label='Temperature (°C)', color='r')
    axs[0].legend(loc='upper right')
    axs[0].set_ylabel('Temperature (°C)')
    axs[0].grid(True)
    
    axs[1].plot(time_data, humidity_data, label='Humidity (%)', color='g')
    axs[1].legend(loc='upper right')
    axs[1].set_ylabel('Humidity (%)')
    axs[1].grid(True)
    
    axs[2].plot(time_data, light_data, label='Light (lx)', color='b')
    axs[2].legend(loc='upper right')
    axs[2].set_ylabel('Light (lx)')
    axs[2].grid(True)
    
    axs[3].plot(time_data, sound_data, label='Sound (dB)', color='m')
    axs[3].legend(loc='upper right')
    axs[3].set_ylabel('Sound (dB)')
    axs[3].set_xlabel('Time (s)')
    axs[3].grid(True)

# Start the serial reading thread
start_serial_thread()

# Set up the animation
ani = FuncAnimation(fig, update_plot, interval=500)

# Display the plot
plt.tight_layout()
plt.show()
