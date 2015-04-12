#!/usr/bin/python

'''
Author : Karan Singla

This script helps to does the following

1. Extracts Audio data using ffmpeg in ".wav" from ".mp4"
2. Then use sox command to convert the file to ".sph" format and also make the data single-channeled
3. Saves the data in same data folder according to different channels

'''

print "      ########################################################################"
print "      ##                 Data-Preprocessing ToolKit                         ##"
print "      ########################################################################\n"
import sys,re,commands
from os.path import basename


###### Set Path to the FFMPEG and BEAMFormIT according your environment ######
ffmpeg = "/home/karan/ffmpeg_sources/ffmpeg/ffmpeg" # path to installation of ffmpeg
beamformit =  "/home/karan/audio/redhen/tools/BeamformIt-3.51/do_beamforming.sh" # set right configurations in the bash file itself

###### Re-oraganizing data according to Networks and extracting Audio from Mp4 Files ######
data_dir = sys.argv[1] #path to data folder
data_org = sys.argv[2] #path to organized and converted data

ls = commands.getstatusoutput("ls "+data_dir)[1].split() #contents of data folder
print "Generate Audio for Data\n"
for fl in ls:
	if fl.split(".")[1] == "mp4":
		network = fl.split("_")[3]+"/"
		print "Video File: "+fl+"in "+network
		commands.getstatusoutput("mkdir -p "+data_org+"/"+network)
		commands.getstatusoutput(ffmpeg+" -i "+data_dir+fl+" -vn -f wav "+data_org+"/"+network+fl.split(".")[0]+".wav")

print "Audio Generated\n"

###### For each network do the beamforming and saved it to  ######
print "Do BeamForming"

networks = commands.getstatusoutput("ls "+data_org)[1].split()
for net in networks:
	print net+" network BeamForming : Running"
	commands.getstatusoutput(beamformit+" "+data_org+"/"+net+" "+net)
	print net+" network BeamForming : Done"

print "BeamForming Done, See Output Folder"
