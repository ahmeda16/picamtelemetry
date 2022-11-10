# piCAMTelemetry

## piCAM Mimicking Script In Python for CDH-TSAT6 Camera Module Telemetry


### Directions

1) Have The Image In Same Directory As Script
2) Make Sure Image Resolution DOES NOT EXCEED 4 BYTES IN SIZE (HEX ASCII)
3) Change {INSERT DIRECTORY HERE} In sentanceWriter For Telemetry Output

### Information Regarding Camera Module

The piCAM is the World’s First Space-Friendly Digital CubeSat Camera module specially designed to provide the colorful imaging in JPEG format and VGA resolution aboard small satellites with external Flashlight control signal.The unit enables a possibility to trigger signal for external LED-based flashlight to illuminate nearby objects of interest in dark orbital periods, such as solar sails, booms, deployable structures, tethers, etc.

The objective of this script is to mimick the camera telemtry data from any given image into a text file. This file can be used for testing C code into image conversion (to a JPEG file) with embedded programming.

Use of NUMPY, Math, and Turtle PIL Libraries required.

Link To Data Sheet: https://www.skyfoxlabs.com/pdf/piCAM_Datasheet_rev_B.pdf
