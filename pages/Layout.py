import streamlit as st
st.code("printf('Hellow World');", language='c')

import streamlit as st

with st.expander("See explanation") :
   st.write(st.session_state.key)
   st.image("https://static.streamlit.io/examples/cat.jpg")
col1, col2, col3 = st.columns(3)

with col1:
   st.header("A cat")
   st.image("https://static.streamlit.io/examples/cat.jpg")

with col2:
   st.header("A dog")
   st.image("https://static.streamlit.io/examples/dog.jpg")

with col3:
   st.header("An owl")
   st.image("https://static.streamlit.io/examples/owl.jpg")