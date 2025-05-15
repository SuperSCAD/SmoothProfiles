// Unit of length: Unit.MM
union()
{
   translate(v = [-20.0, 0.0, 0.0])
   {
      polygon(points = [[0.0, 0.0], [0.0, 20.0], [20.0, 20.0], [20.0, 0.0]]);
   }
   translate(v = [20.0, 0.0, 0.0])
   {
      polygon(points = [[0.0, 0.0], [0.0, 20.0], [20.0, 20.0], [20.0, 0.0]]);
   }
}
