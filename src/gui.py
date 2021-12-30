import tkinter
from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
import re
import math
import ToolTip as ttip


# TODO:
#   multi-file functionality
class MainWindow:
    def __init__(self):
        self.width = 500
        self.height = 350
        self.full_file_paths = []
        self.selected_fnames = []
        self.colors = BgColors()
        self.root = Tk()
        self.main_frame = None
        self.file_label_frame = None
        self.file_frame_w = self.width - 20
        self.file_frame_h = 130

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

        self.file_label_frame = tkinter.Frame(self.main_frame, height=self.file_frame_h, width=self.file_frame_w, bg=self.colors.light_blue, borderwidth=3, relief="sunken")
        self.file_label_frame.pack(pady=10)

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
            if file_full_path not in self.full_file_paths:
                # add full file path to list of files to transcribe
                self.full_file_paths.append(file_full_path)
            else:
                showinfo("File already added", "You have already selected this file")
                return

            # add file name to main window UI
            fname = re.split(r'\\|/', file_full_path)[-1]
            self.selected_fnames.append(fname)
            for i in range(len(self.selected_fnames)):
                # trim long filenames to fit in the gui
                trimmed_fname = self.trim_fname_len(self.selected_fnames[i])
                label = tkinter.Label(self.file_label_frame, text=trimmed_fname, bg=self.colors.light_blue)
                label.place(y=i * 20 + 2, x=2)
                # add tooltip to display full file name
                ttip.CreateToolTip(label, self.selected_fnames[i])

        except TypeError:
            print("No file selected")

    def trim_fname_len(self, fname):
        """
        Trim down long filenames to fit nicely in the GUI window
        :param fname: File name to trim
        :return: A subset of the filename for display purposes
        """
        print("Fname length: %s" % len(fname))
        print("Frame_width: %s" % self.file_frame_w)
        x = fname.split('8')[0]
        print(x)
        print(len(x))
        trimmed_fname = ""
        # Length of each character in pixels (approximately) for the default tkinter font
        CHAR_LEN = 8.25
        # the available characters that can be stored in the frame
        avail_char_len = math.floor(self.file_frame_w / CHAR_LEN)
        print("Available: %s" % avail_char_len)
        if len(fname) > avail_char_len:
            # subtract some characters and add a '...' to show the filename is cut off
            trimmed_fname = fname[:avail_char_len-3] + "..."
            print("Trimmed: %s" % trimmed_fname)
        # fname doesn't need to be trimmed
        else:
            print("Didn't need to trim")
            return fname

        return trimmed_fname

class BgColors:
    def __init__(self):
        self.light_blue = "#b7d4f0"
        self.white = "#ffffff"
        self.red = "#ff0000"
