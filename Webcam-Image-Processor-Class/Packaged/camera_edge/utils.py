# camera_edge/utils.py

import os
from datetime import datetime

def ensure_dir(path):
    os.makedirs(path, exist_ok=True)

def timestamped_filename(prefix="frame", ext="png"):
    now = datetime.now().strftime("%Y%m%d_%H%M%S")
    return f"{prefix}_{now}.{ext}"

