from super_scad.boolean.Difference import Difference
from super_scad.boolean.Union import Union
from super_scad.d2.Polygon import Polygon
from super_scad.scad.Context import Context
from super_scad.scad.Scad import Scad
from super_scad.type import Vector2
from super_scad_smooth_profile.SmoothProfileParams import SmoothProfileParams

from super_scad_smooth_profiles.Chamfer import Chamfer
from super_scad_smooth_profiles.InteriorChamferWidget import InteriorChamferWidget
from test.ScadTestCase import ScadTestCase


class InteriorChamferTest(ScadTestCase):
    """
    Testcases for chamfers.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def test_convexity(self):
        """
        Test the convexity of a chamfer.
        """
        profile = Chamfer(skew_length=5.0)
        self.assertEqual(profile.convexity, 2)

    # ------------------------------------------------------------------------------------------------------------------
    def test_sizes(self):
        """
        Test the size of a fillet.
        """
        # Positive radius.
        profile = Chamfer(skew_length=5.0)

        # Sharp angle.
        self.assertAlmostEqual(6.5328, profile.offset1(inner_angle=45.0), places=4)
        self.assertAlmostEqual(6.5328, profile.offset2(inner_angle=45.0), places=4)

        # Oblique angle.
        self.assertAlmostEqual(2.7060, profile.offset1(inner_angle=135.0), places=4)
        self.assertAlmostEqual(2.7060, profile.offset2(inner_angle=135.0), places=4)

        # Concave corner.
        self.assertAlmostEqual(6.5328, profile.offset1(inner_angle=315.0), places=4)
        self.assertAlmostEqual(6.5328, profile.offset2(inner_angle=315.0), places=4)

        # Zero angle.
        self.assertEqual(0.0, profile.offset1(inner_angle=180.0))
        self.assertEqual(0.0, profile.offset2(inner_angle=180.0))

        # Zero skew length.
        profile = Chamfer(skew_length=0.0)
        self.assertEqual(0.0, profile.offset1(inner_angle=45.0))
        self.assertEqual(0.0, profile.offset2(inner_angle=315.0))

    # ------------------------------------------------------------------------------------------------------------------
    def test_skew_length(self):
        """
        Test chamfer given the length of the skew side.
        """
        profile = Chamfer(skew_length=5.0)

        # Sharp angle.
        inner_angle = 45.0

        p1 = Vector2(0.5 * profile.skew_length(inner_angle=inner_angle), 0.0)
        p2 = p1 + Vector2.from_polar(profile.offset1(inner_angle=inner_angle),                                                 90.0 + 0.5 * inner_angle)

        self.assertAlmostEqual(5.0, profile.skew_length(inner_angle=inner_angle))
        self.assertAlmostEqual(0.0, p2.x)
        self.assertAlmostEqual(p2.y, profile.skew_height(inner_angle=inner_angle))
        self.assertAlmostEqual(profile.offset1(inner_angle=inner_angle), profile.offset2(inner_angle=inner_angle))

        # Concave corner.
        self.assertAlmostEqual(profile.skew_height(inner_angle=45.0), profile.skew_height(inner_angle=315.0))
        self.assertAlmostEqual(profile.skew_length(inner_angle=45.0), profile.skew_length(inner_angle=315.0))

        # Oblige angle.
        inner_angle = 135.0

        p1 = Vector2(0.5 * profile.skew_length(inner_angle=inner_angle), 0.0)
        p2 = p1 + Vector2.from_polar(profile.offset1(inner_angle=inner_angle),                                                 90.0 + 0.5 * inner_angle)

        self.assertAlmostEqual(5.0, profile.skew_length(inner_angle=inner_angle))
        self.assertAlmostEqual(0.0, p2.x)
        self.assertAlmostEqual(p2.y, profile.skew_height(inner_angle=inner_angle))
        self.assertAlmostEqual(profile.offset1(inner_angle=inner_angle), profile.offset2(inner_angle=inner_angle))

    # ------------------------------------------------------------------------------------------------------------------
    def test_skew_height(self):
        """
        Test chamfer given the height of the skew side.
        """
        profile = Chamfer(skew_height=5.0)

        # Sharp angle.
        inner_angle = 45.0

        p1 = Vector2(0.5 * profile.skew_length(inner_angle=inner_angle), 0.0)
        p2 = p1 + Vector2.from_polar(profile.offset1(inner_angle=inner_angle), 90.0 + 0.5 * inner_angle)

        self.assertAlmostEqual(5.0, profile.skew_height(inner_angle=inner_angle))
        self.assertAlmostEqual(0.0, p2.x)
        self.assertAlmostEqual(p2.y, profile.skew_height(inner_angle=inner_angle))
        self.assertAlmostEqual(profile.offset1(inner_angle=inner_angle), profile.offset2(inner_angle=inner_angle))

        negative, positive = profile.create_smooth_profiles(params=SmoothProfileParams(inner_angle=inner_angle,
                                                                                       normal_angle=0.0,
                                                                                       position=Vector2.origin))
        self.assertIsInstance(negative, InteriorChamferWidget)
        self.assertAlmostEqual(profile.skew_height(inner_angle=inner_angle), negative.skew_height)
        self.assertAlmostEqual(profile.skew_length(inner_angle=inner_angle), negative.skew_length)

        # Concave corner.
        inner_angle = 315.0
        self.assertAlmostEqual(profile.skew_height(inner_angle=45.0), profile.skew_height(inner_angle=inner_angle))
        self.assertAlmostEqual(profile.skew_length(inner_angle=45.0), profile.skew_length(inner_angle=inner_angle))

        negative, positive = profile.create_smooth_profiles(params=SmoothProfileParams(inner_angle=inner_angle,
                                                                                       normal_angle=0.0,
                                                                                       position=Vector2.origin))
        self.assertIsInstance(positive, InteriorChamferWidget)
        self.assertAlmostEqual(profile.skew_height(inner_angle=inner_angle), positive.skew_height)
        self.assertAlmostEqual(profile.skew_length(inner_angle=inner_angle), positive.skew_length)

        # Oblige angle.
        inner_angle = 135.0

        p1 = Vector2(0.5 * profile.skew_length(inner_angle=inner_angle), 0.0)
        p2 = p1 + Vector2.from_polar(profile.offset1(inner_angle=inner_angle), 90.0 + 0.5 * inner_angle)

        self.assertAlmostEqual(5.0, profile.skew_height(inner_angle=inner_angle))
        self.assertAlmostEqual(0.0, p2.x)
        self.assertAlmostEqual(p2.y, profile.skew_height(inner_angle=inner_angle))
        self.assertAlmostEqual(profile.offset1(inner_angle=inner_angle), profile.offset2(inner_angle=inner_angle))

        negative, positive = profile.create_smooth_profiles(params=SmoothProfileParams(inner_angle=inner_angle,
                                                                                       normal_angle=0.0,
                                                                                       position=Vector2.origin))
        self.assertIsInstance(negative, InteriorChamferWidget)
        self.assertAlmostEqual(profile.skew_height(inner_angle=inner_angle), negative.skew_height)
        self.assertAlmostEqual(profile.skew_length(inner_angle=inner_angle), negative.skew_length)

    # ------------------------------------------------------------------------------------------------------------------
    def test_convex(self) -> None:
        """
        Test chamfer for convex corners with sharp and oblique angles.
        """
        context = Context()
        scad = Scad(context=context)
        body = Polygon(points=[Vector2(0, 10), Vector2(-20, 0), Vector2(0, -10), Vector2(20, 0)])

        profile = Chamfer(skew_length=5.0)
        inner_angles = body.inner_angles(context)
        normal_angles = body.normal_angles(context)
        nodes = body.primary
        for index in range(len(nodes)):
            params = SmoothProfileParams(inner_angle=inner_angles[index],
                                         normal_angle=normal_angles[index],
                                         position=nodes[index])
            negative, positive = profile.create_smooth_profiles(params=params)
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

        profile = Chamfer(skew_length=5.0)

        index = 0
        params = SmoothProfileParams(inner_angle=inner_angles[index],
                                     normal_angle=normal_angles[index],
                                     position=nodes[index])
        negative, positive = profile.create_smooth_profiles(params=params)
        if negative:
            body = Difference(children=[body, negative])
        if positive:
            body = Union(children=[body, positive])

        index = 2
        params = SmoothProfileParams(inner_angle=inner_angles[index],
                                     normal_angle=normal_angles[index],
                                     position=nodes[index])
        negative, positive = profile.create_smooth_profiles(params=params)
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
    def test_concave_oblique(self) -> None:
        """
        Test chamfer for concave corners with an oblique angle.
        """
        context = Context()
        body = Polygon(points=[Vector2(0, 10), Vector2(20, 0), Vector2(0, 5), Vector2(-20, 0)])

        inner_angles = body.inner_angles(context)
        normal_angles = body.normal_angles(context)
        nodes = body.primary

        profile = Chamfer(skew_length=5.0)

        index = 2
        params = SmoothProfileParams(inner_angle=inner_angles[index],
                                     normal_angle=normal_angles[index],
                                     position=nodes[index])
        negative, positive = profile.create_smooth_profiles(params=params)
        if negative:
            body = Difference(children=[body, negative])
        if positive:
            body = Union(children=[body, positive])

        scad = Scad(context=context)
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

        body = Polygon(points=[Vector2.origin, Vector2(0, 20), Vector2(10, 20), Vector2(20, 20), Vector2(20.0, 0.0)])

        inner_angles = body.inner_angles(context)
        normal_angles = body.normal_angles(context)
        nodes = body.primary

        profile = Chamfer(skew_length=5.0)

        index = 2
        self.assertAlmostEqual(inner_angles[index], 180.0)
        self.assertTrue(profile.is_internal)
        self.assertFalse(profile.is_external)
        self.assertFalse(profile.side)

        params = SmoothProfileParams(inner_angle=inner_angles[index],
                                     normal_angle=normal_angles[index],
                                     position=nodes[index])
        negative, positive = profile.create_smooth_profiles(params=params)
        if negative:
            body = Difference(children=[body, negative])
        if positive:
            body = Union(children=[body, positive])

        scad = Scad(context=context)
        path_actual, path_expected = self.paths()
        scad.run_super_scad(body, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

# ----------------------------------------------------------------------------------------------------------------------
