import OSC



while 1:
	a = raw_input("press enter to execute cue:")
	client = OSC.OSCClient()
	msg = OSC.OSCMessage()
	msg.setAddress("/cue/3/start")
	client.sendto(msg, ('192.168.100.17', 53000))


'''
while 1:
	a = input("cue number: ")
	msg.setAddress("/select/"+str(a))
	msg.append("/cue/"+str(a)+"/start")
	client.sendto(msg, ('192.168.43.24', 53000))

'''
