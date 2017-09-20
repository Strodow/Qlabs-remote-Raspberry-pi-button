import OSC

"""
Configuration
"""
#This is the ip that the packet is being sent to from the ip
ip = "192.168.1.1"

#This is the port that the packet is being sent to from the pi
sendPort = 53000

#This is the command number to effect the cue number in /cue/{cue_number}/command {number}
#	command numbers reference are in documentatino file
commandNum = 1

#This is the Number of the cue that will execute when triggered
cueNumber = 1




"""
Main Program
"""

#This deffinition will automaticly a request to the ip and port
#/cue/{cue_number}/command {number} (referenced in the documentation)
'''
def Qsend(cueNumber, commandNum, ip, port):
	client = OSC.OSCClient()
	client.connect( (str(ip), port) ) # note that the argument is a tupple and not two arguments
	msg = OSC.OSCMessage()
	msg.setAddress("/print") # I don't really know what this does but it was in the sample code
	msg.append("/cue/"+cueNumber+"/command"+commandNum) # This is the command that will reference the configuration code
	client.send(msg)
	'''
def tempTest(cueNumber, commandNum, ip, sendPort):
	print("/cue/"+str(cueNumber)+"/command"+" "+str(commandNum))
	print(ip, sendPort)

tempTest(cueNumber, commandNum, ip, sendPort)