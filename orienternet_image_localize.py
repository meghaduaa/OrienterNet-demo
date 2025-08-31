#@markdown Select one of the 4 example images or upload your own
image_name = 'upload!' #@param ["zurich_1", "vancouver_1", "vancouver_2", "vancouver_3", "upload!"]

#@markdown OrienterNet needs a coarse location (within ~100-200 meters) to query OpenStreetMap for the right area. 
address = "Connaught Place, New Delhi, India" #@param {type:"string"}

#@markdown The search radius around the location prior.
tile_size_meters = "64" #@param [64, 128, 256, 512]

from google.colab import files

if not address:
  address = None

if image_name == "upload!":
  uploaded = files.upload()
  for fn in uploaded.keys():
      image_path = fn
  if not address:
      address = "India Gate, New Delhi, India"  
else:
  image_path = f"assets/query_{image_name}.JPG"
  if image_name == "zurich_1":
    address = "ETH CAB Zurich"
  elif image_name == "vancouver_1":
    address = "Vancouver Waterfront Station"
  else:
    address = None

print(f"Using image {image_path} with location prior '{address}'")

# Read input image
image, camera, gravity, proj, bbox = demo.read_input_image(
    image_path,
    prior_address=address,  
)

bbox = bbox + 10  

# Query map tiles
from maploc.osm.tiling import TileManager
tiler = TileManager.from_bbox(proj, bbox, demo.config.data.pixel_per_meter)
canvas = tiler.query(bbox)

# Visualize only once
from maploc.osm.viz import GeoPlotter
plot = GeoPlotter(zoom=16)
plot.points(proj.latlonalt[:2], "red", name="location prior", size=10)
plot.bbox(proj.unproject(bbox), "blue", name="map tile")
plot.fig.show()
