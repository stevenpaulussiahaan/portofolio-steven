"""Website portofolio Steven Paulus Siahaan (Flask).

Jalankan lokal untuk uji coba:   python app.py
Jalankan di hosting publik:      gunicorn app:app   (lihat README.md)
"""
import os
from datetime import date

from flask import Flask, render_template

app = Flask(__name__)

PROFIL = {
    "nama": "Steven Paulus Siahaan",
    "tagline": "Mahasiswa Matematika · Programmer · Drummer",
    "kampus": "Universitas Sumatera Utara (USU)",
    "prodi": "S1 Matematika",
    "nim": "250803028",
    "semester": 3,
    "lahir": "Pematang Siantar, 11 Oktober 2007",
    "ringkasan": (
        "Pembelajar yang menyeimbangkan ketajaman logika matematika dengan "
        "eksplorasi kreatif di dunia pemrograman dan musik. Terbiasa memecahkan "
        "masalah komputasional, membangun visualisasi dan aplikasi, serta "
        "menyusun dokumen akademik dengan LaTeX."
    ),
}

PENDIDIKAN = [
    {
        "judul": "S1 Matematika",
        "tempat": "Universitas Sumatera Utara (USU)",
        "waktu": "2025 – sekarang (semester 3)",
        "detail": "NIM 250803028",
    },
    {
        "judul": "SMA",
        "tempat": "SMAS Sultan Iskandar Muda",
        "waktu": "Lulusan",
        "detail": "Medali Perak bidang Kimia dan Biologi pada Olimpiade Siswa Indonesia (OSI)." "Medali Emas bidang Matematika pada Education Expo & Science Olympiad USU 2024."
    },
]

ORGANISASI = [
    {
        "judul": "Pengurus Himpunan Mahasiswa Matematika (HMM) USU",
        "waktu": "Periode 2026/2027",
        "detail": "Dilantik pada September 2026.",
    },
]

SKILLS = {
    "Pemrograman": ["Python", "Flask", "Streamlit", "SymPy", "Pascal", "MATLAB", "Flutter"],
    "Matematika & Komputasi": ["Analisis Numerik", "Visualisasi Matriks", "Aplikasi Kalkulator"],
    "Penulisan Akademik": ["LaTeX", "BibTeX", "Template Jurnal", "Presentasi Lanjutan"],
    "Musik & Audio": ["Gitar", "Pop & Rock", "Pedal Reverb", "Equalizer & Mixing"],
}

PROYEK = [
    {
        "judul": "Visualisasi Matriks",
        "deskripsi": "Alat bantu visual untuk memahami operasi dan struktur matriks.",
        "tag": ["Python", "SymPy"],
    },
    {
        "judul": "Aplikasi Kalkulator",
        "deskripsi": "Kalkulator berbasis web dan mobile untuk perhitungan matematis.",
        "tag": ["Flask", "Streamlit", "Flutter"],
    },
    {
        "judul": "Penyelesaian Analisis Numerik",
        "deskripsi": "Implementasi metode numerik untuk menyelesaikan persoalan komputasional.",
        "tag": ["Python", "MATLAB"],
    },
    {
        "judul": "Template Jurnal & Presentasi",
        "deskripsi": "Template akademik tingkat lanjut menggunakan LaTeX dan BibTeX.",
        "tag": ["LaTeX", "BibTeX"],
    },
]

MUSIK = (
    "Di luar angka dan kode, saya seorang gitaris yang menggemari genre pop dan rock "
    "(termasuk band Vierra). Saya detail soal sound engineering praktis: sering "
    "bereksperimen dengan pedal reverb dan konfigurasi equalizer agar mixing suara "
    "terdengar pas saat bermain."
)

TARGET = [
    {
        "judul": "Beasiswa Bakti BCA",
        "detail": "Mendaftar program beasiswa sebagai langkah terstruktur menuju pengembangan diri.",
    },
    {
        "judul": "Mathematics Sciences Competition (MSC) 2027",
        "detail": "Mengambil peran strategis sebagai Ketua / Koordinator Pembuat Soal.",
    },
]

GALERI = ["img/foto-2.jpg", "img/foto-3.jpg"]


@app.route("/")
def beranda():
    return render_template(
        "index.html",
        p=PROFIL,
        pendidikan=PENDIDIKAN,
        organisasi=ORGANISASI,
        skills=SKILLS,
        proyek=PROYEK,
        musik=MUSIK,
        target=TARGET,
        galeri=GALERI,
        tahun=date.today().year,
    )


@app.route("/health")
def health():
    return "ok"


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
