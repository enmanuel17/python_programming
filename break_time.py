#program to take a break at work.
#Enmanuel Hernandez
import webbrowser
import time

counter = 0 #counter to keep track of the loop/breaks
numOfBreaks = 3 # number of wanted breaks

while (counter < numOfBreaks):
	print "take a break!"
	time.sleep(5) #sleeps 5 seconds
	webbrowser.open("https://www.youtube.com/watch?v=NlmezywdxPI")
	counter = counter + 1