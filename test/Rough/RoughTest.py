from super_scad.boolean.Empty import Empty
from super_scad.d2.Square import Square
from super_scad.scad.Context import Context
from super_scad.scad.Scad import Scad
from super_scad.type import Vector2

from super_scad_smooth_profiles.Rough import Rough
from super_scad_smooth_profiles.RoughFactory import RoughFactory
from test.ScadTestCase import ScadTestCase


class RoughTest(ScadTestCase):
    """
    Testcases for rough profile.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def test_sizes(self):
        """
        Test the sizes of rough profile.
        """
        profile = Rough(child=Empty())

        self.assertAlmostEqual(0.0, profile.size1)
        self.assertAlmostEqual(0.0, profile.size2)

    # ------------------------------------------------------------------------------------------------------------------
    def test_on_child(self) -> None:
        """
        Test fillet for convex corners with sharp and oblique angles.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(context=Context())
        body = Square(size=10.0)

        factory = RoughFactory()
        body = factory.create_smooth_profile(inner_angle=90.0,
                                             normal_angle=45.0,
                                             position=Vector2.origin,
                                             child=body)

        scad.run_super_scad(body, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

# ----------------------------------------------------------------------------------------------------------------------
