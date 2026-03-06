import streamlit as st
import pandas as pd
import random

st.set_page_config(page_title="학급 자리 배치", layout="wide")

st.title("학급 자리 배치 프로그램")

uploaded_file = st.file_uploader("명렬표 업로드 (반, 번호, 이름)", type=["xlsx","csv"])

if uploaded_file:

    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)

    st.success("파일 업로드 완료")

    classes = sorted(df["반"].unique())
    selected_class = st.selectbox("반 선택", classes)

    class_df = df[df["반"] == selected_class].sort_values("번호")

    st.write("학생 목록")
    st.dataframe(class_df)

    students = list(class_df["이름"])

    rows = st.number_input("행", min_value=1, max_value=10, value=5)
    cols = st.number_input("열", min_value=1, max_value=10, value=6)

    if st.button("랜덤 자리 배치"):

        random.shuffle(students)

        grid = [["" for c in range(cols)] for r in range(rows)]

        index = 0

        for r in range(rows):
            for c in range(cols):

                if index < len(students):
                    grid[r][c] = students[index]
                    index += 1

        seat_df = pd.DataFrame(grid)

        st.subheader("자리 배치 결과")

        st.dataframe(seat_df)
