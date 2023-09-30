"""
This takes two args, a filepath to an audio file and an integer.

It will sample the file specified for that many minutes.

`ffmpeg` is a requirement for this to work.

Example usage:
    Format:  python interviewkit/slicer.py path_to_audio_file audio_start audio_end
    Example: python interviewkit/slicer.py data/Martine+Barrat_FINAL.mp3 2 3

This generates:

    data/sampled-5-Martine+Barrat_FINAL.mp3

"""
import sys
from pathlib import Path
import shutil

try:
    import pydub
except ImportError:
    print("Please install pydub: pip install pydub")
    exit(1)

if shutil.which("ffmpeg") is None:
    print("Please install ffmpeg: https://ffmpeg.org/download.html")
    print("  On mac you can: brew install ffmpeg")
    exit(1)


def main():
    if len(sys.argv) != 4:
        print("Usage: python3 slicer.py <filepath> <number of minutes>")
        return

    path = Path(sys.argv[1])
    audio_start = int(sys.argv[2])
    audio_end = int(sys.argv[3])
    # minutes = int(sys.argv[2])

    # print("Sampling {} for {} minutes".format(path, minutes))
    print("Sampling {} from {} for {} minutes".format(path, audio_start, audio_end))

    audio = pydub.AudioSegment.from_file(path)
    # audio = audio[:minutes * 60 * 1000]
    audio = audio[audio_start * 60 * 1000:audio_end * 60 * 1000]
    new_filename = f"{path.parent}/sampled-{audio_start}-{audio_end}-{path.name}"
    audio.export(new_filename, format="mp3")
    print("Created new file: ", new_filename)

if __name__ == '__main__':
    main()
