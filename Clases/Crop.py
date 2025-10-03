
"""
Crop Class: Represents a crop with ideal growth conditions.
"""
class Crop:
    def __init__(self, name, ph, sun, humidity, richness):
        self.name = name
        self.ideal_ph = ph
        self.ideal_sun = sun
        self.ideal_humidity = humidity
        self.ideal_richness = richness