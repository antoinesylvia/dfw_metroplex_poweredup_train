from pybricks.pupdevices import ColorDistanceSensor, DCMotor
from pybricks.parameters import Port
from pybricks.tools import wait
from pybricks.parameters import Color

# Define a function to get the color based on HSV values
def get_sensor_color(sensor):
    # Define a dictionary with the color data (H,S,V)
    # Each set of HSV values consists of a lower bound and an upper bound, which define a range of colors that the algorithm will consider as "BLUE".
    # Using the sensor readings, the default color readings were replaced by HSV values representing better accuracy for my lego pieces.  
    # Enable debug_mode below to collect data for your specific colors of legos then build your custom color ranges in the color_map section. 
    color_data = {
        "BLUE": (((212, 92, 60), (218, 95, 66)), ((240, 100, 100), (240, 100, 100))), #2 HSV Sets
        "RED": (((0, 50, 50), (5, 100, 100)), ((356, 95, 65), (0, 97, 67))), #2 HSV Sets
        "GREEN": (((110, 50, 50), (130, 100, 100)), ((213, 92, 60), (218, 95, 64))), #2 HSV Sets
        "YELLOW": (((25, 50, 50), (35, 100, 100)), ((49, 96, 90), (53, 97, 92)), ((60, 50, 50), (65, 100, 100))), #3 HSV Sets
    }

    # Get the color object and its HSV value
    color_obj = sensor.color()
    hsv_value = (color_obj.h, color_obj.s, color_obj.v)

    # Make sure the HSV value is a tuple
    if not isinstance(hsv_value, tuple):
        print(f"hsv_value is not a tuple: {hsv_value}")
        return None

    # Find the matching color
    h, s, v = hsv_value
    for color, ranges in color_data.items():
        for lower, upper in ranges:
            if lower[0] <= h <= upper[0] and lower[1] <= s <= upper[1] and lower[2] <= v <= upper[2]:
                return color
            if lower[0] > upper[0] and (h >= lower[0] or h <= upper[0]) and lower[1] <= s <= upper[1] and lower[2] <= v <= upper[2]:
                return color

    # If no match is found, fall back to the default color
    return str(sensor.color())


# Define a function to get the next stop index
def get_next_stop_index(current_stop, train_stops, direction):
    next_stop_index = current_stop + direction

    if 0 <= next_stop_index < len(train_stops):
        return next_stop_index, direction
    else:
        return None

# Initialize the motor and sensor
motor = DCMotor(Port.B)
sensor = ColorDistanceSensor(Port.A)

# Define functions to move and stop the train
def move_train(speed):
    motor.dc(speed)

def stop_train():
    motor.stop()

# Define functions to print detected and found colors
def print_detected_color(color):
    print(f"Looking for color: {color}")

def print_found_color(color):
    print(f"Found color: {color}")
	
def finish():
    train_stops = ["GREEN", "BLUE", "RED", "YELLOW"] #Set the order of your station colors here, you need at least 2, my order: (GREEN <-->BLUE <-->RED <-->Yellow). You can start the train from any color once set!
    direction = 1 #this number moves the train forward, -1 moves if backward.
    stop_duration = 5000 #stop time in milliseconds at each station
    max_speed = 50 #RPM
    debug_mode = True #Prints read time sensor readings (HSV and Color), useful to collect and build our your own color_map with custom colors.
    debug2_mode = True #Will let you know the detected color vs. expected color.
    debug3_mode = True #Will let you know if an exact HSV match was found, if not fall back to a default color.
    debug_interval = 35 #intervals, in units of time.
    debug2_interval = 35
    debug3_interval = 35
    color_check_interval = 100

    # Detect the starting color
    start_color = get_sensor_color(sensor)
    if start_color not in train_stops:
        print(f"Unable to determine the starting station color. Defaulting to the first station in the list.")
        start_color = train_stops[0]

    # Set the current stop to the starting color
    current_stop = train_stops.index(start_color)
    last_printed_color = None
    iteration_count = 0

    # Keep looping until the program is stopped manually
    while True:
        # Get the detected color
        detected_color = get_sensor_color(sensor)
        expected_color = train_stops[current_stop]

        # Debugging: Print the "No match found" message every 'debug3_interval' iterations when debug3_mode is set to True
        if debug3_mode and iteration_count % debug3_interval == 0 and detected_color != expected_color:
            print(f"No match found for HSV value: {sensor.hsv()}, falling back to default color: {sensor.color()}")

        # Debugging: print the sensor color and HSV values every 'debug_interval' iterations
        if debug_mode and iteration_count % debug_interval == 0:
            sensor_color = sensor.color()
            hsv_value = sensor.hsv()
            print(f"Sensor color: {sensor_color}, HSV value: {hsv_value}")

        # Debugging: print the detected color and expected color every 'debug2_interval' iterations
        if debug2_mode and iteration_count % debug2_interval == 0:
            print(f"Detected color: {detected_color}, Expected color: {expected_color}")

        # Print the expected color if it has changed since the last iteration
        if expected_color != last_printed_color:
            print_detected_color(expected_color)
            last_printed_color = expected_color

        # If the detected color matches the expected color, stop the train and move to the next stop
        if detected_color == expected_color:
            print_found_color(detected_color)

            stop_train()
            wait(stop_duration)

            next_stop_info = get_next_stop_index(current_stop, train_stops, direction)
            if next_stop_info is None:
                direction = -direction
                next_stop_index = current_stop + direction
            else:
                next_stop_index, direction = next_stop_info
            current_stop = next_stop_index

            print(f"Next Stop, {train_stops[current_stop]}")

            move_train(max_speed * direction)
        else:
            move_train(max_speed * direction)

        iteration_count += 1
        wait(color_check_interval)

    stop_train()

if __name__ == "__main__":
    finish()
