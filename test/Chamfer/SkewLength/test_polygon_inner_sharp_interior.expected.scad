// Unit of length: Unit.MM
$fn = 11;
$vpr = [0.0, 0.0, 0.0];

union()
{
   color(c = [0.0, 0.502, 0.0, 1.0])
   {
      polygon(points = [[-0.0011, 0.0099], [0.0081, 0.0059], [0.0091, -0.0041], [-4.0423, -9.1466], [-4.0514, -9.1425], [-9.9434, -1.0626], [-9.9444, -1.0527]]);
   }
   color(c = [1.0, 1.0, 0.0, 0.3])
   {
      translate(v = [0.0, 0.0])
      {
         intersection()
         {
            circle(d = 50.0);
            polygon(points = [[0.0, 0.0], [-10.4858, -23.6626], [-10.4874, -23.6725], [20.8396, -28.5782], [28.5782, 20.8396], [-20.8396, 28.5782], [-25.7452, -2.7488], [-25.7354, -2.7503]], convexity = 2);
         }
      }
   }
   color(c = [1.0, 0.0, 0.0, 1.0])
   {
      translate(v = [-9.9434, -1.0626])
      {
         circle(d = 0.5, $fn = 36);
      }
   }
   color(c = [1.0, 0.647, 0.0, 1.0])
   {
      translate(v = [-4.0514, -9.1425])
      {
         circle(d = 0.5, $fn = 36);
      }
   }
}
