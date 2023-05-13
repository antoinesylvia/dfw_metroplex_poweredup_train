# dfw_metroplex_poweredup_train

This is a side project I recently accomplished for my kids (2 & 4). Wrote some code leveraging Pybricks which allows us to run Python(micro) on a Lego train I acquired from Goodwill, swapped out the Power Functions for the Lego Powered Up Hubs which support Bluetooth, and added a Color and Distance sensor to the bottom of the locomotive to scan for 4 colors representing train stations on our outdoor HotWheels/Legoland track! The train track itelf, isn't a loop, shape of a "J" therefore like on trains in Boston (area where I am from), you get the end of the line and reverse directon.

As I mentioned the Color and distance sensor is mounted under the train, instead of leveraging default color values, we built custom color ranges for each of the 4 colors via HSV data collected by the sensor (establish upper and lower color thresholds). We placed white lego plates down the center help prevent color misreads between stations as well as building a semi enclosure around the mounted sensor as an additional measure. Code is documented throughout. 

Train can start on any of the 4 colors and know which way to head next. This page will hold 2 of the projects I've been working on since early April 2023. Click on each folder name for more information in another readme file. 

Project 1 - Utilizes only 1 Powered Up hub with 1 motor installed in a locomative.
 
TikTok Demo on Test Track: https://www.tiktok.com/@cyber_toine/video/7224726223010663722

TikTok Demo on outdoor HotWheel/LegoLand Track: https://www.tiktok.com/@cyber_toine/video/7225054602733915435

Project 2 - Leverages/requires a beta Pybricks firmware which enables hub to hub communication to Bluetooth. I was intriguied to see if I could get this going, basically each locomotive has a hub and motor. They work in together, the main hub (code built 85% in project 1) sends speed and direction to the 2nd locomotive via Bluetooth over a dedicated topic. There are some bugs at the firmware level, so that's out of my control but for the most part it's 95% functional.

TikTok Demo on Test Track: https://www.tiktok.com/@cyber_toine/video/7227364883552013614

TikTok Demo on outdoor HotWheel/LegoLand Track: https://www.tiktok.com/@cyber_toine/video/7229516604227276074
