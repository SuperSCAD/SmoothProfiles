// Unit of length: Unit.MM
$fn = 11;
$vpr = [0.0, 0.0, 0.0];

union()
{
   color(c = [0.0, 0.502, 0.0, 1.0])
   {
      rotate(a = 330.0)
      {
         difference()
         {
            polygon(points = [[0.0, 0.0141], [7.0781, -7.064], [7.0711, -7.0711], [-7.0711, -7.0711], [-7.0781, -7.064]], convexity = 2);
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
            polygon(points = [[0.0, 0.0], [-24.1481, -6.4705], [-24.1578, -6.4731], [-17.6847, -30.6309], [6.4731, -24.1578], [6.4705, -24.1481]], convexity = 1);
         }
      }
   }
   color(c = [1.0, 0.0, 0.0, 1.0])
   {
      translate(v = [-9.6593, -2.5882])
      {
         circle(d = 0.5, $fn = 36);
      }
   }
   color(c = [1.0, 0.647, 0.0, 1.0])
   {
      translate(v = [-7.0711, -2.2474])
      {
         circle(d = 0.5, $fn = 36);
      }
   }
   color(c = [0.0, 0.502, 0.0, 1.0])
   {
      translate(v = [-2.0711, -3.5872])
      {
         circle(d = 0.5, $fn = 36);
      }
   }
   color(c = [0.0, 0.0, 1.0, 1.0])
   {
      translate(v = [1.5892, -7.2474])
      {
         circle(d = 0.5, $fn = 36);
      }
   }
   color(c = [0.0, 0.0, 1.0, 1.0])
   {
      translate(v = [2.5882, -9.6593])
      {
         circle(d = 0.5, $fn = 36);
      }
   }
}
