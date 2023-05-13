from pybricks.pupdevices import DCMotor
from pybricks.parameters import Port
from pybricks.experimental import Broadcast
from pybricks.tools import wait

# Initialize the motor
motor = DCMotor(Port.B)

# Initialize the broadcast object with the same unique topic as the main hub
radio = Broadcast(topics=["train"])

# Define a function to match the speed and direction of the motor on the main hub
def match_motor_speed_and_direction(data):
    # Convert data to a tuple if it is not already one
    if type(data) == int:
        data = (data,)

    # Check if speed and direction are present in the data tuple
    if len(data) > 0:
        print("Found Speed!")
        speed = data[0]
        motor.dc(speed)

    if len(data) > 1:
        print("Found Direction!")
        direction = data[1]
        reverse_direction = True
        if reverse_direction:
            direction *= -1
        motor.brake()
        motor.dc(speed * direction)

# Define a function to continuously receive the motor speed from the main hub
def receive_speed():
    while True:
        # Wait for a message on the "train" topic
        message = radio.receive("train")

        if message is None:
            print("No message received on 'train' topic.")
        elif isinstance(message, int) and -100 <= message <= 100:
            print(f"Found! Received message, max_speed: {message}")
            # 0 = stop, negative number = backwards, positive number = forward, max_speed is received from main hub!
            # Extract the speed from the message tuple and set the motor speed accordingly
            speed = message
            direction = 1
            match_motor_speed_and_direction((speed, direction))
        elif isinstance(message, tuple) and len(message) == 2 and -100 <= message[0] <= 100 and message[1] in [1, -1]:
            print(f"Found! Received message, max_speed: {message}")
            # 0 = stop, negative number = backwards, positive number = forward, max_speed is received from main hub!
            # Extract the speed and direction from the message tuple and set the motor speed accordingly
            speed = message[0]
            direction = message[1]
            match_motor_speed_and_direction((speed, direction))
        else:
            print(f"Invalid message received on 'train' topic. Message was: {message}")

        wait(185) # Wait for 50 milliseconds


# Start receiving the motor speed from the main hub
receive_speed()
