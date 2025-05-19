import cv2
import os
import argparse

# This script captures images from a webcam and processes them using a pipeline of image processing functions.
# The pipeline is user-defined and can include steps like grayscale conversion, blurring, edge detection, etc.
# The processed images can be saved to a specified directory.
# The script uses OpenCV for image processing and capturing images from the webcam.
# The script can be run from the command line with options to specify the output directory, camera index, and processing steps.
class WebcamImageProcessor:
    def __init__(self, save_dir="snapshots", camera_index=0, step_names=["gray", "canny"]):

        # Initialize the webcam and other parameters
        self.camera_index = camera_index
        self.cap = cv2.VideoCapture(camera_index)  # 0 = default webcam
        self.save_dir = save_dir

        # initialize the pipeline
        self.step_names = step_names
        self.pipeline = self.build_pipeline(step_names)

        # create the directory to save snapshots
        os.makedirs(save_dir, exist_ok=True)
        self.saved_frame_count = 0

    
    # Define the processing steps
    # These functions will be used to process the frames
    def do_gray(self, frame):
        return cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    def do_blur(self, frame, ksize=(5, 5)):
        return cv2.GaussianBlur(frame, ksize, 0)
    
    def do_negate(self, frame):
        return cv2.bitwise_not(frame)
    
    def do_resize(self, frame, scale=0.5):
        height, width = frame.shape[:2]
        return cv2.resize(frame, (int(width * scale), int(height * scale)))
    
    def do_threshold(self, frame, thresh=127):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        _, binary = cv2.threshold(gray, thresh, 255, cv2.THRESH_BINARY)
        return binary
    
    def do_dilate(self, frame, kernel_size=(3, 3), iterations=1):
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, kernel_size)
        return cv2.dilate(frame, kernel, iterations=iterations)
    
    def do_erode(self, frame, kernel_size=(3, 3), iterations=1):
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, kernel_size)
        return cv2.erode(frame, kernel, iterations=iterations)
    
    def do_canny(self, frame, threshold1=100, threshold2=200):
        edges = cv2.Canny(frame, threshold1, threshold2)
        return edges
    
    
    # Create a hardcoded pipeline
    # This function will create a pipeline with the following steps:
    # This is really just for example, testing, and illustration of what the pipeline looks like.
    def make_hardcoded_pipeline(self):
        pipeline = [
            self.do_gray,
            lambda f: self.do_blur(f, (3, 3)),
            lambda f: self.do_canny(f, 50, 150)
        ]
        return pipeline
    
    # Create a user-defined pipeline based on the provided step names
    # This function will create a pipeline based on the step names provided
    def build_pipeline(self, step_names):

        # Define a mapping of step names to functions
        step_map = {
            "gray": self.do_gray,
            "blur": lambda f: self.do_blur(f, (3, 3)),
            "canny": lambda f: self.do_canny(f, 50, 150),
            "negate": self.do_negate,
            "resize": lambda f: self.do_resize(f, 0.5),
            "threshold": self.do_threshold,
            "dilate": lambda f: self.do_dilate(f, (3, 3)),
            "erode": lambda f: self.do_erode(f, (3, 3)),
        }

        # Create the pipeline based on the step names
        # The pipeline is a list of functions that will be applied to the frame
        pipeline = []
        for name in step_names:
            if name not in step_map:
                raise ValueError(f"Unknown step: '{name}'")
            pipeline.append(step_map[name])
        
        return pipeline
    
    # Apply the pipeline to a frame
    # This function will apply each step in the pipeline to the frame
    # and return the final processed frame
    # The pipeline is a list of functions that take a frame as input
    def apply_pipeline(self, frame):

        for step in self.pipeline:
            frame = step(frame)
        return frame

    # Run the webcam image processor
    # This function will capture frames from the webcam and apply the pipeline to each frame
    def run(self):
        print("Press 's' to save, 'q' to quit")
        while True:

            # Read a frame from the camera
            ret, frame = self.cap.read()

            # Check if the frame was read successfully
            if not ret:
                print("Failed to read frame from camera.")
                break

            # Process the frame based on the selected
            # pipeline = self.hardcoded_pipeline()

            processed = self.apply_pipeline(frame)
                
            # Display the processed frame if the variable is set
            if 'processed' in locals():
                cv2.imshow("Process - "+ "Processed", processed)

            # Check for key presses
            # 's' to save the current frame
            # 'q' to quit the program
            # 'c' to capture the current frame
            key = cv2.waitKey(1) & 0xFF
            if key == ord('s'):
                filename = os.path.join(self.save_dir, f"edge_{self.saved_frame_count}.png")
                cv2.imwrite(filename, processed)
                print(f"Saved {filename}")
                self.saved_frame_count += 1
            elif key == ord('q'):
                break

        self.cap.release()
        cv2.destroyAllWindows()

def main():

    # Parse command line arguments
    parser = argparse.ArgumentParser(description="Webcam Image Processor CLI")
    parser.add_argument("--output", type=str, default="snapshots", help="Directory to save snapshots")
    parser.add_argument("--camera", type=int, default=0, help="Camera index to use")
    parser.add_argument("--steps", nargs="+", default=["gray", "canny"],
                        help="Sequence of processing steps (e.g. gray blur canny)")
    args = parser.parse_args()

    # Create the Image Processor object
    processor = WebcamImageProcessor(save_dir=args.output, camera_index=args.camera, step_names=args.steps)

    ## Example of adding steps to the pipeline
    #args.steps.append("dilate")
    #args.steps.append("dilate")
    #args.steps.append("dilate")
    #processor.pipeline = processor.build_pipeline(args.steps)

    processor.run()

if __name__ == "__main__":
    main()