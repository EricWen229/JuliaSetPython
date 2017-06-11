import numpy as np
import threading
import time
import PIL.Image
from .utility import JuliaSetColor, Complex

class JuliaSet:
    def __init__(self):
        self.center = Complex()
        self.window = 4.0
        self.const = Complex(-0.5, 0.0)
        self.color = JuliaSetColor(hue=0, brightness=0.8, saturation=1.0)
    
class JuliaSetRenderer:
    def __init__(self):
        pass
    
    def render(self, juliaSet, pixelSize): 
        width = pixelSize[0]
        height = pixelSize[1]
        assert(width > 0 and height > 0)

        xValue = self.generateXValues(width, height, juliaSet)
        yValue = self.generateYValues(width, height, juliaSet)

        imageBuffer = list()
        
        cx = juliaSet.const.x
        cy = juliaSet.const.y
        loop = 200
        
        color = juliaSet.color.toRGBRange()
        cin = color.colorIn
        cout = color.colorOut
        
        for y in yValue:
            row = list()
            for x in xValue:
                c = 0.0

                currX = x
                currY = y
                
                for i in range(loop):
                    currX, currY = (currX * currX - currY * currY + cx, 2.0 * currX * currY + cy)
                    if currX * currX + currY * currY > 4.0:
                        c = float(i) / loop
                        break
                                
                rgb = [0.0, 0.0, 0.0]
                for i in range(3):
                    if cin[i] != cout[i]:
                        rgb[i] = ((c - cin[i]) / (cout[i] - cin[i])) * 1.8
                    else:
                        rgb[i] = 1.0 if c > cin[i] else 0.0
                    rgb[i] = np.uint8(255 * min(max(rgb[i], 0.0), 1.0))
                                
                row.append(rgb)
            imageBuffer.append(row)
            
        imageBuffer = np.array(imageBuffer)
        image = PIL.Image.fromarray(imageBuffer, mode='RGB')
        return image
    
    def generateXValues(self, width, height, juliaSet):
        arr = list()

        pixelW = juliaSet.window / float(width)
        startX = (juliaSet.center.x - juliaSet.window / 2.0) + pixelW / 2.0

        for i in range(width):
            arr.append(startX + i * pixelW)
        
        return arr
    
    def generateYValues(self, width, height, juliaSet):
        arr = list()

        windowY = juliaSet.window * (float(height) / width)
        pixelH = windowY / height
        startY = (juliaSet.center.y - windowY / 2) + pixelH / 2

        for i in range(height):
            arr.append(startY + i * pixelH)
        
        return list(reversed(arr))
