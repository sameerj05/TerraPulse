from flask import Blueprint, request, jsonify
from app.models import db, TrashEmissions
from app.services import (
    transcribe_audio,
    calculate_trash_emissions,
    generate_suggestions,
    recommend_local_services
)
import os

bp = Blueprint('routes', __name__)

@bp.route('/analyze_trash', methods=['POST'])
def analyze_trash():
    # Save the uploaded audio file
    audio = request.files['audio']
    audio_path = f"uploads/{audio.filename}"
    os.makedirs("uploads", exist_ok=True)
    audio.save(audio_path)

    # Transcribe audio
    transcription = transcribe_audio(audio_path)

    # Calculate emissions
    emissions = calculate_trash_emissions(transcription)

    # Generate suggestions and local services
    suggestions = generate_suggestions(transcription)
    services = recommend_local_services()

    # Store results in the database
    new_record = TrashEmissions(
        audio_file=audio.filename,
        emission_kg=emissions,
        suggestions=", ".join(suggestions),
        services=", ".join(services)
    )
    db.session.add(new_record)
    db.session.commit()

    # Return results as JSON
    return jsonify({
        'transcription': transcription,
        'emission_kg': emissions,
        'suggestions': suggestions,
        'services': services
    })
