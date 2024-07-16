import streamlit as st 

if 'key' not in st.session_state :
    st.session_state.key = "NULL"


if st.button("버튼떳다") :
    st.session_state.key = "Hi"
else :
    st.session_state.key = "Bye"
