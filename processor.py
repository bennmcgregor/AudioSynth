import numpy
import math
        
def roundPitch(pitch):
    '''takes in a (?) pitch and returns the integer-rounded value of the pitch, a number between 1 and 12
    where pitch 1 is C, pitch 12 is B'''
    if pitch != None:
        pitch = round(float(pitch))
        pitch %= 12
        pitch += 1
    return pitch

'''To implement for the MIDI File (an extension to the project)
def setVolume():
'''
    
