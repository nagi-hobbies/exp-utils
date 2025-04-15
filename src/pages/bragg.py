import numpy as np
import streamlit as st


class BraggPage:
    def __init__(self):
        st.set_page_config(
            layout="wide",
        )

    def run(self):
        st.markdown("# Bragg's Law")

        st.divider()

        st.markdown("## $\lambda$, $2\\theta$ -> $d$")
        cols = st.columns(3, gap="small")

        with cols[0]:
            st.metric("2θ", "2θ[deg]", label_visibility="hidden")
            two_theata = st.number_input(
                "$2\\theta$",
                key="1_two_theata",
                min_value=0.0,
                max_value=180.0,
                value=20.0,
                step=0.01,
                label_visibility="hidden",
            )

        with cols[1]:
            st.metric("λ", "λ[Å]", label_visibility="hidden")
            lumbda = st.number_input(
                "λ",
                key="1_lumbda",
                min_value=0.0,
                max_value=10.0,
                value=2.0,
                step=0.01,
                label_visibility="hidden",
            )

        with cols[2]:
            st.metric("n", "n", label_visibility="hidden")
            n = st.number_input(
                "n",
                key="1_n",
                min_value=1,
                max_value=10,
                value=1,
                step=1,
                label_visibility="hidden",
            )

        theta = two_theata / 2
        d = lumbda / (2 * n * np.sin(theta * np.pi / 180))

        st.metric("d", f"d = {d:.2f} [Å]", label_visibility="hidden")

        st.divider()

        st.markdown("## $d$, $2\\theta$ -> $\lambda$")
        cols = st.columns(3, gap="small")

        with cols[0]:
            st.metric("d", "d[Å]", label_visibility="hidden")
            d = st.number_input(
                "d",
                key="2_d",
                min_value=0.0,
                max_value=10.0,
                value=2.0,
                step=0.01,
                label_visibility="hidden",
            )

        with cols[1]:
            st.metric("2θ", "2θ[deg]", label_visibility="hidden")
            two_theata = st.number_input(
                "$2\\theta$",
                key="2_two_theata",
                min_value=0.0,
                max_value=180.0,
                value=20.0,
                step=0.01,
                label_visibility="hidden",
            )

        with cols[2]:
            st.metric("n", "n", label_visibility="hidden")
            n = st.number_input(
                "n",
                key="2_n",
                min_value=1,
                max_value=10,
                value=1,
                step=1,
                label_visibility="hidden",
            )

        theta = two_theata / 2
        lumbda = d / (2 * n * np.sin(theta * np.pi / 180))

        st.metric("λ", f"λ = {lumbda:.2f} [Å]", label_visibility="hidden")


if __name__ == "__main__":
    BraggPage().run()
