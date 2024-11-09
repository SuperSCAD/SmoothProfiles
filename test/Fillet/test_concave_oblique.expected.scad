// Unit of length: Unit.MM
$fa = 1.0;
$fs = 0.1;

union()
{
   polygon(points = [[0.0, 10.0], [20.0, 0.0], [0.0, 5.0], [-20.0, 0.0]]);
   translate(v = [0.0, 5.0])
   {
      difference()
      {
         polygon(points = [[0.0, 0.01], [1.2227, -0.3032], [-1.2227, -0.3032]], convexity = 2);
         translate(v = [0.0, -5.1539])
         {
            circle(d = 10.0, $fn = 316);
         }
      }
   }
}
