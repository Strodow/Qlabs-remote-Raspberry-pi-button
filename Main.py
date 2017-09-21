import OSC


### Configuration ###

#needs to be a string
ip = "192.168.1.1"
#DebugWS (Debug with sending data from computer)
DebugWS = 0
#DebugWoS (Debug without sending data from computer)
DebugWoS = 1



### Defs ###


def qStart(qNum):
	a = "/cue/"+str(qNum)+"/start"
	return a

def debugLineWS():
	a = "--DebugWS-- "
	return a
def debugLineWoS():
	a = "--DebugWoS-- "
	return a
def errorLine():
	a = "--Error-- "
	return a


### Main Block ###
if (DebugWS and DebugWoS):
	print(errorLine()+"Conflicting Configuration...\n"+errorLine()+"Please switch either both DebugWoS and DebugWS off, or use one at a time.")


def qSend(cueCMD, ip):
	if (DebugWS):
		print(debugLineWS()+"Dest: "+ip+"\n\t\t"+"data: "+cueCMD)
		### connect
		### create message block
		### set command message
		### close and send

		client = OSC.OSCClient()
		msg = OSC.OSCMessage()
		#msg.setAddress("/cue/1/start")
		msg.setAddress(cueCMD)
		client.sendto(msg, (ip, 53000) )

	elif (DebugWoS):
		print(debugLineWoS()+"Dest: "+ip+"\n\t\t"+"data: "+cueCMD)
	
	else:
		### connect
		### create message block
		### set command message
		### close and send

		client = OSC.OSCClient()
		msg = OSC.OSCMessage()
		#example:  msg.setAddress("/cue/1/start")
		msg.setAddress(cueCMD)
		client.sendto(msg, (ip, 53000) )



if __name__ == '__main__':
	#if DebugWoS and DebugWS are not on:
	if (not DebugWoS and DebugWS):
		print("--Program has started without debugging--")

		"""
		Raspberry Pi code
		"""

		print("Program has ended")

	#if either DebugWoS or Debug WS are on but not both
	elif ((DebugWoS or DebugWS) and not (DebugWS and DebugWoS)):
		if(DebugWS):
			print("--Program has started Debug mode with sending--")
		elif(DebugWoS):
			print("--Program has started Debug mode without sending--")

		while 1:
			try:
				startCue = raw_input("Enter a number if you would like to start a cue: ")
				if (startCue):
					qSend(qStart(int(startCue)),ip)
			except EOFError:
				pass

	#if both are on, they shouldn't be
	elif (DebugWoS and DebugWS):
		print("Program has ended")

	#if you ever get here you have broken logic itself
	else:
		print("However you got here. Don't.")
		print("Program has ended")