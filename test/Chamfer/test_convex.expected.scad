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
            polygon(points = [[0.0, 10.01], [0.0045, 10.0089], [2.5045, 8.7589], [2.5, 8.75], [-2.5, 8.75], [-2.5045, 8.7589], [-0.0045, 10.0089]]);
         }
         polygon(points = [[-20.01, 0.0], [-20.0045, 0.0089], [-15.0045, 2.5089], [-15.0, 2.5], [-15.0, -2.5], [-15.0045, -2.5089], [-20.0045, -0.0089]]);
      }
      polygon(points = [[0.0, -10.01], [-0.0045, -10.0089], [-2.5045, -8.7589], [-2.5, -8.75], [2.5, -8.75], [2.5045, -8.7589], [0.0045, -10.0089]]);
   }
   polygon(points = [[20.01, 0.0], [20.0045, -0.0089], [15.0045, -2.5089], [15.0, -2.5], [15.0, 2.5], [15.0045, 2.5089], [20.0045, 0.0089]]);
}