"""
This file defines variables for the modelled legislation.

A variable is a property of an Entity such as a Person, a Household…

See https://openfisca.org/doc/key-concepts/variables.html
"""

from openfisca_core import periods, variables

# Import the Entities specifically defined for this tax and benefit system
from openfisca_cov.entities import TitledProperty
from openfisca_cov.variables.zones import Zones


class laneway_house__applicable(variables.Variable):
    value_type = bool
    entity = TitledProperty
    default_value = True
    definition_period = periods.YEAR
    label = "Can a laneway house be added to the property"
    reference = ""

    def formula(titled_property, period):
        """Can a laneway house be added to the property."""
        return titled_property("zone", period) == Zones.RS_1
