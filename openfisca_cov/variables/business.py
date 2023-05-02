"""
This file defines variables for the modelled legislation.

A variable is a property of an Entity such as a Person, a Household…

See https://openfisca.org/doc/key-concepts/variables.html
"""

from openfisca_core import indexed_enums
from openfisca_core import periods, variables
# Import the Entities specifically defined for this tax and benefit system
from openfisca_cov.entities import Business


class BusinessType(indexed_enums.Enum):
    __order__ = "backyard_pay_parking barber beauty_salon fitness_centre liquor_establishment"
    backyard_pay_parking = "Backyard Pay Parking"
    barber = "Barber Shop"
    beauty_salon = "Beauty Salon"
    fitness_centre = "Fitness Centre"
    liquor_establishment = "Liquor Establishment"


class business_type(variables.Variable):
    value_type = indexed_enums.Enum
    possible_values = BusinessType
    entity = Business
    default_value = BusinessType.fitness_centre
    definition_period = periods.ETERNITY
    label = "The type of the business"


class floor_area(variables.Variable):
    value_type = float
    entity = Business
    definition_period = periods.ETERNITY
    label = "The floor area of the business"


class person_capacity(variables.Variable):
    value_type = int
    entity = Business
    definition_period = periods.ETERNITY
    label = "The person capacity of the business"


class parking_spaces(variables.Variable):
    value_type = int
    entity = Business
    definition_period = periods.ETERNITY
    label = "Number of parking spaces"
