// Unit of length: Unit.MM
$fa = 1.0;
$fs = 0.1;

union()
{
   translate(v = [-20.0, 0.0, 0.0])
   {
      difference()
      {
         difference()
         {
            difference()
            {
               difference()
               {
                  polygon(points = [[20.0, 0.0], [0.0, -10.0], [-20.0, 0.0], [0.0, 10.0]]);
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
   }
   translate(v = [20.0, 0.0, 0.0])
   {
      polygon(points = [[11.0557, 4.4721], [11.1161, 4.4414], [11.204, 4.3949], [11.2909, 4.3466], [11.3768, 4.2966], [11.4618, 4.2449], [11.5456, 4.1915], [11.6284, 4.1365], [11.7101, 4.0799], [11.7907, 4.0216], [11.87, 3.9617], [11.9482, 3.9003], [12.0251, 3.8373], [12.1008, 3.7728], [12.1752, 3.7068], [12.2482, 3.6394], [12.3199, 3.5705], [12.3902, 3.5002], [12.4591, 3.4285], [12.5265, 3.3555], [12.5925, 3.2811], [12.657, 3.2055], [12.7199, 3.1285], [12.7814, 3.0504], [12.8412, 2.971], [12.8995, 2.8905], [12.9562, 2.8088], [13.0112, 2.726], [13.0646, 2.6421], [13.1163, 2.5572], [13.1663, 2.4712], [13.2145, 2.3843], [13.2611, 2.2965], [13.3059, 2.2077], [13.3489, 2.1181], [13.3901, 2.0276], [13.4295, 1.9364], [13.4671, 1.8443], [13.5028, 1.7516], [13.5367, 1.6581], [13.5688, 1.564], [13.5989, 1.4693], [13.6272, 1.3739], [13.6536, 1.2781], [13.678, 1.1817], [13.7005, 1.0849], [13.7211, 0.9876], [13.7398, 0.89], [13.7565, 0.792], [13.7713, 0.6937], [13.7841, 0.5951], [13.795, 0.4963], [13.8039, 0.3973], [13.8108, 0.2981], [13.8157, 0.1988], [13.8187, 0.0994], [13.8197, 0.0], [13.8187, -0.0994], [13.8157, -0.1988], [13.8108, -0.2981], [13.8039, -0.3973], [13.795, -0.4963], [13.7841, -0.5951], [13.7713, -0.6937], [13.7565, -0.792], [13.7398, -0.89], [13.7211, -0.9876], [13.7005, -1.0849], [13.678, -1.1817], [13.6536, -1.2781], [13.6272, -1.3739], [13.5989, -1.4693], [13.5688, -1.564], [13.5367, -1.6581], [13.5028, -1.7516], [13.4671, -1.8443], [13.4295, -1.9364], [13.3901, -2.0276], [13.3489, -2.1181], [13.3059, -2.2077], [13.2611, -2.2965], [13.2145, -2.3843], [13.1663, -2.4712], [13.1163, -2.5572], [13.0646, -2.6421], [13.0112, -2.726], [12.9562, -2.8088], [12.8995, -2.8905], [12.8412, -2.971], [12.7814, -3.0504], [12.7199, -3.1285], [12.657, -3.2055], [12.5925, -3.2811], [12.5265, -3.3555], [12.4591, -3.4285], [12.3902, -3.5002], [12.3199, -3.5705], [12.2482, -3.6394], [12.1752, -3.7068], [12.1008, -3.7728], [12.0251, -3.8373], [11.9482, -3.9003], [11.87, -3.9617], [11.7907, -4.0216], [11.7101, -4.0799], [11.6284, -4.1365], [11.5456, -4.1915], [11.4618, -4.2449], [11.3768, -4.2966], [11.2909, -4.3466], [11.204, -4.3949], [11.1161, -4.4414], [11.0557, -4.4721], [2.2361, -8.882], [2.2077, -8.896], [2.1181, -8.939], [2.0276, -8.9802], [1.9364, -9.0197], [1.8443, -9.0572], [1.7516, -9.093], [1.6581, -9.1269], [1.564, -9.1589], [1.4693, -9.1891], [1.3739, -9.2174], [1.2781, -9.2437], [1.1817, -9.2682], [1.0849, -9.2907], [0.9876, -9.3113], [0.89, -9.33], [0.792, -9.3467], [0.6937, -9.3615], [0.5951, -9.3743], [0.4963, -9.3851], [0.3973, -9.394], [0.2981, -9.4009], [0.1988, -9.4059], [0.0994, -9.4088], [0.0, -9.4098], [-0.0994, -9.4088], [-0.1988, -9.4059], [-0.2981, -9.4009], [-0.3973, -9.394], [-0.4963, -9.3851], [-0.5951, -9.3743], [-0.6937, -9.3615], [-0.792, -9.3467], [-0.89, -9.33], [-0.9876, -9.3113], [-1.0849, -9.2907], [-1.1817, -9.2682], [-1.2781, -9.2437], [-1.3739, -9.2174], [-1.4693, -9.1891], [-1.564, -9.1589], [-1.6581, -9.1269], [-1.7516, -9.093], [-1.8443, -9.0572], [-1.9364, -9.0197], [-2.0276, -8.9802], [-2.1181, -8.939], [-2.2077, -8.896], [-2.2361, -8.882], [-11.0557, -4.4721], [-11.1161, -4.4414], [-11.204, -4.3949], [-11.2909, -4.3466], [-11.3768, -4.2966], [-11.4618, -4.2449], [-11.5456, -4.1915], [-11.6284, -4.1365], [-11.7101, -4.0799], [-11.7907, -4.0216], [-11.87, -3.9617], [-11.9482, -3.9003], [-12.0251, -3.8373], [-12.1008, -3.7728], [-12.1752, -3.7068], [-12.2482, -3.6394], [-12.3199, -3.5705], [-12.3902, -3.5002], [-12.4591, -3.4285], [-12.5265, -3.3555], [-12.5925, -3.2811], [-12.657, -3.2055], [-12.7199, -3.1285], [-12.7814, -3.0504], [-12.8412, -2.971], [-12.8995, -2.8905], [-12.9562, -2.8088], [-13.0112, -2.726], [-13.0646, -2.6421], [-13.1163, -2.5572], [-13.1663, -2.4712], [-13.2145, -2.3843], [-13.2611, -2.2965], [-13.3059, -2.2077], [-13.3489, -2.1181], [-13.3901, -2.0276], [-13.4295, -1.9364], [-13.4671, -1.8443], [-13.5028, -1.7516], [-13.5367, -1.6581], [-13.5688, -1.564], [-13.5989, -1.4693], [-13.6272, -1.3739], [-13.6536, -1.2781], [-13.678, -1.1817], [-13.7005, -1.0849], [-13.7211, -0.9876], [-13.7398, -0.89], [-13.7565, -0.792], [-13.7713, -0.6937], [-13.7841, -0.5951], [-13.795, -0.4963], [-13.8039, -0.3973], [-13.8108, -0.2981], [-13.8157, -0.1988], [-13.8187, -0.0994], [-13.8197, 0.0], [-13.8187, 0.0994], [-13.8157, 0.1988], [-13.8108, 0.2981], [-13.8039, 0.3973], [-13.795, 0.4963], [-13.7841, 0.5951], [-13.7713, 0.6937], [-13.7565, 0.792], [-13.7398, 0.89], [-13.7211, 0.9876], [-13.7005, 1.0849], [-13.678, 1.1817], [-13.6536, 1.2781], [-13.6272, 1.3739], [-13.5989, 1.4693], [-13.5688, 1.564], [-13.5367, 1.6581], [-13.5028, 1.7516], [-13.4671, 1.8443], [-13.4295, 1.9364], [-13.3901, 2.0276], [-13.3489, 2.1181], [-13.3059, 2.2077], [-13.2611, 2.2965], [-13.2145, 2.3843], [-13.1663, 2.4712], [-13.1163, 2.5572], [-13.0646, 2.6421], [-13.0112, 2.726], [-12.9562, 2.8088], [-12.8995, 2.8905], [-12.8412, 2.971], [-12.7814, 3.0504], [-12.7199, 3.1285], [-12.657, 3.2055], [-12.5925, 3.2811], [-12.5265, 3.3555], [-12.4591, 3.4285], [-12.3902, 3.5002], [-12.3199, 3.5705], [-12.2482, 3.6394], [-12.1752, 3.7068], [-12.1008, 3.7728], [-12.0251, 3.8373], [-11.9482, 3.9003], [-11.87, 3.9617], [-11.7907, 4.0216], [-11.7101, 4.0799], [-11.6284, 4.1365], [-11.5456, 4.1915], [-11.4618, 4.2449], [-11.3768, 4.2966], [-11.2909, 4.3466], [-11.204, 4.3949], [-11.1161, 4.4414], [-11.0557, 4.4721], [-2.2361, 8.882], [-2.2077, 8.896], [-2.1181, 8.939], [-2.0276, 8.9802], [-1.9364, 9.0197], [-1.8443, 9.0572], [-1.7516, 9.093], [-1.6581, 9.1269], [-1.564, 9.1589], [-1.4693, 9.1891], [-1.3739, 9.2174], [-1.2781, 9.2437], [-1.1817, 9.2682], [-1.0849, 9.2907], [-0.9876, 9.3113], [-0.89, 9.33], [-0.792, 9.3467], [-0.6937, 9.3615], [-0.5951, 9.3743], [-0.4963, 9.3851], [-0.3973, 9.394], [-0.2981, 9.4009], [-0.1988, 9.4059], [-0.0994, 9.4088], [0.0, 9.4098], [0.0994, 9.4088], [0.1988, 9.4059], [0.2981, 9.4009], [0.3973, 9.394], [0.4963, 9.3851], [0.5951, 9.3743], [0.6937, 9.3615], [0.792, 9.3467], [0.89, 9.33], [0.9876, 9.3113], [1.0849, 9.2907], [1.1817, 9.2682], [1.2781, 9.2437], [1.3739, 9.2174], [1.4693, 9.1891], [1.564, 9.1589], [1.6581, 9.1269], [1.7516, 9.093], [1.8443, 9.0572], [1.9364, 9.0197], [2.0276, 8.9802], [2.1181, 8.939], [2.2077, 8.896], [2.2361, 8.882]]);
   }
}
