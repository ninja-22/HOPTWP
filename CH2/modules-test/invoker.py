#!/usr/local/bin/python

from shapes import area_finder as AF
import shapes.area_finder as AFF

def find_area():
    AF.compute_area("circle", radius = 4)
    AF.compute_area("triangle", base = 4, altitude = 6)
    AF.compute_area("rect", length = 12, width = 5)
    AF.compute_area("square", side = 3)


find_area()