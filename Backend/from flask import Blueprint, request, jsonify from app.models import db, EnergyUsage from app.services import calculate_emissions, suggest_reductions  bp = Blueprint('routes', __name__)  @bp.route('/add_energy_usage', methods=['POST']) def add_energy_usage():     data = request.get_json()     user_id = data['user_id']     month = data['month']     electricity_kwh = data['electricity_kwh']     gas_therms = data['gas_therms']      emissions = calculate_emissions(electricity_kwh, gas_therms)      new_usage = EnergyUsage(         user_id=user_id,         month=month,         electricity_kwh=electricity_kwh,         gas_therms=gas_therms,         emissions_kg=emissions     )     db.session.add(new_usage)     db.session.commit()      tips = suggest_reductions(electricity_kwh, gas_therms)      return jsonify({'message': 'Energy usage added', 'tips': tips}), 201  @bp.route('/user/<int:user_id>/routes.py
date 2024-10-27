from flask import Blueprint, request, jsonify
from app.models import db, EnergyUsage
from app.services import calculate_emissions, suggest_reductions

bp = Blueprint('routes', __name__)

@bp.route('/add_energy_usage', methods=['POST'])
def add_energy_usage():
    data = request.get_json()
    user_id = data['user_id']
    month = data['month']
    electricity_kwh = data['electricity_kwh']
    gas_therms = data['gas_therms']

    emissions = calculate_emissions(electricity_kwh, gas_therms)

    new_usage = EnergyUsage(
        user_id=user_id,
        month=month,
        electricity_kwh=electricity_kwh,
        gas_therms=gas_therms,
        emissions_kg=emissions
    )
    db.session.add(new_usage)
    db.session.commit()

    tips = suggest_reductions(electricity_kwh, gas_therms)

    return jsonify({'message': 'Energy usage added', 'tips': tips}), 201

@bp.route('/user/<int:user_id>/summary', methods=['GET'])
def user_summary(user_id):
    usage = EnergyUsage.query.filter_by(user_id=user_id).all()
    total_emissions = sum([u.emissions_kg for u in usage])

    return jsonify({
        'user_id': user_id,
        'total_emissions_kg': total_emissions,
        'monthly_usage': [{'month': u.month, 'emissions_kg': u.emissions_kg} for u in usage]
    })
