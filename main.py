import os
import argparse
import cv2
from enhancer import enhance_image
from utils import save_comparison, save_histogram

# ====== Konfigurasi awal ======
EXDARK_ROOT = "input_images/exdark"
OUTPUT_FOLDER = "output_images"
ENHANCED_DIR = os.path.join(OUTPUT_FOLDER, "enhanced")
COMPARE_DIR = os.path.join(OUTPUT_FOLDER, "before_after")
HISTO_DIR = os.path.join(OUTPUT_FOLDER, "histogram")

# Pastikan semua folder output tersedia
os.makedirs(ENHANCED_DIR, exist_ok=True)
os.makedirs(COMPARE_DIR, exist_ok=True)
os.makedirs(HISTO_DIR, exist_ok=True)

def process_image(input_path, output_name):
    original = cv2.imread(input_path)
    if original is None:
        print(f"[!] Gagal membaca gambar: {input_path}")
        return

    enhanced = enhance_image(original)

    output_enhanced = os.path.join(ENHANCED_DIR, f"{output_name}_enhanced.jpg")
    output_comparison = os.path.join(COMPARE_DIR, f"{output_name}_before_after.jpg")
    output_histogram = os.path.join(HISTO_DIR, f"{output_name}_histogram.png")

    cv2.imwrite(output_enhanced, enhanced)
    save_comparison(original, enhanced, output_comparison)
    save_histogram(original, enhanced, output_histogram)

    print(f"[✓] Selesai: {output_name}")

def main():
    parser = argparse.ArgumentParser(description="Enhanced Night Vision - ExDark Subfolder Selector")
    parser.add_argument('--category', type=str, required=True,
                        help="Nama subfolder kategori di ExDark, contoh: Street, Window, Car")
    args = parser.parse_args()

    category_path = os.path.join(EXDARK_ROOT, args.category)

    if not os.path.exists(category_path):
        print(f"[!] Folder tidak ditemukan: {category_path}")
        return

    print(f"[•] Memproses kategori: {args.category}")

    for filename in os.listdir(category_path):
        if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
            input_path = os.path.join(category_path, filename)
            output_name = f"{args.category}_{os.path.splitext(filename)[0]}"
            process_image(input_path, output_name)

if __name__ == "__main__":
    main()
