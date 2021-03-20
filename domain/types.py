class Inventory:
    def __init__(self, items):
        self.items = items
    
    def update_inventory(self):
        for item in self.items:
            item.update_quality()

    def get_item(self):
        return self.items
            
class Item:
    def __init__ (self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality
    
    @property
    def name(self):
        return self.__name

    @property
    def sell_in(self):
        return self.__sell_in

    @property
    def quality(self):
        return self.__quality
    
    @name.setter
    def name(self, value):
        self.__name = value

    @sell_in.setter
    def sell_in(self, value):
        self.__sell_in = value

    @sell_in.setter
    def quality(self, value):
        self.__quality = value
    
    def __eq__(self, other):
        return self.name == other.name \
               and self.sell_in == other.sell_in \
               and self.quality == other.quality
               
    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

class Updateable:
    def update_quality(self):
        # No se puede modificar la clase Item, entonces usamos esta clase 
        #   con un método vacío para sobreescribirlo más adelante
        pass

class NormalItem(Item, Updateable):
    def __init__(self, name, sell_in, quality):
        Item.__init__(self, name, sell_in, quality)

    # La calidad de un artículo nunca es negativa
    # La calidad no puede ser más grande de 50
    # Cada día que pasa, los items envejecen
    # Cada día que pasa, los items pierden 1 de calidad 
    #   y en el momento en que caducan, pierden 2 de calidad por día

    def setSell_in(self):
        self.sell_in -= 1

    def setQuality(self, valor):
        if self.quality + valor > 50:
            self.quality = 50
        elif self.quality + valor >= 0:
            self.quality = self.quality + valor
        else:
            self.quality = 0
            
    def update_quality(self):
        if self.sell_in > 0:
            self.setQuality(-1)
        else:
            self.setQuality(-2)
        self.setSell_in()           

class ConjuredItem(Item, Updateable):
    def __init__(self, name, sell_in, quality):
        Item.__init__(self, name, sell_in, quality)
    
    # Envejece 2 veces más rápido que los NormalItems
    
    def setSell_in(self):
        self.sell_in -= 1

    def setQuality(self, valor):
        if self.quality + valor > 50:
            self.quality = 50
        elif self.quality + valor >= 0:
            self.quality = self.quality + valor
        else:
            self.quality = 0

    def update_quality(self):
        if self.sell_in > 0:
            self.setQuality(-2)
        else:
            self.setQuality(-4)
        self.setSell_in()

class AgedBrie(NormalItem):
    def __init__(self, name, sell_in, quality):
        NormalItem.__init__(self, name, sell_in, quality)

    # Según pasan los días aumenta su calidad

    def update_quality(self):
        if self.sell_in > 0:
            self.setQuality(1)
        else:
            self.setQuality(2)
        self.setSell_in()

class Sulfuras(NormalItem):

    def __init__(self, name, sell_in, quality):
        NormalItem.__init__(self, name, sell_in, quality)

    def update_quality(self):
        # Ni se vende ni envejece
        pass

class Backstage(NormalItem):

    def __init__(self, name, sell_in, quality):
        NormalItem.__init__(self, name, sell_in, quality)
    
    # Aumenta en 2 la calidad cuando quedan 10 días o menos
    # Aumenta en 3 la calidad cuando quedan 5 días o menos
    # Cuando caduca, su calidad es 0

    def update_quality(self):
        if self.sell_in > 10:
            self.setQuality(1)
        elif self.sell_in > 5:
            self.setQuality(2)
        elif self.sell_in > 0:
            self.setQuality(3)
        else:
            self.quality = 0
        self.setSell_in()