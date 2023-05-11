"""
This file defines variables for the modelled legislation.

A variable is a property of an Entity such as a Person, a Household…

See https://openfisca.org/doc/key-concepts/variables.html
"""

from openfisca_core import indexed_enums
from openfisca_core import periods, variables

from openfisca_cov.entities import TitledProperty

# Not necessarily a complete list, needs comprehensive review
class Zones(indexed_enums.Enum):
    __order__ = "BCPED C_1 C_2 C_2B C_2C C_2C1 C_3 C_3A C_4 C_5 C_5A C_6 C_7 CD_1 DD DEOD FC_1 FC_2 FCCDD FSHCA HA_1 HA_1A HA_2 HA_3 IC_1 IC_2 IC_3 I_1 I_1A I_1B I_2 I_3 I_4 M_1 M_1A M_2 MC_1 RM_1 RM_1N RM_2 RM_3 RM_3A RM_4 RM_4N RM_5 RM_5A RM_5B RM_5C RM_5D RM_7N RM_7AN RM_8A RM_8AN RM_9A RM_9AN RM_9BN RM_10N RM_11 RM_11N RM_12N RS_1 RS_1A RS_2 RS_3 RS_4 RS_5 RS_6 RS_7 RT_1 RT_2 RT_3 RT_4 RT_4AN RT_4N RT_5 RT_5N RT_6 RT_7 RT_8 RT_9 RT_10 RT_10N RT_11 RT_11N RT_12 RT_12N"
    BCPED = "BCPED"
    C_1 = "C-1"
    C_2 = "C-2"
    C_2B = "C-2B"
    C_2C = "C-2C"
    C_2C1 = "C-2C1"
    C_3 = "C-3"
    C_3A = "C-3A"
    C_4 = "C-4"
    C_5 = "C-5"
    C_5A = "C-5A"
    C_6 = "C-6"
    C_7 = "C-7"
    CD_1 = "CD-1"
    DD = "DD"
    DEOD = "DEOD"
    FC_1 = "FC-1"
    FC_2 = "FC-2"
    FCCDD = "FCCDD"
    FSHCA = "FSHCA"
    HA_1 = "HA-1"
    HA_1A = "HA-1A"
    HA_2 = "HA-2"
    HA_3 = "HA-3"
    IC_1 = "IC-1"
    IC_2 = "IC-2"
    IC_3 = "IC-3"
    I_1 = "I-1"
    I_1A = "I-1A"
    I_1B = "I-1B"
    I_2 = "I-2"
    I_3 = "I-3"
    I_4 = "I-4"
    M_1 = "M-1"
    M_1A = "M-1A"
    M_2 = "M-2"
    MC_1 = "MC-1"
    RM_1 = "RM-1"
    RM_1N = "RM-1N"
    RM_2 = "RM-2"
    RM_3 = "RM-3"
    RM_3A = "RM-3A"
    RM_4 = "RM-4"
    RM_4N = "RM-4N"
    RM_5 = "RM-5"
    RM_5A = "RM-5A"
    RM_5B = "RM-5B"
    RM_5C = "RM-5C"
    RM_5D = "RM-5D"
    RM_7N = "RM-7N"
    RM_7AN = "RM-7AN"
    RM_8A = "RM-8A"
    RM_8AN = "RM-8AN"
    RM_9A = "RM-9A"
    RM_9AN = "RM-9AN"
    RM_9BN = "RM-9BN"
    RM_10N = "RM-10N"
    RM_11 = "RM-11"
    RM_11N = "RM-11N"
    RM_12N = "RM-12N"
    RS_1 = "RS-1"
    RS_1A = "RS-1A"
    RS_2 = "RS-2"
    RS_3 = "RS-3"
    RS_4 = "RS-4"
    RS_5 = "RS-5"
    RS_6 = "RS-6"
    RS_7 = "RS-7"
    RT_1 = "RT-1"
    RT_2 = "RT-2"
    RT_3 = "RT-3"
    RT_4 = "RT-4"
    RT_4AN = "RT-4AN"
    RT_4N = "RT-4N"
    RT_5 = "RT-5"
    RT_5N = "RT-5N"
    RT_6 = "RT-6"
    RT_7 = "RT-7"
    RT_8 = "RT-8"
    RT_9 = "RT-9"
    RT_10 = "RT-10"
    RT_10N = "RT-10N"
    RT_11 = "RT-11"
    RT_11N = "RT-11N"
    RT_12 = "RT-12"
    RT_12N = "RT-12N"


class zone(variables.Variable):
    value_type = indexed_enums.Enum
    possible_values = Zones
    entity = TitledProperty
    default_value = Zones.RS_1
    definition_period = periods.ETERNITY
    label = "The zone of a property"
