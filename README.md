## Qlabs-remote-Raspberry-pi-button

This program is made for a specific use, but it should work well as a base if you are getting started using OSC with Qlab.
If you are interested in it's use Qlab is running in the back of the room and on stage an actor needs to push a doorbell. In order to get the timeing perfectt using an arduino zero connected to a doorbell button, when pushed tells Qlab to play a specific cue.

### Qlab communication

If you want to quickly see how it connects:

```markdown
import OSC


while 1:
	a = raw_input("press enter to execute cue:")
	client = OSC.OSCClient()
	msg = OSC.OSCMessage()
	msg.setAddress("/cue/3/start")
	client.sendto(msg, ('192.168.100.17', 53000))

```

