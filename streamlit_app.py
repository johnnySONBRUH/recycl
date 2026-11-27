import streamlit as st

pages = {
    'Main': [
        st.Page('classifier.py', title='Classifier', icon='♻️'),
        st.Page('about.py', title='About', icon='ℹ️'),
    ],
}

pg = st.navigation(pages)
pg.run()
