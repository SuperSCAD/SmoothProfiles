// Unit of length: Unit.MM
$fn = 11;
$vpr = [0.0, 0.0, 0.0];

union()
{
   color(c = [0.0, 0.0, 1.0, 1.0])
   {
      rotate(a = 20.0)
      {
         difference()
         {
            polygon(points = [[-0.0084, 0.0054], [0.0, 0.0], [8.4339, -13.2386], [-8.4339, -13.2386], [-8.4423, -13.2332]], convexity = 2);
            translate(v = [0.0, -18.6116])
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
            polygon(points = [[0.0, 0.0], [-20.3154, 15.5885], [-20.3245, 15.5928], [-33.2364, -12.0971], [-5.5466, -25.0091], [-5.5424, -25.0]], convexity = 1);
         }
      }
   }
   color(c = [1.0, 0.0, 0.0, 1.0])
   {
      translate(v = [12.4532, -9.5556])
      {
         circle(d = 0.5, $fn = 36);
      }
   }
   color(c = [1.0, 0.647, 0.0, 1.0])
   {
      translate(v = [8.102, -7.6411])
      {
         circle(d = 0.5, $fn = 36);
      }
   }
   color(c = [0.0, 0.502, 0.0, 1.0])
   {
      translate(v = [2.9453, -8.0922])
      {
         circle(d = 0.5, $fn = 36);
      }
   }
   color(c = [0.0, 0.0, 1.0, 1.0])
   {
      translate(v = [-1.2949, -11.0613])
      {
         circle(d = 0.5, $fn = 36);
      }
   }
   color(c = [0.0, 0.0, 1.0, 1.0])
   {
      translate(v = [-3.3974, -15.3248])
      {
         circle(d = 0.5, $fn = 36);
      }
   }
}
