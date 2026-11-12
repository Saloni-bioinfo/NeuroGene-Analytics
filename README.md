# NeuroGene Analytics

## Exploratory Brain Gene Expression Analysis of Alzheimer's Disease

A Python-based bioinformatics and data science project exploring gene-expression patterns in human hippocampus samples.

**Important:** This is an exploratory research application, not a validated diagnostic or classification model.

## Dataset
- GEO accession: GSE48350
- Platform: GPL570 (Affymetrix Human Genome U133 Plus 2.0)
- Original dataset: 253 samples across four brain regions.
- Hippocampus: 62 samples (43 Control, 19 AD).
- Age-restricted comparison: 40 samples (21 Control, 19 AD).

Dataset: https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE48350

## Technologies
- Python, Pandas, NumPy, SciPy
- Scikit-learn
- Matplotlib, Seaborn, Plotly
- Streamlit and Jupyter Notebook

## Analysis Workflow
1. Dataset acquisition and metadata extraction.
2. Expression matrix preparation and hippocampus selection.
3. Data quality assessment.
4. PCA and confounding investigation.
5. Differential expression using Welch's t-test.
6. Benjamini-Hochberg correction.
7. Probe annotation and GO summaries.
8. PCA, volcano plot and heatmap visualization.
9. Machine-learning feasibility assessment.
10. Interactive Streamlit dashboard.

## Key Findings
- 54,675 probes evaluated.
- 20,353 probes had adjusted p-values below 0.05 in the age-restricted comparison.
- Gene annotations and GO term frequencies summarized.

## Scientific Limitations
Disease status is perfectly confounded with accession group:

| Accession | AD | Control |
|---|---:|---:|
| GSM1176 | 19 | 0 |
| GSM300 | 0 | 21 |

Disease-related differences cannot be separated from possible cohort, accession, source, or processing differences.
No machine-learning classifier was trained or reported.
GO term counts are descriptive annotation frequencies, not statistical enrichment.
Expression differences are not interpreted as fold changes because the expression scale has not been conclusively established.

## Streamlit Dashboard
Sections: Dashboard Overview, Exploratory Analysis, Visualizations, Gene Annotation, and Modelling Assessment.

Install dependencies: `pip install -r requirements.txt`

Run locally: `streamlit run app.py`

Download the GEO expression matrix and GPL570 annotation into data/raw/ and prepare the required result files before launching.

## Project Structure
- app.py
- requirements.txt
- notebooks/NeuroGene_Analytics.ipynb
- data/raw/ and data/processed/
- results/
- src/

**Notebook note:** The included notebook currently documents the project workflow and findings. It is not yet a complete executable reproduction of all analysis steps.

## Future Improvements
- Build a fully reproducible analysis notebook.
- Validate findings using independent brain transcriptomics datasets.
- Investigate cohort and processing effects.
- Perform statistical pathway enrichment.
- Develop and externally validate predictive models using suitable independent data.

## References
1. NCBI GEO GSE48350: https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE48350
2. NCBI GPL570: https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GPL570

**Project Focus:** Bioinformatics | Python | Data Science | Transcriptomics | Exploratory Analysis
