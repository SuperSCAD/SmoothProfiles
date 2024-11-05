import inspect
import unittest
from pathlib import Path


class ScadTestCase(unittest.TestCase):
    """
    Parent test case for SuperSCAD test cases.
    """

    # ------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def paths():
        """
        Returns a path to the actual generated OpenSCAD code and the expected OpenSCAD code.
        """
        directory = Path(inspect.stack()[1][1]).parent
        method = inspect.stack()[1][3]
        path_actual = Path.joinpath(directory, method + '.actual.scad')
        path_expected = Path.joinpath(directory, method + '.expected.scad')

        return path_actual, path_expected

# ----------------------------------------------------------------------------------------------------------------------
