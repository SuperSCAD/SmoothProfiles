import math
from typing import Any, Dict, List, Tuple

from super_scad.boolean.Empty import Empty
from super_scad.d2.Polygon import Polygon
from super_scad.scad.ArgumentValidator import ArgumentValidator
from super_scad.scad.Context import Context
from super_scad.scad.ScadWidget import ScadWidget
from super_scad.transformation.Translate2D import Translate2D
from super_scad.type import Vector2
from super_scad.type.Angle import Angle
from super_scad_smooth_profile.EdgeOrder import EdgeOrder
from super_scad_smooth_profile.SmoothProfile3D import SmoothProfile3D
from super_scad_smooth_profile.SmoothProfileParams import SmoothProfileParams


class _ExteriorChamferWidget(ScadWidget):
    """
    Applies an exterior chamfer to an edge at a node.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self,
                 *,
                 skew_length: float | None = None,
                 skew_height: float | None = None,
                 side: EdgeOrder,
                 inner_angle: float,
                 normal_angle: float,
                 position: Vector2,
                 preceding_edge_is_extended_by_eps: bool,
                 succeeding_edge_is_extended_by_eps: bool):
        """
        Object constructor.

        :param skew_length: The length of the skew side of the chamfer.
        :param skew_height: The height of the chamfer, measured perpendicular for the skew size to the node.
        :param side: The edge on which the exterior chamfer must be applied.
        :param inner_angle: The inner angle between the two edges.
        :param normal_angle: The normal angle of the two edges, i.e., the angle of the vector that lies exactly between
                             the two edges and with origin at the node.
        :param preceding_edge_is_extended_by_eps: Whether the preceding edge is extended by eps.
        :param succeeding_edge_is_extended_by_eps: Whether the succeeding edge is extended by eps.
        """
        ScadWidget.__init__(self)

        self._skew_length = skew_length
        """
        The length of the skew side of the chamfer.
        """

        self._skew_height = skew_height
        """
        The height of the chamfer, measured perpendicular for the skew size to the node.
        """

        self._side: EdgeOrder = side
        """
        The edge on which the exterior chamfer must be applied. 
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

        self.__validate_arguments(locals())

    # ------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def __validate_arguments(args: Dict[str, Any]) -> None:
        """
        Validates the arguments supplied to the constructor of this profile.
        """
        admission = ArgumentValidator(args)
        admission.validate_exclusive({'skew_length'}, {'skew_height'})

    # ------------------------------------------------------------------------------------------------------------------
    @property
    def skew_height(self) -> float:
        """
        The skew_height of the chamfer, measured perpendicular for the skew size to the node.
        """
        if self._skew_height is None:
            outer_angle = 180.0 - self._inner_angle
            self._skew_height = 0.5 * self.skew_length / math.tan(math.radians(0.5 * outer_angle))

        return self._skew_height

    # ------------------------------------------------------------------------------------------------------------------
    @property
    def skew_length(self) -> float:
        """
        The length of the skew side of the chamfer.
        """
        if self._skew_length is None:
            outer_angle = 180.0 - self._inner_angle
            self._skew_length = 2.0 * self.skew_height * math.tan(math.radians(0.5 * outer_angle))

        return self._skew_length

    # ------------------------------------------------------------------------------------------------------------------
    def build(self, context: Context) -> ScadWidget:
        """
        Builds a SuperSCAD widget.

        :param context: The build context.
        """
        if self.skew_length > 0.0:
            if self._side == EdgeOrder.PRECEDING:
                polygon = self._build_polygon(self._normal_angle,
                                              True,
                                              self._succeeding_edge_is_extended_by_eps)

                return polygon

            if self._side == EdgeOrder.SUCCEEDING:
                polygon = self._build_polygon(Angle.normalize(self._normal_angle - 180.0),
                                              self._preceding_edge_is_extended_by_eps,
                                              True)

                return polygon

            raise ValueError(f'Unknown side: {self._side}.')

        return Empty()

    # ------------------------------------------------------------------------------------------------------------------
    def _build_polygon(self,
                       normal_angle: float,
                       extent_by_eps0: bool,
                       extent_by_eps2: bool) -> ScadWidget:
        """
        Returns a masking polygon.

        :param normal_angle: The normal angle of the two edges.
        """
        p2 = Vector2.from_polar(self.skew_height, normal_angle - 90.0) + \
             Vector2.from_polar(0.5 * self.skew_length, normal_angle)
        p3 = p2 + Vector2.from_polar(self.skew_length, normal_angle - 180.0)

        return Translate2D(vector=self._position,
                           child=Polygon(points=[Vector2.origin, p2, p3],
                                         extend_by_eps_sides=[extent_by_eps0, False, extent_by_eps2]))


# ----------------------------------------------------------------------------------------------------------------------
class _InteriorChamferWidget(ScadWidget):
    """
    Applies a chamfer to the edges at a node.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self,
                 *,
                 skew_length: float | None = None,
                 skew_height: float | None = None,
                 inner_angle: float,
                 normal_angle: float,
                 position: Vector2):
        """
        Object constructor.

        :param skew_length: The length of the skew side of the chamfer.
        :param skew_height: The height of the chamfer, measured perpendicular for the skew size to the node.
        :param inner_angle: The inner angle between the two edges.
        :param normal_angle: The normal angle of the two edges, i.e., the angle of the vector that lies exactly between
                             the two edges and with origin at the node.
        """
        ScadWidget.__init__(self)

        self._skew_length = skew_length
        """
        The length of the skew side of the chamfer.
        """

        self._skew_height = skew_height
        """
        The height of the chamfer, measured perpendicular for the skew size to the node.
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

        self.__validate_arguments(locals())

    # ------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def __validate_arguments(args: Dict[str, Any]) -> None:
        """
        Validates the arguments supplied to the constructor of this profile.
        """
        validator = ArgumentValidator(args)
        validator.validate_exclusive({'skew_length'}, {'skew_height'})

    # ------------------------------------------------------------------------------------------------------------------
    @property
    def skew_height(self) -> float:
        """
        The skew_height of the chamfer, measured perpendicular for the skew size to the node.
        """
        if self._skew_height is None:
            inner_angle = self._inner_angle
            if inner_angle > 180:
                inner_angle = 360.0 - inner_angle
            self._skew_height = 0.5 * self.skew_length / math.tan(math.radians(0.5 * inner_angle))

        return self._skew_height

    # ------------------------------------------------------------------------------------------------------------------
    @property
    def skew_length(self) -> float:
        """
        The length of the skew side of the chamfer.
        """
        if self._skew_length is None:
            inner_angle = self._inner_angle
            if inner_angle > 180:
                inner_angle = 360.0 - inner_angle
            self._skew_length = 2.0 * self.skew_height * math.tan(math.radians(0.5 * inner_angle))

        return self._skew_length

    # ------------------------------------------------------------------------------------------------------------------
    def build(self, context: Context) -> ScadWidget:
        """
        Builds a SuperSCAD widget.

        :param context: The build context.
        """
        if self._inner_angle < 180.0:
            # The corner is convex.
            return self._build_polygon(self._normal_angle)

        if self._inner_angle > 180.0:
            # The corner is concave.
            return self._build_polygon(Angle.normalize(self._normal_angle - 180.0))

        return Empty()

    # ------------------------------------------------------------------------------------------------------------------
    def _build_polygon(self, normal_angle: float) -> ScadWidget:
        """
        Returns a masking polygon.

        :param normal_angle: The normal angle of the two edges.
        """
        p1 = self._position
        p2 = self._position + \
             Vector2.from_polar(self.skew_height, normal_angle) + \
             Vector2.from_polar(0.5 * self.skew_length, normal_angle + 90.0)
        p3 = p2 + Vector2.from_polar(self.skew_length, normal_angle - 90.0)

        return Polygon(points=[p1, p2, p3], extend_by_eps_sides={0, 2})


# ----------------------------------------------------------------------------------------------------------------------
class Chamfer(SmoothProfile3D):
    """
    A profile that produces exterior chamfer smoothing profile widgets.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self,
                 *,
                 skew_length: float | None = None,
                 skew_height: float | None = None,
                 side: EdgeOrder | None = None):
        """
        Object constructor.

        :param skew_length: The length of the skew side of the chamfer.
        :param skew_height: The skew_height of the chamfer, measured perpendicular for the skew size to the node.
        :param side: The edge on which the exterior chamfer must be applied.
        """
        self._skew_length: float = skew_length
        """
        The length of the chamfer.
        """

        self._skew_height: float = skew_height
        """
        The height of the chamfer.
        """

        self._side: EdgeOrder | None = side
        """
        The edge on which the exterior chamfer must be applied. 
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
    def skew_height(self, *, inner_angle: float) -> float:
        """
        The skew_height of the chamfer, measured perpendicular for the skew size to the node.

        :param inner_angle: The inner angle between the two edges.
        """
        if self._skew_height is not None:
            return self._skew_height

        if self._side is None:
            if inner_angle > 180.0:
                inner_angle = 360.0 - inner_angle

            return 0.5 * self._skew_length / math.tan(math.radians(0.5 * inner_angle))

        outer_angle = 180.0 - inner_angle

        return 0.5 * self._skew_length / math.tan(math.radians(0.5 * outer_angle))

    # ------------------------------------------------------------------------------------------------------------------
    def skew_length(self, *, inner_angle: float) -> float:
        """
        The length of the skew side of the chamfer.

        :param inner_angle: The inner angle between the two edges.
        """
        if self._skew_length is not None:
            return self._skew_length

        if self._side is None:
            if inner_angle > 180.0:
                inner_angle = 360.0 - inner_angle

            return 2.0 * self._skew_height * math.tan(math.radians(0.5 * inner_angle))

        outer_angle = 180.0 - inner_angle

        return 2.0 * self._skew_height * math.tan(math.radians(0.5 * outer_angle))

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
            if inner_angle == 180.0:
                return 0.0

            if inner_angle > 180.0:
                inner_angle = 360.0 - inner_angle

            return self.skew_height(inner_angle=inner_angle) / math.cos(math.radians(0.5 * inner_angle))

        if self._side == EdgeOrder.PRECEDING:
            if inner_angle == 180.0:
                return 0.0

            outer_angle = 180.0 - inner_angle

            return self.skew_height(inner_angle=inner_angle) / math.cos(math.radians(0.5 * outer_angle))

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
            return self.offset_preceding_edge(inner_angle=inner_angle)

        if self._side == EdgeOrder.SUCCEEDING:
            if inner_angle == 180.0:
                return 0.0

            outer_angle = 180.0 - inner_angle

            return self.skew_height(inner_angle=inner_angle) / math.cos(math.radians(0.5 * outer_angle))

        if self._side == EdgeOrder.PRECEDING:
            return 0.0

        raise ValueError(f'Unknown side: {self._side}.')

    # ------------------------------------------------------------------------------------------------------------------
    def create_smooth_profiles(self, *, params: SmoothProfileParams) -> Tuple[ScadWidget | None, ScadWidget | None]:
        """
        Returns a smoothing profile widget creating a chamfer.

        :param params: The parameters for the smooth profile widget.
        """
        if params.inner_angle == 180.0 or self._skew_height == 0.0 or self._skew_length == 0.0:
            return None, None

        if self._side is None:
            widget = _InteriorChamferWidget(skew_length=self._skew_length,
                                            skew_height=self._skew_height,
                                            inner_angle=params.inner_angle,
                                            normal_angle=params.normal_angle,
                                            position=params.position)

            if params.inner_angle < 180.0:
                return widget, None

            return None, widget

        widget = _ExteriorChamferWidget(skew_length=self._skew_length,
                                        skew_height=self._skew_height,
                                        side=self._side,
                                        inner_angle=params.inner_angle,
                                        normal_angle=params.normal_angle,
                                        position=params.position,
                                        preceding_edge_is_extended_by_eps=params.preceding_edge_is_extended_by_eps,
                                        succeeding_edge_is_extended_by_eps=params.succeeding_edge_is_extended_by_eps)

        return None, widget

    # ------------------------------------------------------------------------------------------------------------------
    def create_polygon(self, *, context: Context, params: SmoothProfileParams) -> List[Vector2]:
        """
        Returns the profile as a polygon.

        :param context: The build context.
        :param params: The parameters for the smooth profile widget.
        """
        if params.inner_angle == 180.0 or self._skew_height == 0.0 or self._skew_length == 0.0:
            return [params.position]

        if params.inner_angle < 180.0:
            if self._side is None:
                return self._create_polygon(context, params.inner_angle, params.normal_angle, params.position)

            if self._side == EdgeOrder.PRECEDING:
                return list(reversed(self._create_polygon(context,
                                                          180.0 - params.inner_angle,
                                                          params.normal_angle - 90.0,
                                                          params.position)))

            if self._side == EdgeOrder.SUCCEEDING:
                return list(reversed(self._create_polygon(context,
                                                          180.0 - params.inner_angle,
                                                          params.normal_angle + 90.0,
                                                          params.position)))

        if params.inner_angle > 180.0:
            if self._side is None:
                return list(reversed(self._create_polygon(context,
                                                          360.0 - params.inner_angle,
                                                          params.normal_angle - 180.0,
                                                          params.position)))

        raise ValueError(f'Unexpected parameters: f{params} for fillet: {self}.')

    # ------------------------------------------------------------------------------------------------------------------
    def _create_polygon(self,
                        context: Context,
                        inner_angle: float,
                        normal_angle: float,
                        position: Vector2) -> List[Vector2]:
        """
        Returns the profile as a polygon.

        :param context: The build context.
        :param inner_angle: The inner angle between the edges.
        :param normal_angle: The normal angle of the two edges.
        :param position: The position of the node.
        """
        if self._skew_height is not None:
            skew_height = self._skew_height
            skew_length = 2.0 * self._skew_height * math.tan(math.radians(0.5 * inner_angle))
        else:
            skew_height = 0.5 * self._skew_length / math.tan(math.radians(0.5 * inner_angle))
            skew_length = self._skew_length

        p1 = position + \
             Vector2.from_polar(skew_height, normal_angle) + \
             Vector2.from_polar(0.5 * skew_length, normal_angle - 90.0)
        p2 = p1 + Vector2.from_polar(skew_length, normal_angle + 90.0)

        return [p1, p2]

# ----------------------------------------------------------------------------------------------------------------------
