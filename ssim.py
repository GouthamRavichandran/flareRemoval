from skimage.metrics import structural_similarity as ssim
import numpy as np
import cv2

def compare(imageA, imageB):
  # Calculate the MSE and SSIM
  s = ssim(imageA, imageB)

  # Return the SSIM. The higher the value, the more "similar" the two images are.
  return s

ssim_avg = []

def main(): 
 # Import images
 for i in range(0,38):
    image1 = cv2.imread("input/" + str(i) + ".png")
    image2 = cv2.imread("output/" + str(i) + ".png", 1)
    image1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
    image2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
    ssim_value = compare(image1, image2)
    # print("SSIM:", ssim_value)
    ssim_avg.append(ssim_value)

if __name__ == '__main__':
  main()
  print(ssim_avg)
  avg = average(ssim_avg)
  print("average ssim is " + str(avg))

  #Reference
  #https://code.adonline.id.au/structural-similarity-index-ssim-in-python/
