# Speaker Diarization Module : Heterogeneous news data

Detailed Documentation : http://web.iiit.ac.in/~karan.singla/redhenproposal.pdf

# Module 1
This will extract 16kz audio date from Mp4 files and divide them according to respective news network
Data-PreProcessing

Requirements :
     1. Python (ofcourse, wrapper is in python)
     2. FFMPEG (https://www.ffmpeg.org/download.html)

python 01_pre-processing.py |path-to-mp4-data| |output_name|

#Module 2
This module takes input the data folder created in previous step and do produces diarization output for each audio with data organized similarly to audio folder with name <inp>_seg

python 02_single_show_diarization.py |path-to-audio-data|

#Module 3
This does cross-show diarization using ILP-Clustering\CLR-Clustering across various files of the same show.

python _cross_show_diarization.py |path-to-seg-folder|

Note : "Scripts" folder contains supporting/utility scripts for the pipeline.
