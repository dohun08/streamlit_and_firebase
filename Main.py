import streamlit as st
import time
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

st.title("streamlit를 활용한 웹 개발")
st.write("streamlit를 이용한 웹 개발 기술들을 정리해보자(시간있을때..)")

ex = "이렇게 단어들이 하나하나 계속 시간에 맞춰서 출력이 됩니다. 오지게 신기하네 거의 뭐 챗 GPT ㅋㅋㅋ"
def stream_data() :
    for word in ex.split(" ") :
       yield word + " " 
       time.sleep(0.08)

if st.button("눌러봐봐"):
    st.write_stream(stream_data)


st.write("코드 작성하기도 가능하다구 노션 만들기 이지할지도?")
code = '''int hello(){
printf("hello");
return 0;
}'''
st.code(code, language='c')


st.markdown(":red[빨강] :orange[오렌쥐] :yellow[노랑]:rainbow[무지개나리어카센터널뛰기차표지판떼기술]")


st.text_input(label="id" "id")
st.text_input(label="pw" "pw")
st.button("제출")


# Fetch the service account key JSON file contents
cred = credentials.Certificate('secrets.json')

# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://test-feedd-default-rtdb.firebaseio.com/'
})

# As an admin, the app has access to read and write all data, regradless of Security Rules
ref = db.reference()
ref.set({"id" : "도훈", "pw" : "1234"})



