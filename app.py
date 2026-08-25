import streamlit as st
import pandas as pd
import numpy as np
import joblib

st.set_page_config(
    page_title="Prediksi Dropout Mahasiswa - Jaya Jaya Institut",
    layout="wide"
)

@st.cache_resource
def load_model_artifacts():
    model = joblib.load('model/model.pkl')
    scaler = joblib.load('model/scaler.pkl')
    features = joblib.load('model/features.pkl')
    return model, scaler, features

model, scaler, features = load_model_artifacts()

st.title("Sistem Prediksi Dropout Mahasiswa")
st.write("Aplikasi deteksi dini risiko dropout mahasiswa untuk Jaya Jaya Institut.")

course_options = {
    171: "Animation and Multimedia Design",
    9254: "Tourism",
    9070: "Communication Design",
    9773: "Journalism and Communication",
    9147: "Management",
    9991: "Management (Evening)",
    9238: "Social Service",
    8014: "Social Service (Evening)",
    9500: "Nursing",
    9085: "Veterinary Nursing",
    9119: "Informatics Engineering",
    9003: "Agronomy",
    9130: "Equinculture",
    9556: "Oral Hygiene",
    9670: "Advertising and Marketing Management",
    9853: "Basic Education",
    33: "Biofuel Production Technologies"
}

st.header("Formulir Data Mahasiswa")

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Informasi Demografi & Pendaftaran")
    gender = st.selectbox("Jenis Kelamin", options=[0, 1], format_func=lambda x: "Perempuan" if x == 0 else "Laki-laki")
    age = st.number_input("Usia saat Mendaftar", min_value=15, max_value=70, value=20)
    marital_status = st.selectbox("Status Pernikahan", options=[1, 2, 3, 4, 5, 6], format_func=lambda x: {1: "Single", 2: "Married", 3: "Widower", 4: "Divorced", 5: "Facto Union", 6: "Legally Separated"}.get(x, str(x)))
    nacionality = st.selectbox("Kewarganegaraan", options=[1, 2, 6, 11, 13, 14, 17, 21, 22, 24, 25, 26, 32, 41, 62, 100, 101, 103, 105, 108, 109], format_func=lambda x: "Portuguese" if x == 1 else ("Brazilian" if x == 41 else f"Code {x}"))
    international = st.selectbox("Mahasiswa Internasional", options=[0, 1], format_func=lambda x: "Tidak" if x == 0 else "Ya")
    displaced = st.selectbox("Perantau (Displaced)", options=[0, 1], format_func=lambda x: "Tidak" if x == 0 else "Ya")
    special_needs = st.selectbox("Kebutuhan Khusus", options=[0, 1], format_func=lambda x: "Tidak" if x == 0 else "Ya")

with col2:
    st.subheader("Jalur & Status Finansial")
    course = st.selectbox("Program Studi", options=list(course_options.keys()), format_func=lambda x: course_options.get(x, str(x)))
    daytime_evening = st.selectbox("Waktu Kuliah", options=[1, 0], format_func=lambda x: "Siang (Daytime)" if x == 1 else "Malam (Evening)")
    application_mode = st.number_input("Kode Application Mode", min_value=1, max_value=60, value=1)
    application_order = st.number_input("Urutan Pilihan Prodi (0-9)", min_value=0, max_value=9, value=1)
    admission_grade = st.number_input("Nilai Masuk (Admission Grade, 0-200)", min_value=0.0, max_value=200.0, value=125.0)
    prev_qualification = st.number_input("Kode Kualifikasi Sebelumnya", min_value=1, max_value=50, value=1)
    prev_grade = st.number_input("Nilai Kualifikasi Sebelumnya (0-200)", min_value=0.0, max_value=200.0, value=120.0)
    tuition_fees = st.selectbox("Status Pembayaran Kuliah Terkini", options=[1, 0], format_func=lambda x: "Lunas / Up to date" if x == 1 else "Menunggak")
    debtor = st.selectbox("Memiliki Tunggakan (Debtor)", options=[0, 1], format_func=lambda x: "Tidak" if x == 0 else "Ya")
    scholarship = st.selectbox("Penerima Beasiswa", options=[0, 1], format_func=lambda x: "Tidak" if x == 0 else "Ya")

with col3:
    st.subheader("Latar Belakang Orang Tua")
    mother_qual = st.number_input("Kualifikasi Pendidikan Ibu", min_value=1, max_value=50, value=19)
    father_qual = st.number_input("Kualifikasi Pendidikan Ayah", min_value=1, max_value=50, value=19)
    mother_occ = st.number_input("Pekerjaan Ibu", min_value=1, max_value=50, value=5)
    father_occ = st.number_input("Pekerjaan Ayah", min_value=1, max_value=50, value=9)

    st.subheader("Kondisi Ekonomi Makro")
    unemployment = st.number_input("Tingkat Pengangguran (%)", min_value=0.0, max_value=30.0, value=10.8)
    inflation = st.number_input("Tingkat Inflasi (%)", min_value=-5.0, max_value=20.0, value=1.4)
    gdp = st.number_input("Pertumbuhan GDP", min_value=-10.0, max_value=10.0, value=1.74)

st.subheader("Performa Akademik Mahasiswa")
col_sem1, col_sem2 = st.columns(2)

with col_sem1:
    st.markdown("**Semester 1**")
    cu_1st_credited = st.number_input("SKS Diakui Sem 1 (Credited)", min_value=0, max_value=30, value=0)
    cu_1st_enrolled = st.number_input("SKS Diambil Sem 1 (Enrolled)", min_value=0, max_value=30, value=6)
    cu_1st_evaluations = st.number_input("Jumlah Evaluasi Sem 1", min_value=0, max_value=30, value=6)
    cu_1st_approved = st.number_input("SKS Lulus Sem 1 (Approved)", min_value=0, max_value=30, value=5)
    cu_1st_grade = st.number_input("Rata-rata Nilai Sem 1 (0-20)", min_value=0.0, max_value=20.0, value=12.0)
    cu_1st_no_eval = st.number_input("SKS Tanpa Evaluasi Sem 1", min_value=0, max_value=30, value=0)

with col_sem2:
    st.markdown("**Semester 2**")
    cu_2nd_credited = st.number_input("SKS Diakui Sem 2 (Credited)", min_value=0, max_value=30, value=0)
    cu_2nd_enrolled = st.number_input("SKS Diambil Sem 2 (Enrolled)", min_value=0, max_value=30, value=6)
    cu_2nd_evaluations = st.number_input("Jumlah Evaluasi Sem 2", min_value=0, max_value=30, value=6)
    cu_2nd_approved = st.number_input("SKS Lulus Sem 2 (Approved)", min_value=0, max_value=30, value=5)
    cu_2nd_grade = st.number_input("Rata-rata Nilai Sem 2 (0-20)", min_value=0.0, max_value=20.0, value=12.0)
    cu_2nd_no_eval = st.number_input("SKS Tanpa Evaluasi Sem 2", min_value=0, max_value=30, value=0)

st.write("---")

if st.button("Prediksi Status Mahasiswa"):
    input_data = {
        'Marital_status': marital_status,
        'Application_mode': application_mode,
        'Application_order': application_order,
        'Course': course,
        'Daytime_evening_attendance': daytime_evening,
        'Previous_qualification': prev_qualification,
        'Previous_qualification_grade': prev_grade,
        'Nacionality': nacionality,
        'Mothers_qualification': mother_qual,
        'Fathers_qualification': father_qual,
        'Mothers_occupation': mother_occ,
        'Fathers_occupation': father_occ,
        'Admission_grade': admission_grade,
        'Displaced': displaced,
        'Educational_special_needs': special_needs,
        'Debtor': debtor,
        'Tuition_fees_up_to_date': tuition_fees,
        'Gender': gender,
        'Scholarship_holder': scholarship,
        'Age_at_enrollment': age,
        'International': international,
        'Curricular_units_1st_sem_credited': cu_1st_credited,
        'Curricular_units_1st_sem_enrolled': cu_1st_enrolled,
        'Curricular_units_1st_sem_evaluations': cu_1st_evaluations,
        'Curricular_units_1st_sem_approved': cu_1st_approved,
        'Curricular_units_1st_sem_grade': cu_1st_grade,
        'Curricular_units_1st_sem_without_evaluations': cu_1st_no_eval,
        'Curricular_units_2nd_sem_credited': cu_2nd_credited,
        'Curricular_units_2nd_sem_enrolled': cu_2nd_enrolled,
        'Curricular_units_2nd_sem_evaluations': cu_2nd_evaluations,
        'Curricular_units_2nd_sem_approved': cu_2nd_approved,
        'Curricular_units_2nd_sem_grade': cu_2nd_grade,
        'Curricular_units_2nd_sem_without_evaluations': cu_2nd_no_eval,
        'Unemployment_rate': unemployment,
        'Inflation_rate': inflation,
        'GDP': gdp
    }

    input_df = pd.DataFrame([input_data])[features]
    input_scaled = scaler.transform(input_df)

    prediction = model.predict(input_scaled)[0]
    probabilities = model.predict_proba(input_scaled)[0]

    st.subheader("Hasil Prediksi")
    if prediction == 1:
        st.error(f"Prediksi: **BERISIKO DROPOUT** (Probabilitas Risiko: {probabilities[1]*100:.2f}%)")
        st.write("Rekomendasi: Mahasiswa memerlukan perhatian khusus pada pembayaran SPP dan pendampingan akademik.")
    else:
        st.success(f"Prediksi: **NON-DROPOUT / AMAN** (Probabilitas Lulus/Aktif: {probabilities[0]*100:.2f}%)")
        st.write("Rekomendasi: Mahasiswa berada dalam jalur akademik dan finansial yang stabil.")
