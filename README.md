# Image Compression

Aplikasi untuk mengubah ukuran suatu gambar menggunakan framework Django

## Fitur Utama

- Pengguna (Umum)

## Teknologi yang Digunakan

- Python
- Django
- HTML & CSS (untuk antarmuka)
- PostgresSQL (database)

## Struktur Folder
imagecompress/
├── manage.py
├── imagecompress/ (Konfigurasi proyek Utama)
├── core/  (Aplikasi inti)
     ├── templates/ (Folder HTML)
     ├── static/ (Folder css) 
├── media/
     ├── gallery (penyimpanan hasil image compress)

## Cara Menjalankan Proyek
1. Jalankan Command prompt
   ```bash
   git clone https://github.com/floralebonna/Hackathon-Sevima-Flora.git
   cd imagecompress

2. Buat dan aktifkan virtual environment
   ```bash
   python -m venv env
   source venv/bin/activate     # Untuk Linux/Mac
   env\Scripts\activate        # Untuk Windows
  
4. Install package manager
   ```bash
   pip install Django
   pip install Pillow
   
5. Jalankan migrasi database
   ```bash
   python manage.py makemigrations
   python manage.py migrate

6. Jalankan server:
  ```bash
  python manage.py runserver
