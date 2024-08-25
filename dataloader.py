import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from pydicom import dcmread
from pydicom.data import get_testdata_file
from pydicom.pixel_data_handlers.util import (
    apply_color_lut,
    apply_modality_lut,
    apply_voi_lut,
)

x = "./stage_2_test/ID_0002d7b0.dcm"
y = dcmread(x)
z = y.pixel_array
# plt.imshow(apply_color_lut(z, y, palette="SUMMER"), cmap="gray")
plt.imshow(z, cmap='gray')
# plt.show()
plt.savefig("output0.png")
