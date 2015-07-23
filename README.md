The python code used to control the snakBot, a cannabalized RC car with a motor driver, a raspberry pi, and two sonar sensors strapped onto it...

The code provided allows for basic tcp communication (should be tweaked a little to be effective) as well as complete control of the vehicle.  

nav2.py allows a user to input a string of lefts and rights that the snakBot must take to get to its destination. 

	ex) input >lrll

with the above input, the snakBot would navigate down a hallway (autocorrecting itself using the sonar sensors (if it gets too close to a wall) and then turning at the first left it approaches, then the next right, then the next left, then the next left again
