// Unit of length: Unit.MM
$fa = 1.0;
$fs = 0.1;

union()
{
   polygon(points = [[0.0, 50.0], [20.0, 0.0], [0.0, 40.0], [-20.0, 0.0]]);
   translate(v = [0.0, 40.0])
   {
      rotate(a = 0.0)
      {
         difference()
         {
            polygon(points = [[-0.0894, 0.0447], [0.0, 0.1], [0.0894, 0.0447], [4.5616, -8.8996], [4.4721, -8.9443], [-4.4721, -8.9443], [-4.5616, -8.8996]], convexity = 2);
            translate(v = [0.0, -11.1803])
            {
               circle(d = 10.0, $fn = 316);
            }
         }
      }
   }
}
