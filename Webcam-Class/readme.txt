Webcam-Class
├── Packaged
│   ├── camera_edge
│   │   ├── __init__.py
│   │   ├── __main__.py
│   │   ├── detector.py
│   │   ├── tools
│   │   │   ├── __init__.py
│   │   │   └── file_tools.py
│   │   └── utils.py
│   ├── main.py
│   └── readme.txt
└── Standalones
    ├── Basic
    │   └── main.py
    ├── Moderate
    │   └── main.py
    ├── Pipeline
    │   └── main.py
    └── readme.txt


Standalones Folder provides three simple illustrations of building an object oriented solution for processing webcam video. 
Each one is comprised of a single file having both the main, and an increasingly complex imageprocessor class defined.  Starting from the most basic, which does not accept arguments, the the more complex that allows users to string along and 
build their image processing Pipeline

The Packaged Folder continues builds upon the Standalones' Image Processor Pipeline.  It illustrates a package with helper function that can be imported into any project.