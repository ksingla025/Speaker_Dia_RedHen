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
import sys
import commands
import threading
from os.path import basename


###### Set Path to the FFMPEG and BEAMFormIT according your environment ######
ffmpeg = "/home/karan/ffmpeg_sources/ffmpeg/ffmpeg" # path to installation of ffmpeg
beamformit =  "/home/karan/audio/redhen/tools/BeamformIt-3.51/do_beamforming.sh" # set right configurations in the bash file itself

###### Re-oraganizing data according to Networks and extracting Audio from Mp4 Files ######
data_dir = sys.argv[1] #path to data folder
data_org = sys.argv[2] #path to organized and converted data
beam_dir = data_org+"_beam" #path to beamformed data generated
commands.getstatusoutput("mkdir -p "+beam_dir) 
ls = commands.getstatusoutput("ls "+data_dir)[1].split() #contents of data folder


print "Generate Audio for Data\n"

def audio(name,lower,upper):

    for i in range(lower,upper):
	if ls[i].split(".")[1] == "mp4":
		network = ls[i].split("_")[3]+"/"
		print name+" : Video File: "+ls[i]+" in "+network+"    "
		commands.getstatusoutput("mkdir -p "+data_org+"/"+network)
		commands.getstatusoutput(ffmpeg+" -i "+data_dir+ls[i]+" -vn -f wav "+data_org+"/"+network+ls[i].split(".")[0]+".wav")

try:
		threads = []
		print ls,"THIS IS LENS",len(ls)
		t1 = threading.Thread(target=audio, args=("Thread-1",0,int(len(ls)/4),))
		t2 = threading.Thread(target=audio, args=("Thread-2",int((len(ls)/4)),int((len(ls)/2)),))
		t3 = threading.Thread(target=audio, args=("Thread-3",int((len(ls)/2)),int((len(ls)*3/4)),))
		t4 = threading.Thread(target=audio, args=("Thread-4",int((len(ls)*3/4)),int((len(ls))),))
		threads.extend([t1,t2,t3,t4])
		for x in threads:
			x.start()
		for x in threads:
			x.join()

except:
	print "Error: unable to start thread"

print "Audio Generated\n"

###### For each network do the beamforming and saved it to  ######
print "Do BeamForming"

net = commands.getstatusoutput("ls "+data_org)[1].split()

def beamform(name,lower,upper):
	for i in range(lower,upper):
		commands.getstatusoutput("mkdir -p temp ; mkdir -p "+beam_dir+"/"+net[i])
		for ls in commands.getstatusoutput("ls "+data_org+"/"+net[i])[1].split():
			commands.getstatusoutput("mv "+data_org+"/"+net[i]+"/"+ls+" temp/")
			print name+" : "+net[i]+" network BeamForming : Running "
			commands.getstatusoutput(beamformit+" temp/ "+ls)
			print name+" : "+net[i]+" network BeamForming : Done "+name
			commands.getstatusoutput("rm temp/*")
			commands.getstatusoutput("cp output/"+ls+"/"+ls+".wav "+beam_dir+"/"+net[i]+"/"+ls)

#	print "BeamForming Done, See Output Folder"

try:
                threads = []
                t1 = threading.Thread(target=beamform, args=("Thread-1",0,int(len(net)/4),))
                t2 = threading.Thread(target=beamform, args=("Thread-2",int((len(net)/4)),int((len(net)/2)),))
                t3 = threading.Thread(target=beamform, args=("Thread-3",int((len(net)/2)),int((len(net)*3/4)),))
                t4 = threading.Thread(target=beamform, args=("Thread-4",int((len(net)*3/4)),int((len(net))),))
                threads.extend([t1,t2,t3,t4])
                for x in threads:
                        x.start()
                for x in threads:
                        x.join()

except:
        print "Error: unable to start thread"

print "BeamForming Done, See "+beam_dir+" Folder"
