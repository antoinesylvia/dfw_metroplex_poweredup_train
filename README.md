# Metroplex Powered Up Train

![p0](https://github.com/antoinesylvia/dfw_metroplex_poweredup_train/blob/8380397289f0077545aec01b9a945f6d8fc9f5ff/zz_train_demo/outdoor_test.gif)

This is a side project I recently accomplished for my kids (2 & 4). Wrote some code leveraging Pybricks which allows us to run Python(micro) on a Lego train I acquired from Goodwill, swapped out the Power Functions for the Lego Powered Up City Hubs which support Bluetooth, and added a Color and Distance sensor to the bottom of the locomotive to scan for 4 colors representing train stations on our outdoor HotWheels/Legoland track! The train track itelf, isn't a loop, shape of a "J" therefore like on trains in Boston (area where I am from), you get the end of the line and reverse directon.

As I mentioned the Color and distance sensor is mounted under the train, instead of leveraging default color values, we built custom color ranges for each of the 4 colors via HSV data collected by the sensor (establish upper and lower color thresholds, I've include samples collected in this repo). We placed white lego plates down the center help prevent color misreads between stations as well as building a semi enclosure around the mounted sensor as an additional measure. Code is documented throughout. 

Train can start on any of the 4 colors and know which way to head next. This page will hold 2 of the projects I've been working on since early April 2023. Click on each folder name for more information in another readme file. 

-----------
Project 1 - Utilizes only 1 Powered Up hub with 1 motor installed in a locomative.

![p1](https://github.com/antoinesylvia/dfw_metroplex_poweredup_train/blob/8380397289f0077545aec01b9a945f6d8fc9f5ff/zz_train_demo/project1.gif)
 
TikTok Demo on Test Track: https://www.tiktok.com/@cyber_toine/video/7224726223010663722

TikTok Demo on outdoor HotWheel/LegoLand Track: https://www.tiktok.com/@cyber_toine/video/7225054602733915435

-----------
Project 2 - Leverages/requires a beta Pybricks firmware which enables hub to hub communication to Bluetooth. I was intriguied to see if I could get this going, basically each locomotive has a hub and motor. They work in together, the main hub (code built 85% in project 1) sends speed and direction to the 2nd locomotive via Bluetooth over a dedicated topic. There are some bugs at the firmware level, so that's out of my control but for the most part it's 95% functional. This requires a user to run code on each hub, you can test it out using https://beta.pybricks.com/ (linked to hub #1) and https://pybricks.com/ (linked to hub #2) with your computer. When you are done testing, remove your computer from the equation as suggested by Pybricks developers for the beta. Creates too much noise over Bluetooth.

![p2](https://github.com/antoinesylvia/dfw_metroplex_poweredup_train/blob/8380397289f0077545aec01b9a945f6d8fc9f5ff/zz_train_demo/project2.gif)

TikTok Demo on Test Track: https://www.tiktok.com/@cyber_toine/video/7227364883552013614

TikTok Demo on outdoor HotWheel/LegoLand Track: https://www.tiktok.com/@cyber_toine/video/7229516604227276074

--------------
Project 3 - Coming early summer, will leverage a Raspberry Pi and a Raspberry Pi Build HAT instead of a Lego Powered Hub. Same idea as project #2, with 2 locomotives working together but it will be direct instead of Bluetooth, the HATs support connection of up to 4 Powered Up connections unlike the Hubs which support only 2. Users going this route might need to invest in a $25 Powered Up extension cable for at least one of the motors.

![p5](https://raw.githubusercontent.com/antoinesylvia/dfw_metroplex_poweredup_train/main/Project%203/project3a.jpg)
![p6](https://raw.githubusercontent.com/antoinesylvia/dfw_metroplex_poweredup_train/main/Project%203/project3.jpg)
--------------
Lego Track Color Layout 

Yellow <--> Red <--> Blue <--> Green

--------------
Lego Track Color Layout (HSV Color Values)

Yellow: (((25, 50, 50), (35, 100, 100)), ((49, 96, 90), (53, 97, 92)), ((60, 50, 50), (65, 100, 100)))
Red: (((0, 50, 50), (5, 100, 100)), ((356, 95, 65), (0, 97, 67))) 
Blue: (((212, 92, 60), (218, 95, 66)), ((240, 100, 100), (240, 100, 100)))
Green: (((110, 50, 50), (130, 100, 100)), ((213, 92, 60), (218, 95, 64)))
