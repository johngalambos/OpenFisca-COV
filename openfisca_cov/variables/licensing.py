from openfisca_core.variables import Variable
from openfisca_core import indexed_enums
from openfisca_core import periods, variables

# Import the Entities specifically defined for this tax and benefit system
from openfisca_cov.entities import BusinessLicense

class requires_clearance(Variable):
    value_type = bool
    entity = BusinessLicense
    default_value = True
    definition_period = periods.ETERNITY

class BusinessType(indexed_enums.Enum):
    __order__ = "fitness_centre barber"
    fitness_centre = "Fitness Centre"
    barber = "Barber"

class business_type(Variable):
    value_type = indexed_enums.Enum
    possible_values = BusinessType
    default_value = BusinessType.fitness_centre
    entity = BusinessLicense
    definition_period = periods.ETERNITY
    label = "The type of the business"

class licensing_fee(Variable):
    value_type = float
    entity = BusinessLicense
    definition_period = periods.YEAR

    def formula(license, period, parameters):
        business_type = license("business_type", period)
        fees = parameters(period).licensing.fees.fees[business_type]
        return fees

