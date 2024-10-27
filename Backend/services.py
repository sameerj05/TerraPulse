def calculate_trash_emissions(trash_items):
    """Estimate emissions based on the provided trash items."""
    emissions = 0.0
    for item in trash_items:
        if item.lower() == "plastic":
            emissions += 6.0  # Example value for plastic waste (kg CO2)
        elif item.lower() == "paper":
            emissions += 1.5  # Example value for paper waste (kg CO2)
        elif item.lower() == "organic":
            emissions += 0.5  # Example value for organic waste (kg CO2)
        elif item.lower() == "metal":
            emissions += 3.0  # Example value for metal waste (kg CO2)

    return emissions

def generate_suggestions(trash_items):
    """Provide suggestions based on the trash items provided."""
    suggestions = []
    if "plastic" in trash_items:
        suggestions.append("Switch to reusable containers.")
    if "paper" in trash_items:
        suggestions.append("Use digital alternatives to reduce paper usage.")
    if "organic" in trash_items:
        suggestions.append("Start composting food waste.")
    if "metal" in trash_items:
        suggestions.append("Take metal waste to a recycling center.")

    return suggestions

def recommend_local_services():
    """Mock service to suggest local eco-friendly services."""
    return [
        "EcoCycle Recycling - 123 Green St",
        "CompostNow - 456 Compost Ave",
        "GreenDelivery - Local eco-friendly courier service"
    ]
