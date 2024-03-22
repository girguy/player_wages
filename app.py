import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    layout="wide",
    page_title="Weekly Player Salaries"
    )

# size of the white space above the title
reduce_header_height_style = """
    <style>
        div.block-container {padding-top:0.4rem;}
    </style>
"""
st.markdown(reduce_header_height_style, unsafe_allow_html=True)

# size of the side bar

st.markdown(
    """
    <style>
    [data-testid="stSidebar"][aria-expanded="true"] > div:first-child {
        width: 250px;
    }
    [data-testid="stSidebar"][aria-expanded="false"] > div:first-child {
        width: 250px;
        margin-left: -250px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


@st.cache_data
def show_power_bi():
    html_string = """<center><iframe title="player_wages" width="100%" height="830" src="https://app.powerbi.com/view?r=eyJrIjoiYTlkYWE2YzYtZDQxNS00YzM1LWJkMDItOTk1YjZjZGU1NGIyIiwidCI6ImJjMDMwMGE0LTJkZmEtNDExYi1iYzFjLWM1NDRlNmJiZWZmMyIsImMiOjl9&pageName=ReportSection24c557b23c6e4e0f4320" frameborder="0" allowFullScreen="true"></iframe></center>"""
    st.markdown(html_string, unsafe_allow_html=True)

show_power_bi()

st.markdown("***")

st.header("Author")

st.markdown("Please feel free to contact me with any issues, comments, or questions.")  # noqa: E501

st.subheader("Guy Girineza")

st.markdown("- Email : guy.girineza@hotmail.com")
st.markdown("- Linkdin : https://www.linkedin.com/in/guy-girineza/")

st.markdown("***")

st.markdown("Developed and Maintained by Guy Girineza")
st.markdown("Most Recently Deposited Entry 2024-")
st.markdown("Copyright (c) 2024 Guy Girineza")
