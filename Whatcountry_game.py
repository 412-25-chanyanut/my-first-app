import streamlit as st

st.title("🌎 Whatcountry_game")

# 1. กำหนดค่าเริ่มต้น
for i in range(1, 11):
    if f"ans{i}_val" not in st.session_state:
        st.session_state[f"ans{i}_val"] = ""


# 2. ฟังก์ชันเริ่มเกมใหม่
def reset_game():
    for i in range(1, 11):
        st.session_state[f"ans{i}_val"] = ""

    st.session_state.is_ended = False


# ----------------------------------------------------
# 3. ฟังก์ชันแสดงผลคะแนน
# ----------------------------------------------------
@st.dialog("📊 สรุปผลการเล่นเกม")
def show_result_dialog(answers):

    st.balloons()
    score = 0

    # คำตอบที่ถูกต้อง
    correct_answers = [
        "Japan",
        "Korea",
        "Spain",
        "Brazil",
        "China",
        "France",
        "Canada",
        "Italy",
        "Philippines",
        "Turkey"
    ]

    # ตรวจคำตอบทั้ง 10 ข้อ
    for i in range(10):

        user_answer = answers[i].strip().lower()
        correct_answer = correct_answers[i].lower()

        if user_answer == correct_answer:

            st.success(
                f"✅ ข้อ {i+1}: ถูกต้อง\n\n"
                f"คำตอบของคุณ: {answers[i]}\n\n"
                f"คำตอบที่ถูกต้อง: {correct_answers[i]}"
            )

            score += 1

        else:

            st.error(
                f"❌ ข้อ {i+1}: ผิด\n\n"
                f"คำตอบของคุณ: {answers[i] if answers[i] else 'ไม่ได้ตอบ'}\n\n"
                f"คำตอบที่ถูกต้อง: {correct_answers[i]}"
            )

    # แสดงคะแนน
    st.info(f"🏆 ได้คะแนนรวม: {score}/10 คะแนน")

    # แสดงผลตามช่วงคะแนน
    if score <= 3:
        st.error("🚨 Try Again")

    elif score <= 6:
        st.warning("⭐ Good Job")

    else:
        st.success("🎉 You Pass")


# ----------------------------------------------------
# 4. ปุ่มเริ่มเกมใหม่
# ----------------------------------------------------
st.button("🎮 เริ่มเกมใหม่", on_click=reset_game)

st.divider()


# ----------------------------------------------------
# 5. คำถามภาษาไทย
# ----------------------------------------------------
questions = [
    "ข้อ 1: ญี่ปุ่น ",
    "ข้อ 2: เกาหลี ",
    "ข้อ 3: สเปน ",
    "ข้อ 4: บราซิล ",
    "ข้อ 5: จีน ",
    "ข้อ 6: ฝรั่งเศส ",
    "ข้อ 7: แคนาดา ",
    "ข้อ 8: อิตาลี ",
    "ข้อ 9: ฟิลิปปินส์ ",
    "ข้อ 10: ตุรกี "
]


# ----------------------------------------------------
# 6. ช่องกรอกคำตอบ
# ----------------------------------------------------
answers = []

for i in range(10):

    answer = st.text_input(
        questions[i],
        value=st.session_state[f"ans{i+1}_val"],
        key=f"input_{i+1}"
    )

    st.session_state[f"ans{i+1}_val"] = answer
    answers.append(answer)


# ----------------------------------------------------
# 7. ปุ่มส่งคำตอบ
# ----------------------------------------------------
if st.button("📥 ส่งคำตอบ"):

    st.session_state.is_ended = True

    show_result_dialog(answers)
