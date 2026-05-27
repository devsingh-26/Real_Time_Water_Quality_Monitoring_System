from datetime import datetime
import json

def analyze_water(data):

    status = "SAFE"

    alerts = []

    if data["ph"] < 6.5 or data["ph"] > 8.5:
        alerts.append("Unsafe pH")

    if data["turbidity"] > 50:
        alerts.append("High Turbidity")

    if data["tds"] > 700:
        alerts.append("High TDS")

    if data["temperature"] > 32:
        alerts.append("High Temperature")

    if data["water_level"] < 30:
        alerts.append("Low Water Level")

    if alerts:
        status = "UNSAFE"

    latest_data = {

        "temperature": data["temperature"],

        "ph": data["ph"],

        "turbidity": data["turbidity"],

        "tds": data["tds"],

        "water_level": data["water_level"],

        "status": status,

        "alerts": alerts,

        "timestamp":
            datetime.now().strftime("%H:%M:%S")
    }

    with open("data.json", "w") as file:

        json.dump(latest_data, file)

    return latest_data