import cv2
import os
import argparse

class WebcamImageProcessor:
    def __init__(self, save_dir="snapshots", camera_index=0):
        self.cap = cv2.VideoCapture(camera_index)  # 0 = default webcam
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
                filename = os.path.join(self.save_dir, f"edge_{self.frame_count}.png")
                cv2.imwrite(filename, edges)
                print(f"Saved {filename}")
                self.frame_count += 1
            elif key == ord('q'):
                break

        self.cap.release()
        cv2.destroyAllWindows()

def main():

    detector = WebcamImageProcessor()
    detector.run()

if __name__ == "__main__":
    main()