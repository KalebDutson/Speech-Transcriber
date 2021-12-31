from deepspeech import Model, version
import os

class Transcribe:
    def __init__(self, file_paths):
        self.file_paths = file_paths
        for file in file_paths:
            # print(file)
            # print("OS:", os.getcwd())
            # print(file.split(os.getcwd()))
            self.transcribe_file(file)

    def transcribe_file(self, fpath):
        print(os.getcwd())

        model_path = os.path.join(os.getcwd(), "model/deepspeech-0.9.3-models.pbmm")
        print("\n\n" + model_path, end="\n\n")

        # TODO: Convert non-WAV files into WAV format
        # dir_path = os.path.join(os.getcwd(), "tmp")
        # if not os.path.isdir(dir_path):
        #     os.makedirs(dir_path)

        ds = Model(model_path)

        # if args.extended:
        #     print(metadata_to_string(ds.sttWithMetadata(audio, 1).transcripts[0]))
        # elif args.json:
        #     print(metadata_json_output(ds.sttWithMetadata(audio, args.candidate_transcripts)))
        # else:
        #     print(ds.stt(audio))
