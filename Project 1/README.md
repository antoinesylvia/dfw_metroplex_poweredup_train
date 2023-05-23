Project 1 - Utilizes only 1 Powered Up hub with 1 motor installed in a locomative.

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
    
    
4. Once all the colors are squared away, and the code has been loaded onto the hub, simply press the "play" button on the website UI or you can also hit the physical hub power button once to execute the code. Top stop hit the "stop" button in the UI or hit the power button once (after it's going). 
