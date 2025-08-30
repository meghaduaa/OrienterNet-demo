# OrienterNet-demo
Provides simple tools to visualize points, bounding boxes, and manage map tiles using OpenStreetMap data.

## Usage

```python
from maploc.osm.viz import GeoPlotter
plot = GeoPlotter(zoom=16)
plot.points(proj.latlonalt[:2], "red", name="location prior", size=10)
plot.bbox(proj.unproject(bbox), "blue", name="map tile")
plot.fig.show()
