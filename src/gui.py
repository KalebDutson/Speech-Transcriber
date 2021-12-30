import tkinter
from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
import re

# TODO:
#   multi-file functionality
class MainWindow:
    def __init__(self):
        self.width = 350
        self.height = 350
        self.full_file_paths = []
        self.selected_fnames = []
        self.colors = BgColors()
        self.root = Tk()
        self.main_frame = None
        self.file_label_frame = None

    def launch(self):
        """
        Launch the main window of the Speech-Transcriber GUI
        """
        self.root.title("Speech Transcriber")
        self.root.geometry('%sx%s+300+300' % (self.width, self.height))
        self.main_frame = tkinter.Frame(self.root, bg=self.colors.white, borderwidth=5, relief="ridge")
        self.main_frame.pack(expand="yes", fill="both")

        desc = tkinter.Label(self.main_frame, text="File selected for transcription")
        desc.pack(padx=10)

        self.file_label_frame = tkinter.Frame(self.main_frame, height=60, width=self.width - 20, bg=self.colors.light_blue, borderwidth=3, relief="sunken")
        self.file_label_frame.pack(pady=10)

        # TODO: Fix large file names going outside the frame
        for i in range(len(self.selected_fnames)):
            label = tkinter.Label(self.file_label_frame, text=self.selected_fnames[i], bg=self.colors.light_blue)
            label.place(y=i * 20 + 2, x=2)
            # label.bind("<Enter>", )

        # label = Label(frame1, text="Hello World !")
        # label.pack(side=TOP)
        frame_buttons = tkinter.Frame(self.main_frame, bg=self.colors.red, width=self.width, height=100)
        frame_buttons.pack(fill="both")
        button_file_dialog = tkinter.Button(frame_buttons, text="Add File",
                                            command=self.file_dialog_callback)
        button_file_dialog.pack(side=LEFT, padx=10)

        self.root.mainloop()

    def file_dialog_callback(self):
        """
        Open the file dialog and allow the user to select a file
        """
        filetypes = (
            ("All audio files", "*.mp3 *.wav"),
            ("MP3 files", "*.mp3"),
            ("WAV files", "*.wav")
        )
        try:
            file_full_path = fd.askopenfilename(
                title="Select a file",
                filetypes=filetypes
            )
            # add full file path to list of files to transcribe
            self.full_file_paths.append(file_full_path)

            # TODO: Fix large file names going outside the frame
            # add file name to main window UI
            fname = re.split(r'\\|/', file_full_path)[-1]
            self.selected_fnames.append(fname)
            for i in range(len(self.selected_fnames)):
                label = tkinter.Label(self.file_label_frame, text=self.selected_fnames[i], bg=self.colors.light_blue)
                label.place(y=i * 20 + 2, x=2)

        except TypeError:
            print("No file selected")

class BgColors:
    def __init__(self):
        self.light_blue = "#b7d4f0"
        self.white = "#ffffff"
        self.red = "#ff0000"
