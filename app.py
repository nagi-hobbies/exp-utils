import streamlit as st

from src.pages.bragg import BraggPage

bragg_page = BraggPage()

pg = st.navigation(
    {
        "": [
            st.Page(
                bragg_page.run,
                title="bragg utils",
                icon=":material/add_circle:",
                url_path="bragg",
            )
        ],
    }
)
pg.run()
