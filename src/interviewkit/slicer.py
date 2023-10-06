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

try:
    import pydub
except ImportError:
    print("Please install pydub: pip install pydub")
    exit(1)

if shutil.which("ffmpeg") is None:
    print("Please install ffmpeg: https://ffmpeg.org/download.html")
    print("  On mac you can: brew install ffmpeg")
    exit(1)

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

    if len(audio_slicing == 2):
        seconds = int(audio_time_split_list[1])
    
    return timedelta(minutes=minutes, seconds=seconds)
   

def export_filename(audio_time_list):
    """ Filename for exported file """
    
    if audio_time_list and len(audio_time_list) == 2:
        return f"{audio_time_list[0]}m{audio_time_list[1]}s"
    elif audio_time_list and len(audio_time_list) == 1:
        return f"{audio_time_list[0]}m"
    else:
        print("Error! Audio slice input params invalid. Please try again with correct parameters.")
        print("Error inside export_filename(audio_time_list) funtion.")
        exit(1)


def slice_audio(audio, start_time: timedelta , end_time: timedelta):
    start_time_ms = start_time.total_seconds() * 1000
    end_time_ms = end_time.total_seconds() * 1000
    
    return audio[start_time_ms, end_time_ms]


def audio_slicing(path, audio_slice_start_time, audio_slice_end_time):
    """ It reads the original audio and uses start and end input time params to generate sliced audio. """
    
    print("Sampling {} from {} to {}".format(path, audio_slice_start_time, audio_slice_end_time))

    # Reading original audio file
    audio = pydub.AudioSegment.from_file(path)
    original_audio_size_ms = audio.duration_seconds * 1000


    # Converting audio start and end times in msecs
    audio_start_time = convert_time_input_to_time_delta(audio_slice_start_time)
    audio_end_time = convert_time_input_to_time_delta(audio_slice_end_time)
    
    # Check if audio start and end times are within original audio size limits
    if(audio_start_time > original_audio_size_ms or audio_end_time > original_audio_size_ms):
        print("Error! Audio slice input params cannot be greater than original audio size. Please try again with correct parameters.")
        exit(1)

    sliced_audio = slice_audio(audio, audio_start_time, audio_end_time)

    
    new_filename = 

    # Filename for exported file
    audio_start_time_name = export_filename(audio_start_time_list)
    audio_end_time_name = export_filename(audio_end_time_list)
    new_filename =  f"{path.parent}/sampled-{audio_start_time_name}-{audio_end_time_name}-{path.name}"
    audio.export(new_filename, format="mp3")
    print("Created new file: ", new_filename)

def main():
    if len(sys.argv) != 4:
        print("Usage: python3 slicer.py <filepath> <audio start time in minutes> <audio end time in minutes>")
        return

    path = Path(sys.argv[1])
    audio_slice_start_time = (sys.argv[2])
    audio_slice_end_time = (sys.argv[3])

    audio_slicing(path, audio_slice_start_time, audio_slice_end_time)

if __name__ == '__main__':
    main()
