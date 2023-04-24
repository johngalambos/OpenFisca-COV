from openfisca_core.variables import Variable
from openfisca_core import indexed_enums
from openfisca_core import periods, variables
from numpy import equal

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

class floor_area(Variable):
    value_type = float
    entity = BusinessLicense
    definition_period = periods.ETERNITY
    label = "The floor area of the business"

class license_class(Variable):
    value_type = int
    entity = BusinessLicense
    default_value = 0
    definition_period = periods.ETERNITY

    def formula(license, period, parameters):
        business_type = license("business_type", period)
        floor_area = license("floor_area", period)
        BusinessTypesEnum = business_type.possible_values
        # print(business_type)
        # business_type 
        # is_fitness_centre = [(bt == BusinessTypesEnum.fitness_centre) for bt in business_type]
        is_fitness_centre = (business_type == BusinessTypesEnum.fitness_centre) 
        print(f"floor area {floor_area}")

        print(is_fitness_centre)
        scale_1 = parameters(period).licensing.fitness_centre_floor_area
        print(scale_1)
        scale_1_calc = scale_1.calc(floor_area)
        print(scale_1_calc)

        return is_fitness_centre * scale_1.calc(floor_area)

        # return people("sole_parent_support__entitled", period) * scale_1.calc(floor_area)
        # print(business_type)
        # print(is_fitness_centre)
        # if fitness centre, then class is based on sq m
        # if casino class is based on capacity
        # return [100 for b in business_type]
        # return business_type * 1


# class license_class(Variable):
#     value_type = int
#     entity = BusinessLicense
#     default_value = 0
#     definition_period = periods.ETERNITY

#     def formula(license, period, parameters):
#         return [1 if license("floor_area", period) > 250 else 2 ]



class licensing_fee(Variable):
    value_type = float
    entity = BusinessLicense
    definition_period = periods.YEAR

    def formula(license, period, parameters):
        business_type = license("business_type", period)
        return [100 for b in business_type]
        # return business_type * 1
        # fees = parameters(period).licensing.fees.fees[business_type]
        # return fees

