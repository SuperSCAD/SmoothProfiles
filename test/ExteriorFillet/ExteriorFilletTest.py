from super_scad.d2.Polygon import Polygon
from super_scad.scad.Context import Context
from super_scad.scad.Scad import Scad
from super_scad.type import Vector2
from super_scad_smooth_profile.SmoothProfileParams import SmoothProfileParams

from super_scad_smooth_profiles.ExteriorFillet import ExteriorFillet
from test.ScadTestCase import ScadTestCase


class ExteriorFilletTest(ScadTestCase):
    """
    Testcases for ExteriorFillet.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def test_sizes_side1(self):
        """
        Test the size of a fillet on the first side.
        """
        # Positive radius.
        profile = ExteriorFillet(radius=5.0, side=1)

        # Sharp angle.
        self.assertAlmostEqual(12.0711, profile.offset1(inner_angle=45.0), places=4)
        self.assertEqual(0.0, profile.offset2(inner_angle=45.0))

        # Oblique angle.
        self.assertAlmostEqual(2.0711, profile.offset1(inner_angle=135.0), places=4)
        self.assertEqual(0.0, profile.offset2(inner_angle=135.0))

        # Concave corner.
        self.assertEqual(0.0, profile.offset1(inner_angle=315.0))
        self.assertEqual(0.0, profile.offset2(inner_angle=315.0))

        # Zero angle.
        self.assertEqual(0.0, profile.offset1(inner_angle=180.0))
        self.assertEqual(0.0, profile.offset2(inner_angle=180.0))

        # Negative radius.
        profile = ExteriorFillet(radius=-5.0, side=1)
        self.assertAlmostEqual(5.0, profile.offset1(inner_angle=45.0), places=4)
        self.assertEqual(0.0, profile.offset2(inner_angle=45.0))

        # Zero radius.
        profile = ExteriorFillet(radius=0.0, side=1)
        self.assertEqual(0.0, profile.offset1(inner_angle=45.0))
        self.assertEqual(0.0, profile.offset2(inner_angle=315.0))

    # ------------------------------------------------------------------------------------------------------------------
    def test_sizes_side2(self):
        """
        Test the size of a fillet on the second side.
        """
        # Positive radius.
        profile = ExteriorFillet(radius=5.0, side=2)

        # Sharp angle.
        self.assertEqual(0.0, profile.offset1(inner_angle=45.0))
        self.assertAlmostEqual(12.0711, profile.offset2(inner_angle=45.0), places=4)

        # Oblique angle.
        self.assertEqual(0.0, profile.offset1(inner_angle=135.0))
        self.assertAlmostEqual(2.0711, profile.offset2(inner_angle=135.0), places=4)

        # Concave corner.
        self.assertEqual(0.0, profile.offset1(inner_angle=315.0))
        self.assertEqual(0.0, profile.offset2(inner_angle=315.0))

        # Zero angle.
        self.assertEqual(0.0, profile.offset1(inner_angle=180.0))
        self.assertEqual(0.0, profile.offset2(inner_angle=180.0))

        # Negative radius.
        profile = ExteriorFillet(radius=-5.0, side=2)
        self.assertEqual(0.0, profile.offset1(inner_angle=45.0))
        self.assertAlmostEqual(5.0, profile.offset2(inner_angle=45.0), places=4)

        # Zero radius.
        profile = ExteriorFillet(radius=0.0, side=2)
        self.assertEqual(0.0, profile.offset1(inner_angle=45.0))
        self.assertEqual(0.0, profile.offset2(inner_angle=315.0))

    # ------------------------------------------------------------------------------------------------------------------
    def test_exterior_fillet_pos(self) -> None:
        """
        Test an exterior fillet with positive radius.
        """
        context = Context(fs=0.1, fa=1.0, eps=0.1)
        scad = Scad(context=context)
        body = Polygon(points=[Vector2.origin, Vector2(2, 20), Vector2(18, 20), Vector2(20, 0)],
                       extend_sides_by_eps={1})

        profiles = [ExteriorFillet(radius=5.0, side=2),
                    ExteriorFillet(radius=5.0, side=1),
                    ExteriorFillet(radius=5.0, side=2),
                    ExteriorFillet(radius=5.0, side=1)]

        inner_angles = body.inner_angles(context)
        normal_angles = body.normal_angles(context)
        extend_sides_by_eps = body.extend_sides_by_eps
        nodes = body.primary

        n = len(nodes)
        for index in range(n):
            extend_side_by_eps1 = (index - 1) % n in extend_sides_by_eps
            extend_side_by_eps2 = index in extend_sides_by_eps

            params = SmoothProfileParams(inner_angle=inner_angles[index],
                                         normal_angle=normal_angles[index],
                                         position=nodes[index],
                                         side1_is_extended_by_eps=extend_side_by_eps1,
                                         side2_is_extended_by_eps=extend_side_by_eps2)

            body = profiles[index].create_smooth_profile(params=params, child=body)

        path_actual, path_expected = self.paths()
        scad.run_super_scad(body, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_exterior_fillet_neg(self) -> None:
        """
        Test an exterior fillet with negative radius.
        """
        context = Context(fs=0.1, fa=1.0, eps=0.1)
        scad = Scad(context=context)
        body = Polygon(points=[Vector2.origin, Vector2(2, 20), Vector2(18, 20), Vector2(20, 0)],
                       extend_sides_by_eps={1})

        profiles = [ExteriorFillet(radius=-5.0, side=2),
                    ExteriorFillet(radius=-5.0, side=1),
                    ExteriorFillet(radius=-5.0, side=2),
                    ExteriorFillet(radius=-5.0, side=1)]

        inner_angles = body.inner_angles(context)
        normal_angles = body.normal_angles(context)
        extend_sides_by_eps = body.extend_sides_by_eps
        nodes = body.primary

        n = len(nodes)
        for index in range(n):
            extend_side_by_eps1 = (index - 1) % n in extend_sides_by_eps
            extend_side_by_eps2 = index in extend_sides_by_eps

            params = SmoothProfileParams(inner_angle=inner_angles[index],
                                         normal_angle=normal_angles[index],
                                         position=nodes[index],
                                         side1_is_extended_by_eps=extend_side_by_eps1,
                                         side2_is_extended_by_eps=extend_side_by_eps2)

            body = profiles[index].create_smooth_profile(params=params, child=body)

        path_actual, path_expected = self.paths()
        scad.run_super_scad(body, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def test_exterior_fillet_zero(self) -> None:
        """
        Test an exterior fillet with zero radius.
        """
        context = Context(fs=0.1, fa=1.0, eps=0.1)
        scad = Scad(context=context)
        body = Polygon(points=[Vector2.origin, Vector2(2, 20), Vector2(18, 20), Vector2(20, 0)],
                       extend_sides_by_eps={1})

        profiles = [ExteriorFillet(radius=0.0, side=2),
                    ExteriorFillet(radius=0.0, side=1),
                    ExteriorFillet(radius=0.0, side=2),
                    ExteriorFillet(radius=0.0, side=1)]

        inner_angles = body.inner_angles(context)
        normal_angles = body.normal_angles(context)
        extend_sides_by_eps = body.extend_sides_by_eps
        nodes = body.primary

        n = len(nodes)
        for index in range(n):
            extend_side_by_eps1 = (index - 1) % n in extend_sides_by_eps
            extend_side_by_eps2 = index in extend_sides_by_eps

            params = SmoothProfileParams(inner_angle=inner_angles[index],
                                         normal_angle=normal_angles[index],
                                         position=nodes[index],
                                         side1_is_extended_by_eps=extend_side_by_eps1,
                                         side2_is_extended_by_eps=extend_side_by_eps2)

            body = profiles[index].create_smooth_profile(params=params, child=body)

        path_actual, path_expected = self.paths()
        scad.run_super_scad(body, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

# ----------------------------------------------------------------------------------------------------------------------
