from mss import mss
from pathlib import Path
import cv2
import numpy as np
import matplotlib.pyplot as plt

script_dir = Path(__file__).resolve().parent
out_file = script_dir / "screenshot.png"

# with mss() as sct:
#     sct.shot(output=str(out_file))


img = cv2.imread("ocr-sudoku\screenshot.png", cv2.IMREAD_COLOR)
# Displaying image using plt.imshow() method
cv2.imshow("image", img)

cv2.waitKey(0)

cv2.destroyAllWindows()
