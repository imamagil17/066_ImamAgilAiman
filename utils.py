import cv2
import numpy as np
import matplotlib.pyplot as plt

def save_comparison(original, enhanced, path):
    # Resize agar kedua gambar punya tinggi yang sama
    height = max(original.shape[0], enhanced.shape[0])
    width = original.shape[1] + enhanced.shape[1]

    # Tambahkan teks label
    label_font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 1
    font_thickness = 2
    text_color = (255, 255, 255)  # Putih

    # Tambahkan padding atas
    pad = 50  # tinggi padding atas untuk tulisan
    orig_with_pad = cv2.copyMakeBorder(original, pad, 0, 0, 0, cv2.BORDER_CONSTANT, value=(0, 0, 0))
    enh_with_pad = cv2.copyMakeBorder(enhanced, pad, 0, 0, 0, cv2.BORDER_CONSTANT, value=(0, 0, 0))

    # Tambahkan teks
    cv2.putText(orig_with_pad, 'BEFORE', (10, 35), label_font, font_scale, text_color, font_thickness, cv2.LINE_AA)
    cv2.putText(enh_with_pad, 'AFTER', (10, 35), label_font, font_scale, text_color, font_thickness, cv2.LINE_AA)

    # Gabungkan samping-samping
    concat = np.hstack((orig_with_pad, enh_with_pad))

    # Simpan hasil
    cv2.imwrite(path, concat)


def save_histogram(original, enhanced, path):
    colors = ('b', 'g', 'r')
    plt.figure(figsize=(10, 4))
    
    for i, color in enumerate(colors):
        orig_hist = cv2.calcHist([original], [i], None, [256], [0, 256])
        enh_hist = cv2.calcHist([enhanced], [i], None, [256], [0, 256])

        plt.plot(orig_hist, color=color, linestyle='--', label=f'Original {color.upper()}')
        plt.plot(enh_hist, color=color, label=f'Enhanced {color.upper()}')

    plt.title('RGB Histogram Comparison')
    plt.xlabel('Intensity Value')
    plt.ylabel('Pixel Count')
    plt.legend()
    plt.tight_layout()
    plt.savefig(path)
    plt.close()
