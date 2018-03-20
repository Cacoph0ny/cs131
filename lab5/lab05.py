##
# Tharin Dresher-Hurst
# lab05.py
# Created basic fuctions - TDH
#   -pipeThick
#   -pipeVolume
# 20 - 3 - 18
##

import math

def pipeThick(radiusOne, radiusTwo):
    pipeThick=radiusOne-radiusTwo
    return pipeThick

def pipeVolume(radiusOne, radiusTwo, height):
    pipeVolumeInner= math.pi * (radiusTwo ** 2) * height
    pipeVolumeOuter= math.pi * (radiusOne ** 2) * height
    pipeVolumeTotal= pipeVolumeOuter - pipeVolumeInner
    return pipeVolumeTotal

def pipeSurfaceInner(radiusTwo, height):
    pipeCircum= 2 * math.pi * radiusTwo
    pipeSurfaceInner= pipeCircum * height
    return pipeSurfaceInner

def pipeSurfaceOuter(radiusOne, height):
    pipeCircum= 2 * math.pi * radiusOne
    pipeSurfaceOuter= pipeCircum * height
    return pipeSurfaceOuter

def pipeSurfaceRing(radiusOne, radiusTwo):
    pipeBigRing= math.pi * (radiusOne ** 2)
    pipeRingSmall= math.pi * (radiusTwo ** 2)
    pipeSurfaceRing= pipeBigRing - pipeRingSmall
    return pipeSurfaceRing

def pipeSurfaceTotal(inner, outer, ring):
    pipeSurfaceTotal= inner + outer + (2 * ring)
    return pipeSurfaceTotal

def main():
    userRadiusOne=float(input("Enter outer radius (r1): "))
    userRadiusTwo=float(input("Enter inner radius (r2): "))
    userLength=float(input("Enter the length (h):    "))
    pipeThickness=float(pipeThick(userRadiusOne, userRadiusTwo))
    pipeVolumeOne=float(pipeVolume(userRadiusOne, userRadiusTwo, userLength))
    pipeInner=float(pipeSurfaceInner(userRadiusTwo, userLength))
    pipeOuter=float(pipeSurfaceOuter(userRadiusOne, userLength))
    pipeRing=float(pipeSurfaceRing(userRadiusOne, userRadiusTwo))
    pipeTotal=float(pipeSurfaceTotal(pipeInner, pipeOuter, pipeRing))
    print("\n\nThe thickness is:\t\t\t %f" %(pipeThickness))
    print("The volume of the pipe is:\t\t %f" %(pipeVolumeOne))
    print("Surface area of the inner pipe:\t\t %f" %(pipeInner))
    print("Surface area of the outer pipe:\t\t %f" %(pipeOuter))
    print("Surface area of the rings:\t\t %f" %(pipeRing))
    print("The total surface area of the pipe:\t %f" %(pipeTotal))

main()
