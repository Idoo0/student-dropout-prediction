# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding
Jaya Jaya Institut merupakan salah satu institusi pendidikan tinggi yang menghadapi tantangan tingginya angka putus sekolah (dropout) pada mahasiswa. Kondisi ini berdampak langsung pada reputasi akademik institusi dan efisiensi operasional pendidikan. Melalui penerapan data science, institusi berupaya mengidentifikasi faktor risiko yang memengaruhi kelulusan mahasiswa serta membangun sistem prediksi dini untuk mendeteksi mahasiswa yang rentan mengalami dropout sebelum semester akhir.

### Permasalahan Bisnis
Permasalahan utama yang ingin diselesaikan adalah tingginya tingkat dropout mahasiswa tanpa adanya sistem deteksi dini. Institusi kesulitan memetakan mahasiswa yang memerlukan intervensi akademik maupun finansial lebih awal, sehingga penanganan sering kali terlambat.

### Cakupan Proyek
Cakupan proyek ini meliputi:
1. Eksplorasi dan analisis data (EDA) untuk mengidentifikasi faktor-faktor utama yang berkorelasi dengan dropout mahasiswa.
2. Pembangunan model machine learning untuk mengklasifikasikan risiko dropout mahasiswa.
3. Pembuatan business dashboard interaktif untuk memonitor performa akademik dan status mahasiswa secara berkala.
4. Pembangunan prototype aplikasi machine learning berbasis Streamlit sebagai alat bantu prediksi bagi staf institusi.
5. Perumusan rekomendasi tindakan (action items) strategis bagi institusi.

### Persiapan

Sumber data: [Students' Performance Dataset](https://github.com/dicodingacademy/dicoding_dataset/tree/main/students_performance) (Jaya Jaya Institut / UCI Machine Learning Repository).

Setup environment:
```bash
# Membuat virtual environment
python -m venv venv

# Mengaktifkan virtual environment
# Windows:
.\venv\Scripts\activate
# Linux/macOS:
source venv/bin/activate

# Menginstal dependensi
pip install -r requirements.txt
```

## Business Dashboard
Business dashboard dibangun menggunakan Looker Studio untuk memonitor performa akademik, status finansial, serta risiko dropout mahasiswa Jaya Jaya Institut secara berkala. Dashboard menampilkan ringkasan metrik utama (total mahasiswa, total dropout, rata-rata nilai semester 1 & 2), distribusi status mahasiswa, pengaruh status pembayaran SPP dan beasiswa terhadap kelulusan, serta breakdown status mahasiswa per program studi dengan fitur filter interaktif.

- Link Looker Studio: https://datastudio.google.com/reporting/288bb3b3-f264-45f9-bd47-488d91049a3a

Screenshot dashboard dapat dilihat pada folder `b_igloo-dashboard/dashboard.png`.

## Menjalankan Sistem Machine Learning
Prototype machine learning dibangun menggunakan Streamlit untuk memprediksi probabilitas dan status risiko dropout mahasiswa berdasarkan parameter demografi, finansial, dan performa akademik semester awal.

Cara menjalankan prototype secara lokal:
```bash
# Menjalankan aplikasi streamlit
streamlit run app.py
```

Prototype juga telah di-deploy dan dapat diakses secara daring melalui tautan berikut:
- Link Streamlit Community Cloud: https://student-dropout-predictiongit-que8bzfh8m9fet8xl8k4ss.streamlit.app/
- Link Repositori GitHub: https://github.com/Idoo0/student-dropout-prediction.git

## Conclusion
Berdasarkan hasil analisis data dan pemodelan machine learning, faktor-faktor yang paling memengaruhi kemungkinan mahasiswa mengalami dropout adalah:
1. **Faktor Finansial**: Mahasiswa yang menunggak pembayaran uang kuliah (*tuition fees not up to date*) memiliki tingkat dropout mencapai 86.5%, dibandingkan dengan mahasiswa yang tertib membayar (24.7%). Mahasiswa yang memiliki status *debtor* juga memiliki kecenderungan dropout yang signifikan (62.0%).
2. **Performa Akademik Semester Awal**: Rata-rata nilai dan jumlah mata kuliah yang diselesaikan (*approved units*) pada semester 1 dan semester 2 mahasiswa yang dropout jauh lebih rendah (rata-rata nilai semester 1 sebesar 7.25 dan semester 2 sebesar 5.90) dibandingkan mahasiswa yang lulus (rata-rata 12.64 di semester 1 dan 12.70 di semester 2).
3. **Penerima Beasiswa**: Mahasiswa penerima beasiswa memiliki tingkat dropout yang sangat rendah (12.2%), berbanding 38.7% pada mahasiswa non-beasiswa.
4. **Performa Model**: Model Logistic Regression menghasilkan akurasi sebesar 88.6% dan F1-Score sebesar 80.5% pada data uji, menjadikannya model yang efektif untuk deteksi dini risiko dropout.

### Rekomendasi Action Items
Untuk meminimalkan angka dropout, Jaya Jaya Institut direkomendasikan menerapkan langkah-langkah berikut:
1. **Sistem Deteksi dan Peringatan Dini (Early Warning System)**: Mengintegrasikan model prediksi ke dalam sistem informasi akademik untuk menandai mahasiswa yang berisiko tinggi dropout berdasarkan nilai dan kelulusan mata kuliah di akhir semester 1.
2. **Konseling Akademik dan Program Remedial**: Menyediakan program mentoring atau pendampingan akademik intensif khusus bagi mahasiswa dengan perolehan SKS semester 1 rendah atau nilai di bawah ambang batas kelulusan.
3. **Fleksibilitas Pembayaran dan Bantuan Finansial**: Mengidentifikasi mahasiswa yang menunggak pembayaran uang kuliah (*tuition fees*) untuk diberikan opsi restrukturisasi cicilan, program kerja paruh waktu kampus (*work-study*), atau beasiswa darurat sebelum mereka memutuskan berhenti kuliah.
4. **Monitoring Berkala Mahasiswa Berusia Lanjut dan Kuliah Malam**: Memberikan dukungan bimbingan karier dan konseling manajemen waktu bagi kelompok mahasiswa kelas malam dan usia masuk lebih tinggi yang memiliki risiko dropout relatif lebih besar.
