import DeepSpeech.transcribe as dpt

class Transcribe:
    def __init__(self, file_paths):
        self.file_paths = file_paths
        for file in file_paths:
            print(file)
            # self.transcribe_file(file)

    def transcribe_file(self, fpath):
        print("Transcribing file:\n%s" % fpath)
        dpt.transcribe_file(fpath, None)
