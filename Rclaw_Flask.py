#Author: Ekram
#Made 30/10/2016
#Roboclaw stuff was copy pasted from Sam's code
#Using python web flask framework, html, javascript
#THIS DOES NOT HAVE PROXIMITY SENSING YET SO PROCEED WITH CAUTION
#WORK LEFT: Adding sqlite to fetch proximity readings from the Monitor_values table in t7.db and use that as argument to limit motion of the tank
#VERY IMPORTANT: BEFORE RUNNING THIS MAKE SURE ALL THE ROOT WEBPAGE ADDRESS IN THIS CODE MATCHES WITH THE pi's IP ADDRESS
#Place Rclaw.py inside /home/pi AND create a folder inside /home/pi called templates and place Rclaw_main.html in there
#Run Rclaw.py from linux command terminal to run this program

#Importing all the relevant stuff
import time
import roboclaw
import serial
import sys
import RPi.GPIO as GPIO
from flask import Flask, render_template, request, url_for

#Global Vars
address = 0x80              #Roboclaw Address

# Initialize the Flask application
app = Flask(__name__)


#----Roboclaw connection function-----------#
def AttemptToConnectToRoboClaw():
    try:
        roboclaw.Open("/dev/ttyACM0",115200)
        #Motor safe state
        roboclaw.ForwardMixed(address, 0)
        roboclaw.TurnRightMixed(address, 0)
       
    except Exception as e:
        print("problem with roboclaw")
        print e
      
        
# Define a route for the default URL, which loads the form. This is root so this webpage will be output to whoever goes to address http://localhost:5000 (localhost= pi IP address)
@app.route('/')
def form():
    return render_template('Rclaw_main.html')


# Define a route for the action of the form, for example '/ManualF/' NOTE THAT THIS IS ONLY FOR FORWARD MOVEMENT, FOR BACKWARD COPY PASTE THIS WITH FORWARD CHANGED TO BACKWARD
@app.route('/ManualF/', methods=['POST'])
def Manual():
    Mvar1=request.form['Motor1']                #Accepting both motor value input from the web page as a string
    Mvar2=request.form['Motor2']
    
    new1 = int(Mvar1)                           #Converting both accepted string numbers into integers, they are still percentage tho
    new2 = int(Mvar2)
    
    Actual_M1 = (new1/100)*127                  #Converting % into actual values from 0 to 127 scale
    Actual_M2 = (new2/100)*127
    
    try:
        roboclaw.ForwardM1(address, Actual_M1)         #Slotting in the two motor integer values into roboclaw forward function
        roboclaw.ForwardM2(address, Actual_M2)
    except:
        print("problem with roboclaw")
        AttemptToConnectToRoboClaw()
#This webpage will be returned when the user presses submit button, the location.href function redirects the page back to rclaw_main.html so this is a placeholder page    
    return '''
<!DOCTYPE html>
   <head>
      <title>Redirect</title>
      <script language="javascript">
    window.location.href = "http://192.168.137.214:5000"
   </script>
   </head>

   <body>
   <h1>The script above me is supposed to redirect this page back to rclaw_main.html before I finish loading.
   If you can read this, either you have horrible internet or somethng went horribly wrong</h1>
   </body>
</html>
'''

#----------------Webpage button URL redirections, all the return statements are copy pasted and identical--------------------#
@app.route("/forward")
def forward():
    try:
        roboclaw.ForwardM1(address, 64)         #Custom forward motion tank motor values
        roboclaw.ForwardM2(address, 64)
    except:
        print("problem with roboclaw")
        AttemptToConnectToRoboClaw()   
    return '''
<!DOCTYPE html>
   <head>
      <title>Redirect</title>
      <script language="javascript">
    window.location.href = "http://192.168.137.214:5000"
   </script>
   </head>

   <body>
   <h1>The script above me is supposed to redirect this page back to rclaw_main.html before I finish loading.
   If you can read this, either you have horrible internet or somethng went horribly wrong</h1>
   </body>
</html>
'''
@app.route("/backward")
def forward():
    try:
        roboclaw.BackwardM1(address, 64)         #Custom backward motion tank motor values
        roboclaw.BackwardM2(address, 64)
    except:
        print("problem with roboclaw")
        AttemptToConnectToRoboClaw()   
    return '''
<!DOCTYPE html>
   <head>
      <title>Redirect</title>
      <script language="javascript">
    window.location.href = "http://192.168.137.214:5000"
   </script>
   </head>

   <body>
   <h1>The script above me is supposed to redirect this page back to rclaw_main.html before I finish loading.
   If you can read this, either you have horrible internet or somethng went horribly wrong</h1>
   </body>
</html>
'''

@app.route("/left")
def forward():
    try:
        roboclaw.ForwardM1(address, 32)         #Custom left motion tank motor values
        roboclaw.ForwardM2(address, 64)
    except:
        print("problem with roboclaw")
        AttemptToConnectToRoboClaw()   
    return '''
<!DOCTYPE html>
   <head>
      <title>Redirect</title>
      <script language="javascript">
    window.location.href = "http://192.168.137.214:5000"
   </script>
   </head>

   <body>
   <h1>The script above me is supposed to redirect this page back to rclaw_main.html before I finish loading.
   If you can read this, either you have horrible internet or somethng went horribly wrong</h1>
   </body>
</html>
'''

@app.route("/right")
def forward():
    try:
        roboclaw.ForwardM1(address, 64)         #Custom right motion tank motor values
        roboclaw.ForwardM2(address, 32)
    except:
        print("problem with roboclaw")
        AttemptToConnectToRoboClaw()   
    return '''
<!DOCTYPE html>
   <head>
      <title>Redirect</title>
      <script language="javascript">
    window.location.href = "http://192.168.137.214:5000"
   </script>
   </head>

   <body>
   <h1>The script above me is supposed to redirect this page back to rclaw_main.html before I finish loading.
   If you can read this, either you have horrible internet or somethng went horribly wrong</h1>
   </body>
</html>
'''

@app.route("/stop")
def forward():
    try:
        roboclaw.ForwardM1(address, 0)         #Custom stop motion tank motor values
        roboclaw.ForwardM2(address, 0)
    except:
        print("problem with roboclaw")
        AttemptToConnectToRoboClaw()   
    return '''
<!DOCTYPE html>
   <head>
      <title>Redirect</title>
      <script language="javascript">
    window.location.href = "http://192.168.137.214:5000"
   </script>
   </head>

   <body>
   <h1>The script above me is supposed to redirect this page back to rclaw_main.html before I finish loading.
   If you can read this, either you have horrible internet or somethng went horribly wrong</h1>
   </body>
</html>
'''


AttemptToConnectToRoboClaw()            #Idk where to call this. If this doesnt work then place this under if statement below (over app.run)

# Run the app :)
if __name__ == "__main__":
   app.run(host='0.0.0.0', debug=True)




