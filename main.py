import streamlit as st
import time

st.title("Streamlit 超入門")

st.write("Interactive Widgets")

text = st.sidebar.text_input("あなたの趣味を教えてください。")
"あなたの趣味: ", text
condition = st.sidebar.slider("あなたの今の調子は？", 0, 100, 50)
"コンディション: ", condition

# if st.checkbox("Show Image"):
#     img = Image.open("sample.png")
#     st.image(img, caption = "Trend chart", use_column_width=True)

# df = pd.DataFrame(
#     np.random.rand(100,2) / [50,50] + [35.69, 139.70],
#     columns=["lat", "lon"]
# )

# st.map(df)