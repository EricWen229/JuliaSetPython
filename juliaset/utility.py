import colorsys
import math

import PIL.ImageColor

class Complex:
    def __init__(self, x=0.0, y=0.0):
        self.x = float(x)
        self.y = float(y)

class RGBRange:
    colorIn = (0.0, 0.0, 0.0)
    colorOut = (0.0, 0.0, 0,0)

class HSBComponents:  
    h = 0.0
    s = 0.0
    b = 0.0
    
    def double3(self):
        return (self.h, self.s, self.b)
    
    def toRGB(self):
        return colorsys.hsv_to_rgb(self.h, self.s, self.b)

class JuliaSetColor:
    def __init__(self, hue=0.0, brightness=0.0, saturation=1.0):
        self.hue = hue
        self.brightness = brightness
        self.saturation = saturation
    
    def toRGBRange(self):
        s = RGBRange()
        hsb = HSBComponents()
        
        hsb.h = self.hue
        hsb.s = self.brightness / 10 + 0.65 * self.saturation
        hsb.b = 1 - self.brightness
        s.colorOut = hsb.toRGB()
        
        hsb.b = (1 - math.cos(hsb.b * math.pi)) / 8
        s.colorIn = hsb.toRGB()
        
        return s
