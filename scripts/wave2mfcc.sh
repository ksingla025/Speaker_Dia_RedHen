#!/bin/bash

wave=$1
dir=`dirname $wave`
base=`basename $wave .wav`

java -Xmx2048m -classpath ./LIUM/lium.jar fr.lium.spkDiarization.tools.Wave2FeatureSet --help --fInputMask=$wave --sInputMask="" --fInputDesc="audio16kHz2sphinx,1:1:0:0:0:0,13,0:0:0" --fOutputMask=$dir/$base.mfcc --fOutputDesc="audio16kHz2sphinx,1:1:0:0:0:0,13,0:0:0" $base

