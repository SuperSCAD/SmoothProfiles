import math
from typing import List, Tuple

from super_scad.boolean.Difference import Difference
from super_scad.boolean.Empty import Empty
from super_scad.d2.Circle import Circle
from super_scad.d2.Polygon import Polygon
from super_scad.scad.Context import Context
from super_scad.scad.ScadWidget import ScadWidget
from super_scad.transformation.Position2D import Position2D
from super_scad.transformation.Translate2D import Translate2D
from super_scad.type import Vector2
from super_scad.type.Angle import Angle
from super_scad.util.Radius2Sides4n import Radius2Sides4n
from super_scad_circle_plus.CircleSector import CircleSector
from super_scad_smooth_profile.EdgeOrder import EdgeOrder
from super_scad_smooth_profile.SmoothProfile3D import SmoothProfile3D
from super_scad_smooth_profile.SmoothProfileParams import SmoothProfileParams


class _ExteriorFilletWidget(ScadWidget):
    """
    Applies an exterior fillet to an edge at a node.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self,
                 *,
                 radius: float,
                 side: EdgeOrder,
                 inner_angle: float,
                 normal_angle: float,
                 position: Vector2,
                 preceding_edge_is_extended_by_eps: bool,
                 succeeding_edge_is_extended_by_eps: bool):
        """
        Object constructor.

        :param radius: The radius of the fillet.
        :param side: The edge on which the exterior fillet must be applied.
        :param inner_angle: The inner angle between the two edges.
        :param normal_angle: The normal angle of the two edges, i.e., the angle of the vector that lies exactly between
                             the two edges and with origin at the node.
        :param preceding_edge_is_extended_by_eps: Whether the preceding edge is extended by eps.
        :param succeeding_edge_is_extended_by_eps: Whether the succeeding edge is extended by eps.
        """
        ScadWidget.__init__(self)

        self._radius: float = radius
        """
        The radius of the fillet.
        """

        self._side: EdgeOrder = side
        """
        The edge on which the exterior fillet must be applied. 
        """

        self._inner_angle: float = Angle.normalize(inner_angle)
        """
        The inner angle between the vertices at the node.
        """

        self._normal_angle: float = Angle.normalize(normal_angle)
        """
        The normal angle of the two edges.
        """

        self._position: Vector2 = position
        """
        The position of the node.
        """

        self._preceding_edge_is_extended_by_eps = preceding_edge_is_extended_by_eps
        """
        Whether the preceding edge is extended by eps.
        """

        self._succeeding_edge_is_extended_by_eps = succeeding_edge_is_extended_by_eps
        """
        Whether the succeeding edge is extended by eps.
        """

    # ------------------------------------------------------------------------------------------------------------------
    def build(self, context: Context) -> ScadWidget:
        """
        Builds a SuperSCAD widget.

        :param context: The build context.
        """
        Radius2Sides4n.r2sides4n(context, self._radius)
        if self._side == EdgeOrder.PRECEDING:
            if self._radius > 0.0:
                # The corner is concave.
                alpha = math.radians(180 - self._inner_angle) / 2.0

                return self._build_fillet_pos(alpha,
                                              0.0,
                                              True,
                                              self._succeeding_edge_is_extended_by_eps)

            if self._radius < 0.0:
                # The corner is concave.
                return self._build_fillet_neg(0.0,
                                              self._succeeding_edge_is_extended_by_eps,
                                              True)

        elif self._side == EdgeOrder.SUCCEEDING:
            if self._radius > 0.0:
                # The corner is concave.
                alpha = math.radians(180 - self._inner_angle) / 2.0

                return self._build_fillet_pos(alpha,
                                              180.0,
                                              self._preceding_edge_is_extended_by_eps,
                                              True)

            if self._radius < 0.0:
                # The corner is concave.
                return self._build_fillet_neg(180.0,
                                              True,
                                              self._preceding_edge_is_extended_by_eps)
        else:
            raise ValueError(f'Unknown side: {self._side}.')

        return Empty()

    # ------------------------------------------------------------------------------------------------------------------
    def _build_fillet_pos(self,
                          alpha: float,
                          rotation: float,
                          extent_by_eps0: bool,
                          extent_by_eps2: bool) -> ScadWidget:
        """
        Builds a fillet with a positive radius.

        :param alpha: The angle of the fillet.
        :param rotation: The (additional) rotation required to rotate the fillet in its correct position.
        :param extent_by_eps0: Whether the first side of the masking polygon must be extended by eps.
        :param extent_by_eps2: Whether the last side of the masking polygon must be extended by eps.
        """
        x = self._radius * math.cos(alpha)
        y = self._radius * math.cos(alpha) ** 2 / math.sin(alpha)
        polygon = Polygon(points=[Vector2.origin, Vector2(x, -y), Vector2(-x, -y)],
                          extend_by_eps_sides=[extent_by_eps0, False, extent_by_eps2],
                          convexity=2)
        circle = Circle(radius=self._radius, fn4n=True)
        fillet = Difference(children=[polygon,
                                      Translate2D(vector=Vector2(0.0, -self._radius / math.sin(alpha)),
                                                  child=circle)])

        return Position2D(angle=self._normal_angle + rotation,
                          vector=self._position,
                          child=fillet)

    # ------------------------------------------------------------------------------------------------------------------
    def _build_fillet_neg(self,
                          rotation: float,
                          extent_by_eps1: bool,
                          extent_by_eps2: bool) -> ScadWidget:
        """
        Builds a fillet with a negative radius.

        :param rotation: The (additional) rotation required to rotate the fillet in its correct position.
        :param extent_by_eps1: Whether the first side of the masking polygon must be extended by eps.
        :param extent_by_eps2: Whether the last side of the masking polygon must be extended by eps.
        """
        return Position2D(angle=rotation,
                          vector=self._position,
                          child=CircleSector(start_angle=self._normal_angle + 0.5 * self._inner_angle + 180.0,
                                             end_angle=self._normal_angle - 0.5 * self._inner_angle,
                                             radius=-self._radius,
                                             extend_by_eps_legs=(extent_by_eps1, extent_by_eps2),
                                             fn4n=True))


# ----------------------------------------------------------------------------------------------------------------------
class _InteriorFilletWidget(ScadWidget):
    """
    Applies a rounding to edges at a node.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self,
                 *,
                 radius: float,
                 inner_angle: float,
                 normal_angle: float,
                 position: Vector2):
        """
        Object constructor.

        :param radius: The radius of the fillet.
        :param inner_angle: Inner angle of the corner.
        :param normal_angle: The normal angle of the two edges, i.e., the angle of the vector that lies exactly between
                             the two edges and with origin at the node.
        """
        ScadWidget.__init__(self)

        self._radius: float = radius
        """
        The radius of the fillet.
        """

        self._inner_angle: float = Angle.normalize(inner_angle)
        """
        The inner angle between the vertices at the node.
        """

        self._normal_angle: float = Angle.normalize(normal_angle)
        """
        The normal angle of the two edges.
        """

        self._position: Vector2 = position
        """
        The position of the node.
        """

    # ------------------------------------------------------------------------------------------------------------------
    def build(self, context: Context) -> ScadWidget:
        """
        Builds a SuperSCAD widget.

        :param context: The build context.
        """
        Radius2Sides4n.r2sides4n(context, self._radius)
        if self._radius > 0.0 and self._inner_angle < 180.0:
            # The corner is convex.
            alpha = math.radians(self._inner_angle) / 2.0
            fillet = self._build_fillet_pos(alpha, 90.0)

            return fillet

        if self._radius > 0.0 and self._inner_angle > 180.0:
            # The corner is concave.
            alpha = math.radians(360.0 - self._inner_angle) / 2.0
            fillet = self._build_fillet_pos(alpha, -90.0)

            return fillet

        if self._radius < 0.0:
            # Negative radius.
            fillet = self._build_fillet_neg()

            return fillet

        return Empty()

    # ------------------------------------------------------------------------------------------------------------------
    def _build_fillet_pos(self,
                          alpha: float,
                          rotation: float) -> ScadWidget:
        """
        Builds a fillet with a positive radius.

        :param alpha: The angle of the fillet.
        """
        x = self._radius * math.cos(alpha)
        y = self._radius * math.cos(alpha) ** 2 / math.sin(alpha)
        polygon = Polygon(points=[Vector2.origin, Vector2(x, -y), Vector2(-x, -y)],
                          extend_by_eps_sides={0, 2},
                          convexity=2)
        circle = Circle(radius=self._radius, fn4n=True)
        fillet = Difference(children=[polygon,
                                      Translate2D(vector=Vector2(0.0, -self._radius / math.sin(alpha)),
                                                  child=circle)])

        return Position2D(angle=self._normal_angle + rotation,
                          vector=self._position,
                          child=fillet)

    # ------------------------------------------------------------------------------------------------------------------
    def _build_fillet_neg(self) -> ScadWidget:
        """
        Builds a fillet with a negative radius.
        """
        return Translate2D(vector=self._position,
                           child=CircleSector(start_angle=self._normal_angle + 0.5 * self._inner_angle,
                                              end_angle=self._normal_angle - 0.5 * self._inner_angle,
                                              radius=-self._radius,
                                              extend_by_eps_legs=True,
                                              fn4n=True))


# ----------------------------------------------------------------------------------------------------------------------
class Fillet(SmoothProfile3D):
    """
    A profile that produces fillet smoothing profile widgets.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self, *, radius: float, side: EdgeOrder | None = None):
        """
        Object constructor.

        :param radius: The radius of the fillet.
        :param side: The edge on which the exterior fillet must be applied.
        """

        self._radius: float = radius
        """
        The radius of the fillet.
        """

        self._side: EdgeOrder | None = side
        """
        The edge on which the exterior fillet must be applied. 
        """

    # ------------------------------------------------------------------------------------------------------------------
    @property
    def is_external(self) -> bool:
        """
        Returns whether the fillet is an external fillet.
        """
        return self._side is not None

    # ------------------------------------------------------------------------------------------------------------------
    @property
    def is_internal(self) -> bool:
        """
        Returns whether the fillet is an internal fillet.
        """
        return self._side is None

    # ------------------------------------------------------------------------------------------------------------------
    @property
    def side(self) -> EdgeOrder | None:
        """
        Returns the edge on which the exterior fillet must be applied.
        """
        return self._side

    # ------------------------------------------------------------------------------------------------------------------
    @property
    def convexity(self) -> int | None:
        """
        Return the convexity of the profile.
        """
        return 2

    # ------------------------------------------------------------------------------------------------------------------
    def offset_preceding_edge(self, *, inner_angle: float) -> float:
        """
        Returns the offset of the smooth profile on the preceding edge.

        :param inner_angle: The inner angle between the two edges.
        """
        if self._side is None:
            if self._radius > 0.0 and inner_angle < 180.0:
                # The corner is convex.
                alpha = math.radians(inner_angle) / 2.0

                return self._radius * math.cos(alpha) / math.sin(alpha)

            if self._radius > 0.0 and inner_angle > 180.0:
                # The corner is concave.
                alpha = math.radians(360.0 - inner_angle) / 2.0

                return self._radius * math.cos(alpha) / math.sin(alpha)

            if self._radius < 0.0:
                # Negative radius.
                return -self._radius

            return 0.0

        if self._side == EdgeOrder.PRECEDING:
            # The corner is convex.
            if self._radius > 0.0 and inner_angle < 180.0:
                # The corner is convex.
                alpha = math.radians(inner_angle) / 2.0

                return self._radius * math.cos(alpha) / math.sin(alpha)

            if self._radius > 0.0 and inner_angle > 180.0:
                # The corner is concave.
                print('Warning: Not possible to apply an exterior fillet on a concave corner.')

                return 0.0

            if self._radius < 0.0:
                # Negative radius.
                return -self._radius

            return 0.0

        if self._side == EdgeOrder.SUCCEEDING:
            return 0.0

        raise ValueError(f'Unknown side: {self._side}.')

    # ------------------------------------------------------------------------------------------------------------------
    def offset_succeeding_edge(self, *, inner_angle: float) -> float:
        """
        Returns the offset of the smooth profile on the succeeding edge.

        :param inner_angle: The inner angle between the two edges.
        """
        if self._side is None:
            if self._radius > 0.0 and inner_angle < 180.0:
                # The corner is convex.
                alpha = math.radians(inner_angle) / 2.0

                return self._radius * math.cos(alpha) / math.sin(alpha)

            if self._radius > 0.0 and inner_angle > 180.0:
                # The corner is concave.
                alpha = math.radians(360.0 - inner_angle) / 2.0

                return self._radius * math.cos(alpha) / math.sin(alpha)

            if self._radius < 0.0:
                # Negative radius.
                return -self._radius

            return 0.0

        if self._side == EdgeOrder.SUCCEEDING:
            if self._radius > 0.0 and inner_angle < 180.0:
                # The corner is convex.
                alpha = math.radians(inner_angle) / 2.0

                return self._radius * math.cos(alpha) / math.sin(alpha)

            if self._radius > 0.0 and inner_angle > 180.0:
                # The corner is concave.
                print('Warning: Not possible to apply an exterior fillet on a concave corner.')

                return 0.0

            if self._radius < 0.0:
                # Negative radius.
                return -self._radius

            return 0.0

        if self._side == EdgeOrder.PRECEDING:
            return 0.0

        raise ValueError(f'Unknown side: {self._side}.')

    # ------------------------------------------------------------------------------------------------------------------
    def create_smooth_profiles(self, *, params: SmoothProfileParams) -> Tuple[ScadWidget | None, ScadWidget | None]:
        """
        Creates widget for creating fillet on an edge.

        :param params: The parameters for the smooth profile widget.
        """
        if self._radius == 0.0 or self._radius > 0.0 and params.inner_angle == 180.0:
            negative, positive = None, None

        elif self._side is None:
            # Interior profile between both edges.
            widget = _InteriorFilletWidget(radius=self._radius,
                                           inner_angle=params.inner_angle,
                                           normal_angle=params.normal_angle,
                                           position=params.position)

            if params.inner_angle < 180.0:
                # Convex corner.
                if self._radius > 0.0:
                    negative, positive = widget, None
                else:
                    negative, positive = None, widget
            else:
                # Concave corner.
                negative, positive = None, widget

        else:
            # Exterior profile on one edge.
            widget = _ExteriorFilletWidget(radius=self._radius,
                                           side=self._side,
                                           inner_angle=params.inner_angle,
                                           normal_angle=params.normal_angle,
                                           position=params.position,
                                           preceding_edge_is_extended_by_eps=params.preceding_edge_is_extended_by_eps,
                                           succeeding_edge_is_extended_by_eps=params.succeeding_edge_is_extended_by_eps)

            negative, positive = None, widget

        return negative, positive

    # ------------------------------------------------------------------------------------------------------------------
    def create_polygon(self, *, context: Context, params: SmoothProfileParams) -> List[Vector2]:
        """
        Returns the profile as a polygon.

        :param context: The build context.
        :param params: The parameters for the smooth profile widget.
        """
        if self._radius == 0.0 or self._radius > 0.0 and params.inner_angle == 180.0:
            return [params.position]

        if params.inner_angle < 180.0:
            if self._side is None and self._radius > 0.0:
                alpha = math.radians(0.5 * params.inner_angle)
                position = params.position + Vector2.from_polar(self._radius / math.sin(alpha), params.normal_angle)
                return self._create_polygon(context,
                                            position,
                                            params.normal_angle - 0.5 * params.inner_angle - 90.0,
                                            180.0 - params.inner_angle,
                                            -1.0)

            if self._side is None and self._radius < 0.0:
                return self._create_polygon(context,
                                            params.position,
                                            params.normal_angle - 0.5 * params.inner_angle,
                                            360.0 - params.inner_angle,
                                            -1.0)

            if self._side == EdgeOrder.PRECEDING and self._radius > 0.0:
                angle_rotation = params.inner_angle
                alpha = math.radians(90.0 - 0.5 * params.inner_angle)
                position = params.position + Vector2.from_polar(self._radius / math.sin(alpha),
                                                                params.normal_angle - 90.0)
                return self._create_polygon(context,
                                            position,
                                            params.normal_angle - 0.5 * params.inner_angle + 90.0,
                                            angle_rotation,
                                            1.0)

            if self._side == EdgeOrder.PRECEDING and self._radius < 0.0:
                angle_rotation = 180.0 - params.inner_angle
                return self._create_polygon(context,
                                            params.position,
                                            params.normal_angle - 0.5 * params.inner_angle,
                                            angle_rotation,
                                            -1.0)

            if self._side == EdgeOrder.SUCCEEDING and self._radius > 0.0:
                angle_rotation = params.inner_angle
                alpha = math.radians(90.0 - 0.5 * params.inner_angle)
                position = params.position + Vector2.from_polar(self._radius / math.sin(alpha),
                                                                params.normal_angle + 90.0)
                return self._create_polygon(context,
                                            position,
                                            params.normal_angle - 0.5 * params.inner_angle - 90.0,
                                            angle_rotation,
                                            1.0)

            if self._side == EdgeOrder.SUCCEEDING and self._radius < 0.0:
                angle_rotation = 180.0 - params.inner_angle
                return self._create_polygon(context,
                                            params.position,
                                            params.normal_angle - 0.5 * params.inner_angle - 180.0,
                                            angle_rotation,
                                            -1.0)

        if params.inner_angle > 180.0:
            if self._side is None and self._radius > 0.0:
                alpha = math.radians(0.5 * params.inner_angle - 180.0)
                position = params.position + Vector2.from_polar(self._radius / math.sin(alpha),
                                                                params.normal_angle)
                return self._create_polygon(context,
                                            position,
                                            params.normal_angle - 0.5 * params.inner_angle + 90.0,
                                            params.inner_angle - 180.0,
                                            1.0)

            if self._side is None and self._radius < 0.0:
                return self._create_polygon(context,
                                            params.position,
                                            params.normal_angle - 0.5 * params.inner_angle,
                                            360.0 - params.inner_angle,
                                            -1.0)

        raise ValueError(f'Unexpected parameters: f{params} for fillet: {self}.')

    # ------------------------------------------------------------------------------------------------------------------
    def _create_polygon(self,
                        context: Context,
                        center: Vector2,
                        angle_start: float,
                        angle_rotation: float,
                        angle_sign: float) -> List[Vector2]:
        """
        Returns the profile as a polygon.

        :param context: The build context.
        :param angle_start: The start angle fillet.
        :param angle_rotation: The angle of rotation of the fillet.
        :param angle_sign: The direction of rotation of the fillet, i.e. -1.0 clockwise, +1.0 counterclockwise.
        """
        nodes = []

        radius = abs(self._radius)
        angle_start = Angle.normalize(angle_start)
        angle_rotation = Angle.normalize(angle_rotation)

        # Carefully align nodes with fn4n=True in InteriorFilletWidget._build_fillet_pos()
        fn = Radius2Sides4n.r2sides4n(context, radius)
        steps = int(fn * angle_rotation / 360.0)
        step_angle = 360.0 / fn

        nodes.append(center + Vector2.from_polar(radius, angle_start))
        if steps % 2 == 0:
            n = steps + 1
            angle = angle_start + 0.5 * angle_sign * abs((angle_rotation - steps * step_angle))
        else:
            n = steps
            angle = angle_start + 0.5 * angle_sign * abs((angle_rotation - (steps - 1) * step_angle))
        for i in range(n):
            nodes.append(center + Vector2.from_polar(radius, angle))
            angle += angle_sign * step_angle
        nodes.append(center + Vector2.from_polar(radius, angle_start + angle_sign * angle_rotation))

        return nodes

# ----------------------------------------------------------------------------------------------------------------------
