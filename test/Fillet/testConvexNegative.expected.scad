// Unit of length: Unit.MM
$fa = 1.0;
$fs = 0.1;

union()
{
   union()
   {
      union()
      {
         union()
         {
            polygon(points = [[0.0, 10.0], [-20.0, 0.0], [0.0, -10.0], [20.0, 0.0]]);
            translate(v = [0.0, 10.0])
            {
               intersection()
               {
                  circle(d = 10.0, $fn = 316);
                  polygon(points = [[0.0, -0.0112], [4.719, -2.3707], [4.7235, -2.3617], [7.0852, 0.0], [0.0, 7.0852], [-7.0852, 0.0], [-4.7235, -2.3617], [-4.719, -2.3707]], convexity = 2);
               }
            }
         }
         translate(v = [-20.0, 0.0])
         {
            intersection()
            {
               circle(d = 10.0, $fn = 316);
               polygon(points = [[0.0224, 0.0], [4.7279, 2.3528], [4.7235, 2.3617], [0.0, 7.0852], [-7.0852, 0.0], [0.0, -7.0852], [4.7235, -2.3617], [4.7279, -2.3528]], convexity = 2);
            }
         }
      }
      translate(v = [0.0, -10.0])
      {
         intersection()
         {
            circle(d = 10.0, $fn = 316);
            polygon(points = [[0.0, 0.0112], [-4.719, 2.3707], [-4.7235, 2.3617], [-7.0852, 0.0], [0.0, -7.0852], [7.0852, 0.0], [4.7235, 2.3617], [4.719, 2.3707]], convexity = 2);
         }
      }
   }
   translate(v = [20.0, 0.0])
   {
      intersection()
      {
         circle(d = 10.0, $fn = 316);
         polygon(points = [[-0.0224, 0.0], [-4.7279, -2.3528], [-4.7235, -2.3617], [0.0, -7.0852], [7.0852, 0.0], [0.0, 7.0852], [-4.7235, 2.3617], [-4.7279, 2.3528]], convexity = 2);
      }
   }
}
