// Unit of length: Unit.MM
$fn = 11;
$vpr = [0.0, 0.0, 0.0];

union()
{
   color(c = [0.0, 0.502, 0.0, 1.0])
   {
      translate(v = [0.0, 0.0])
      {
         polygon(points = [[0.0098, -0.0021], [0.0, 0.0], [-6.9165, 1.4702], [1.4702, 6.9165], [1.4799, 6.9145]]);
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
      translate(v = [1.4702, 6.9165])
      {
         circle(d = 0.5, $fn = 36);
      }
   }
   color(c = [1.0, 0.647, 0.0, 1.0])
   {
      translate(v = [-6.9165, 1.4702])
      {
         circle(d = 0.5, $fn = 36);
      }
   }
}