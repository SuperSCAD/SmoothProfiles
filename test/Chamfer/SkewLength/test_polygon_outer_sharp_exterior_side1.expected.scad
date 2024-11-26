// Unit of length: Unit.MM
$fn = 11;
$vpr = [0.0, 0.0, 0.0];

union()
{
   color(c = [0.0, 0.502, 0.0, 1.0])
   {
      translate(v = [0.0, 0.0])
      {
         polygon(points = [[0.0, 0.0], [0.0052, 0.0085], [5.0052, -3.0555], [5.0, -3.064], [-5.0, -3.064]]);
      }
   }
   color(c = [1.0, 1.0, 0.0, 0.3])
   {
      translate(v = [0.0, 0.0])
      {
         intersection()
         {
            circle(d = 50.0);
            polygon(points = [[0.0, 0.0], [25.0, -15.32], [25.01, -15.32], [25.01, 15.32], [25.0, 15.32]], convexity = 1);
         }
      }
   }
   color(c = [1.0, 0.0, 0.0, 1.0])
   {
      translate(v = [-5.0, -3.064])
      {
         circle(d = 0.5, $fn = 36);
      }
   }
   color(c = [1.0, 0.647, 0.0, 1.0])
   {
      translate(v = [5.0, -3.064])
      {
         circle(d = 0.5, $fn = 36);
      }
   }
}
