from numpy.lib.function_base import average
from math import log10, sqrt
import cv2
import numpy as np
  
def PSNR(original, compressed):
    mse = np.mean((original - compressed) ** 2)
    if(mse == 0):  # MSE is zero means no noise is present in the signal .
                  # Therefore PSNR have no importance.
        return 100
    max_pixel = 255.0
    psnr = 20 * log10(max_pixel / sqrt(mse))
    return psnr
  
psnr = []

def main():
  for i in range(0,38):
    original = cv2.imread("input/" + str(i) + ".png")
    compressed = cv2.imread("output/" + str(i) + ".png", 1)
    value = PSNR(original, compressed)
    psnr.append(value)
    # print(f"PSNR value is {value} dB")
       
if __name__ == "__main__":
    main()
    print(psnr)
    avg = average(psnr)
    print("average psnr is " + str(avg))
    
    #Reference
    #https://www.geeksforgeeks.org/python-peak-signal-to-noise-ratio-psnr/
