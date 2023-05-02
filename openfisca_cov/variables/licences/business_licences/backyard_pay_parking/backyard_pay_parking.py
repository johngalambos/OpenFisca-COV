from openfisca_core.variables import Variable
from openfisca_core import indexed_enums
from openfisca_core import periods, variables
from numpy import clip

# Import the Entities specifically defined for this tax and benefit system
from openfisca_cov.entities import Business

from openfisca_cov.variables.business import BusinessType


class backyard_pay_parking__applicable(Variable):
    value_type = bool
    entity = Business
    default_value = True
    definition_period = periods.YEAR
    label = "Does the licence apply in the scenario"
    reference = "https://bylaws.vancouver.ca/4450c.PDF"

    def formula(business, period, parameters):
        return business("business_type", period) == BusinessType.backyard_pay_parking


class backyard_pay_parking__fee(Variable):
    value_type = float
    entity = Business
    definition_period = periods.YEAR
    reference = "https://bylaws.vancouver.ca/4450c.PDF"

    def formula(business, period, parameters):
        parking_spaces = business("parking_spaces", period)
        first_two_fee = parameters(period).licences.business_licences.backyard_pay_parking.fees.first_two_spaces
        additional_fee = parameters(period).licences.business_licences.backyard_pay_parking.fees.additional_spaces

        return (((parking_spaces > 0) * first_two_fee) + ((parking_spaces-2).clip(min=0) * additional_fee)) * business("backyard_pay_parking__applicable", period)
