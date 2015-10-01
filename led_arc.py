from math import sin, cos, radians
import pcbnew

pcb = pcbnew.GetBoard()

# wxPoint units appear to be nanometers. 1 inch is 25,400,000 nm.

resistor_radius = 76200000 # 3 * 25,400,000
led_radius = 76200000 + 12700000

arc_center_x =  76200000 # 3 * 25,400,000
arc_center_y = 125730000 # 4.95 * 25,400,000
degrees_per_component = 3.0

def GetAngle(index):
    return (6.5 - index) * 3.0 # might need to convert this to an int

def GetPositionX(angle, radius):
    return int(arc_center_x + radius * cos(radians(angle)))

def GetPositionY(angle, radius):
    return int(arc_center_y + radius * sin(radians(angle)))

def placeComponentFamily(prefix, radius):
    for index in range(1,13):
        name = prefix + str(index)
        r = pcb.FindModuleByReference(name)
        angle = GetAngle(index)
        #print angle
        r.SetOrientation(int(angle))
        x = GetPositionX(angle, radius)
        y = GetPositionY(angle, radius)
        #print '{0},{1}'.format(x,y)
        r.SetPosition(pcbnew.wxPoint(x, y))

placeComponentFamily('R', resistor_radius)
placeComponentFamily('LED', led_radius)