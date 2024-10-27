import whisper
from pydub import AudioSegment

# Load Whisper model for transcription
model = whisper.load_model("base")

def transcribe_audio(audio_path):
    """Transcribe audio to text using Whisper."""
    result = model.transcribe(audio_path)
    return result["text"]

def calculate_trash_emissions(transcription):
    """Analyze the transcription and estimate emissions."""
    emissions = 0.0
    if "plastic" in transcription:
        emissions += 6.0  # Example value for plastic waste (kg CO2)
    if "paper" in transcription:
        emissions += 1.5  # Example value for paper waste (kg CO2)
    if "organic" in transcription:
        emissions += 0.5  # Example value for organic waste (kg CO2)

    return emissions

def generate_suggestions(transcription):
    """Provide suggestions based on waste type."""
    suggestions = []
    if "plastic" in transcription:
        suggestions.append("Switch to reusable containers.")
    if "paper" in transcription:
        suggestions.append("Use digital alternatives.")
    if "organic" in transcription:
        suggestions.append("Start composting food waste.")

    return suggestions

def recommend_local_services():
    """Mock service for suggesting eco-friendly services."""
    return [
        "EcoCycle Recycling - 123 Green St",
        "CompostNow - 456 Compost Ave",
        "GreenDelivery - Local eco-friendly courier service"
    ]
