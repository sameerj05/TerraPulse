def calculate_emissions(electricity_kwh, gas_therms):
    ELECTRICITY_CO2_PER_KWH = 0.233  # kg CO2 per kWh
    GAS_CO2_PER_THERM = 5.3  # kg CO2 per therm

    emissions_from_electricity = electricity_kwh * ELECTRICITY_CO2_PER_KWH
    emissions_from_gas = gas_therms * GAS_CO2_PER_THERM

    return emissions_from_electricity + emissions_from_gas

def suggest_reductions(electricity_kwh, gas_therms):
    tips = []
    if electricity_kwh > 300:
        tips.append("Consider switching to LED bulbs to reduce energy usage.")
    if gas_therms > 50:
        tips.append("Lower your thermostat by 1-2 degrees to save energy.")
    tips.append("Use appliances during off-peak hours for efficiency.")
    tips.append("Maintain humidity between 50-60% for optimal home climate.")

    return tips
