// Unit of length: Unit.MM
$fn = 11;
$vpr = [0.0, 0.0, 0.0];

union()
{
   color(c = [0.0, 0.502, 0.0, 1.0])
   {
      rotate(a = 110.0)
      {
         difference()
         {
            polygon(points = [[-0.0052, 0.0085], [0.0, 0.0], [5.225, -3.2019], [-5.225, -3.2019], [-5.2302, -3.1933]], convexity = 2);
            translate(v = [0.0, -11.7283])
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
            polygon(points = [[0.0, 0.0], [-5.8456, -28.7321], [-5.8422, -28.7415], [22.95, -18.262], [22.9466, -18.2526]], convexity = 1);
         }
      }
   }
   color(c = [1.0, 0.0, 0.0, 1.0])
   {
      translate(v = [1.2217, 6.005])
      {
         circle(d = 0.5, $fn = 36);
      }
   }
   color(c = [1.0, 0.647, 0.0, 1.0])
   {
      translate(v = [1.1729, 5.7478])
      {
         circle(d = 0.5, $fn = 36);
      }
   }
   color(c = [0.0, 0.502, 0.0, 1.0])
   {
      translate(v = [1.624, 0.5911])
      {
         circle(d = 0.5, $fn = 36);
      }
   }
   color(c = [0.0, 0.0, 1.0, 1.0])
   {
      translate(v = [4.5931, -3.6491])
      {
         circle(d = 0.5, $fn = 36);
      }
   }
   color(c = [0.0, 0.0, 1.0, 1.0])
   {
      translate(v = [4.7958, -3.8148])
      {
         circle(d = 0.5, $fn = 36);
      }
   }
}
