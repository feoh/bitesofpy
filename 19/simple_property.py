from datetime import datetime

NOW = datetime.now()


class Promo:
    def __init__(self, name, expires):
        self._name = name
        self._expires = expires
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        self._name = value
    
    @property
    def expired(self):
        return self._expires < NOW
    
