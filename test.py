import serial
import pynmea2
from geopy.distance import geodesic

# Define a function to read GPS data from the serial port
def read_gps_data(port, baudrate):
    with serial.Serial(port, baudrate) as ser:
        while True:
            line = ser.readline().decode('utf-8')
            if line.startswith('$GPGGA'):
                try:
                    msg = pynmea2.parse(line)
                    yield (msg.latitude, msg.longitude)
                except pynmea2.ParseError:
                    pass

# Define a function to count the number of footsteps
def count_steps(gps_points, step_length):
    steps = 0
    prev_point = None
    for point in gps_points:
        if prev_point is not None:
            distance = geodesic(prev_point, point).meters
            if distance >= step_length:
                steps += 1
        prev_point = point
    return steps

# Set the goal number of steps
steps_goal = 10000

# Read GPS data from the serial port
gps_points = read_gps_data('/dev/ttyUSB0', 9600)  # Replace '/dev/ttyUSB0' with the correct name of the serial port

# Count the number of footsteps
step_length = 0.7  # Average step length in meters
steps_counter = count_steps(gps_points, step_length)

# Check if the goal has been reached
if steps_counter >= steps_goal:
    print(f"Goal reached! Good job!\n{abs(steps_counter - steps_goal)} steps over the goal!")
else:
    print(f"{abs(steps_goal - steps_counter)} more steps to reach goal.")