#!/bin/bash
# Download scRNA-seq data from GEO (GSE249572)
# Total download: ~1.1 GB, ~4.4 GB uncompressed

set -e

DATA_DIR="data"
mkdir -p "$DATA_DIR"

echo "Downloading scRNA-seq data from GEO GSE249572..."
wget -q --show-progress -O "$DATA_DIR/GSE249572_RAW.tar" \
    "https://www.ncbi.nlm.nih.gov/geo/download/?acc=GSE249572&format=file&id=1,2"

echo "Extracting..."
cd "$DATA_DIR"
tar xf GSE249572_RAW.tar
rm GSE249572_RAW.tar
gunzip *.gz

echo ""
echo "Done. Files:"
ls -lh *.h5ad | wc -l
echo "samples downloaded"
