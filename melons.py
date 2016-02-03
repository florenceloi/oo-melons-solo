"""This file should have our order classes in it."""

from random import randint
from datetime import datetime

class AbstractMelonOrder(object):
    """An abstract class that other Melon Orders inherit from."""
    
    def __init__(self, species, qty, order_type, tax):
        """Initialize melon order attributes"""

        self.species = species
        self.qty = qty
        self.shipped = False
        self.order_type = order_type
        self.tax = tax
        self.splurge_factor = randint(5, 9)

    def get_base_price(self):
        """Calculate base price."""

        base_price = self.splurge_factor
        
    def get_total(self):
        """Calculate total price."""

        base_price = get_base_price
        
        if self.species = "Christmas melon":
            base_price = base_price * 1.5      
      
        total = (1 + self.tax) * self.qty * base_price

        if self.order_type = "international" and self.qty < 10:
            total += 3

        return total

    def mark_shipped(self):
        """Set shipped to true."""

        self.shipped = True


class DomesticMelonOrder(AbstractMelonOrder):
    """A domestic (in the US) melon order."""

    def __init__(self, species, qty):
        """Initialize melon order attributes"""

        return super(DomesticMelonOrder, self).__init__(species, 
                                                        qty,                                                    
                                                        "domestic",
                                                        0.08)


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes"""

        return super(InternationalMelonOrder, self).__init__(species,
                                                             qty,                                                             
                                                             "international",
                                                             0.17)
       
        self.country_code = country_code
        
    def get_country_code(self):
        """Return the country code."""

        return self.country_code


class GovernmentMelonOrder(AbstractMelonOrder):
    """A government (US) melon order, with discount."""

    def __init(self, species, qty):
        """Initialize melon order attributes."""

        return super(GovernmentMelonOrder, self).__init(species,
                                                        qty,
                                                        "government",
                                                        0.00)

        self.passed_inspection = False

    def inspect_melon(self, passed):
        """Set inspection to passed"""

        self.passed_inspection = passed