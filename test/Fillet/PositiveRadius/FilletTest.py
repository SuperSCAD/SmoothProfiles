import random

from super_scad.boolean.Compound import Compound
from super_scad.boolean.Difference import Difference
from super_scad.boolean.Union import Union
from super_scad.d2.Polygon import Polygon
from super_scad.scad.Context import Context
from super_scad.scad.Scad import Scad
from super_scad.transformation.Paint import Paint
from super_scad.type import Vector2, Vector3
from super_scad_smooth_profile.SmoothProfileParams import SmoothProfileParams

from super_scad_smooth_profiles.Fillet import Fillet
from test.ScadTestCase import ScadTestCase


class FilletTest(ScadTestCase):
    """
    Testcases for Fillet with positive radius.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def create_profile(self, side=None):
        """
        Creates a fillet profile.
        """
        return Fillet(radius=10.0, side=side)

    # ------------------------------------------------------------------------------------------------------------------
    def test_convexity(self):
        """
        Test the convexity of a fillet.
        """
        profile = Fillet(radius=5.0)
        self.assertEqual(profile.convexity, 2)

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

        self.assertAlmostEqual(5.0, profile.offset1(inner_angle=90.0), places=4)
        self.assertAlmostEqual(5.0, profile.offset2(inner_angle=90.0), places=4)

        # Oblique angle.
        self.assertAlmostEqual(2.0711, profile.offset1(inner_angle=135.0), places=4)
        self.assertAlmostEqual(2.0711, profile.offset2(inner_angle=135.0), places=4)

        self.assertAlmostEqual(5.0, profile.offset1(inner_angle=270.0), places=4)
        self.assertAlmostEqual(5.0, profile.offset2(inner_angle=270.0), places=4)

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

        profile = Fillet(radius=0.0)
        params = SmoothProfileParams(inner_angle=inner_angles[2],
                                     normal_angle=normal_angles[2],
                                     position=nodes[2])
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
    def test_polygon0(self) -> None:
        """
        Test for profile as polygon.
        """
        context = Context()

        profile = Fillet(radius=0.0)
        params = SmoothProfileParams(inner_angle=180.0,
                                     normal_angle=random.uniform(0, 360.0),
                                     position=Vector2.origin)
        polygon = profile.create_polygon(context=context, params=params)
        self.assertTrue(profile.is_internal)
        self.assertFalse(profile.is_external)
        self.assertFalse(profile.side)
        self.assertEqual(polygon, [params.position])

        profile = Fillet(radius=0.0)
        params = SmoothProfileParams(inner_angle=random.uniform(0, 360.0),
                                     normal_angle=random.uniform(0, 360.0),
                                     position=Vector2.origin)
        polygon = profile.create_polygon(context=context, params=params)
        self.assertTrue(profile.is_internal)
        self.assertFalse(profile.is_external)
        self.assertFalse(profile.side)
        self.assertEqual(polygon, [params.position])

        profile = Fillet(radius=0.0)
        params = SmoothProfileParams(inner_angle=random.uniform(0, 360.0),
                                     normal_angle=random.uniform(0, 360.0),
                                     position=Vector2.origin)
        polygon = profile.create_polygon(context=context, params=params)
        self.assertTrue(profile.is_internal)
        self.assertFalse(profile.is_external)
        self.assertFalse(profile.side)
        self.assertEqual(polygon, [params.position])

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
