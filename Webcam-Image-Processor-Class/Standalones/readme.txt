Standalones
├── Basic
│   └── main.py
├── Exclusive
│   └── main.py
├── Pipeline
│   └── main.py
├── readme.txt
└── tree.py

Leveraging Python's object oriented capacities, this folder provide three illustrations of building a simple video image processing tool.

Each one is comprised of a single file having both the main, and imageprocessor class defined.

The simplest is the Basic.  Everythig is hardcoded.  The class reads from the webcam (0), creates a local folder to save video frames, and listens for user interaction to save the video frames or close the video UI.

Next is the Moderate.  Arguments are accepted for Camera Index, Output Folder, and one of three image processor functions defind (gray, blur, canny)

Finally, there is the Pipeline.  The pipeline method dynamically builds a sequence of image-processing operations based on user-defined step names (e.g. "gray", "blur", "canny"). It maps these names to the corresponding processing functions, allowing flexible control over how each frame is transformed.

This lets users customize the image-processing flow through a simple list, such as: ["gray", "blur", "canny"].  

Advantages of the Pipeline Method:
    Modular: Easily add or remove steps.
    User-configurable: Steps can be defined via CLI or config files.
    eadable: Logic stays clean and centralized in one method.