#coding:utf-8
#############################
#Put @fn_timer on the function you want test,
#and run the function to get the TIME the function use.
#############################
###needed for time evaulation.
import time
from functools import wraps
##############################

import cv2 as cv
import numpy as np
from pylab import *
from PIL import Image
import matplotlib.pylab as plt



def fn_timer(function):
  @wraps(function)
  def function_timer(*args, **kwargs):
    t0 = time.time()
    result = function(*args, **kwargs)
    t1 = time.time()
    print ("Total time running %s: %s seconds" %
        (function.func_name, str(t1-t0))
        )
    return result
  return function_timer

@fn_timer
def npread():
    im = array(Image.open("1.png"))
    print np.max(im)

@fn_timer
def cvread():
    number=0
    mask = cv.imread("1.png",cv.IMREAD_ANYDEPTH)
    rol=mask.shape[0]
    row=mask.shape[1]
    for i in range(rol):
        for j in range(row):
            if mask[i,j]>number:
                number=mask[i,j]
    print number



#npread()
cvread()
