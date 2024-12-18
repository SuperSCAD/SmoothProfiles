// Unit of length: Unit.MM
$fa = 1.0;
$fs = 0.1;

union()
{
   polygon(points = [[0.0, 50.0], [20.0, 0.0], [0.0, 40.0], [-20.0, 0.0]]);
   translate(v = [0.0, 40.0])
   {
      intersection()
      {
         circle(d = 10.0, $fn = 316);
         polygon(points = [[0.0894, 0.0447], [0.0, 0.1], [-0.0894, 0.0447], [-2.5894, -4.9553], [-2.5851, -5.0526], [-2.5, -5.1], [2.5, -5.1], [2.5851, -5.0526], [2.5894, -4.9553]], convexity = 1);
      }
   }
}
