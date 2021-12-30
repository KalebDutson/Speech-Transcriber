import tkinter
from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
import re

WHITE = "#ffffff"
LIGHT_BLUE = "#b7d4f0"
RED = "#ff0000"
full_file_paths = []
selected_fnames = []

# TODO:
#   multi-file functionality
def main():
    WIDTH = 350
    HEIGHT = 350
    root = Tk()
    root.title("Speech Transcriber")
    root.geometry('%sx%s+300+300' % (WIDTH, HEIGHT))

    main_frame = tkinter.Frame(root, bg=WHITE, borderwidth=5, relief="ridge")
    main_frame.pack(expand="yes", fill="both")

    desc = tkinter.Label(main_frame, text="File selected for transcription")
    desc.pack(padx=10)

    frame1 = tkinter.Frame(main_frame, height=60, width=WIDTH - 20, bg=LIGHT_BLUE, borderwidth=3, relief="sunken")
    frame1.pack(pady=10)

    # TODO: Fix large file names going outside the frame
    for i in range(len(selected_fnames)):
        label = tkinter.Label(frame1, text=selected_fnames[i], bg=LIGHT_BLUE)
        label.place(y=i*20+2, x=2)
        label.bind("<Enter>", )

    # label = Label(frame1, text="Hello World !")
    # label.pack(side=TOP)
    frame_buttons = tkinter.Frame(main_frame, bg=RED, width=WIDTH, height=100)
    frame_buttons.pack(fill="both")
    button_file_dialog = tkinter.Button(frame_buttons, text="Add File", command=lambda:file_dialog_callback(frame1))
    button_file_dialog.pack(side=LEFT, padx=10)

    root.mainloop()


def file_dialog_callback(frame1):
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
        full_file_paths.append(file_full_path)

        # TODO: Fix large file names going outside the frame
        # add file name to main window UI
        fname = re.split(r'\\|/', file_full_path)[-1]
        selected_fnames.append(fname)
        for i in range(len(selected_fnames)):
            label = tkinter.Label(frame1, text=selected_fnames[i], bg=LIGHT_BLUE)
            label.place(y=i * 20 + 2, x=2)

    except TypeError:
        print("No file selected")


if __name__ == "__main__":
    main()
