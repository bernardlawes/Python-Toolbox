import cv2
import os

from camera_edge.tools.file_tools import save_image

from camera_edge.utils import ensure_dir, timestamped_filename

class CameraEdgeDetector:
    
    def __init__(self, save_dir="snapshots"):
        self.cap = cv2.VideoCapture(0)  # 0 = default webcam
        self.save_dir = save_dir
        os.makedirs(save_dir, exist_ok=True)
        self.frame_count = 0

    def process_frame(self, frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(gray, 100, 200)
        return edges

    def run(self):
        print("Press 's' to save, 'q' to quit")
        while True:
            ret, frame = self.cap.read()
            if not ret:
                print("Failed to read frame from camera.")
                break

            edges = self.process_frame(frame)
            cv2.imshow("Edge Detection", edges)

            key = cv2.waitKey(1) & 0xFF
            if key == ord('s'):
                filename = timestamped_filename("edge", "png")
                #filename = os.path.join(self.save_dir, f"edge_{self.frame_count}.png")
                full_path = os.path.join(self.save_dir, filename)
                cv2.imwrite(full_path, edges)
                print(f"Saved {full_path}")
                self.frame_count += 1
            elif key == ord('q'):
                break

        self.cap.release()
        cv2.destroyAllWindows()