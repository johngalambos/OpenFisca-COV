from openfisca_core.variables import Variable
from openfisca_core import indexed_enums
from openfisca_core import periods, variables
from numpy import char,clip

# Import the Entities specifically defined for this tax and benefit system
from openfisca_cov.entities import Business

from openfisca_cov.variables.business import BusinessType


class beauty_salon__applicable(Variable):
    value_type = bool
    entity = Business
    default_value = True
    definition_period = periods.YEAR
    label = "Does the licence apply in the scenario"
    reference = "https://bylaws.vancouver.ca/4450c.PDF"

    def formula(business, period, parameters):
        return business("business_type", period) == BusinessType.beauty_salon


class beauty_salon__fee(Variable):
    value_type = float
    entity = Business
    definition_period = periods.YEAR
    reference = "https://bylaws.vancouver.ca/4450c.PDF"

    def formula(business, period, parameters):
        return parameters(period).licences.business_licences.beauty_salon.fees * business("beauty_salon__applicable", period)
