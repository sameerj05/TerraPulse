from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class EnergyUsage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)  # Link to user
    month = db.Column(db.String(20), nullable=False)  # Month for usage
    electricity_kwh = db.Column(db.Float, nullable=False)  # Electricity in kWh
    gas_therms = db.Column(db.Float, nullable=False)  # Gas in therms
    emissions_kg = db.Column(db.Float, nullable=True)  # Total emissions in kg
