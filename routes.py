from flask import Blueprint, request, jsonify
from app.models import db, TrashEmissions
from app.services import (
    calculate_trash_emissions,
    generate_suggestions,
    recommend_local_services
)

bp = Blueprint('routes', __name__)

@bp.route('/analyze_trash', methods=['POST'])
def analyze_trash():
    # Get the list of trash items from the JSON request
    data = request.get_json()
    trash_items = data.get('trash_items', [])

    # Calculate emissions based on the provided list
    emissions = calculate_trash_emissions(trash_items)

    # Generate suggestions and local services
    suggestions = generate_suggestions(trash_items)
    services = recommend_local_services()

    # Store results in the database
    new_record = TrashEmissions(
        audio_file=None,
        emission_kg=emissions,
        suggestions=", ".join(suggestions),
        services=", ".join(services)
    )
    db.session.add(new_record)
    db.session.commit()

    # Return the results as JSON
    return jsonify({
        'trash_items': trash_items,
        'emission_kg': emissions,
        'suggestions': suggestions,
        'services': services
    })
