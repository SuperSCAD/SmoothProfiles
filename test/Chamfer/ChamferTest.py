from super_scad.d2.Polygon import Polygon
from super_scad.scad.Context import Context
from super_scad.scad.Scad import Scad
from super_scad.type import Vector2

from super_scad_smooth_profiles.Chamfer import Chamfer
from super_scad_smooth_profiles.ChamferFactory import ChamferFactory
from test.ScadTestCase import ScadTestCase


class FilletTest(ScadTestCase):
    """
    Testcases for chamfers.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def testConvex(self) -> None:
        """
        Test chamfer for convex corners with sharp and oblique angles.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(context=Context(fs=0.1, fa=1.0))
        body = Polygon(points=[Vector2(0, 10), Vector2(-20, 0), Vector2(0, -10), Vector2(20, 0)])

        factory = ChamferFactory(length=5.0)
        inner_angles = body.inner_angles
        normal_angles = body.normal_angles
        nodes = body.primary
        for index in range(len(nodes)):
            body = factory.create_smooth_profile(inner_angle=inner_angles[index],
                                                 normal_angle=normal_angles[index],
                                                 position=nodes[index],
                                                 child=body)

        scad.run_super_scad(body, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def testConcaveSharp(self) -> None:
        """
        Test chamfer for concave corners with a sharp angle.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(context=Context(fs=0.1, fa=1.0))
        body = Polygon(points=[Vector2(0, 50), Vector2(20, 0), Vector2(0, 40), Vector2(-20, 0)])

        inner_angles = body.inner_angles
        normal_angles = body.normal_angles
        nodes = body.primary
        body = Chamfer(length=5.0,
                       inner_angle=inner_angles[0],
                       normal_angle=normal_angles[0],
                       position=nodes[0],
                       child=body)
        body = Chamfer(length=5.0,
                       inner_angle=inner_angles[2],
                       normal_angle=normal_angles[2],
                       position=nodes[2],
                       child=body)

        scad.run_super_scad(body, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

# ----------------------------------------------------------------------------------------------------------------------
