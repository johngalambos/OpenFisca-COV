"""
This file defines variables for the modelled legislation.

A variable is a property of an Entity such as a Person, a Household…

See https://openfisca.org/doc/key-concepts/variables.html
"""

from openfisca_core import periods, variables

# Import the Entities specifically defined for this tax and benefit system
from openfisca_cov.entities import Business
from openfisca_cov.variables.business import BusinessType


class backyard_pay_parking__applicable(variables.Variable):
    value_type = bool
    entity = Business
    default_value = True
    definition_period = periods.YEAR
    label = "Does the Backyard Pay Parking licence apply in the scenario"
    reference = "https://bylaws.vancouver.ca/4450c.PDF"

    def formula(business, period):
        """Is the business a Backyard Pay Parking business."""
        return business("business_type", period) == BusinessType.backyard_pay_parking


class backyard_pay_parking__fee(variables.Variable):
    value_type = float
    entity = Business
    definition_period = periods.YEAR
    reference = "https://bylaws.vancouver.ca/4450c.PDF"

    def formula(business, period, parameters):
        """What is the fee payable for a Backyard Pay Parking business based on the number of parking spaces the business has."""
        parking_spaces = business("parking_spaces", period)
        first_two_fee = parameters(period).licences.business_licences.backyard_pay_parking.fees.first_two_spaces
        additional_fee = parameters(period).licences.business_licences.backyard_pay_parking.fees.additional_spaces

        return (((parking_spaces > 0) * first_two_fee) + ((parking_spaces - 2).clip(min = 0) * additional_fee)) * business("backyard_pay_parking__applicable", period)
