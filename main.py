import streamlit as st
st.title('CampusX')
col1,col2 = st.columns(2)

with col1:
    st.image('campusxlogo.jpeg')
with col2:
    st.write(""" Hello, I'm Nitish Singh, the founder of CampusX,
    your online gateway into the world of data science! At CampusX,
    we believe that quality education is a universal right, not a privilege. 
    We aim to provide TOP TIER data education to everyone with a  passion to learn. 
    On our YouTube channel, we provide high quality free content covering everything
    related to data. Apart from this, we also provide paid mentorship programs 
    for students where enrolled students get the benefit of personalized guidance 
    through live and recorded video lectures, daily skill-building activities,
    hands-on projects, assignments, and interactions with industry experts. 
    Leveraging my 10 years of teaching experience in the data industry, 
    primarily in Machine/Deep Learning, I bring real-life industry experiences 
    directly to your learning journey.
    """)
    # AFter 1st commit

    st.header("Courses offered")
    st.subheader('Data Science and Machine learning')
    st.subheader('Data Analysis')
    st.subheader('Pyhton')
    st.subheader('SQL')
    st.subheader('DSA')

    st.sidebar.title('Menu')
    st.sidebar.markdown("""
- Home
- About
- Contact
- Career
- Login

""")