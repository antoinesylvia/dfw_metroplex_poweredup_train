# Metroplex Powered Up Train

![p0](https://github.com/antoinesylvia/dfw_metroplex_poweredup_train/blob/8380397289f0077545aec01b9a945f6d8fc9f5ff/zz_train_demo/outdoor_test.gif)

This is a side project I recently accomplished for my kids (2 & 4). Wrote some code leveraging Pybricks which allows us to run Python(micro) on a Lego train I acquired from Goodwill, swapped out the Power Functions for the Lego Powered Up Hubs which support Bluetooth, and added a Color and Distance sensor to the bottom of the locomotive to scan for 4 colors representing train stations on our outdoor HotWheels/Legoland track! The train track itelf, isn't a loop, shape of a "J" therefore like on trains in Boston (area where I am from), you get the end of the line and reverse directon.

As I mentioned the Color and distance sensor is mounted under the train, instead of leveraging default color values, we built custom color ranges for each of the 4 colors via HSV data collected by the sensor (establish upper and lower color thresholds, I've include samples collected in this repo). We placed white lego plates down the center help prevent color misreads between stations as well as building a semi enclosure around the mounted sensor as an additional measure. Code is documented throughout. 

Train can start on any of the 4 colors and know which way to head next. This page focus on Project #2, started in mid April 2023. 

-----------
# Project 2 - 2 Powered Up hubs and 2 motors, installed in each locomative.

Leverages/requires a beta Pybricks firmware which enables hub to hub communication to Bluetooth. I was intriguied to see if I could get this going, basically each locomotive has a hub and motor. They work in together, the main hub (code built 85% in project 1) sends speed and direction to the 2nd locomotive via Bluetooth over a dedicated topic. There are some bugs at the firmware level, so that's out of my control but for the most part it's 95% functional. This requires a user to run code on each hub, you can test it out using https://beta.pybricks.com/ (linked to hub #1) and https://pybricks.com/ (linked to hub #2) with your computer. When you are done testing, remove your computer from the equation as suggested by Pybricks developers for the beta. Creates too much noise over Bluetooth.

![p2](https://github.com/antoinesylvia/dfw_metroplex_poweredup_train/blob/8380397289f0077545aec01b9a945f6d8fc9f5ff/zz_train_demo/project2.gif)

TikTok Demo on Test Track: https://www.tiktok.com/@cyber_toine/video/7227364883552013614

TikTok Demo on outdoor HotWheel/LegoLand Track: https://www.tiktok.com/@cyber_toine/video/7229516604227276074

![p7](https://github.com/antoinesylvia/dfw_metroplex_poweredup_train/blob/e925099dfa361e17136ee8cde5be219d2045f652/Project%201/colordistance.png)
<br>
Color and Distance sensor required on main locomotive (place at the bottom of the locomotive and build a small enclosure around it to boost read effectiveness).

-----------
How to use (Hub 1, main):

1. Install the Pybricks firmware to your Lego Hub. Go to https://code.pybricks.com/ and click on the gear at the top left then hit "install Pybricks firmware". Follow the steps provided by the website.
2. Once complete, hit the "+" sign and create a new file (don't use a template). Paste in the code located here in project 2 (Hub to Hub): https://github.com/antoinesylvia/dfw_metroplex_poweredup_train/blob/main/Project%202/train_2_hubs_main_hub(load_to_pybricks).py
3. The only thing you must do is customize the color of the stations if you aren't using any of the 4 colors I have (red, blue, green and yellow). There's "debug_mode" function that will collect and output custom HSV color values (within the terminal output in Pybricks website). You can then use this information and add it to color_data within the get_sensor_color function. Use this approach to lessen the chance of color misreads on the track (default color readings were replaced by HSV values representing better accuracy).  Each set of HSV values consists of a lower bound and an upper bound, which define a range of colors that the algorithm will consider as "BLUE, RED, YELLOW or GREEN". 

        "BLUE": (((212, 92, 60), (218, 95, 66)), ((240, 100, 100), (240, 100, 100))), #2 HSV Sets
        "RED": (((0, 50, 50), (5, 100, 100)), ((356, 95, 65), (0, 97, 67))), #2 HSV Sets
        "GREEN": (((110, 50, 50), (130, 100, 100)), ((213, 92, 60), (218, 95, 64))), #2 HSV Sets
        "YELLOW": (((25, 50, 50), (35, 100, 100)), ((49, 96, 90), (53, 97, 92)), ((60, 50, 50), (65, 100, 100))), #3 HSV Sets
    
My HSV low and high thresholds per color were established primarily from sample data I collected using debug_mode (set as true) for the color sensor: https://github.com/antoinesylvia/dfw_metroplex_poweredup_train/blob/main/zz_hsv_sample_data/hsv_sample_values_debug_mode.txt

4. Once all the colors are squared away, and the code has been loaded onto the hub, simply press the "play" button on the website UI or you can also hit the physical hub power button once to execute the code. Hit the "stop" button in the UI or hit the power button once (after it's going) if you want prevent further execution of the code.
--------------

How to use (Hub 2, secondary):

1. Install the "Beta" Pybricks firmware to your Lego Hub (required as of May 2023 to make use of the hub to hub communication over bluetooth). Go to https://beta.pybricks.com and click on the gear at the top left then hit "install Pybricks firmware", now select "advanced" and import the beta firmware from: https://github.com/pybricks/pybricks-projects/blob/master/tutorials/wireless/hub-to-hub/broadcast/cityhub-firmware-build-2178.zip. Newer beta firmware seems to have broken this bluetooth communication feature for city hubs according to the Pybricks team. Follow the steps provided by the website after import.
2. Once complete, hit the "+" sign and create a new file (don't use a template). Paste in the code located here in project 2 (Hub to Hub): https://github.com/antoinesylvia/dfw_metroplex_poweredup_train/blob/main/Project%202/train_2_hubs_support_hub(load_to_pybricks).py
3. Once code has been loaded onto the secondary city hub, simply press the "play" on the main hub (via website https://pybricks.com or physical button) then immediately press the "play" on the main hub (via website https://beta.pybricks.com or physical button). Hit the "stop" button in the UI or hit the power button once (after it's going) for both hubs if you want prevent further execution of the code.
4. Once everything is optimized in terms of the code and the function of the broadcasting between the two hubs, be sure to remove the use of the computer. This was advised from the Pybricks project due to noise issues, the best approach is using the physical buttons on the city hubs (hit the main hub once after it's powered on, and do the same for the secondary hub).

Note: There's still lingering issues at the firmware level for this beta which might result in communication issues and occasional run-offs. Project leaders for Pybicks cite issues with the bluetooth chip itself and how data is being presented. These issues don't exist in project 1 (1 Hub). 

(https://pybricks.com/projects/tutorials/wireless/hub-to-hub/broadcast/)
(https://github.com/orgs/pybricks/discussions/2002)
(https://github.com/pybricks/pybricks-micropython/pull/158)
(https://pybricks.com/project/hub-to-hub-communication/)
--------------

Lego Track Color Layout 

Yellow <--> Red <--> Blue <--> Green
