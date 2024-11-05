// Unit of length: Unit.MM
$fa = 1.0;
$fs = 0.1;

difference()
{
   difference()
   {
      difference()
      {
         difference()
         {
            polygon(points = [[0.0, 10.0], [-20.0, 0.0], [0.0, -10.0], [20.0, 0.0]]);
            translate(v = [0.0, 10.0])
            {
               rotate(a = 0.0)
               {
                  difference()
                  {
                     polygon(points = [[0.0, 0.01], [2.2461, -1.118], [-2.2461, -1.118]], convexity = 2);
                     translate(v = [0.0, -5.5902])
                     {
                        circle(d = 10.0, $fn = 316);
                     }
                  }
               }
            }
         }
         translate(v = [-20.0, 0.0])
         {
            rotate(a = 90.0)
            {
               difference()
               {
                  polygon(points = [[0.0, 0.01], [4.4821, -8.9443], [-4.4821, -8.9443]], convexity = 2);
                  translate(v = [0.0, -11.1803])
                  {
                     circle(d = 10.0, $fn = 316);
                  }
               }
            }
         }
      }
      translate(v = [0.0, -10.0])
      {
         rotate(a = 180.0)
         {
            difference()
            {
               polygon(points = [[0.0, 0.01], [2.2461, -1.118], [-2.2461, -1.118]], convexity = 2);
               translate(v = [0.0, -5.5902])
               {
                  circle(d = 10.0, $fn = 316);
               }
            }
         }
      }
   }
   translate(v = [20.0, 0.0])
   {
      rotate(a = 270.0)
      {
         difference()
         {
            polygon(points = [[0.0, 0.01], [4.4821, -8.9443], [-4.4821, -8.9443]], convexity = 2);
            translate(v = [0.0, -11.1803])
            {
               circle(d = 10.0, $fn = 316);
            }
         }
      }
   }
}
