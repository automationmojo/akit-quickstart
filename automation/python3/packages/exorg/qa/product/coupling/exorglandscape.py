
from akit.integration.landscaping.landscape import Landscape

from exorg.qa.product.coupling.exorglandscapedescription import ExOrgLandscapeDescription
from exorg.qa.product.coupling.exorgtopologydescription import ExOrgTopologyDescription

class ExOrgLandscape(Landscape):
    """
    """

    landscape_description = ExOrgLandscapeDescription
    topology_description = ExOrgTopologyDescription

    def __init__(self):
        super().__init__()
