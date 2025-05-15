// Unit of length: Unit.MM
$fn = 11;
$vpr = [0.0, 0.0, 0.0];

union()
{
   color(c = [1.0, 0.0, 0.0, 1.0])
   {
      rotate(a = 213.0)
      {
         difference()
         {
            polygon(points = [[0.0, 0.0126], [6.0937, -4.6633], [6.0876, -4.6712], [-6.0876, -4.6712], [-6.0937, -4.6633]], convexity = 2);
            translate(v = [0.0, -12.6047])
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
            polygon(points = [[0.0, 0.0], [8.4172, 23.7694], [8.4193, 23.7792], [-19.2636, 29.6633], [-25.1478, 1.9805], [-25.138, 1.9784]], convexity = 1);
         }
      }
   }
   color(c = [1.0, 0.0, 0.0, 1.0])
   {
      translate(v = [2.5614, 7.2331])
      {
         circle(d = 0.5, $fn = 36);
      }
   }
   color(c = [1.0, 0.647, 0.0, 1.0])
   {
      translate(v = [2.045, 6.0313])
      {
         circle(d = 0.5, $fn = 36);
      }
   }
   color(c = [0.0, 0.502, 0.0, 1.0])
   {
      translate(v = [-1.4186, 2.1845])
      {
         circle(d = 0.5, $fn = 36);
      }
   }
   color(c = [0.0, 0.0, 1.0, 1.0])
   {
      translate(v = [-6.3417, 0.5849])
      {
         circle(d = 0.5, $fn = 36);
      }
   }
   color(c = [0.0, 0.0, 1.0, 1.0])
   {
      translate(v = [-7.6496, 0.602])
      {
         circle(d = 0.5, $fn = 36);
      }
   }
}
