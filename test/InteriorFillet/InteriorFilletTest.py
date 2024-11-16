from super_scad.d2.Polygon import Polygon
from super_scad.scad.Context import Context
from super_scad.scad.Scad import Scad
from super_scad.type import Vector2
from super_scad_smooth_profile.SmoothProfileParams import SmoothProfileParams

from super_scad_smooth_profiles.Fillet import Fillet
from super_scad_smooth_profiles.InteriorFilletWidget import InteriorFilletWidget
from test.ScadTestCase import ScadTestCase


class FilletTest(ScadTestCase):
    """
    Testcases for Fillet.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def test_sizes(self):
        """
        Test the size of a fillet.
        """
        # Positive radius.
        profile = Fillet(radius=5.0)

        # Sharp angle.
        self.assertAlmostEqual(12.0711, profile.offset1(inner_angle=45.0), places=4)
        self.assertAlmostEqual(12.0711, profile.offset2(inner_angle=45.0), places=4)

        # Oblique angle.
        self.assertAlmostEqual(2.0711, profile.offset1(inner_angle=135.0), places=4)
        self.assertAlmostEqual(2.0711, profile.offset2(inner_angle=135.0), places=4)

        # Concave corner.
        self.assertAlmostEqual(12.0711, profile.offset1(inner_angle=315.0), places=4)
        self.assertAlmostEqual(12.0711, profile.offset2(inner_angle=315.0), places=4)

        # Zero angle.
        self.assertEqual(0.0, profile.offset1(inner_angle=180.0))
        self.assertEqual(0.0, profile.offset2(inner_angle=180.0))

        # Negative radius.
        profile = Fillet(radius=-5.0)
        self.assertAlmostEqual(5.0, profile.offset1(inner_angle=45.0), places=4)
        self.assertAlmostEqual(5.0, profile.offset2(inner_angle=45.0), places=4)

        # Zero radius.
        profile = Fillet(radius=0.0)
        self.assertEqual(0.0, profile.offset1(inner_angle=45.0))
        self.assertEqual(0.0, profile.offset2(inner_angle=315.0))

    # ------------------------------------------------------------------------------------------------------------------
    def test_convex(self) -> None:
        """
        Test fillet for convex corners with sharp and oblique angles.
        """
        context = Context(fs=0.1, fa=1.0, eps=0.1)
        scad = Scad(context=context)
        body = Polygon(points=[Vector2(0, 10), Vector2(-20, 0), Vector2(0, -10), Vector2(20, 0)])

        profile = Fillet(radius=5.0)

        inner_angles = body.inner_angles(context)
        normal_angles = body.normal_angles(context)
        nodes = body.primary
        for index in range(len(nodes)):
            body = profile.create_smooth_profile(params=SmoothProfileParams(inner_angle=inner_angles[index],
                                                                            normal_angle=normal_angles[index],
                                                                            position=nodes[index]),
                                                 child=body)

        path_actual, path_expected = self.paths()
        scad.run_super_scad(body, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_concave_sharp(self) -> None:
        """
        Test fillet for concave corners with a sharp angle.
        """
        context = Context(fs=0.1, fa=1.0, eps=0.1)
        scad = Scad(context=context)
        points = [Vector2(0, 50), Vector2(20, 0), Vector2(0, 40), Vector2(-20, 0)]
        body = Polygon(points=points)

        inner_angles = body.inner_angles(context)
        normal_angles = body.normal_angles(context)
        nodes = body.primary
        body = InteriorFilletWidget(radius=5.0,
                                    inner_angle=inner_angles[2],
                                    normal_angle=normal_angles[2],
                                    position=nodes[2],
                                    child=body)

        path_actual, path_expected = self.paths()
        scad.run_super_scad(body, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_concave_oblique(self) -> None:
        """
        Test fillet for concave corners with an oblique angle.
        """
        context = Context(fs=0.1, fa=1.0, eps=0.1)
        scad = Scad(context=context)
        body = Polygon(points=[Vector2(0, 10), Vector2(20, 0), Vector2(0, 5), Vector2(-20, 0)])

        inner_angles = body.inner_angles(context)
        normal_angles = body.normal_angles(context)
        nodes = body.primary
        body = InteriorFilletWidget(radius=5.0,
                                    inner_angle=inner_angles[2],
                                    normal_angle=normal_angles[2],
                                    position=nodes[2],
                                    child=body)

        path_actual, path_expected = self.paths()
        scad.run_super_scad(body, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_convex_negative(self) -> None:
        """
        Test fillet for convex corners with sharp and oblique angles.
        """
        context = Context(fs=0.1, fa=1.0, eps=0.1)
        scad = Scad(context=context)
        body = Polygon(points=[Vector2(0, 10), Vector2(-20, 0), Vector2(0, -10), Vector2(20, 0)])

        inner_angles = body.inner_angles(context)
        normal_angles = body.normal_angles(context)
        nodes = body.primary
        for index in range(len(nodes)):
            body = InteriorFilletWidget(radius=-5.0,
                                        inner_angle=inner_angles[index],
                                        normal_angle=normal_angles[index],
                                        position=nodes[index],
                                        child=body)

        path_actual, path_expected = self.paths()
        scad.run_super_scad(body, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_concave_neg(self) -> None:
        """
        Test fillet for concave corners with a sharp angle.
        """
        context = Context(fs=0.1, fa=1.0, eps=0.1)
        scad = Scad(context=context)
        body = Polygon(points=[Vector2(0, 50), Vector2(20, 0), Vector2(0, 40), Vector2(-20, 0)])

        inner_angles = body.inner_angles(context)
        normal_angles = body.normal_angles(context)
        nodes = body.primary
        body = InteriorFilletWidget(radius=-5.0,
                                    inner_angle=inner_angles[2],
                                    normal_angle=normal_angles[2],
                                    position=nodes[2],
                                    child=body)

        path_actual, path_expected = self.paths()
        scad.run_super_scad(body, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_zero_radius(self) -> None:
        """
        Test fillet with zero radius.
        """
        context = Context()
        scad = Scad(context=context)
        body = Polygon(points=[Vector2.origin, Vector2(0, 20), Vector2(20, 20), Vector2(20.0, 0.0)])

        inner_angles = body.inner_angles(context)
        normal_angles = body.normal_angles(context)
        nodes = body.primary

        body = InteriorFilletWidget(radius=0.0,
                                    inner_angle=inner_angles[2],
                                    normal_angle=normal_angles[2],
                                    position=nodes[2],
                                    child=body)

        path_actual, path_expected = self.paths()
        scad.run_super_scad(body, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_barney(self) -> None:
        """
        Test fillet node with an inner angle of one hundred and eighty degrees.
        """
        context = Context()
        scad = Scad(context=context)
        body = Polygon(points=[Vector2.origin, Vector2(0, 20), Vector2(10, 20), Vector2(20, 20), Vector2(20.0, 0.0)])

        inner_angles = body.inner_angles(context)
        normal_angles = body.normal_angles(context)
        nodes = body.primary

        index = 2
        self.assertAlmostEqual(inner_angles[index], 180.0)

        body = InteriorFilletWidget(radius=5.0,
                                    inner_angle=inner_angles[index],
                                    normal_angle=normal_angles[index],
                                    position=nodes[index],
                                    child=body)

        path_actual, path_expected = self.paths()
        scad.run_super_scad(body, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

# ----------------------------------------------------------------------------------------------------------------------
