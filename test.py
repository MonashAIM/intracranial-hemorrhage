import PIL.Image
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pydicom
import PIL
from PIL import Image
from pydicom import *
from pydicom.data import get_testdata_file
import pydicom.multival

dicom_file = read_file("./stage_2_test/ID_000a2d7b0.dcm")
dicom_array = dicom_file.pixel_array

def convert_to_hu(dicom_file):
    bias = dicom_file.RescaleIntercept
    slope = dicom_file.RescaleSlope
    pixel_values = dicom_file.pixel_array
    new_pixel_values = (pixel_values * slope) + bias
    return new_pixel_values

hu_pixels = convert_to_hu(dicom_file)

level = dicom_file.WindowCenter
window = dicom_file.WindowWidth

if (type(level) != pydicom.multival.MultiValue or type(window) != pydicom.multival.MultiValue):
    level = list()
    window = list()
    level.append(dicom_file.WindowCenter)
    window.append(dicom_file.WindowWidth)

# ...or set window/level manually to values you want
vmin = level[0] - window[0]/2
vmax = level[0] + window[0]/2
plt.imshow(hu_pixels, cmap='gray', vmin=vmin, vmax=vmax)
# plt.show()
plt.savefig("output1.png")