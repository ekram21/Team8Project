# Team8Project
All the code I am currently working on for the team 8 autonomous buggy project

Current architecture will consist of one raspberry pi which will handle all the motor running functions/ input to the system while a second raspberry pi will be responsible for outputting all useful data onto a dynamic website. This website will also have a dynamic google map with imaging of buggy approaching its destination.

The end project code will be huge with multple different actions occuring at the same time. Hence the several different files in the repository right now are all experimental tests to make sure each small piece of the block are running perfectly so that they can be incorporated into the whole together later. A brief decription of each has been provided below.

Note: To run these files make a folder inside /home/pi called templates and place all html files there while the .py files go into /home/pi

The objective of Rclaw_Flask.py is to set up a web browser with buttons to wireless control the buggy. To this end it calls the Rclaw_main.html file which will be output to the user on the browser. It also contains code for the voice recognition driven input but needs the paths of Rclaw_main.html to be changed to Google_SPEECH_API.html.

Proximity_Flask.py is a standalone file which takes dynamic readings from the proximity sensors and streams it directly into a website.

Map_GPS.py is responsible for creating a google map instance on the user's browser and mark with a tank icon the current location of the buggy. It also allows the user to click on the map and this co-ordinate is then sent to the pi which can then be used to drive the buggy. The algorithm to achieve this is being worked upon currently. This python file calls the maptest.html which contains the Google map coding stuff.
