"""
This takes three args, a filepath to an audio file, audio start and audio end times.

It will sample the file specified for that many minutes and seconds. 

The audio start and end times params currently support time in 2 ways either minutes and seconds or minutes only.

`ffmpeg` is a requirement for this to work.

Example usage:
    Format:  python interviewkit/slicer.py path_to_audio_file audio_slice_start_time audio_slice_end_time
    Example 1: python interviewkit/slicer.py data/MartineBarrat_FINAL.mp3 2 3 
             (Audio will be sliced from 2mins to 4mins)
    Example 2: python interviewkit/slicer.py data/Martine+Barrat_FINAL.mp3 70:40 80:40 
             (Audio will be sliced from 105mins 40secs to 107mins and 40secs)

This generates:
    data/sampled-70m40s-80m40s-MartineBarrat_FINAL.mp3
    data/sampled-2m-4m-MartineBarrat_FINAL.mp3

Note: 
The Script currently doesn't support input in hours format, so hours will need to converted to mins:secs format.
Example: If we want audio from 1hr 20mins 30 secs to 1hr 30mins 40secs, it can be done as shown below:
1hr 20mins 30 secs = 80mins 30secs
1hr 30mins 40sec = 90mins 40secs

python interviewkit/slicer.py data/Martine+Barrat_FINAL.mp3 80:30 90:40

"""
import sys
from pathlib import Path
import shutil
from datetime import timedelta

from dataclasses import dataclass

import logging

try:
    import pydub
except ImportError:
    print("Please install pydub: pip install pydub")
    exit(1)

if shutil.which("ffmpeg") is None:
    print("Please install ffmpeg: https://ffmpeg.org/download.html")
    print("  On mac you can: brew install ffmpeg")
    exit(1)

@dataclass
class AudioSubset:
    name: str
    audio: pydub.AudioSegment
    start_time: timedelta
    end_time: timedelta

    def as_audio(self):
        start_time_ms = self.start_time.total_seconds() * 1000
        end_time_ms = self.end_time.total_seconds() * 1000
    
        return self.audio[start_time_ms, end_time_ms]

    def export(self, filepath, format):
        start_time_output = f'{self.start_time.min}m{self.start_time.seconds}s'
        end_time_output = f'{self.end_time.min}m{self.end_time.seconds}s'
        output_filepath = Path(filepath)
        new_filename =  output_filepath + f"/sampled-{start_time_output}-{end_time_output}-{self.name}"
        self.audio.export(new_filename, format)
        logging.log(f'Created new file: {new_filename}')


def convert_time_input_to_time_delta(time_input: str):
    """ Converting mins and secs to msecs for pydub computation """

    # Fetching mins and secs from audio input
    audio_time_split_list = time_input.split(":")

    if not audio_time_split_list:
        raise ValueError("input time not found")
    
    if len(audio_time_split_list) > 2:
        raise ValueError("Audio slice input params invalid. Audio slice supports start/end time in mins or mins:secs format. Please try again with correct input times") 

    minutes = int(audio_time_split_list[0])
    
    seconds = 0

    if len(time_input == 2):
        seconds = int(audio_time_split_list[1])
    
    return timedelta(minutes=minutes, seconds=seconds)


def slice_audio(audio, start_time: timedelta , end_time: timedelta):
    start_time_ms = start_time.total_seconds() * 1000
    end_time_ms = end_time.total_seconds() * 1000
    
    return audio[start_time_ms, end_time_ms]


def parse_input(argv):
    if len(argv) != 4:
        raise ValueError("Usage: python3 slicer.py <filepath> <audio start time in minutes> <audio end time in minutes>")
    
    path = Path(argv[1])
     
    audio = pydub.AudioSegment.from_file(path)

    # Converting audio start and end times in msecs
    audio_start_time = convert_time_input_to_time_delta(argv[2])
    audio_end_time = convert_time_input_to_time_delta(argv[3])

    return AudioSubset(path.name, audio, audio_start_time, audio_end_time)


def main():

    
    audio_subset = parse_input(sys.argv)

    try:
       audio_subset.export("¬/", "mp3")
    except IndexError:
        raise ValueError("Error! Audio slice input params cannot be greater than original audio size. Please try again with correct parameters.")

if __name__ == '__main__':
    main()
