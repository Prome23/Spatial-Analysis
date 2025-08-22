# Converting GeoDa steps to Python (PySAL)

This guide maps common **GeoDa** operations to **Python** so the workflow is fully reproducible.

## Weights (Queen / KNN)
```python
from libpysal.weights import Queen, KNN
w = Queen.from_dataframe(gdf)  # or KNN.from_dataframe(gdf, k=8)
w.transform = "R"  # row-standardize
```

## Local Moran's I (LISA)
```python
from esda import Moran_Local
from splot.esda import lisa_cluster
y = gdf["cancer_risk"].values
lisa = Moran_Local(y, w, permutations=999)
gdf["lisa_q"] = lisa.q
gdf["lisa_p"] = lisa.p_sim
ax = lisa_cluster(lisa, gdf, p=0.05)
```

## Spatial lag regression
```python
from spreg import ML_Lag
X = gdf[["rent_burden","cash_assist","log_income","pct_black",
         "pct_higher_ed","count_clean","count_fossil"]].to_numpy()
y = gdf[["cancer_risk"]].to_numpy()
slag = ML_Lag(y, X, w, name_y="cancer_risk",
              name_x=["rent_burden","cash_assist","log_income","pct_black",
                      "pct_higher_ed","count_clean","count_fossil"])
print(slag.summary)
```

## Interactive maps (Folium)
```python
import folium
m = folium.Map(location=[37.5,-119], zoom_start=6, tiles="cartodbpositron")
folium.Choropleth(
  gdf.to_crs(4326).to_json(),
  data=gdf, columns=["GEOID","cancer_risk"],
  key_on="feature.properties.GEOID",
  legend_name="Cancer risk (per million)",
  fill_opacity=0.8, line_opacity=0.2,
).add_to(m)
m.save("docs/maps/ca_cancer_risk.html")
```
