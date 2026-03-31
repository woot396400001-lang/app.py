น้อนวุ้ดด streamlit as st

# ปรับหน้าตาเว็บให้ดูดี
st.set_page_config(page_title="แปลงหน่วยที่ดิน", page_icon="🏡")

st.title("🏡 เครื่องมือแปลงหน่วยที่ดิน")
st.write("สร้างโดย Wut (น้อนวุ้ดด)")

# ส่วนรับข้อมูล
i = st.number_input("ใส่จำนวนพื้นที่ (ไร่)", min_value=0, value=1)
b = st.radiต้องการแปลงเป็นหน่วยอะไระไร?", ["ตารางวา", "งาน"])

# ส่วนการคำนวณและแสดงผล
if b == "ตารางวา":
    result = i * 400
    st.success(f"✅ {i} ไร่ เท่ากับ {result:,.0f} ตารางวา")
elif b == "งาน":
    result = i * 4
    st.success(f"✅ {i} ไร่ เท่ากับ {result:,.0f} งาน")

st.divider()
st.info("ทริค: 1 ไร่ = 4 งาน = 400 ตารางวา")
