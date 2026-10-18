# Portofolio Steven Paulus Siahaan

Website portofolio berbasis Python (Flask).

## Struktur
```
app.py              # aplikasi Flask + semua data portofolio
templates/index.html
static/style.css
static/img/         # foto
requirements.txt
Procfile / render.yaml
```

## Uji coba di komputer sendiri
```bash
pip install -r requirements.txt
python app.py
```
Buka http://localhost:5000 (hanya untuk uji coba, belum bisa diakses orang lain).

## Hosting publik (bisa diakses semua orang)

### Opsi A: Render.com (gratis, paling mudah)
1. Buat akun GitHub, buat repository baru, upload seluruh isi folder ini.
2. Daftar di https://render.com dan login dengan GitHub.
3. Klik **New +** > **Web Service**, pilih repository tadi.
4. Isi: Runtime `Python 3`, Build Command `pip install -r requirements.txt`, Start Command `gunicorn app:app`, Instance Type `Free`.
5. Klik **Create Web Service**. Setelah selesai, Anda mendapat link publik seperti `https://portofolio-steven.onrender.com`.

(File `render.yaml` sudah disiapkan, jadi bisa juga lewat **New +** > **Blueprint**.)
Catatan: paket gratis Render akan "tidur" bila lama tidak dikunjungi, jadi akses pertama bisa lambat beberapa detik.

### Opsi B: PythonAnywhere (gratis, tanpa GitHub)
1. Daftar di https://www.pythonanywhere.com (akun Beginner gratis).
2. Tab **Files**: upload semua file proyek (pertahankan struktur folder).
3. Tab **Web** > **Add a new web app** > **Flask** > pilih Python terbaru.
4. Set *Source code* ke folder proyek, lalu edit file WSGI agar berisi:
   ```python
   import sys
   sys.path.insert(0, "/home/USERNAME/portofolio-steven")
   from app import app as application
   ```
5. Klik **Reload**. Link publik: `https://USERNAME.pythonanywhere.com`.

## Mengubah isi
Semua teks (profil, pendidikan, skill, proyek, target) ada di bagian atas `app.py`. Ganti foto dengan menimpa file di `static/img/`.
