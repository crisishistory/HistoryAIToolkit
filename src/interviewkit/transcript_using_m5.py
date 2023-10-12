from pathlib import Path
from rich.console import Console
import sys
import os
from transformers import T5Tokenizer, T5ForConditionalGeneration

try:
    import whisper
except ImportError:
    print("Please install Whisper: pip install openai-whisper")
    exit(1)

from whisper.utils import get_writer
from pydantic import BaseModel

console = Console()

class Transcript(BaseModel):
    """The Transcript entity represents the transcript of an interview."""
    content: str

# Load T5 model and tokenizer
tokenizer = T5Tokenizer.from_pretrained("t5-base")
model = T5ForConditionalGeneration.from_pretrained("t5-base")
def chunk_text(text, max_length):
    """Split the text into chunks of max_length."""
    words = text.split()
    chunks = []
    current_chunk = []
    current_length = 0
    
    for word in words:
        if current_length + len(word) <= max_length:
            current_length += len(word) + 1  # +1 for the space
            current_chunk.append(word)
        else:
            chunks.append(" ".join(current_chunk))
            current_chunk = [word]
            current_length = len(word)
    
    chunks.append(" ".join(current_chunk))  # Don't forget the last chunk
    return chunks

def generate_questions_for_all_chunks(chunks):
    all_questions = []
    for chunk in chunks:
        questions = generate_questions(chunk)
        all_questions.append(questions)
    return all_questions

def generate_questions(transcript_chunk):
    # Ensure transcript_chunk is a string
    if not isinstance(transcript_chunk, str):
        print("Warning: transcript_chunk is not a string. Trying to convert...")
        transcript_chunk = str(transcript_chunk)

    input_text = "Generate questions based on the Interview texts: " + transcript_chunk
    input_ids = tokenizer(input_text, return_tensors="pt").input_ids

    outputs = model.generate(input_ids)
    questions = tokenizer.decode(outputs[0])
    
    return questions

def transcribe_from_paths(source: Path, target: Path) -> None:
    console.print("Loading whisper base model...")
    model = whisper.load_model("base")

    with console.status("Transcribing audio file..."):
        result = model.transcribe((str(source)), fp16=False)

    txt_file_options = {
        "max_line_width": 50,  
        "max_line_count": 1,
        "highlight_words": False,  
    }

    console.print("Saving transcript as a .txt file...")
    txt_writer = get_writer("txt", str(target))
    txt_writer(result, source.name, txt_file_options)

    console.print("Transcript saved to:")
    console.print(f"    [green bold]{target / source.name}.txt[/green bold]")

    transcript_chunk = result['text']
    max_length = 512
    chunks = chunk_text(transcript_chunk, max_length)
    
    all_questions = generate_questions_for_all_chunks(chunks)
    
    for i, questions in enumerate(all_questions):
        console.print(f"Generated Questions for chunk {i+1}:\n", questions)

    
    # chunks = chunk_text(transcript_chunk, max_length)
    # questions = generate_questions(chunks[0])
    # console.print("Generated Questions:\n", questions)

if __name__ == "__main__":
    source = Path(sys.argv[1])
    target = Path(sys.argv[2])
    if source.suffix not in [".mp3", ".wav"]:
        raise ValueError("File must be an .mp3 or .wav file")
    transcribe_from_paths(source, target)
