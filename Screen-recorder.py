import tkinter as tk
from tkinter import messagebox, Toplevel, Label, Button
import pyautogui
import cv2
import numpy as np
import os
from datetime import datetime
import threading

class ScreenRecorder:
    def __init__(self, root):
        self.root = root
        self.root.title("Screen Recorder")
        self.root.geometry("350x250")
        self.root.configure(bg="#1e1e1e")

        self.is_recording = False

        self.title_label = Label(root, text="Screen Recorder", font=("Helvetica", 18, "bold"), bg="#1e1e1e", fg="#ffffff")
        self.title_label.pack(pady=10)

        self.start_button = Button(root, text="Start Recording", font=("Helvetica", 12), command=self.start_recording, bg="#4CAF50", fg="#ffffff", activebackground="#45a049", width=20, height=2)
        self.start_button.pack(pady=10)

        self.stop_button = Button(root, text="Stop Recording", font=("Helvetica", 12), command=self.stop_recording, bg="#f44336", fg="#ffffff", activebackground="#e41c1c", width=20, height=2)
        self.stop_button.pack(pady=10)
        self.stop_button.config(state=tk.DISABLED)

    def start_recording(self):
        self.is_recording = True
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)
        threading.Thread(target=self.record_screen).start()

    def stop_recording(self):
        self.is_recording = False
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)
        messagebox.showinfo("Screen Recorder", "Recording stopped and saved in Downloads folder.")

    def record_screen(self):
        screen_size = pyautogui.size()
        messagebox.showinfo("Screen Recorder", "Recording started. High quality and high graphics settings applied.")
        fourcc = cv2.VideoWriter_fourcc(*"XVID")
        output_path = os.path.join(os.path.expanduser("~"), "Downloads", f"recording_{datetime.now().strftime('%Y%m%d_%H%M%S')}.avi")
        out = cv2.VideoWriter(output_path, fourcc, 20.0, screen_size)

        while self.is_recording:
            img = pyautogui.screenshot()
            frame = np.array(img)
            frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
            out.write(frame)

        out.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    root = tk.Tk()
    app = ScreenRecorder(root)
    root.mainloop()