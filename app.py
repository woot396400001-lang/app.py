import streamlit as st

st.title("🏡 เครื่องมือแปลงหน่วยที่ดิน")

i = st.number_input("เลือกขนาด (ไร่)", min_value=0)
b = st.selectbox("เลือกหน่วยที่ต้องการแปลง", ["ตารางวา", "งาน"])

if st.button("คำนวณ"):
    if b == "ตารางวา":
        st.success(f"{i} ไร่ เท่ากับ {i * 400} ตารางวา")
    elif b == "งาน":
        st.success(f"{i} ไร่ เท่ากับ {i * 4} งาน")
