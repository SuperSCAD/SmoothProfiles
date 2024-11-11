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
               difference()
               {
                  polygon(points = [[0.0, 0.1118], [2.2808, -1.0286], [2.2361, -1.118], [-2.2361, -1.118], [-2.2808, -1.0286]], convexity = 2);
                  translate(v = [0.0, -5.5902])
                  {
                     circle(d = 10.0, $fn = 316);
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
                  polygon(points = [[-0.0894, 0.0447], [0.0, 0.1], [0.0894, 0.0447], [4.5616, -8.8996], [4.4721, -8.9443], [-4.4721, -8.9443], [-4.5616, -8.8996]], convexity = 2);
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
               polygon(points = [[0.0, 0.1118], [2.2808, -1.0286], [2.2361, -1.118], [-2.2361, -1.118], [-2.2808, -1.0286]], convexity = 2);
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
            polygon(points = [[-0.0894, 0.0447], [0.0, 0.1], [0.0894, 0.0447], [4.5616, -8.8996], [4.4721, -8.9443], [-4.4721, -8.9443], [-4.5616, -8.8996]], convexity = 2);
            translate(v = [0.0, -11.1803])
            {
               circle(d = 10.0, $fn = 316);
            }
         }
      }
   }
}
