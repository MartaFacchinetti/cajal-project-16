from pathlib import Path

import anndata as ad
import pandas as pd

DATA_DIR = Path("data")
OUTPUT_NAME = "ngn2_scrna_raw.h5ad"

# Required when obs/var contain pandas StringArray columns.
ad.settings.allow_write_nullable_strings = True
pd.options.future.infer_string = False

output_path = DATA_DIR / OUTPUT_NAME
input_paths = sorted(
    p for p in DATA_DIR.glob("GSM*.h5ad") if p.name != OUTPUT_NAME
)

adatas = [ad.read_h5ad(path) for path in input_paths]
keys = [path.stem for path in input_paths]
combined = ad.concat(adatas)

plate_prefix = combined.obs["plateID"].astype(str).str.extract(r"(p[12])", expand=False)
combined.obs["parse_id"] = plate_prefix + "_" + combined.obs["bc1_well"].astype(str)

parse_meta_path = DATA_DIR / "parse_meta.csv"
parse_meta = pd.read_csv(parse_meta_path)

combined.obs = combined.obs.join(
    parse_meta.set_index("parse_id"),
    on="parse_id",
    how="left",
    validate="m:1",
)

combined.write_h5ad(output_path)

print(f"Wrote combined dataset to {output_path}")
print(f"Input files: {[p.name for p in input_paths]}")
print(f"Combined shape: {combined.shape}")
