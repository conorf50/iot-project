# WebLED
#### Student Name:  Conor Farrell

#### Original Concept:
The project is a simple home alarm and automation system. The original idea was to sense a user's position using either a mobile phone an ultrasonic sensor. Once a user has been identified, the system can turn on lights, play music etc.. An RGB LED may be used to provide a substitute for smart LED lights such as the Philips Hue where the colour of the light can change depending on a number of factors based on the user's preferences. Overall the application was too complex and due to technical problems with Wyliodrin, the consept had to be scrapped.


#### The Actual Project.
Due to technical difficulties with the Wyliodrin mobile sensors app, this was changed to a web API controlling a relay. 
#### Tools, Technologies and Equipment

The final system uses an Intel Galileo with the Grove shield and components. The system uses a Grove LCD and a relay to facilitate home automation. The Wyliodrin platform is used to tie the system together and also hosts a small web server on the Galileo to process requests. At the moment the LCD only displays the IP address of the board but this could be upgraded with a message facility, enabling a user to write messages and leave them visible on the screen.



