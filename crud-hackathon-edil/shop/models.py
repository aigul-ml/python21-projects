class Cars:
    objects = []
    _id = 0
    cuzov = ("sedan", "universal", "cupe", "hatchback", "minivan", "jeep", "pickup")

    def __init__(self, marka, model, year, volume, color, cuzov, probeg, price):
        self._id = Cars._id
        self.marka = marka
        self.model = model
        self.year = year
        self.volume = volume
        self.color = color
        if cuzov in Cars.cuzov:
            self.cuzov = cuzov
        else:
            raise Exception("Car 'cuzov' is not valid")
        self.price = price
        self.probeg = probeg
        Cars.objects.append(self)
        Cars._id += 1