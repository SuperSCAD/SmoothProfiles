from super_scad.boolean.Compound import Compound
from super_scad.scad.Context import Context
from super_scad.scad.Scad import Scad
from super_scad.transformation.Paint import Paint
from super_scad.type import Vector2, Vector3
from super_scad_smooth_profile.SmoothProfileParams import SmoothProfileParams

from super_scad_smooth_profiles.Chamfer import Chamfer
from super_scad_smooth_profiles.InteriorChamferWidget import InteriorChamferWidget
from test.ScadTestCase import ScadTestCase


class ChamferTest(ScadTestCase):
    """
    Testcases for chamfers.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def create_profile(self, side=None):
        """
        Creates a chamfer profile.
        """
        return Chamfer(skew_height=10.0, side=side)

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
        p2 = p1 + Vector2.from_polar(profile.offset1(inner_angle=inner_angle),
                                                 90.0 + 0.5 * inner_angle)

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
    def test_polygon_outer_sharp_interior(self) -> None:
        """
        Test for interior profile at an outer corner as polygon.
        """
        context = Context(fn=11, vpr=Vector3.origin)

        profile = self.create_profile()

        self.assertTrue(profile.is_internal)
        self.assertFalse(profile.is_external)
        self.assertIsNone(profile.side)

        params = SmoothProfileParams(inner_angle=75.0,
                                     normal_angle=-123.0,
                                     position=Vector2.origin)

        negative, positive = profile.create_smooth_profiles(params=params)
        body = [Paint(color='green', child=negative if negative is not None else positive)]

        polygon = profile.create_polygon(context=context, params=params)
        body += self.mark_nodes(params, polygon)

        body = Compound(children=body)

        scad = Scad(context=context)
        path_actual, path_expected = self.paths()
        scad.run_super_scad(body, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_polygon_outer_oblique_interior(self) -> None:
        """
        Test for interior profile at an outer corner as polygon.
        """
        context = Context(fn=11, vpr=Vector3.origin)

        profile = self.create_profile()

        self.assertTrue(profile.is_internal)
        self.assertFalse(profile.is_external)
        self.assertIsNone(profile.side)

        inner_angle = 105.0
        normal_angle = 123.0
        position = Vector2.origin
        params = SmoothProfileParams(inner_angle=inner_angle,
                                     normal_angle=normal_angle,
                                     position=position)

        negative, positive = profile.create_smooth_profiles(params=params)
        body = [Paint(color='green', child=negative if negative is not None else positive)]

        polygon = profile.create_polygon(context=context, params=params)
        body += self.mark_nodes(params, polygon)

        body = Compound(children=body)

        scad = Scad(context=context)
        path_actual, path_expected = self.paths()
        scad.run_super_scad(body, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_polygon_outer_right_interior(self) -> None:
        """
        Test for interior profile at an outer corner as polygon.
        """
        context = Context(fn=11, vpr=Vector3.origin)

        profile = self.create_profile()

        self.assertTrue(profile.is_internal)
        self.assertFalse(profile.is_external)
        self.assertIsNone(profile.side)

        inner_angle = 90.0
        normal_angle = 240.0
        position = Vector2.origin
        params = SmoothProfileParams(inner_angle=inner_angle,
                                     normal_angle=normal_angle,
                                     position=position)

        negative, positive = profile.create_smooth_profiles(params=params)
        body = [Paint(color='green', child=negative if negative is not None else positive)]

        polygon = profile.create_polygon(context=context, params=params)
        body += self.mark_nodes(params, polygon)

        body = Compound(children=body)

        scad = Scad(context=context)
        path_actual, path_expected = self.paths()
        scad.run_super_scad(body, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_polygon_outer_oblique_exterior_side1(self) -> None:
        """
        Test for exterior profile at an outer corner at side 1 as polygon.
        """
        context = Context(fn=11, vpr=Vector3.origin)

        profile = self.create_profile(side=1)

        self.assertFalse(profile.is_internal)
        self.assertTrue(profile.is_external)
        self.assertEqual(profile.side, 1)

        inner_angle = 115.0
        normal_angle = 200.0
        position = Vector2.origin
        params = SmoothProfileParams(inner_angle=inner_angle,
                                     normal_angle=normal_angle,
                                     position=position)

        negative, positive = profile.create_smooth_profiles(params=params)
        body = [Paint(color='green', child=negative if negative is not None else positive)]

        polygon = profile.create_polygon(context=context, params=params)
        body += self.mark_nodes(params, polygon)

        body = Compound(children=body)

        scad = Scad(context=context)
        path_actual, path_expected = self.paths()
        scad.run_super_scad(body, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_polygon_outer_oblique_exterior_side2(self) -> None:
        """
        Test for exterior profile at an outer corner at side 1 as polygon.
        """
        context = Context(fn=11, vpr=Vector3.origin)

        profile = self.create_profile(side=2)

        self.assertFalse(profile.is_internal)
        self.assertTrue(profile.is_external)
        self.assertEqual(profile.side, 2)

        params = SmoothProfileParams(inner_angle=115.0,
                                     normal_angle=200.0,
                                     position=Vector2.origin)

        negative, positive = profile.create_smooth_profiles(params=params)
        body = [Paint(color='green', child=negative if negative is not None else positive)]

        polygon = profile.create_polygon(context=context, params=params)
        body += self.mark_nodes(params, polygon)

        body = Compound(children=body)

        scad = Scad(context=context)
        path_actual, path_expected = self.paths()
        scad.run_super_scad(body, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_polygon_outer_sharp_exterior_side1(self) -> None:
        """
        Test for exterior profile at an outer corner at side 1 as polygon.
        """
        context = Context(fn=11, vpr=Vector3.origin)

        profile = self.create_profile(side=1)

        self.assertFalse(profile.is_internal)
        self.assertTrue(profile.is_external)
        self.assertEqual(profile.side, 1)

        inner_angle = 63.0
        normal_angle = 290.0
        position = Vector2.origin
        params = SmoothProfileParams(inner_angle=inner_angle,
                                     normal_angle=0,
                                     position=position)

        negative, positive = profile.create_smooth_profiles(params=params)
        body = [Paint(color='green', child=negative if negative is not None else positive)]

        polygon = profile.create_polygon(context=context, params=params)
        body += self.mark_nodes(params, polygon)

        body = Compound(children=body)

        scad = Scad(context=context)
        path_actual, path_expected = self.paths()
        scad.run_super_scad(body, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_polygon_outer_sharp_exterior_side2(self) -> None:
        """
        Test for exterior profile at an outer corner at side 1 as polygon.
        """
        context = Context(fn=11, vpr=Vector3.origin)

        profile = self.create_profile(side=2)

        self.assertFalse(profile.is_internal)
        self.assertTrue(profile.is_external)
        self.assertEqual(profile.side, 2)

        inner_angle = 63.0
        normal_angle = 290.0
        position = Vector2.origin
        params = SmoothProfileParams(inner_angle=inner_angle,
                                     normal_angle=normal_angle,
                                     position=position)

        negative, positive = profile.create_smooth_profiles(params=params)
        body = [Paint(color='green', child=negative if negative is not None else positive)]

        polygon = profile.create_polygon(context=context, params=params)
        body += self.mark_nodes(params, polygon)

        body = Compound(children=body)

        scad = Scad(context=context)
        path_actual, path_expected = self.paths()
        scad.run_super_scad(body, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_polygon_outer_right_exterior_side1(self) -> None:
        """
        Test for exterior profile at an outer corner at side 1 as polygon.
        """
        context = Context(fn=11, vpr=Vector3.origin)

        profile = self.create_profile(side=1)

        self.assertFalse(profile.is_internal)
        self.assertTrue(profile.is_external)
        self.assertEqual(profile.side, 1)

        inner_angle = 90.0
        normal_angle = 33.0
        position = Vector2.origin
        params = SmoothProfileParams(inner_angle=inner_angle,
                                     normal_angle=normal_angle,
                                     position=position)

        negative, positive = profile.create_smooth_profiles(params=params)
        body = [Paint(color='green', child=negative if negative is not None else positive)]

        polygon = profile.create_polygon(context=context, params=params)
        body += self.mark_nodes(params, polygon)

        body = Compound(children=body)

        scad = Scad(context=context)
        path_actual, path_expected = self.paths()
        scad.run_super_scad(body, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_polygon_outer_right_exterior_side2(self) -> None:
        """
        Test for exterior profile at an outer corner at side 1 as polygon.
        """
        context = Context(fn=11, vpr=Vector3.origin)

        profile = self.create_profile(side=2)

        self.assertFalse(profile.is_internal)
        self.assertTrue(profile.is_external)
        self.assertEqual(profile.side, 2)

        inner_angle = 90.0
        normal_angle = 33.0
        position = Vector2.origin
        params = SmoothProfileParams(inner_angle=inner_angle,
                                     normal_angle=normal_angle,
                                     position=position)

        negative, positive = profile.create_smooth_profiles(params=params)
        body = [Paint(color='green', child=negative if negative is not None else positive)]

        polygon = profile.create_polygon(context=context, params=params)
        body += self.mark_nodes(params, polygon)

        body = Compound(children=body)

        scad = Scad(context=context)
        path_actual, path_expected = self.paths()
        scad.run_super_scad(body, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_polygon_inner_sharp_interior(self) -> None:
        """
        Test for interior profile at an inner corner as polygon.
        """
        context = Context(fn=11, vpr=Vector3.origin)

        profile = self.create_profile()

        self.assertTrue(profile.is_internal)
        self.assertFalse(profile.is_external)
        self.assertIsNone(profile.side)

        inner_angle = 300.0
        normal_angle = 36.1
        position = Vector2.origin
        params = SmoothProfileParams(inner_angle=inner_angle,
                                     normal_angle=normal_angle,
                                     position=position)

        negative, positive = profile.create_smooth_profiles(params=params)
        body = [Paint(color='green', child=negative if negative is not None else positive)]

        polygon = profile.create_polygon(context=context, params=params)
        body += self.mark_nodes(params, polygon)

        body = Compound(children=body)

        scad = Scad(context=context)
        path_actual, path_expected = self.paths()
        scad.run_super_scad(body, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_polygon_inner_oblique_interior(self) -> None:
        """
        Test for interior profile at an inner corner as polygon.
        """
        context = Context(fn=13, vpr=Vector3.origin)

        profile = self.create_profile()

        self.assertTrue(profile.is_internal)
        self.assertFalse(profile.is_external)
        self.assertIsNone(profile.side)

        inner_angle = 260.0
        normal_angle = 105.1
        position = Vector2.origin
        params = SmoothProfileParams(inner_angle=inner_angle,
                                     normal_angle=normal_angle,
                                     position=position)

        negative, positive = profile.create_smooth_profiles(params=params)
        body = [Paint(color='green', child=negative if negative is not None else positive)]

        polygon = profile.create_polygon(context=context, params=params)
        body += self.mark_nodes(params, polygon)

        body = Compound(children=body)

        scad = Scad(context=context)
        path_actual, path_expected = self.paths()
        scad.run_super_scad(body, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

# ----------------------------------------------------------------------------------------------------------------------
