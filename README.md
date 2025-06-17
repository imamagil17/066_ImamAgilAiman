# Imam Agil Aiman F55123066 Teknik Informatik B

# Enhanced Night Vision

Proyek ini bertujuan untuk meningkatkan kualitas gambar dalam kondisi gelap atau malam hari menggunakan teknik pemrosesan citra digital, seperti peningkatan kontras (CLAHE) dan pengurangan noise (bilateral filter). Dataset yang digunakan adalah ExDark (Exclusively Dark).

## Fitur Utama

- Peningkatan kontras adaptif menggunakan CLAHE (Contrast Limited Adaptive Histogram Equalization)
- Pengurangan noise menggunakan bilateral filter
- Perbandingan visual antara gambar sebelum dan sesudah peningkatan
- Analisis histogram RGB untuk membandingkan distribusi intensitas
- Proses otomatis untuk semua gambar dalam satu kategori dari dataset ExDark

## Struktur Folder

├── enhancer.py # Fungsi peningkatan kualitas gambar

├── main.py # Program utama

├── utils.py # Fungsi tambahan (histogram dan perbandingan)

├── input_images/

│ └── exdark/ # Dataset ExDark (berisi subfolder kategori: Car, Street, dll)

├── output_images/ # Hasil pemrosesan: enhanced, before-after, histogram


## Cara Menjalankan

1. Pastikan dataset ExDark sudah diletakkan di dalam folder `input_images/exdark/`, misalnya:
   `input_images/exdark/Car/*.jpg`

2. Jalankan program menggunakan perintah: "python main.py --category Car

Ganti `Car` dengan nama kategori lain seperti `Street`, `Window`, dan sebagainya.

## Dependensi

- Python 3.x
- OpenCV
- NumPy
- Matplotlib

Untuk menginstal semua dependensi:
pip install opencv-python numpy matplotlib


## Output

Setiap gambar akan menghasilkan:

- Gambar hasil peningkatan (`*_enhanced.jpg`)
- Perbandingan gambar sebelum dan sesudah (`*_before_after.jpg`)
- Histogram RGB (`*_histogram.png`)

Semuanya disimpan di dalam folder `output_images`.

## Informasi Tambahan

- Dataset: ExDark (https://github.com/cs-chan/Exclusively-Dark-Image-Dataset)
- Digunakan untuk tugas mata kuliah Pengolahan Citra Digital
- Kode ditulis menggunakan bahasa Python
