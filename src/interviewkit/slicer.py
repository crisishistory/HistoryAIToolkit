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
from datetime import timedelta, datetime
from dataclasses import dataclass
import logging
import pydub


if shutil.which("ffmpeg") is None:
    print("Please install ffmpeg: https://ffmpeg.org/download.html")
    print("  On mac you can: brew install ffmpeg")
    exit(1)


EXPECTED_TIME_FORMAT = "%H:%M:%S"

@dataclass
class SlicerInput:
    path: Path
    start_time: timedelta
    end_time: timedelta

def convert_time_input_to_time_delta(time_input: str):

    time_info_values = zip(reversed(time_input.split(":")), reversed(EXPECTED_TIME_FORMAT.split(":")))

    full_time_value, time_info = zip(*time_info_values)

    time =  datetime.strptime(":".join(full_time_value), ":".join(time_info))

    return timedelta(hours=time.hour, minutes=time.minute, seconds=time.second)


def parse_input(argv: list[str]):
    if len(argv) != 4:
        raise ValueError("Usage: python3 slicer.py <filepath> <audio start time in minutes> <audio end time in minutes>")
    
    path = Path(argv[1])
     
    # Converting audio start and end times in msecs
    audio_start_time = convert_time_input_to_time_delta(argv[2])
    audio_end_time = convert_time_input_to_time_delta(argv[3])

    return SlicerInput(path, audio_start_time, audio_end_time)

def create_output_path(input: SlicerInput):
    start_minutes, start_seconds = divmod(input.start_time.seconds, 60)
    end_minutes, end_seconds = divmod(input.end_time.seconds, 60)
    start_time_output = f'{start_minutes}m{start_seconds}s'
    end_time_output = f'{end_minutes}m{end_seconds}s'
    new_filepath =   input.path.parent / f"sampled-{start_time_output}-{end_time_output}-{input.path.name}"
    return new_filepath

def slice_audio(audio: pydub.AudioSegment, start_time: timedelta , end_time: timedelta):
    start_time_ms = int(start_time.total_seconds() * 1000)
    end_time_ms = int(end_time.total_seconds() * 1000)
    
    return audio[start_time_ms:end_time_ms]


def main():

    argv = parse_input(sys.argv)

    audio = pydub.AudioSegment.from_file(argv.path)

    try:
       sliced_audio =  slice_audio(audio, argv.start_time, argv.end_time)
    except IndexError:
        raise ValueError("Error! Audio slice input params cannot be greater than original audio size. Please try again with correct parameters.")
    
    output_file_path = create_output_path(argv)
    sliced_audio.export(output_file_path, "mp3")

    print(f'Created new file: {output_file_path}')


if __name__ == '__main__':
    main()
