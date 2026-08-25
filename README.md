# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding
Jaya Jaya Institut adalah institusi pendidikan tinggi yang sudah berdiri sejak tahun 2000 dan sudah meluluskan banyak mahasiswa. Masalahnya, angka mahasiswa yang dropout (tidak menyelesaikan pendidikan) juga cukup tinggi, dan ini jadi perhatian serius karena berpengaruh ke reputasi institusi.

Selama ini pihak institusi baru tahu seorang mahasiswa berisiko dropout setelah kondisinya sudah cukup parah, bukan dari awal. Makanya diperlukan cara untuk mendeteksi mahasiswa berisiko sejak semester-semester awal, supaya bisa dikasih pendampingan sebelum mereka benar-benar berhenti kuliah.

### Permasalahan Bisnis
- Institusi belum punya sistem untuk mengetahui lebih awal mahasiswa mana yang berpotensi dropout.
- Belum jelas faktor apa saja yang paling berpengaruh terhadap dropout, jadi program intervensi selama ini masih menyasar semua mahasiswa secara umum, bukan yang benar-benar berisiko.
- Tidak ada dashboard yang bisa dipakai tim akademik untuk memantau performa mahasiswa secara berkala.

### Cakupan Proyek
Proyek ini mencakup:
- Eksplorasi data untuk melihat pola dan faktor yang berkaitan dengan dropout.
- Membangun model machine learning untuk memprediksi risiko dropout mahasiswa.
- Membuat dashboard untuk memantau performa dan status mahasiswa.
- Membuat prototype aplikasi (Streamlit) supaya model bisa langsung dipakai oleh staf institusi.
- Menyusun rekomendasi tindakan untuk institusi berdasarkan hasil analisis.

### Persiapan

Sumber data: [Students' Performance Dataset](https://github.com/dicodingacademy/dicoding_dataset/tree/main/students_performance) (Jaya Jaya Institut / UCI Machine Learning Repository).

Setup environment:
```bash
python -m venv venv

# Windows
.\venv\Scripts\activate
# Linux/macOS
source venv/bin/activate

pip install -r requirements.txt
```

## Business Dashboard
Dashboard dibuat pakai Looker Studio, isinya untuk memantau performa akademik, status finansial, dan risiko dropout mahasiswa. Ada ringkasan jumlah mahasiswa dan dropout, rata-rata nilai semester 1 dan 2, distribusi status mahasiswa per program studi, sampai perbandingan status pembayaran SPP dan beasiswa terhadap status kelulusan. Ada filter per program studi juga.

- Link Looker Studio: https://datastudio.google.com/reporting/288bb3b3-f264-45f9-bd47-488d91049a3a

Screenshot dashboard ada di folder `b_igloo-dashboard/dashboard.png`.

## Menjalankan Sistem Machine Learning
Prototype dibuat pakai Streamlit, dipakai untuk memprediksi apakah seorang mahasiswa berisiko dropout atau tidak berdasarkan data demografi, finansial, dan nilai semester awal.

Cara jalanin secara lokal:
```bash
streamlit run app.py
```

Sudah di-deploy juga dan bisa diakses online lewat link berikut:
- Streamlit Community Cloud: https://student-dropout-predictiongit-que8bzfh8m9fet8xl8k4ss.streamlit.app/
- Repository GitHub: https://github.com/Idoo0/student-dropout-prediction.git

## Conclusion
Dari hasil EDA dan modeling, ada beberapa faktor yang kelihatan paling berpengaruh ke dropout mahasiswa.

Yang paling kentara adalah faktor finansial. Mahasiswa yang menunggak SPP (tuition fees not up to date) punya tingkat dropout sampai 86.5%, jauh di atas mahasiswa yang pembayarannya lancar (24.7%). Status debtor juga cenderung berbanding lurus dengan dropout, sekitar 62%.

Performa akademik di semester 1 dan 2 juga jadi indikator kuat. Mahasiswa yang dropout rata-rata nilainya jauh lebih rendah dibanding yang lulus (sekitar 7.25 vs 12.64 di semester 1, dan 5.90 vs 12.70 di semester 2) — artinya kalau nilai semester awal sudah rendah, itu bisa jadi sinyal peringatan dini.

Beasiswa juga kelihatan berpengaruh: mahasiswa penerima beasiswa dropout rate-nya cuma 12.2%, sedangkan yang tidak dapat beasiswa 38.7%.

Untuk modelnya sendiri dipilih Logistic Regression, akurasinya 88.6% dan F1-Score 80.5% di data uji — cukup layak dipakai untuk deteksi dini risiko dropout.

### Rekomendasi Action Items
- Bangun sistem early warning yang menandai mahasiswa berisiko tinggi begitu nilai dan SKS lulus semester 1 sudah bisa dihitung, jangan tunggu sampai semester akhir.
- Sediakan program pendampingan/remedial khusus untuk mahasiswa dengan nilai atau SKS lulus semester 1 di bawah ambang batas.
- Untuk mahasiswa yang menunggak SPP, tawarkan opsi cicilan, kerja paruh waktu di kampus, atau beasiswa darurat sebelum mereka memutuskan berhenti — ini kelompok dengan risiko dropout paling tinggi.
- Pantau lebih rutin mahasiswa kelas malam dan yang usia masuknya lebih tua, karena kelompok ini juga menunjukkan risiko dropout yang relatif lebih besar dibanding rata-rata.
