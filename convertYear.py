import streamlit as st
st.title ("แอปพลิเคชั่นเเปลงปี พ.ศ. เป็น ค.ศ.")

bh_year=st.number_input("กรอกปี พ.ศ. ที่ต้องการเปลี่ยนเเปลง",value=2569)
ce_year=bh_year-543
st.header(f"ปี ค.ศ. คือ :{ce_year}")
