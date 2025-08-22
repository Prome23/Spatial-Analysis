# Environmental Justice & Power Plants: Spatial Risk Analysis (Work Sample)

This repo turns a graduate course paper into a **reproducible work sample** with Python-only tooling (no GeoDa), interactive maps, and a clean structure for reviewers.

## What this is
- **Goal:** Explore how tract-level cancer risk (EPA AirToxScreen 2020) relates to power-plant siting and sociodemographics in California and Pennsylvania using **spatial statistics** (Local Moran's I) and **spatial lag models**.
- **Stack:** `geopandas`, `libpysal/esda/spreg`, `mapclassify`, `matplotlib`, `folium`, `pandas`, `numpy`.
- **Outputs:** Static figures (PNG/SVG) and **interactive maps** (served via GitHub Pages).

> 🔎 *This repo replaces prior GeoDa steps with equivalent **PySAL** code so anyone can reproduce the analysis.*

---

## Quickstart (GitHub Desktop)

1) **Download/Unzip** this repo locally and open **GitHub Desktop**.
2) Click **File → Add local repository...** and select the folder.
3) Click **Publish repository** to push it to your GitHub account.
4) Open the folder in your editor (VS Code, etc.) to run code/notebooks.

### Python environment
```bash
# using conda
conda env create -f environment.yml
conda activate ej-risk

# or plain pip
pip install -r requirements.txt
```

### Run notebooks
- Open `notebooks/02_eda_mapping.ipynb` and `03_spatial_lag_models.ipynb` in Jupyter/VS Code.
- Results and figures will be saved under `figures/` and `docs/maps/`.

---

## GitHub Pages (to host interactive maps)
1) Commit and push your first map HTML into `docs/maps/` (e.g., `docs/maps/ca_cancer_risk.html`).
2) On GitHub: **Settings → Pages → Build and deployment → Branch:** `main` and **Folder:** `/docs` → **Save**.
3) Your site will be available at `https://<your-user>.github.io/<repo>/` (maps under `/maps/...`).

---

## Repo layout
```
.
├─ data/
│  ├─ raw/          # keep raw sources out of Git (large files); add fetch scripts instead
│  └─ processed/    # cleaned & joined data for modeling
├─ docs/            # GitHub Pages source
│  └─ maps/         # interactive folium maps
├─ figures/         # static images for the README/paper
├─ maps/            # working maps (optional)
├─ notebooks/
│  ├─ 01_data_acquire.ipynb
│  ├─ 02_eda_mapping.ipynb
│  └─ 03_spatial_lag_models.ipynb
├─ paper/           # polished PDF/markdown version of the write-up
├─ src/             # reusable utilities
│  ├─ io_fetch.py
│  ├─ features.py
│  ├─ weights.py
│  ├─ models.py
│  └─ viz.py
├─ environment.yml  # conda env (recommended)
├─ requirements.txt # pip alternative
├─ .gitignore
└─ README.md
```

---

## Data sources (add links + retrieval dates)
| Dataset | Source | Notes |
|---|---|---|
| AirToxScreen 2020 (cancer risk) | EPA | tract-level estimates |
| ACS Demographics | Census API | race, income, rent burden, public assistance |
| EIA Plant Points | EIA | generation type; add emissions intensity if available |
| State Screens (e.g., CalEnviroScreen) | OEHHA | supplemental indicators |
| TIGER/Line Tracts | Census | geometries for joins |

---

## Replacing GeoDa with PySAL: TL;DR
- **Weights:** `libpysal.weights.Queen/ KNN`
- **Spatial autocorrelation:** `esda.Moran_Local`
- **Spatial regression:** `spreg.ML_Lag` / `spreg.ML_Error`
- **Mapping:** `splot` for statics; `folium` for interactive

See `convert_geoda_to_python.md` and `src/weights.py`, `src/models.py` for working examples.

---

## License
Choose a license (e.g., MIT) if you intend others to reuse code. Edit `LICENSE` accordingly.

## Citation
If you cite the paper, please include a link to this repository and the final write-up in `/paper`.
