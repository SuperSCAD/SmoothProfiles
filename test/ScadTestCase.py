import inspect
import unittest
from abc import ABC
from pathlib import Path
from typing import List

from super_scad.d2.Circle import Circle
from super_scad.scad.ScadWidget import ScadWidget
from super_scad.transformation.Paint import Paint
from super_scad.transformation.Translate2D import Translate2D
from super_scad.type import Vector2
from super_scad.type.Color import Color
from super_scad_circle_sector.CircleSector import CircleSector
from super_scad_smooth_profile.SmoothProfileParams import SmoothProfileParams


class ScadTestCase(unittest.TestCase, ABC):
    """
    Parent test case for SuperSCAD test cases.
    """

    # ------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def paths():
        """
        Returns a path to the actual generated OpenSCAD code and the expected OpenSCAD code.
        """
        directory = Path(inspect.stack()[1][1]).parent
        method = inspect.stack()[1][3]
        path_actual = Path.joinpath(directory, method + '.actual.scad')
        path_expected = Path.joinpath(directory, method + '.expected.scad')

        return path_actual, path_expected

    # ------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def mark_nodes(params: SmoothProfileParams, polygon: List[Vector2]) -> List[ScadWidget]:
        """
        Marks the nodes of a polygon.
        """
        markers = [Paint(color=Color('yellow', alpha=0.3),
                         child=Translate2D(vector=params.position,
                                           child=CircleSector(
                                                   start_angle=params.normal_angle - 0.5 * params.inner_angle,
                                                   end_angle=params.normal_angle + 0.5 * params.inner_angle,
                                                   radius=25.0)))]
        for index in range(len(polygon)):
            circle = Paint(color='red' if index == 0 else 'orange' if index == 1 else 'green' if index == 2 else 'blue',
                           child=Translate2D(vector=polygon[index],
                                             child=Circle(diameter=0.5, fn=36)))
            markers.append(circle)

        return markers

# ----------------------------------------------------------------------------------------------------------------------
