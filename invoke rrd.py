import rerun as rr
import os
from http.server import SimpleHTTPRequestHandler, HTTPServer

# Initialize Rerun
rr.init("NuScenes Demo")

# Load the RRD file
rrd_path = "C://Users//XED1COB//OneDrive - Bosch Group//Rerun//NuScenes//nuscenes_dataset//nuscenes.rrd"

rr.load_rrd(rrd_path)

# Start the HTTP server
PORT = 8000
Handler = SimpleHTTPRequestHandler
httpd = HTTPServer(("localhost", PORT), Handler)

print(f"Serving Rerun visualization at http://localhost:{PORT}")
httpd.serve_forever()
