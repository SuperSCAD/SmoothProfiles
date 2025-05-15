from super_scad.boolean.Difference import Difference
from super_scad.boolean.Union import Union
from super_scad.d2.Polygon import Polygon
from super_scad.scad.Context import Context
from super_scad.scad.Scad import Scad
from super_scad.type import Vector2
from super_scad_smooth_profile.SmoothProfileParams import SmoothProfileParams

from super_scad_smooth_profiles.Chamfer import Chamfer
from super_scad_smooth_profiles.ExteriorChamferWidget import ExteriorChamferWidget
from test.ScadTestCase import ScadTestCase


class ExteriorChamferTest(ScadTestCase):
    """
    Testcases for ExteriorChamfer.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def test_convexity(self):
        """
        Test the convexity of a chamfer.
        """
        profile = Chamfer(skew_length=5.0, side=1)
        self.assertEqual(profile.convexity, 2)

    # ------------------------------------------------------------------------------------------------------------------
    def test_sizes_side1(self):
        """
        Test the size of a chamfer on the first side.
        """
        # Positive radius.
        profile = Chamfer(skew_length=5.0, side=1)

        # Sharp angle.
        self.assertAlmostEqual(2.7060, profile.offset1(inner_angle=45.0), places=4)
        self.assertEqual(0.0, profile.offset2(inner_angle=45.0))

        # Oblique angle.
        self.assertAlmostEqual(6.5328, profile.offset1(inner_angle=135.0), places=4)
        self.assertEqual(0.0, profile.offset2(inner_angle=135.0))

        # Zero angle.
        self.assertEqual(0.0, profile.offset1(inner_angle=180.0))
        self.assertEqual(0.0, profile.offset2(inner_angle=180.0))

        # Zero skew length.
        profile = Chamfer(skew_length=0.0, side=1)
        self.assertEqual(0.0, profile.offset1(inner_angle=45.0))
        self.assertEqual(0.0, profile.offset2(inner_angle=315.0))

    # ------------------------------------------------------------------------------------------------------------------
    def test_sizes_side2(self):
        """
        Test the size of a chamfer on the second side.
        """
        # Positive radius.
        profile = Chamfer(skew_length=5.0, side=2)

        # Sharp angle.
        self.assertEqual(0.0, profile.offset1(inner_angle=45.0))
        self.assertAlmostEqual(2.7060, profile.offset2(inner_angle=45.0), places=4)

        # Oblique angle.
        self.assertEqual(0.0, profile.offset1(inner_angle=135.0))
        self.assertAlmostEqual(6.5328, profile.offset2(inner_angle=135.0), places=4)

        # Zero angle.
        self.assertEqual(0.0, profile.offset1(inner_angle=180.0))
        self.assertEqual(0.0, profile.offset2(inner_angle=180.0))

        # Zero skew length.
        profile = Chamfer(skew_length=0.0, side=2)
        self.assertEqual(0.0, profile.offset1(inner_angle=45.0))
        self.assertEqual(0.0, profile.offset2(inner_angle=315.0))

    # ------------------------------------------------------------------------------------------------------------------
    def test_skew_length(self):
        """
        Test chamfer given the length of the skew side.
        """
        profile = Chamfer(skew_length=5.0, side=1)

        # Sharp angle.
        inner_angle = 45.0

        p1 = Vector2(0.5 * profile.skew_length(inner_angle=inner_angle), 0.0)
        p2 = p1 + Vector2.from_polar(profile.offset1(inner_angle=inner_angle),                                                 90.0 + 0.5 * (180.0 - inner_angle))

        self.assertAlmostEqual(5.0, profile.skew_length(inner_angle=inner_angle))
        self.assertAlmostEqual(0.0, p2.x)
        self.assertAlmostEqual(p2.y, profile.skew_height(inner_angle=inner_angle))

        # Oblige angle.
        inner_angle = 135.0

        p1 = Vector2(0.5 * profile.skew_length(inner_angle=inner_angle), 0.0)
        p2 = p1 + Vector2.from_polar(profile.offset1(inner_angle=inner_angle),                                                 90.0 + 0.5 * (180.0 - inner_angle))

        self.assertAlmostEqual(5.0, profile.skew_length(inner_angle=inner_angle))
        self.assertAlmostEqual(0.0, p2.x)
        self.assertAlmostEqual(p2.y, profile.skew_height(inner_angle=inner_angle))

    # ------------------------------------------------------------------------------------------------------------------
    def test_skew_height(self):
        """
        Test chamfer given the height of the skew side.
        """
        profile = Chamfer(skew_height=5.0, side=2)

        # Sharp angle.
        inner_angle = 45.0

        p1 = Vector2(0.5 * profile.skew_length(inner_angle=inner_angle), 0.0)
        p2 = p1 + Vector2.from_polar(profile.offset2(inner_angle=inner_angle),                                                 90.0 + 0.5 * (180.0 - inner_angle))

        self.assertAlmostEqual(5.0, profile.skew_height(inner_angle=inner_angle))
        self.assertAlmostEqual(0.0, p2.x)
        self.assertAlmostEqual(p2.y, profile.skew_height(inner_angle=inner_angle))

        negative, positive = profile.create_smooth_profiles(params=SmoothProfileParams(inner_angle=inner_angle,
                                                                                       normal_angle=0.0,
                                                                                       position=Vector2.origin))

        self.assertIsInstance(positive, ExteriorChamferWidget)
        self.assertAlmostEqual(profile.skew_height(inner_angle=inner_angle), positive.skew_height)
        self.assertAlmostEqual(profile.skew_length(inner_angle=inner_angle), positive.skew_length)

        negative, positive = profile.create_smooth_profiles(params=SmoothProfileParams(inner_angle=inner_angle,
                                                                                       normal_angle=0.0,
                                                                                       position=Vector2.origin))
        self.assertIsInstance(positive, ExteriorChamferWidget)
        self.assertAlmostEqual(profile.skew_height(inner_angle=inner_angle), positive.skew_height)
        self.assertAlmostEqual(profile.skew_length(inner_angle=inner_angle), positive.skew_length)

        # Oblige angle.
        inner_angle = 135.0

        p1 = Vector2(0.5 * profile.skew_length(inner_angle=inner_angle), 0.0)
        p2 = p1 + Vector2.from_polar(profile.offset2(inner_angle=inner_angle),                                                 90.0 + 0.5 * (180.0 - inner_angle))

        self.assertAlmostEqual(5.0, profile.skew_height(inner_angle=inner_angle))
        self.assertAlmostEqual(0.0, p2.x)
        self.assertAlmostEqual(p2.y, profile.skew_height(inner_angle=inner_angle))

        negative, positive = profile.create_smooth_profiles(params=SmoothProfileParams(inner_angle=inner_angle,
                                                                                       normal_angle=0.0,
                                                                                       position=Vector2.origin))
        self.assertIsInstance(positive, ExteriorChamferWidget)
        self.assertAlmostEqual(profile.skew_height(inner_angle=inner_angle), positive.skew_height)
        self.assertAlmostEqual(profile.skew_length(inner_angle=inner_angle), positive.skew_length)

    # ------------------------------------------------------------------------------------------------------------------
    def test_exterior_chamfer_pos(self) -> None:
        """
        Test an exterior chamfer with positive radius.
        """
        context = Context(eps=0.1)
        scad = Scad(context=context)
        points = [Vector2.origin, Vector2(2, 20), Vector2(18, 20), Vector2(20, 0)]
        body = Polygon(points=points,
                       extend_by_eps_sides={1})

        profiles = [Chamfer(skew_length=5.0, side=2),
                    Chamfer(skew_height=3.0, side=1),
                    Chamfer(skew_height=3.0, side=2),
                    Chamfer(skew_length=5.0, side=1)]

        inner_angles = body.inner_angles(context)
        normal_angles = body.normal_angles(context)
        extend_by_eps_sides = body.extend_by_eps_sides
        nodes = body.primary

        n = len(nodes)
        for index in range(n):
            extend_side_by_eps1 = (index - 1) % n in extend_by_eps_sides
            extend_side_by_eps2 = index in extend_by_eps_sides

            params = SmoothProfileParams(inner_angle=inner_angles[index],
                                         normal_angle=normal_angles[index],
                                         position=nodes[index],
                                         edge1_is_extended_by_eps=extend_side_by_eps1,
                                         edge2_is_extended_by_eps=extend_side_by_eps2)

            negative, positive = profiles[index].create_smooth_profiles(params=params)
            if negative:
                body = Difference(children=[body, negative])
            if positive:
                body = Union(children=[body, positive])

        path_actual, path_expected = self.paths()
        scad.run_super_scad(body, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_exterior_chamfer_zero(self) -> None:
        """
        Test an exterior chamfer without chamfer.
        """
        context = Context(eps=0.1)
        scad = Scad(context=context)
        points = [Vector2.origin, Vector2(2, 20), Vector2(18, 20), Vector2(20, 0)]
        body = Polygon(points=points,
                       extend_by_eps_sides={1})

        factories = [Chamfer(skew_length=0.0, side=2),
                     Chamfer(skew_height=0.0, side=1),
                     Chamfer(skew_height=0.0, side=2),
                     Chamfer(skew_length=0.0, side=1)]

        inner_angles = body.inner_angles(context)
        normal_angles = body.normal_angles(context)
        extend_by_eps_sides = body.extend_by_eps_sides
        nodes = body.primary

        n = len(nodes)
        for index in range(n):
            extend_side_by_eps1 = (index - 1) % n in extend_by_eps_sides
            extend_side_by_eps2 = index in extend_by_eps_sides

            params = SmoothProfileParams(inner_angle=inner_angles[index],
                                         normal_angle=normal_angles[index],
                                         position=nodes[index],
                                         edge1_is_extended_by_eps=extend_side_by_eps1,
                                         edge2_is_extended_by_eps=extend_side_by_eps2)

            negative, positive = factories[index].create_smooth_profiles(params=params)
            if negative:
                body = Difference(children=[body, negative])
            if positive:
                body = Union(children=[body, positive])

        path_actual, path_expected = self.paths()
        scad.run_super_scad(body, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

# ----------------------------------------------------------------------------------------------------------------------
