"""
This file defines variables for the modelled legislation.

A variable is a property of an Entity such as a Person, a Household…

See https://openfisca.org/doc/key-concepts/variables.html
"""

from numpy import clip
from openfisca_core import periods, variables
# Import the Entities specifically defined for this tax and benefit system
from openfisca_cov.entities import Business
from openfisca_cov.variables.business import BusinessType


class extended_liquor__applicable(variables.Variable):
    value_type = bool
    entity = Business
    default_value = True
    definition_period = periods.YEAR
    label = "Does the licence apply in the scenario, i.e. the Extended Liquor licence is applicable"
    reference = "https://bylaws.vancouver.ca/4450c.PDF"

    def formula(business, period):
        """Is the business a Liquor Establishment."""
        return business("business_type", period) == BusinessType.liquor_establishment


class extended_liquor__class(variables.Variable):
    value_type = int
    entity = Business
    default_value = 0
    definition_period = periods.YEAR
    reference = "https://bylaws.vancouver.ca/4450c.PDF"

    def formula(business, period, parameters):
        """What is the Extended Liquor licence class for the Liquor Establishment based on person capacity."""
        person_capacity = business("person_capacity", period)
        return parameters(period).licences.business_licences.extended_liquor.classes.calc(person_capacity) * business("extended_liquor__applicable", period)


class extended_liquor__fee(variables.Variable):
    value_type = float
    entity = Business
    definition_period = periods.YEAR
    reference = "https://bylaws.vancouver.ca/4450c.PDF"

    def formula(business, period, parameters):
        """What is the Extended Liquor licence fee payable for the Liquor Establishment based on person capacity."""
        person_capacity = business("person_capacity", period)
        minimum = parameters(period).licences.business_licences.extended_liquor.fees.minimum
        maximum = parameters(period).licences.business_licences.extended_liquor.fees.maximum
        per_person = parameters(period).licences.business_licences.extended_liquor.fees.per_person

        return clip(per_person * person_capacity, minimum, maximum) * business("extended_liquor__applicable", period)
