// Unit of length: Unit.MM
$fn = 13;
$vpr = [0.0, 0.0, 0.0];

union()
{
   color(c = [0.0, 0.502, 0.0, 1.0])
   {
      polygon(points = [[-0.0034, 0.0126], [14.1153, -6.5411], [14.1111, -6.5502], [-8.901, -12.7593], [-8.9092, -12.7536]]);
   }
   color(c = [1.0, 1.0, 0.0, 0.3])
   {
      translate(v = [0.0, 0.0])
      {
         intersection()
         {
            circle(d = 50.0);
            polygon(points = [[0.0, 0.0], [22.7627, -10.5661], [22.7714, -10.5711], [34.1483, 9.2139], [-9.2139, 34.1483], [-34.1483, -9.2139], [-14.3633, -20.5908], [-14.3583, -20.5821]], convexity = 2);
         }
      }
   }
   color(c = [1.0, 0.0, 0.0, 1.0])
   {
      translate(v = [-8.901, -12.7593])
      {
         circle(d = 0.5, $fn = 36);
      }
   }
   color(c = [1.0, 0.647, 0.0, 1.0])
   {
      translate(v = [14.1111, -6.5502])
      {
         circle(d = 0.5, $fn = 36);
      }
   }
}