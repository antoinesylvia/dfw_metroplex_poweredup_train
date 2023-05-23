# Metroplex Powered Up Train

![p0](https://github.com/antoinesylvia/dfw_metroplex_poweredup_train/blob/8380397289f0077545aec01b9a945f6d8fc9f5ff/zz_train_demo/outdoor_test.gif)

This is a side project I recently accomplished for my kids (2 & 4). Wrote some code leveraging Pybricks which allows us to run Python(micro) on a Lego train I acquired from Goodwill, swapped out the Power Functions for the Lego Powered Up Hubs which support Bluetooth, and added a Color and Distance sensor to the bottom of the locomotive to scan for 4 colors representing train stations on our outdoor HotWheels/Legoland track! The train track itelf, isn't a loop, shape of a "J" therefore like on trains in Boston (area where I am from), you get the end of the line and reverse directon.

As I mentioned the Color and distance sensor is mounted under the train, instead of leveraging default color values, we built custom color ranges for each of the 4 colors via HSV data collected by the sensor (establish upper and lower color thresholds, I've include samples collected in this repo). We placed white lego plates down the center help prevent color misreads between stations as well as building a semi enclosure around the mounted sensor as an additional measure. Code is documented throughout. 

Train can start on any of the 4 colors and know which way to head next. This page focus on Project #1, started in early April 2023. 

-----------
# Project 1 - 1 Powered Up hub and 1 motor, installed in a locomative.

![p1](https://github.com/antoinesylvia/dfw_metroplex_poweredup_train/blob/8380397289f0077545aec01b9a945f6d8fc9f5ff/zz_train_demo/project1.gif)
 
TikTok Demo on Test Track: https://www.tiktok.com/@cyber_toine/video/7224726223010663722

TikTok Demo on outdoor HotWheel/LegoLand Track: https://www.tiktok.com/@cyber_toine/video/7225054602733915435

-----------
How to use:

1. Install the Pybricks firmware to your Lego Hub. Go to https://code.pybricks.com/ and click on the gear at the top left then hit "install Pybricks firmware". Follow the steps provided by the website.
2. Once complete, hit the "+" sign and create a new file (don't use a template). Paste in the code located here in project 1 (1 Hub only function): https://github.com/antoinesylvia/dfw_metroplex_poweredup_train/blob/main/Project%201/train_1_hub_main(load_to_pybricks).py
3. The only thing you must do is customize the color of the stations if you aren't using any of the 4 colors I have (red, blue, green and yellow). There's "debug_mode" function that will collect and output custom HSV color values (within the terminal output in Pybricks website). You can then use this information and add it to color_data within the get_sensor_color function. Use this approach to lessen the chance of color misreads on the track (default color readings were replaced by HSV values representing better accuracy).  Each set of HSV values consists of a lower bound and an upper bound, which define a range of colors that the algorithm will consider as "BLUE, RED, YELLOW or GREEN". 

        "BLUE": (((212, 92, 60), (218, 95, 66)), ((240, 100, 100), (240, 100, 100))), #2 HSV Sets
        "RED": (((0, 50, 50), (5, 100, 100)), ((356, 95, 65), (0, 97, 67))), #2 HSV Sets
        "GREEN": (((110, 50, 50), (130, 100, 100)), ((213, 92, 60), (218, 95, 64))), #2 HSV Sets
        "YELLOW": (((25, 50, 50), (35, 100, 100)), ((49, 96, 90), (53, 97, 92)), ((60, 50, 50), (65, 100, 100))), #3 HSV Sets
    
My HSV low and high thresholds per color were established primarily from sample data I collected using debug_mode (set as true) for the color sensor: https://github.com/antoinesylvia/dfw_metroplex_poweredup_train/blob/main/zz_hsv_sample_data/hsv_sample_values_debug_mode.txt

4. Once all the colors are squared away, and the code has been loaded onto the hub, simply press the "play" button on the website UI or you can also hit the physical hub power button once to execute the code. Hit the "stop" button in the UI or hit the power button once (after it's going) if you want prevent further execution of the code.

--------------
Lego Track Color Layout 

Yellow <--> Red <--> Blue <--> Green
