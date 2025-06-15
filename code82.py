FREEZING_POINT = 0
BOILING_POINT = 100


def water_state(temperature):
    if temperature <= FREEZING_POINT:
        return "Solid"
    elif 0 < temperature < 100:
        return "Liquid"
    elif temperature >= BOILING_POINT:
        return "Gas"
