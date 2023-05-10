"""
This file defines variables for the modelled legislation.

A variable is a property of an Entity such as a Person, a Household…

See https://openfisca.org/doc/key-concepts/variables.html
"""

from openfisca_core import periods, variables

# Import the Entities specifically defined for this tax and benefit system
from openfisca_cov.entities import Business
from openfisca_cov.variables.business import BusinessType


class barber__applicable(variables.Variable):
    value_type = bool
    entity = Business
    default_value = True
    definition_period = periods.YEAR
    label = "Does the Barber Shop licence apply in the scenario"
    reference = "https://bylaws.vancouver.ca/4450c.PDF"

    def formula(business, period):
        """Is the business a Barber Shop."""
        return business("business_type", period) == BusinessType.barber


class barber__fee(variables.Variable):
    value_type = float
    entity = Business
    definition_period = periods.YEAR
    reference = "https://bylaws.vancouver.ca/4450c.PDF"

    def formula(business, period, parameters):
        """What is the fee payable for the Barber Shop."""
        return parameters(period).licences.business_licences.barber.fees * business("barber__applicable", period)
