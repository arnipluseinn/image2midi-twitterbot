from PIL import Image
import PIL.ImageOps
import numpy as np
from midiutil.MidiFile import MIDIFile
import sys 

#python image.jpg track_name

size = 128, 128
imgname = sys.argv[1]
trackname = sys.argv[2]
print(imgname + " " + trackname)

mf = MIDIFile(1, file_format=1, adjust_origin=False)
track = 0  
time = 0    
mf.addTrackName(track, time, trackname)
mf.addTempo(track, time, 120)
channel = 0
#volume = 100
photo = Image.open(imgname).transpose(Image.FLIP_TOP_BOTTOM)

photo = photo.resize(size, Image.NEAREST)
photo = PIL.ImageOps.invert(photo)
photo = photo.convert('RGB')
width = photo.size[0] 
height = photo.size[1]

for y in range(0, height):
	row = ""
	for x in range(0, width):
		RGB = photo.getpixel((x,y))
		R,G,B = RGB  
		brightness = (R/2)+(G/2)+(B/2)
		volume = brightness/3
		#print(y + "\n")
		#print "\n\n"
		pitch = y
		time = x             
		duration = 1         
		mf.addNote(track, channel, pitch, time, duration, volume)

with open("midi/" + trackname + ".mid", 'wb') as outf:
	mf.writeFile(outf)
