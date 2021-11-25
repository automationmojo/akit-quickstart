from akit.integration.landscaping.landscapedescription import LandscapeDescription


class ExOrgLandscapeDescription(LandscapeDescription):
    """
    """

    def validate_landscape(self, landscape_info):
        """
            Validates the landscape description file.
        """
        errors, warnings = super(ExOrgLandscapeDescription, self).validate_landscape(landscape_info)
        return errors, warnings
