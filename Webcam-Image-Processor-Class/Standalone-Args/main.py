import cv2
import os
import argparse

class WebcamImageProcessor:
    def __init__(self, save_dir="snapshots", camera_index=0, method="none"):
        self.cap = cv2.VideoCapture(camera_index)  # 0 = default webcam
        self.save_dir = save_dir
        self.method = method
        if self.method not in ["gray", "blur", "canny","none"]:
            raise ValueError("\n\nInvalid method. Choose from one of 'gray', 'blur', or 'canny'.")
        os.makedirs(save_dir, exist_ok=True)
        self.frame_count = 0

    def do_gray(self, frame):
        return cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    def do_blur(self, frame, ksize=(5, 5)):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        return cv2.GaussianBlur(gray, ksize, 0)
    
    def do_canny(self, frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(gray, 100, 200)
        return edges

    def run(self):
        print("Press 's' to save, 'q' to quit")
        while True:

            # Read a frame from the camera
            ret, frame = self.cap.read()

            # Check if the frame was read successfully
            if not ret:
                print("Failed to read frame from camera.")
                break

            # Process the frame based on the selected method
            match self.method:
                case "gray":
                    processed = self.do_gray(frame)
                case "blur":
                    processed = self.do_blur(frame)
                case "canny":
                    processed = self.do_canny(frame)
                case _:
                    cv2.imshow("Edge Detection", frame)
                
            # Display the processed frame if the variable is set
            if 'processed' in locals():
                cv2.imshow("Process - "+ self.method, processed)

            # Check for key presses
            # 's' to save the current frame
            # 'q' to quit the program
            # 'c' to capture the current frame
            key = cv2.waitKey(1) & 0xFF
            if key == ord('s'):
                filename = os.path.join(self.save_dir, f"edge_{self.frame_count}.png")
                cv2.imwrite(filename, processed)
                print(f"Saved {filename}")
                self.frame_count += 1
            elif key == ord('q'):
                break

        self.cap.release()
        cv2.destroyAllWindows()

def main():

    parser = argparse.ArgumentParser(description="Webcam Image Processor CLI")
    parser.add_argument("--output", type=str, default="snapshots", help="Directory to save snapshots")
    parser.add_argument("--camera", type=int, default=0, help="Camera index to use")
    parser.add_argument("--method", type=str, default="none", help="Image Processing Method: 'gray', 'blur', 'canny'")
    args = parser.parse_args()

    detector = WebcamImageProcessor(save_dir=args.output, camera_index=args.camera, method=args.method)
    detector.run()

if __name__ == "__main__":
    main()