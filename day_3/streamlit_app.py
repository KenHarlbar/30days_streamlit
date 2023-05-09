import streamlit as st

st.header('st.button')

st.title('Radio Buttons, Checkboxes, and Buttons')
page_names = ['Checkbox', 'Button']
page = st.radio('Naviagtion', page_names)
st.subheader('**The variable \'page\' returns:** ', page)


if page == 'Checkbox':
    st.subheader('Welcome to the Checkbox page')
    st.write('Nice to meet you, :wave:')
    check = st.checkbox('Check me out')
    st.write('State of the checkbox:', check)
    if check:
        st.write(':smile:'*12)
else:
    st.subheader('Welcome to the Button page')
    st.write('Nice to meet you :wave:')
    result = st.button('Click me')
    st.write('State of the button:', result)
    if result:
        st.write(':smile:')