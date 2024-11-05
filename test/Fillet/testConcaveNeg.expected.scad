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
         polygon(points = [[0.0, 0.01], [-0.0089, 0.0045], [-2.5139, -5.0055], [-2.505, -5.01], [2.505, -5.01], [2.5139, -5.0055], [0.0089, 0.0045]], convexity = 1);
      }
   }
}
