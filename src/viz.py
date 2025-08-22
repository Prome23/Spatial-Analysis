# src/viz.py
import folium, geopandas as gpd

def choropleth_map(gdf: gpd.GeoDataFrame, value_col: str, out_html: str):
    m = folium.Map(location=[37.5,-119], zoom_start=6, tiles="cartodbpositron")
    folium.Choropleth(
        gdf.to_crs(4326).to_json(),
        data=gdf, columns=[gdf.index.name or 'index', value_col],
        key_on=f'feature.properties.{gdf.index.name or "index"}',
        legend_name=value_col,
        fill_opacity=0.8, line_opacity=0.2
    ).add_to(m)
    m.save(out_html)
    return out_html
