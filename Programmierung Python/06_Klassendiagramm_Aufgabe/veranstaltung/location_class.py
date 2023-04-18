class Location:
    def __init__(self, name, ort):
        self.name = name
        self.ort = ort

    def __str__(self):
        return f"Location:(({self.name})({self.ort}))"
    
    