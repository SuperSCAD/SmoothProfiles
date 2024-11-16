from super_scad.boolean.Empty import Empty
from super_scad.d2.Polygon import Polygon
from super_scad.scad.Context import Context
from super_scad.scad.Scad import Scad
from super_scad.type import Vector2
from super_scad_smooth_profile.SmoothProfileParams import SmoothProfileParams

from super_scad_smooth_profiles.InteriorChamfer import InteriorChamfer
from super_scad_smooth_profiles.InteriorChamferFactory import InteriorChamferFactory
from test.ScadTestCase import ScadTestCase


class InteriorChamferTest(ScadTestCase):
    """
    Testcases for chamfers.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def test_sizes(self):
        """
        Test the size of a fillet.
        """
        # Positive radius.
        factory = InteriorChamferFactory(skew_length=5.0)

        # Sharp angle.
        self.assertAlmostEqual(6.5328, factory.offset1(inner_angle=45.0), places=4)
        self.assertAlmostEqual(6.5328, factory.offset2(inner_angle=45.0), places=4)

        # Oblique angle.
        self.assertAlmostEqual(2.7060, factory.offset1(inner_angle=135.0), places=4)
        self.assertAlmostEqual(2.7060, factory.offset2(inner_angle=135.0), places=4)

        # Concave corner.
        self.assertAlmostEqual(6.5328, factory.offset1(inner_angle=315.0), places=4)
        self.assertAlmostEqual(6.5328, factory.offset2(inner_angle=315.0), places=4)

        # Zero angle.
        self.assertEqual(0.0, factory.offset1(inner_angle=180.0))
        self.assertEqual(0.0, factory.offset2(inner_angle=180.0))

        # Zero skew length.
        factory = InteriorChamferFactory(skew_length=0.0)
        self.assertEqual(0.0, factory.offset1(inner_angle=45.0))
        self.assertEqual(0.0, factory.offset2(inner_angle=315.0))

    # ------------------------------------------------------------------------------------------------------------------
    def test_skew_length(self):
        """
        Test chamfer given the length of the skew side.
        """
        factory = InteriorChamferFactory(skew_length=5.0)

        # Sharp angle.
        inner_angle = 45.0

        p1 = Vector2(0.5 * factory.skew_length(inner_angle=inner_angle), 0.0)
        p2 = p1 + Vector2.from_polar_coordinates(factory.offset1(inner_angle=inner_angle),
                                                 90.0 + 0.5 * inner_angle)

        self.assertAlmostEqual(5.0, factory.skew_length(inner_angle=inner_angle))
        self.assertAlmostEqual(0.0, p2.x)
        self.assertAlmostEqual(p2.y, factory.skew_height(inner_angle=inner_angle))
        self.assertAlmostEqual(factory.offset1(inner_angle=inner_angle), factory.offset2(inner_angle=inner_angle))

        # Concave corner.
        self.assertAlmostEqual(factory.skew_height(inner_angle=45.0), factory.skew_height(inner_angle=315.0))
        self.assertAlmostEqual(factory.skew_length(inner_angle=45.0), factory.skew_length(inner_angle=315.0))

        # Oblige angle.
        inner_angle = 135.0

        p1 = Vector2(0.5 * factory.skew_length(inner_angle=inner_angle), 0.0)
        p2 = p1 + Vector2.from_polar_coordinates(factory.offset1(inner_angle=inner_angle),
                                                 90.0 + 0.5 * inner_angle)

        self.assertAlmostEqual(5.0, factory.skew_length(inner_angle=inner_angle))
        self.assertAlmostEqual(0.0, p2.x)
        self.assertAlmostEqual(p2.y, factory.skew_height(inner_angle=inner_angle))
        self.assertAlmostEqual(factory.offset1(inner_angle=inner_angle), factory.offset2(inner_angle=inner_angle))

    # ------------------------------------------------------------------------------------------------------------------
    def test_skew_height(self):
        """
        Test chamfer given the height of the skew side.
        """
        factory = InteriorChamferFactory(skew_height=5.0)

        # Sharp angle.
        inner_angle = 45.0

        p1 = Vector2(0.5 * factory.skew_length(inner_angle=inner_angle), 0.0)
        p2 = p1 + Vector2.from_polar_coordinates(factory.offset1(inner_angle=inner_angle), 90.0 + 0.5 * inner_angle)

        self.assertAlmostEqual(5.0, factory.skew_height(inner_angle=inner_angle))
        self.assertAlmostEqual(0.0, p2.x)
        self.assertAlmostEqual(p2.y, factory.skew_height(inner_angle=inner_angle))
        self.assertAlmostEqual(factory.offset1(inner_angle=inner_angle), factory.offset2(inner_angle=inner_angle))

        profile = factory.create_smooth_profile(params=SmoothProfileParams(inner_angle=inner_angle,
                                                                           normal_angle=0.0,
                                                                           position=Vector2.origin),
                                                child=Empty())
        self.assertIsInstance(profile, InteriorChamfer)
        self.assertAlmostEqual(factory.skew_height(inner_angle=inner_angle), profile.skew_height)
        self.assertAlmostEqual(factory.skew_length(inner_angle=inner_angle), profile.skew_length)

        # Concave corner.
        inner_angle = 315.0
        self.assertAlmostEqual(factory.skew_height(inner_angle=45.0), factory.skew_height(inner_angle=inner_angle))
        self.assertAlmostEqual(factory.skew_length(inner_angle=45.0), factory.skew_length(inner_angle=inner_angle))

        profile = factory.create_smooth_profile(params=SmoothProfileParams(inner_angle=inner_angle,
                                                                           normal_angle=0.0,
                                                                           position=Vector2.origin),
                                                child=Empty())
        self.assertIsInstance(profile, InteriorChamfer)
        self.assertAlmostEqual(factory.skew_height(inner_angle=inner_angle), profile.skew_height)
        self.assertAlmostEqual(factory.skew_length(inner_angle=inner_angle), profile.skew_length)

        # Oblige angle.
        inner_angle = 135.0

        p1 = Vector2(0.5 * factory.skew_length(inner_angle=inner_angle), 0.0)
        p2 = p1 + Vector2.from_polar_coordinates(factory.offset1(inner_angle=inner_angle), 90.0 + 0.5 * inner_angle)

        self.assertAlmostEqual(5.0, factory.skew_height(inner_angle=inner_angle))
        self.assertAlmostEqual(0.0, p2.x)
        self.assertAlmostEqual(p2.y, factory.skew_height(inner_angle=inner_angle))
        self.assertAlmostEqual(factory.offset1(inner_angle=inner_angle), factory.offset2(inner_angle=inner_angle))

        profile = factory.create_smooth_profile(params=SmoothProfileParams(inner_angle=inner_angle,
                                                                           normal_angle=0.0,
                                                                           position=Vector2.origin),
                                                child=Empty())
        self.assertIsInstance(profile, InteriorChamfer)
        self.assertAlmostEqual(factory.skew_height(inner_angle=inner_angle), profile.skew_height)
        self.assertAlmostEqual(factory.skew_length(inner_angle=inner_angle), profile.skew_length)

    # ------------------------------------------------------------------------------------------------------------------
    def test_convex(self) -> None:
        """
        Test chamfer for convex corners with sharp and oblique angles.
        """
        context = Context()
        scad = Scad(context=context)
        body = Polygon(points=[Vector2(0, 10), Vector2(-20, 0), Vector2(0, -10), Vector2(20, 0)])

        factory = InteriorChamferFactory(skew_length=5.0)
        inner_angles = body.inner_angles(context)
        normal_angles = body.normal_angles(context)
        nodes = body.primary
        for index in range(len(nodes)):
            body = factory.create_smooth_profile(params=SmoothProfileParams(inner_angle=inner_angles[index],
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
        Test chamfer for concave corners with a sharp angle.
        """
        context = Context()
        scad = Scad(context=context)
        body = Polygon(points=[Vector2(0, 50), Vector2(20, 0), Vector2(0, 40), Vector2(-20, 0)])

        inner_angles = body.inner_angles(context)
        normal_angles = body.normal_angles(context)
        nodes = body.primary
        body = InteriorChamfer(skew_length=5.0,
                               inner_angle=inner_angles[0],
                               normal_angle=normal_angles[0],
                               position=nodes[0],
                               child=body)
        body = InteriorChamfer(skew_length=5.0,
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
        Test chamfer for concave corners with an oblique angle.
        """
        context = Context()
        scad = Scad(context=context)
        body = Polygon(points=[Vector2(0, 10), Vector2(20, 0), Vector2(0, 5), Vector2(-20, 0)])

        inner_angles = body.inner_angles(context)
        normal_angles = body.normal_angles(context)
        nodes = body.primary
        body = InteriorChamfer(skew_length=5.0,
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

        body = InteriorChamfer(skew_length=5.0,
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
