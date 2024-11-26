// Unit of length: Unit.MM
$fn = 11;
$vpr = [0.0, 0.0, 0.0];

union()
{
   color(c = [0.0, 0.502, 0.0, 1.0])
   {
      rotate(a = 33.0)
      {
         difference()
         {
            polygon(points = [[0.0, 0.0], [0.0071, 0.0071], [7.0781, -7.064], [7.0711, -7.0711], [-7.0711, -7.0711]], convexity = 2);
            translate(v = [0.0, -14.1421])
            {
               circle(d = 20.0, $fn = 12);
            }
         }
      }
   }
   color(c = [1.0, 1.0, 0.0, 0.3])
   {
      translate(v = [0.0, 0.0])
      {
         intersection()
         {
            circle(d = 50.0);
            polygon(points = [[0.0, 0.0], [24.4537, -5.1978], [24.4635, -5.1999], [29.6633, 19.2636], [5.1999, 24.4635], [5.1978, 24.4537]], convexity = 1);
         }
      }
   }
   color(c = [1.0, 0.0, 0.0, 1.0])
   {
      translate(v = [-2.0791, -9.7815])
      {
         circle(d = 0.5, $fn = 36);
      }
   }
   color(c = [1.0, 0.647, 0.0, 1.0])
   {
      translate(v = [-1.2077, -7.3207])
      {
         circle(d = 0.5, $fn = 36);
      }
   }
   color(c = [0.0, 0.502, 0.0, 1.0])
   {
      translate(v = [2.256, -3.4739])
      {
         circle(d = 0.5, $fn = 36);
      }
   }
   color(c = [0.0, 0.0, 1.0, 1.0])
   {
      translate(v = [7.179, -1.8743])
      {
         circle(d = 0.5, $fn = 36);
      }
   }
   color(c = [0.0, 0.0, 1.0, 1.0])
   {
      translate(v = [9.7815, -2.0791])
      {
         circle(d = 0.5, $fn = 36);
      }
   }
}
