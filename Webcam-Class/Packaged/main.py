# main.py (outside the package folder)
from camera_edge.detector import CameraEdgeDetector
from camera_edge.tools.file_tools import list_images
from camera_edge import __version__

import camera_edge.tools as tools
print(dir(tools)) 


if __name__ == "__main__":

    print(f"CameraEdge version: {__version__}")
    CameraEdgeDetector().run()

    # Now that the UI has closed... llist the images captured during this session
    images = list_images("snapshots", ext=".png")
    print("\nImages captured up through this session:")
    for img in images:
        print("-", img)
