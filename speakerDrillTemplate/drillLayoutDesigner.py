import svgwrite
import math

# Design something looking like radiation sign

def main():
 d = 27
 n = [8, 9, 15, 24, 30] # skip first one
 r = 5 # radius

 circleObjects = []

 for i in range(1, len(n)): # skip first one
     m = n[i]
     for j in range(0, m):
         theta = 2 * math.pi * j / m # => ANGLE
         x = d * (i + 1) * math.cos(theta) # => polar x
         y = d * (i + 1) * math.sin(theta) # => polar y

         r = j%10 + 2 if i == 4 else j%8 + 2 if i == 3 else j%5 + 4 if i == 2 else j%3 + 5 if i == 1 else 0

         circleObjects.append(Circle(x, y, r))

 width = max([c.x for c in circleObjects]) * 2.2
 height = max([c.y for c in circleObjects]) * 2.2
 dwg = svgwrite.Drawing('template.svg', size=(width, height))

 # offsets for shifting all circles so that the SVG can be easily viewed in browser
 x_offset = min([c.x for c in circleObjects]) * 1.1
 y_offset = min([c.y for c in circleObjects]) * 1.1

 for c in circleObjects:
     adjusted_x = c.x - x_offset
     adjusted_y = c.y - y_offset
     dwg.add(svgwrite.shapes.Circle((adjusted_x, adjusted_y), c.r))

 dwg.save()

class Circle:
     def __init__(self, x, y, r):
         self.x = x
         self.y = y
         self.r = r

if __name__ == "__main__":
 main()