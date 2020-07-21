# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 10:09:43 2020

@author: user
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create() 
import random

while True:
    
    mc.setBlocks(x+5,y-1,z+5,x-5,y-1,z-5,17,color)

