from deepspeech import Model, version
import os
import numpy as np
import wave
from timeit import default_timer as timer


class Transcribe:
    """
        Transcribe an audio file in .WAV format into text
        Pieces of this class were from https://deepspeech.readthedocs.io/en/r0.9/Python-Examples.html#py-api-example
    """
    def __init__(self, file_paths):
        self.file_paths = file_paths
        self.inferences = {}
        for file in file_paths:
            # print(file)
            # print("OS:", os.getcwd())
            # print(file.split(os.getcwd()))

            inference = self.transcribe_file(file)
            self.inferences[file] = inference

    def transcribe_file(self, audio_path):
        """
        Transcribe an audio file
        :param audio_path: Full path to the audio input
        :return: TODO: will this return a string, or write to a file?
        """
        print(os.getcwd())

        model_path = os.path.join(os.getcwd(), "model/deepspeech-0.9.3-models.pbmm")
        print("\n\n" + model_path, end="\n\n")

        # TODO: Convert non-WAV files into WAV format
        # dir_path = os.path.join(os.getcwd(), "tmp")
        # if not os.path.isdir(dir_path):
        #     os.makedirs(dir_path)

        ds = Model(model_path)

        # convert audio buffer into 1D numpy array
        fin = wave.open(audio_path, 'rb')
        fs_orig = fin.getframerate()
        audio_length = fin.getnframes() * (1/fs_orig)
        audio = np.frombuffer(fin.readframes(fin.getnframes()), np.int16)
        fin.close()

        print("Starting inference")
        inference_start = timer()
        inference = ds.stt(audio)
        inference_end = timer() - inference_start
        print('Inference took %0.3fs for %0.3fs audio file.' % (inference_end, audio_length))
        return inference
        # print(inference)

        # if args.extended:
        #     print(metadata_to_string(ds.sttWithMetadata(audio, 1).transcripts[0]))
        # elif args.json:
        #     print(metadata_json_output(ds.sttWithMetadata(audio, args.candidate_transcripts)))
        # else:
        #     print(ds.stt(audio))

    def prep_input(self, audio_path):
        """
        TODO: might want to rewrite this function to use it for converting into a .wav format instead
        Prepare a .WAV file to be put in the DeepSpeech model for transcription
        :param audio_path: Full file path of the audio file
        :return:
        """
        # convert audio buffer into 1D numpy array
        fin = wave.open(audio_path, 'rb')
        fs_orig = fin.getframerate()

        audio = np.frombuffer(fin.readframes(fin.getnframes()), np.int16)

        audio_length = fin.getnframes() * (1 / fs_orig)
        fin.close()