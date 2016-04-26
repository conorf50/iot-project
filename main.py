from wyliodrin import *

import os

import struct

from datetime import *
from subprocess import *

from flask import Flask
app = Flask (__name__)

from flask import render_template

from flask import request



cmd = "ip addr show enp0s20f6 | grep inet | awk '{print $2}' | cut -d/ -f1"
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
color = colorToRGB('#33ccff')
lcd2.setRGB(color[0], color[1], color[2] )
lcd2.write(str( ipaddr ) )

@app.route ("/led", methods=['GET'])
def route():
  return render_template ('/form.html', lcd=lcd)
  
@app.route ("/led", methods=['POST'])
def route2():
  if (request.form['state']) == 'on':
    digitalWrite(grove+4, 1)
  elif (request.form['state']) == 'off':
    digitalWrite(grove+4, 0)
  return render_template ('/form.html', lcd=lcd)
  
  
  
  
  
app.run (host='0.0.0.0')
