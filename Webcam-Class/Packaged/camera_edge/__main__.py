# Add __main__.py (optional)
# If you want to run the package directly using `python -m camera_edge`, you can create a `__main__.py` file inside the `camera_edge` directory. This file will serve as the entry point for the package when run as a module.
# This is useful if you want to run the package without specifying the script name.
# The `__main__.py` file should contain the same code as the main script, but it will be executed when you run the package.
# This allows you to run the package directly using `python -m camera_edge`.

# camera_edge/__main__.py
from camera_edge.detector import CameraEdgeDetector

if __name__ == "__main__":
    CameraEdgeDetector().run()
