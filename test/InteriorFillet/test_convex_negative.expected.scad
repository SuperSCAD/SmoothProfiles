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
                  polygon(points = [[0.0, -0.1118], [4.7338, -2.4787], [7.2125, 0.0], [0.0, 7.2125], [-7.2125, 0.0], [-4.7338, -2.4787]], convexity = 2);
               }
            }
         }
         translate(v = [-20.0, 0.0])
         {
            intersection()
            {
               circle(d = 10.0, $fn = 316);
               polygon(points = [[0.2236, 0.0], [4.7588, 2.2676], [4.8128, 2.341], [4.7848, 2.4277], [0.0, 7.2125], [-7.2125, 0.0], [0.0, -7.2125], [4.7848, -2.4277], [4.8128, -2.341], [4.7588, -2.2676]], convexity = 2);
            }
         }
      }
      translate(v = [0.0, -10.0])
      {
         intersection()
         {
            circle(d = 10.0, $fn = 316);
            polygon(points = [[0.0, 0.1118], [-4.7338, 2.4787], [-7.2125, 0.0], [0.0, -7.2125], [7.2125, 0.0], [4.7338, 2.4787]], convexity = 2);
         }
      }
   }
   translate(v = [20.0, 0.0])
   {
      intersection()
      {
         circle(d = 10.0, $fn = 316);
         polygon(points = [[-0.2236, 0.0], [-4.7588, -2.2676], [-4.8128, -2.341], [-4.7848, -2.4277], [0.0, -7.2125], [7.2125, 0.0], [0.0, 7.2125], [-4.7848, 2.4277], [-4.8128, 2.341], [-4.7588, 2.2676]], convexity = 2);
      }
   }
}
