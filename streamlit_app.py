import streamlit as st

st.title("Selamat Datang Di Web Ghibli Informatika")
st.write(
    "ngodingseru bersama Virna Nadhiva"
)
st.image("IMG_7321.jpeg")


st.tittle("Aplikasi Sederhana")
st.header("Aplikasi Mengecek Nilai Genap/Ganjil")
angka = st.number_input("Tulis sebuah Angka:", value=0, step=1

if (angka % 2) == 0: 
    st.write(f"{angka} adalah Bilangan Genap")
else:
    st.write(f"{angka} adalah Bulangan Ganjil")
                        

                        

