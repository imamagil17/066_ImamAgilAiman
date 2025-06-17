import cv2
import numpy as np

def enhance_image(img):
    # Konversi ke YCrCb untuk kontrol kontras
    ycrcb = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)
    y, cr, cb = cv2.split(ycrcb)

    # CLAHE untuk memperbaiki kontras channel Y
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    y_enhanced = clahe.apply(y)

    # Menggabungkan kembali
    ycrcb_enhanced = cv2.merge((y_enhanced, cr, cb))
    enhanced = cv2.cvtColor(ycrcb_enhanced, cv2.COLOR_YCrCb2BGR)

    # Bilateral filter untuk hilangkan noise sambil jaga edge
    enhanced = cv2.bilateralFilter(enhanced, d=9, sigmaColor=75, sigmaSpace=75)

    return enhanced
