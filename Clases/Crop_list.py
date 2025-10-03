from Clases.Crop import Crop

class CropFactory:
    @staticmethod
    def create_crops():
        """
        Generates a list of predefined crops.
        """
        crops = [
            Crop('Potato', 6.0, 8.0, 60, 70),
            Crop('Tomato', 6.5, 9.0, 55, 75),
            Crop('Barley', 7.0, 7.5, 50, 80),
            Crop('Corn', 6.8, 10.0, 65, 85),
            Crop('Carrot', 6.2, 8.5, 70, 60)
        ]
        return crops
