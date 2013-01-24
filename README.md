Rabbity-Pi
==========

Integration of a Raspberry-Pi to control a Nabaztag v1.

Nabaztag hardware investigations
================================

Some links
----------

Nabaztag v1
http://asia.cnet.com/cracking-open-the-nabaztag-wi-fi-rabbit-62036366.htm
http://www.techrepublic.com/photos/cracking-open-the-nabaztag-wi-fi-rabbit/164137
(same pictures on both links)

Nabaztag v2
http://www.petertyser.com/2007/03/11/nabaztag-nabaztagtag-dissection/

Personnal investigation (ongoing)
---------------------------------

**General**

All external elements (motors, sensors, button and power) are connected to the motherboard by removable connectors, but it seems that some glue was added. I managed to disconnect them using a flat screwdriver.

**LEDs**

In order to have a nice circle on the Nabaztag body instead of a blurry light, LEDs are focused by pieces of black plastic, which are glued to the motherboard. As I want to keep the motherboard intact, I will have to find substitute for those little black tubes.
The LEDs themselves seems to be RGB SMD LEDs. I don't really need to investigate more than that as I will not reuse those LEDs. I just have to find suitable RGB LEDs (not SMD as I don't have any experience with those tiny components).

**Ears**

Each ear is put in motion by an electric motors with some plastic reduction gear box. In the v2 of the Nabaztag it seems that they changed that with a pulleys-belt system.
At first I thought that the motors were stepper motors, but it seems that they are in fact just classic DC motors (only two wires are connected to them).

The ear positionning is controled by an optical encoder (which I suppose is absolute as the rabbit always put the ears in the right position after moving them manually). This optical encoder is linked to the motherboard by 4 wires, so I guess that there is 16 possible postions.

Todo:
- Find the characteristics of the motors, then find a good driver board (an H bridge which can control two motors such as L298N seems suitable).
- Test the optical encoder to understand how the different positions are encoded.

**Loudspeaker**

The loudspeaker is very classic (and very low fidelity). I will have to investigate to see if I can connect it directly to the audio output of the Raspberry-Pi without fear of damaging it.

**Button**

The button on the head is connected to the motherboard using a removable connector, I will be able to reuse it directly.

**Power**

At first I wasn't interested in re-using the Nabaztag power system but as it provides a removable connector that may be easily connected to my electronic board, I may reuse it. At least to power the motors, and maybe the Raspberry-Pi itself if the voltage and other characteristics are suitable.

Raspberry-Pi
============

This is my first Raspberry-Pi project.

I installed the official Raspbian on an SD card and tried to boot, at some point during the boot process an error (mmc0: Timeout waiting for hardware interrupt) is spamming. It seems to be a known issue and I just have to test it for more than 10 min. 

I also need to get a keyboard :)

GPIO
----

This is an estimation of the number of GPIO I will need for the project:
- LEDs : 3 per RGB LED and 5 LEDs => 15
- Motors : 2 per Motor and 2 Motors => 4
- Encoder : 4 per encoder and 2 encoders => 8
- Button : 1

This is a total of 28 GPIO, which is too much for the Raspberry-Pi (Max 17 GPIO?). I need to see if I can reduce the needs on the encoders (I don't really need a 16 step ear rotation resolution) as well as the need for LEDs (maybe I can have some common pins or some LEDs may not need to be RGB).
