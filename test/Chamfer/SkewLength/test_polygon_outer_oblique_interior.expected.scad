// Unit of length: Unit.MM
$fn = 11;
$vpr = [0.0, 0.0, 0.0];

union()
{
   color(c = [0.0, 0.502, 0.0, 1.0])
   {
      polygon(points = [[0.0069, -0.0106], [-6.2837, 0.4845], [-6.2829, 0.4945], [2.1038, 5.9409], [2.1132, 5.9375]]);
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
      translate(v = [2.1038, 5.9409])
      {
         circle(d = 0.5, $fn = 36);
      }
   }
   color(c = [1.0, 0.647, 0.0, 1.0])
   {
      translate(v = [-6.2829, 0.4945])
      {
         circle(d = 0.5, $fn = 36);
      }
   }
}
