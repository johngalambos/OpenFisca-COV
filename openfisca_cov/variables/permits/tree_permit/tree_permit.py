"""
This file defines variables for the modelled legislation.

A variable is a property of an Entity such as a Person, a Household…

See https://openfisca.org/doc/key-concepts/variables.html
"""

from numpy import logical_not
from openfisca_core import periods, variables

# Import the Entities specifically defined for this tax and benefit system
from openfisca_cov.entities import TitledProperty


class tree_permit__required(variables.Variable):
    value_type = bool
    entity = TitledProperty
    default_value = True
    definition_period = periods.YEAR
    label = "Do I need to apply for a tree permit"
    reference = ""

    def formula(titled_property, period):
        """Do I need to apply for a tree permit."""
        partOfHedge = titled_property("tree_permit__part_of_hedge", period)
        within_threshold = titled_property("tree_permit__within_threshold", period)

        return logical_not(within_threshold * logical_not(partOfHedge)) * logical_not(partOfHedge)


class tree_permit__part_of_hedge(variables.Variable):
    value_type = bool
    entity = TitledProperty
    definition_period = periods.ETERNITY
    # This is an example of what NOT TO DO. Replicating the natural language rule here is failure from a maintaince perspective
    # Ideally you would want to directly reference the hedge definition
    label = "Is the tree in question part of a hedge, “hedge” means five or more trees or shrubs less than five metres high, and planted less than 1.25 metres apart;"
    reference = "https://bylaws.vancouver.ca/9958c.PDF"


class tree_permit__combined_diameter(variables.Variable):
    value_type = float
    entity = TitledProperty
    definition_period = periods.ETERNITY
    label = "What is the combined diameter of the two of three largest trunks or stems in cm's"
    reference = "https://bylaws.vancouver.ca/9958c.PDF"


class tree_permit__within_threshold(variables.Variable):
    value_type = bool
    entity = TitledProperty
    default_value = False
    definition_period = periods.ETERNITY
    label = "Does the combined diameter exceed the threshold"
    reference = "https://bylaws.vancouver.ca/9958c.PDF"

    def formula(titled_property, period, parameters):
        """Do I need to apply for a tree permit."""
        return titled_property("tree_permit__combined_diameter", period) < parameters(period).permits.tree_permit.diameter_threshold
