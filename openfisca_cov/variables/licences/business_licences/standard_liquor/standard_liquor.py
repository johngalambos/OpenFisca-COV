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


class standard_liquor__applicable(variables.Variable):
    value_type = bool
    entity = Business
    default_value = True
    definition_period = periods.YEAR
    label = "Does the Standard Liquor licence apply in the scenario"
    reference = "https://bylaws.vancouver.ca/4450c.PDF"

    def formula(business, period):
        """Is the business a Liquor Establishment, i.e. the Standard Liquor licence is applicable."""
        return business("business_type", period) == BusinessType.liquor_establishment


class standard_liquor__class(variables.Variable):
    value_type = int
    entity = Business
    default_value = 0
    definition_period = periods.YEAR
    reference = "https://bylaws.vancouver.ca/4450c.PDF"

    def formula(business, period, parameters):
        """What is the Standard Liquor licence class for the Liquor Establishment based on person capacity."""
        person_capacity = business("person_capacity", period)
        return parameters(period).licences.business_licences.standard_liquor.classes.calc(person_capacity) * business("standard_liquor__applicable", period)


class standard_liquor__fee(variables.Variable):
    value_type = float
    entity = Business
    definition_period = periods.YEAR
    reference = "https://bylaws.vancouver.ca/4450c.PDF"

    def formula(business, period, parameters):
        """What is the fee for the Standard Liquor licence based on person capacity."""
        person_capacity = business("person_capacity", period)
        minimum = parameters(period).licences.business_licences.standard_liquor.fees.minimum
        maximum = parameters(period).licences.business_licences.standard_liquor.fees.maximum
        per_person = parameters(period).licences.business_licences.standard_liquor.fees.per_person

        return clip(per_person * person_capacity, minimum, maximum) * business("standard_liquor__applicable", period)
