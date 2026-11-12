
import streamlit as st
import pandas as pd
import numpy as np
import os
import plotly.express as px

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="NeuroGene Analytics",
    page_icon="🧠",
    layout="wide"
)

BASE = os.path.dirname(os.path.abspath(__file__))
RESULTS = BASE

st.title("🧠 NeuroGene Analytics")
st.subheader(
    "Exploratory Brain Gene Expression Analysis"
)
st.caption(
    "Alzheimer's Disease vs Control | GEO: GSE48350"
)

# ---------------- LOAD DATA ----------------
@st.cache_data
def load_data():
    de = pd.read_csv(
        os.path.join(RESULTS,
                     "differential_expression_results.csv")
    )

    genes = pd.read_csv(
        os.path.join(RESULTS,
                     "annotated_top20_genes.csv")
    )

    go = pd.read_csv(
        os.path.join(RESULTS,
                     "GO_summary.csv")
    )

    go_details = pd.read_csv(
        os.path.join(RESULTS,
                     "top20_GO_annotations.csv")
    )

    audit = pd.read_csv(
        os.path.join(RESULTS,
                     "modeling_feasibility_audit.csv")
    )

    return de, genes, go, go_details, audit


try:
    de, genes, go, go_details, audit = load_data()
except Exception as error:
    st.error(f"Unable to load project files: {error}")
    st.stop()

# ---------------- SIDEBAR ----------------
st.sidebar.title("Navigation")

section = st.sidebar.radio(
    "Choose a section",
    [
        "Dashboard Overview",
        "Exploratory Analysis",
        "Visualizations",
        "Gene Annotation",
        "Modelling Assessment"
    ]
)

# ---------------- OVERVIEW ----------------
if section == "Dashboard Overview":

    st.header("Project Overview")

    c1, c2, c3 = st.columns(3)

    c1.metric("Total Probes", f"{len(de):,}")
    c2.metric("Significant Probes",
              f"{(de['Adjusted_P_Value'] < 0.05).sum():,}")
    c3.metric("Annotated Top Probes",
              f"{genes['Gene symbol'].notna().sum()} / {len(genes)}")

    st.markdown("### Dataset Information")

    st.write("""
    - **GEO Accession:** GSE48350
    - **Platform:** GPL570
    - **Tissue:** Hippocampus
    - **Comparison:** 19 AD and 21 Control samples
    - **Analysis:** Exploratory gene expression analysis
    """)

    st.info(
        "This application is intended for educational "
        "and research exploration, not clinical diagnosis."
    )

    st.markdown("### Analysis Workflow")

    st.write("""
    Dataset → Quality Assessment → PCA → Statistical Testing
    → Probe Annotation → GO Summary → Scientific Assessment
    """)

# ---------------- EXPLORATORY ANALYSIS ----------------
elif section == "Exploratory Analysis":

    st.header("Exploratory Differential Expression")

    threshold = st.slider(
        "Adjusted p-value threshold",
        min_value=0.001,
        max_value=0.10,
        value=0.05,
        step=0.001
    )

    significant = de[
        de["Adjusted_P_Value"] < threshold
    ].copy()

    st.metric("Probes below selected threshold",
              f"{len(significant):,}")

    direction = st.selectbox(
        "Expression direction",
        [
            "All",
            "Higher in AD",
            "Higher in Control"
        ]
    )

    if direction == "Higher in AD":
        significant = significant[
            significant["Mean_Difference"] > 0
        ]

    elif direction == "Higher in Control":
        significant = significant[
            significant["Mean_Difference"] < 0
        ]

    st.dataframe(
        significant.sort_values("Adjusted_P_Value"),
        use_container_width=True
    )

    st.download_button(
        "Download filtered results",
        significant.to_csv(index=False),
        file_name="filtered_probe_results.csv",
        mime="text/csv"
    )

# ---------------- VISUALIZATIONS ----------------
elif section == "Visualizations":

    st.header("Gene Expression Visualizations")

    plot_choice = st.selectbox(
        "Select visualization",
        [
            "Volcano Plot",
            "PCA Plot",
            "Top 20 Probe Heatmap"
        ]
    )

    if plot_choice == "Volcano Plot":

        plot_data = de.copy()

        plot_data["Minus_Log10_FDR"] = -np.log10(
            plot_data["Adjusted_P_Value"].clip(
                lower=1e-300
            )
        )

        plot_data["Group"] = np.where(
            plot_data["Adjusted_P_Value"] < 0.05,
            "FDR < 0.05",
            "Not significant"
        )

        fig = px.scatter(
            plot_data,
            x="Mean_Difference",
            y="Minus_Log10_FDR",
            color="Group",
            hover_data=["Probe_ID"],
            title="Exploratory Volcano Plot"
        )

        st.plotly_chart(fig, use_container_width=True)

    elif plot_choice == "PCA Plot":

        image_path = os.path.join(
            RESULTS, "PCA_plot.png"
        )

        if os.path.exists(image_path):
            st.image(image_path, use_container_width=True)
        else:
            st.warning("PCA image not found.")

    else:

        image_path = os.path.join(
            RESULTS, "top20_gene_heatmap.png"
        )

        if os.path.exists(image_path):
            st.image(image_path, use_container_width=True)
        else:
            st.warning("Heatmap image not found.")

# ---------------- GENE ANNOTATION ----------------
elif section == "Gene Annotation":

    st.header("Probe and Gene Annotation")

    st.write(
        "Top 20 probes selected from the exploratory "
        "statistical comparison."
    )

    st.dataframe(
        genes,
        use_container_width=True
    )

    st.markdown("### GO Functional Summary")

    st.dataframe(
        go,
        use_container_width=True
    )

    st.markdown("### Individual GO Annotations")

    st.dataframe(
        go_details,
        use_container_width=True
    )

# ---------------- MODELLING ASSESSMENT ----------------
elif section == "Modelling Assessment":

    st.header("Data Science Modelling Feasibility")

    st.warning(
        "A valid AD prediction classifier was not trained "
        "because disease status is perfectly confounded "
        "with accession group in the current comparison."
    )

    st.markdown("### Accession Group vs Disease Status")

    st.dataframe(
        audit,
        use_container_width=True
    )

    st.markdown("### Scientific Decision")

    st.write("""
    - No supervised AD classifier is reported.
    - Random train-test splitting cannot resolve this confounding.
    - Age and sex matching do not remove accession-group confounding.
    - Independent validation data are required before prediction.
    """)

    st.markdown("### Future Machine Learning Plan")

    st.write("""
    1. Obtain a suitable independent dataset.
    2. Assess platform and cohort compatibility.
    3. Prevent subject-level data leakage.
    4. Perform feature selection within training folds.
    5. Evaluate regularized logistic regression, Random Forest
       and Support Vector Machine.
    6. Use external validation.
    """)

    st.info(
        "The application is a research exploration tool, "
        "not an Alzheimer's disease diagnostic system."
    )

# ---------------- FOOTER ----------------
st.divider()

st.caption(
    "NeuroGene Analytics | Python for Bioinformatics Project "
    "| Educational and research use only"
)
