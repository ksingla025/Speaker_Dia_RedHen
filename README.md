# Speaker Diarization Module : Heterogeneous news data

Detailed Documentation : http://web.iiit.ac.in/~karan.singla/redhenproposal.pdf

# Module 0

# Data-PreProcessing

#Requirements :
     1. Python (ofcourse, wrapper is in python)
     2. FFMPEG (https://www.ffmpeg.org/download.html)
     3. BeamformIt (http://www.xavieranguera.com/beamformit/)

#To Do :

Set paths to "ffmpeg" and "beamformit" in 01_pre-processing.py

ALso set configurations of beamformit in "do_beamforming.sh" in beamformit directory

#Usage :

python 01_pre-processing.py |path-to-mp4-data| |output_name|

