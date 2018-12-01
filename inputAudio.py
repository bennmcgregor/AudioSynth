import numpy
import pyaudio
import analyse
import math
import processor
import serial
import time

ser = serial.Serial('/dev/ttyACM0', 9600)

class RecordObject: 
    isRecording = False

    def __init__(self):
        self.pyaud = pyaudio.PyAudio()
  
    def record(self):
        # To prevent multiple streams from being opened at the same time
        if not self.isRecording:
            stream = self.pyaud.open(
                format = pyaudio.paInt16,
                channels = 2,
                rate = 44100, #adjustable - higher frequency -> more sensitive
                input = True)

            self.isRecording = True
            old_pitch = 0
            pitch = -1
            currentTime = int(round(time.time() * 1000))
            oldTime = currentTime
            delta = currentTime - oldTime
            while self.isRecording:
                # Read raw microphone data
                rawsamps = stream.read(1024)
                # Convert raw data to NumPy array
                samps = numpy.frombuffer(rawsamps, dtype=numpy.int16)
                # Show the volume and pitch
                old_pitch = pitch
                pitch = processor.roundPitch(analyse.musical_detect_pitch(rawsamps))
                if pitch != old_pitch:
                    currentTime = int(round(time.time() * 1000))
                    #Take these values as input to Arduino:
                    #pitch
                    delta = currentTime - oldTime
                    oldTime = currentTime
                    print("Midi note: " + str(pitch) + " Delta: " + str(delta))#" Loudness: " + str(analyse.loudness(samps)) + " dB")
                    ser.write(str.encode(str(pitch)))
            stream.close()
            ser.write(b'0')

    def endRecord(self):
        self.isRecording = False

