# CAJAL Computational Mini-Project 16

## Project information

**Title:** Investigating regulatory mechanism of neuronal diversity programming from Single-Cell Perturbation Screening

**Description:** Neuronal diversity in the brain is orchestrated by morphogenetic cues that activate specific transcriptional
programs, which in turns dictate the neuronal subtype identity. In this project, we will analyse a single-cell RNA-
seq (scRNA-seq) dataset from a large-scale combinatorial morphogen perturbation screen to investigate the
regulatory mechanism underlying neuronal fate specification. We will perform analysis of the perturbation
screening data to identify the neuronal subtypes that arose as a result of the morphogenetic patterning,
followed by identification of gene programs and gene regulatory network associated with specific morphogens
combinations. As an optional extension, we will utilise a subset of the perturbation screening data to train a
generative deep learning model to perform in silico combinatorial perturbation screen to evaluate the capability
of such model in recapitulating in vitro screen.

**Data:** Parse scRNA-seq dataset from a large-scale combinatorial morphogen perturbation screen.

## Structure

```
01_scrna_analysis.ipynb                     # Starting point for scRNA-seq analysis
data/
  parse_meta.csv                            # Metadata for scRNA-seq dataset
scripts/                                    # Data download and preparation (reproducible)
  01_download_scrna.sh
  02_prepare_data.py
```

## Setup

```bash
# Clone and set up environment
git clone <this-repo>
cd cajal_neuromics_project
uv venv && uv pip install -e "."

# Download and prepare data
bash scripts/01_download_scrna.sh
uv run python scripts/02_prepare_data.py

# Launch JupyterLab
uv run jupyter lab
```

Requires Python 3.12+ and [uv](https://docs.astral.sh/uv/).
