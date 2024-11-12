from super_scad.boolean.Empty import Empty
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
    def test_skew_length(self):
        """
        Test chamfer given the length of the skew side.
        """
        factory = ChamferFactory(skew_length=5.0)

        # Sharp angle.
        inner_angle = 45.0
        profile = factory.create_smooth_profile(inner_angle=inner_angle,
                                                normal_angle=0.0,
                                                position=Vector2.origin, child=Empty())

        self.assertIsInstance(profile, Chamfer)

        p1 = Vector2(0.5 * profile.skew_length, 0.0)
        p2 = p1 + Vector2.from_polar_coordinates(factory.offset1(inner_angle=inner_angle),
                                                 90.0 + 0.5 * inner_angle)

        self.assertAlmostEqual(5.0, profile.skew_length)
        self.assertAlmostEqual(0.0, p2.x)
        self.assertAlmostEqual(p2.y, profile.skew_height)
        self.assertAlmostEqual(factory.offset1(inner_angle=inner_angle), factory.offset2(inner_angle=inner_angle))

        # Oblige angle.
        inner_angle = 135.0
        profile = factory.create_smooth_profile(inner_angle=inner_angle,
                                                normal_angle=0.0,
                                                position=Vector2.origin, child=Empty())

        self.assertIsInstance(profile, Chamfer)

        p1 = Vector2(0.5 * profile.skew_length, 0.0)
        p2 = p1 + Vector2.from_polar_coordinates(factory.offset1(inner_angle=inner_angle),
                                                 90.0 + 0.5 * inner_angle)

        self.assertAlmostEqual(5.0, profile.skew_length)
        self.assertAlmostEqual(0.0, p2.x)
        self.assertAlmostEqual(p2.y, profile.skew_height)
        self.assertAlmostEqual(factory.offset1(inner_angle=inner_angle), factory.offset2(inner_angle=inner_angle))

    # ------------------------------------------------------------------------------------------------------------------
    def test_skew_height(self):
        """
        Test chamfer given the height of the skew side.
        """
        factory = ChamferFactory(skew_height=5.0)

        # Sharp angle.
        inner_angle = 45.0
        profile = factory.create_smooth_profile(inner_angle=inner_angle,
                                                normal_angle=0.0,
                                                position=Vector2.origin,
                                                child=Empty())
        self.assertIsInstance(profile, Chamfer)

        p1 = Vector2(0.5 * profile.skew_length, 0.0)
        p2 = p1 + Vector2.from_polar_coordinates(factory.offset1(inner_angle=inner_angle), 90.0 + 0.5 * inner_angle)

        self.assertAlmostEqual(5.0, profile.skew_height)
        self.assertAlmostEqual(0.0, p2.x)
        self.assertAlmostEqual(p2.y, profile.skew_height)
        self.assertAlmostEqual(factory.offset1(inner_angle=inner_angle), factory.offset2(inner_angle=inner_angle))

        # Oblige angle.
        inner_angle = 135.0
        profile = factory.create_smooth_profile(inner_angle=inner_angle,
                                                normal_angle=0.0,
                                                position=Vector2.origin,
                                                child=Empty())

        self.assertIsInstance(profile, Chamfer)

        p1 = Vector2(0.5 * profile.skew_length, 0.0)
        p2 = p1 + Vector2.from_polar_coordinates(factory.offset1(inner_angle=inner_angle), 90.0 + 0.5*inner_angle )

        self.assertAlmostEqual(5.0, profile.skew_height)
        self.assertAlmostEqual(0.0, p2.x)
        self.assertAlmostEqual(p2.y, profile.skew_height)
        self.assertAlmostEqual(factory.offset1(inner_angle=inner_angle), factory.offset2(inner_angle=inner_angle))

    # ------------------------------------------------------------------------------------------------------------------
    def test_convex(self) -> None:
        """
        Test chamfer for convex corners with sharp and oblique angles.
        """
        path_actual, path_expected = self.paths()

        context = Context(fs=0.1, fa=1.0, eps=0.5)
        scad = Scad(context=context)
        body = Polygon(points=[Vector2(0, 10), Vector2(-20, 0), Vector2(0, -10), Vector2(20, 0)])

        factory = ChamferFactory(skew_length=5.0)
        inner_angles = body.inner_angles(context)
        normal_angles = body.normal_angles(context)
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
    def test_concave_sharp(self) -> None:
        """
        Test chamfer for concave corners with a sharp angle.
        """
        path_actual, path_expected = self.paths()

        context = Context(fs=0.1, fa=1.0, eps=0.5)
        scad = Scad(context=context)
        body = Polygon(points=[Vector2(0, 50), Vector2(20, 0), Vector2(0, 40), Vector2(-20, 0)])

        inner_angles = body.inner_angles(context)
        normal_angles = body.normal_angles(context)
        nodes = body.primary
        body = Chamfer(skew_length=5.0,
                       inner_angle=inner_angles[0],
                       normal_angle=normal_angles[0],
                       position=nodes[0],
                       child=body)
        body = Chamfer(skew_length=5.0,
                       inner_angle=inner_angles[2],
                       normal_angle=normal_angles[2],
                       position=nodes[2],
                       child=body)

        scad.run_super_scad(body, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

# ----------------------------------------------------------------------------------------------------------------------
