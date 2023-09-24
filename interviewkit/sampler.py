"""
This takes two args, a filepath to an audio file and an integer.

It will sample the file specified for that many minutes.

`ffmpeg` is a requirement for this to work.

Example usage:

    python interviewkit/sampler.py data/Martine+Barrat_FINAL.mp3 2

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
    if len(sys.argv) != 3:
        print("Usage: python3 sampler.py <filepath> <number of minutes>")
        return

    path = Path(sys.argv[1])
    minutes = int(sys.argv[2])

    print("Sampling {} for {} minutes".format(path, minutes))

    audio = pydub.AudioSegment.from_file(path)
    audio = audio[:minutes * 60 * 1000]
    new_filename = f"{path.parent}/sampled-{minutes}-{path.name}"
    audio.export(new_filename, format="mp3")
    print("Created new file: ", new_filename)

if __name__ == '__main__':
    main()