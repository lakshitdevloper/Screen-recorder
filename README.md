# Screen-recorder😀
It is made by fully python languages.There are many libraries are used in this software

## Requirements

- Python 3
- Numpy library 
- Tkinter library 
- Opencv library
- pyautogui library

```
    pip install pyautogui
```

```
    pip install Opencv-python
```

```
    pip install numpy
```

```
    pip install tkinter
```
## Uses of libraries:-
- Tkinter: Used for creating the GUI.
- Pyautogui: Used for capturing screenshots.
- OpenCV library for video processing.
- Numpy: Used for array manipulation.
- Os: Used for file path operations.
- Datetime: Used for timestamping the output file.
- Threading: Used to run the screen recording in a separate thread.
# Code explanation:
## ScreenRecorder Class:
``` python
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
```

- ##### init: Initializes the GUI components and sets up the initial state.
    * root: The main windo
    * is_recording: A flag to indicate if recording is in progress.
    * title_label: A label for the title.
    * start_button: A button to start recording.
    * stop_button: A button to stop recording, initially disabled

Start recording

``` python
        def start_recording(self):
        self.is_recording = True
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)
        threading.Thread(target=self.record_screen).start()
```
- ##### start_recording: Sets the recording flag to ```True```, disables the start button, enables the stop button, and starts the recording in a new thread.
Stop recording

``` python
        def stop_recording(self):
        self.is_recording = False
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)
        messagebox.showinfo("Screen Recorder", "Recording stopped and saved in Downloads folder.")
```
- ##### stop_recording: Sets the recording flag to ```False```, enables the start button, disables the stop button, and shows a message box indicating that recording has stopped.
Record screen
``` python
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
```
- #### record_screen: Captures the screen and writes it to a video file:
    * screen_size: Gets the screen size.
    *   fourcc: Specifies the codec for the video.
    *  output_path: Constructs the output file path.
    * out: Creates a ```VideoWriter``` object.
    * while self.is_recording: Continuously captures screenshots and writes them to the video file while recording is active.
    * out.release(): Releases the video writer object.
    * cv2.destroyAllWindows(): Closes any OpenCV windows.

Main block
``` python
    if __name__ == "__main__":
    root = tk.Tk()
    app = ScreenRecorder(root)
    root.mainloop()
```
- ##### Main Block: Creates the main window and starts the Tkinter event loop.

This code sets up a simple screen recorder with a GUI, allowing the user to start and stop recording the screen. The recording is saved as a video file in the Downloads folder.

## Intallation:

There is exe file But I cannot post here in github

- you can use software in you editior like vs code i alreday paste link.
- Or ````pip install pyintaller ```` and make exe file.
- To see how create python file to exe see this video: 


[![Watch the video](https://i.ytimg.com/vi/bEBMo52OCis/maxresdefault.jpg)](https://youtu.be/32sHvb4oigk)

