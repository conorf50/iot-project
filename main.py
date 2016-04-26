from wyliodrin import *
import os
import struct
from datetime import *
from subprocess import *
from flask import Flask
app = Flask (__name__)
from flask import render_template
from flask import request



cmd = "A=$(ip addr show dev enp0s20f6); A=${A##*inet }; echo ${A%%/*}"
def run_cmd(cmd):
        p = Popen(cmd, shell=True, stdout=PIPE)
        output = p.communicate()[0]
        return output


lcd = None

pinMode (13, 1)

if os.getenv ("wyliodrin_board") == "raspberrypi":
  grove = 300
  grovepiSetup (grove, 4)
else:
  grove = 0

lcd2 = rgb_lcd()
lcd2.begin(16, 2)

def colorToRGB (color):
  return struct.unpack ('BBB', color[1:].decode('hex'))

pinMode (4, 1)


print('Starting...')

ipaddr = run_cmd(cmd)

digitalWrite (13, 1)
color = colorToRGB('#33ccfe')
lcd2.setRGB(color[0], color[1], color[2] )
lcd2.write("IP=" + str(ipaddr)+ "    " )

@app.route ("/control", methods=['GET'])
def route():
  return render_template ('/form.html', lcd=lcd)
  
@app.route ("/control", methods=['POST'])
def route2():
  if (request.form['state']) == 'relayOn':
    digitalWrite(grove+4, 1)
  if (request.form['state']) == 'relayOff':
    digitalWrite(grove+4, 0)
  return render_template ('/form.html', lcd=lcd)
  
@app.route ("/control", methods=['POST'])
def route3():
  if (request.form['state']) == 'on':
    digitalWrite(grove+4, 0)
  if (request.form['state']) == 'off':
    digitalWrite(grove+4, 0)    
  return render_template ('/form.html', lcd=lcd)
  
@app.route ("/control", methods=['POST'])
def route4():
  if (request.form['state']) == 'message':
    lcd2.write(str(message))
  return render_template ('/form.html', lcd=lcd)
  
  
 
app.run (host='0.0.0.0')











