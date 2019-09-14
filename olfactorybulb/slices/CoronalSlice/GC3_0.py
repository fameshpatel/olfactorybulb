
from neuron import h

class TransformGC3:
    def __init__(self):

        # Create a section lookup by section name
        # Note: this assumes each section has a unique name
        self.name2section = { sec.name(): sec for sec in h.allsec() }

        # This will store the new section coordinates
        self.section_coords = { }

    def set_coords(self, sec_name):
        # Lookup the section
        nrn_section = self.name2section[sec_name]

        # Lookup its new coords
        new_coords = self.section_coords[sec_name]

        # Use 3D points as section L and diam sources
        h.pt3dconst(1, sec=nrn_section)

        # Clear the existing points - and allocate room for the incoming points
        h.pt3dclear(len(new_coords["diam"]), sec=nrn_section)

        # Use vectorization to add the points to section
        xvec = h.Vector(new_coords["x"])
        yvec = h.Vector(new_coords["y"])
        zvec = h.Vector(new_coords["z"])
        dvec = h.Vector(new_coords["diam"])

        h.pt3dadd(xvec, yvec, zvec, dvec, sec=nrn_section)

    def set_all(self):
        for sec_name in self.section_coords.keys():
            self.set_coords(sec_name)

    @staticmethod
    def apply_on(prefix):
        t = TransformGC3()
        t.define_coords(prefix)
        t.set_all()

    @staticmethod
    def apply():
        t = TransformGC3()
        t.define_coords()
        t.set_all()

    def define_coords(self, prefix = 'GC3[0]'):
        if prefix != '':
            prefix += '.'

        self.section_coords = {
          prefix + 'apic[8]': {
              'x':[-310.789,-311.737,-315.256,-317.708,-319.214,-320.887,-322.273,-323.236,-323.553,-325.650,-328.228,-331.092,-333.535,-334.982,-335.750,-336.359,-336.870,-337.552,-339.477,-341.719,-343.961,-345.245,-346.382,-348.280,-349.845,-350.506,-351.163,-352.731,-354.988,-357.103,-358.646,-359.684,-360.178,-360.724,-361.038,-361.799,-362.780,-363.609,-364.181,-364.861,-366.019,-367.779,-370.018,-371.889,-372.890,-373.850,-375.465,-377.006,-378.066,-378.558,-379.045],
              'y':[702.090,702.159,702.569,702.895,703.154,703.369,703.597,704.116,704.364,704.363,704.319,704.286,704.325,704.451,704.583,704.519,704.388,704.165,703.709,703.622,703.581,703.562,703.560,703.610,703.796,704.475,704.999,705.056,705.012,704.888,704.686,704.246,703.789,703.502,703.516,703.769,703.883,703.921,704.143,704.600,704.818,705.025,705.159,705.260,705.480,705.761,705.987,706.165,706.523,706.993,707.545],
              'z':[-529.674,-530.275,-530.969,-531.591,-532.126,-532.697,-533.224,-534.079,-534.994,-536.103,-536.808,-537.550,-538.289,-538.925,-539.961,-540.997,-541.999,-543.019,-544.085,-544.821,-545.578,-546.253,-546.877,-547.537,-548.093,-548.716,-549.512,-550.043,-550.504,-550.885,-551.383,-552.362,-553.258,-554.223,-555.184,-556.182,-556.763,-557.357,-558.333,-559.210,-559.705,-560.221,-560.756,-561.261,-561.722,-562.181,-562.739,-563.331,-564.347,-565.189,-565.976],
              'diam':[0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521]
          },

          prefix + 'apic[6]': {
              'x':[-293.818,-296.954,-298.326,-298.591,-298.813,-299.315,-300.697,-302.443,-303.294,-303.661,-303.982,-305.980,-306.853,-307.941,-309.120,-310.147,-310.788],
              'y':[705.859,705.695,705.498,704.983,704.269,703.301,703.187,703.148,703.097,702.902,702.551,702.216,702.055,701.790,701.750,701.828,702.090],
              'z':[-515.752,-516.831,-517.550,-518.864,-520.001,-520.952,-521.555,-522.236,-522.815,-523.761,-524.661,-525.798,-526.367,-527.446,-528.066,-528.685,-529.674],
              'diam':[0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521]
          },

          prefix + 'apic[4]': {
              'x':[-307.243,-310.740,-313.358,-314.801,-316.201,-316.912,-318.542,-319.831,-321.431,-323.034,-324.063,-325.296,-326.735,-327.629,-328.496,-329.228,-329.707,-330.198,-330.534,-330.909,-331.311,-331.598,-331.847,-332.134,-332.498,-332.972,-333.424,-334.111,-334.899,-337.643,-339.243,-340.398,-341.211,-341.861,-342.243,-342.514,-342.833,-343.099,-343.277,-343.512,-343.852],
              'y':[707.669,708.019,708.063,708.084,708.193,708.647,709.069,709.190,709.195,709.133,709.077,708.964,709.104,709.173,708.655,707.860,707.216,707.351,707.835,708.296,708.432,708.174,708.093,707.909,707.583,707.269,707.280,707.532,707.564,707.514,707.507,707.647,707.837,707.744,707.716,708.454,709.048,710.032,711.275,712.410,713.373],
              'z':[-512.435,-512.492,-512.859,-512.880,-512.393,-511.821,-511.538,-511.494,-511.568,-511.618,-511.454,-510.939,-510.451,-509.788,-508.792,-507.883,-506.858,-505.649,-504.465,-503.291,-502.064,-500.812,-499.529,-498.261,-497.042,-495.837,-494.631,-493.474,-492.313,-492.284,-492.365,-491.790,-491.124,-489.956,-488.737,-487.699,-486.576,-485.790,-485.397,-484.833,-484.010],
              'diam':[0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521]
          },

          prefix + 'apic[0]': {
              'x':[-42.128,-43.974,-45.014,-45.756,-46.620,-48.151,-50.125,-51.926,-53.477,-54.461,-56.194,-57.290,-58.373,-59.696,-61.589,-63.495,-64.499,-65.232,-65.927,-67.929,-69.814,-72.348,-74.837,-76.342,-77.723,-78.930,-79.893,-80.892,-82.618,-83.842,-84.830,-86.947,-89.583,-91.678,-92.726,-93.526,-94.751,-95.897,-97.436,-99.353,-101.663,-103.464,-104.582,-106.306,-107.600,-108.733,-110.706,-112.638,-114.595,-116.862,-118.552,-119.763,-120.795,-123.037,-125.317,-127.489,-129.215,-130.229,-132.746,-135.191,-137.941,-140.286,-141.639,-142.656,-144.417,-146.462,-148.280,-150.354,-153.014,-155.896,-158.365,-160.133,-161.360,-162.473,-163.253,-164.117,-165.103,-166.850,-168.956,-170.892,-172.753,-174.739,-176.186,-177.311,-178.624,-180.273,-182.093,-183.771,-185.489,-187.536,-189.593,-191.231,-192.665,-194.038,-196.308,-198.627,-201.062,-203.352,-205.642,-207.351,-208.479,-209.938,-211.672,-213.474,-215.189,-217.204,-219.240,-221.214,-222.955,-224.246,-225.449,-226.565,-227.718,-229.562,-231.725,-233.716,-235.687,-237.466,-239.284,-241.235,-242.939,-244.706,-246.447,-248.139,-249.963,-251.420,-252.533,-253.755,-254.899,-256.075,-257.499,-258.815,-259.969,-261.075,-262.205,-264.121,-265.379,-266.645,-268.068,-269.679,-271.098,-272.459,-273.835,-275.613,-277.273,-278.842,-280.558,-282.184,-283.686,-285.225,-286.857],
              'y':[673.740,673.841,674.449,675.132,675.468,675.729,675.932,676.187,676.490,676.851,677.614,677.965,678.296,678.540,678.698,678.894,679.227,680.031,680.819,681.383,681.492,681.528,681.633,681.913,682.666,682.998,683.349,683.988,684.474,685.105,685.395,685.522,685.594,685.769,686.112,686.941,687.613,687.800,687.926,688.020,688.107,688.290,689.027,689.723,689.958,690.390,690.708,690.995,691.101,691.180,691.359,691.630,692.444,693.007,693.080,693.147,693.249,693.389,693.612,693.657,693.696,693.843,694.159,694.518,694.792,695.026,695.245,695.356,695.353,695.345,695.410,695.577,695.829,696.247,696.516,696.822,696.925,696.925,696.876,696.958,697.122,697.165,697.079,696.732,696.432,696.385,696.486,696.691,696.869,696.913,696.847,696.775,696.825,697.284,697.712,697.765,697.802,697.816,697.809,697.761,697.583,697.459,697.514,697.588,697.687,697.779,697.883,697.992,697.981,697.973,698.050,698.165,698.242,698.219,698.246,698.413,698.597,698.718,698.834,698.996,699.198,699.374,699.503,699.648,699.820,699.908,699.852,699.890,700.292,700.470,700.582,700.679,700.847,700.994,701.098,701.452,701.695,701.935,702.149,702.402,702.657,703.130,703.508,703.624,703.807,704.023,704.186,704.307,704.426,704.573,704.643],
              'z':[-496.376,-496.827,-497.603,-498.326,-498.746,-499.222,-499.685,-500.071,-500.434,-500.747,-501.288,-501.456,-501.567,-501.683,-501.946,-502.279,-502.373,-502.208,-502.016,-502.144,-502.396,-502.898,-503.459,-503.782,-504.219,-504.506,-504.600,-504.273,-504.033,-503.776,-503.819,-504.168,-504.655,-505.010,-505.163,-505.142,-504.985,-504.951,-505.022,-505.254,-505.673,-505.953,-505.871,-506.071,-506.182,-505.725,-505.545,-505.254,-505.482,-505.835,-506.011,-506.133,-506.325,-506.913,-507.347,-507.638,-507.752,-507.636,-507.537,-507.930,-508.492,-508.977,-509.304,-509.579,-510.068,-510.645,-511.056,-511.429,-511.986,-512.652,-513.102,-513.304,-513.372,-512.930,-512.275,-511.698,-511.561,-511.677,-511.929,-512.170,-512.451,-512.690,-512.690,-512.151,-511.657,-511.745,-511.929,-512.130,-512.320,-512.563,-512.797,-512.900,-512.926,-512.578,-512.548,-512.880,-513.260,-513.582,-513.908,-514.002,-513.434,-512.528,-512.674,-512.831,-512.963,-513.214,-513.560,-513.934,-514.109,-514.049,-513.958,-513.825,-513.729,-513.871,-514.162,-514.446,-514.741,-514.924,-515.132,-515.432,-515.655,-515.869,-516.051,-516.201,-516.440,-516.537,-516.443,-515.925,-515.473,-515.440,-515.457,-515.441,-514.882,-514.315,-514.243,-514.024,-514.083,-514.163,-514.291,-514.558,-514.735,-514.408,-514.054,-514.257,-514.423,-514.607,-514.824,-514.932,-514.978,-515.044,-515.203],
              'diam':[0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521]
          },

          prefix + 'apic[9]': {
              'x':[-286.857,-287.033,-287.253,-287.527,-287.777,-288.107,-288.222,-288.351,-288.506,-288.714,-288.845,-288.731,-288.679,-288.676,-288.713,-288.994,-289.386,-289.821,-290.365,-290.862,-291.137,-291.395,-291.622,-291.880,-292.094,-292.267,-292.518,-292.887,-296.203,-299.489,-302.718,-305.954,-309.230,-312.601,-316.020,-319.460,-320.031,-320.503,-321.220,-321.989,-322.710,-323.361,-324.205,-324.972,-325.657,-327.511,-328.772,-329.658,-330.670,-331.681,-333.024,-333.798,-334.780,-337.009,-338.813,-339.867,-340.830,-341.782,-342.456,-343.404,-344.225,-344.952,-345.731,-346.660,-347.344,-348.112,-348.838,-349.543,-350.258,-351.008,-351.675,-352.369,-353.114,-353.635,-354.272,-354.595,-354.835,-355.007,-355.369,-355.977,-356.608,-356.948,-357.370,-357.767,-358.556,-359.722,-360.991,-362.198,-363.463,-364.144,-364.879,-365.604,-366.240,-366.869,-367.259,-367.801,-368.566,-369.203,-369.979,-370.705,-371.272,-371.635,-371.594,-370.851,-370.383],
              'y':[704.643,703.585,702.265,700.955,699.753,698.744,697.551,696.371,695.210,694.287,693.360,692.209,691.064,689.821,688.528,687.464,686.269,684.998,683.790,682.576,681.272,679.958,678.681,677.409,676.109,674.784,673.678,673.175,673.045,672.404,671.281,670.223,669.552,669.252,669.114,668.878,667.687,666.419,665.416,664.640,664.204,663.602,663.101,662.467,661.925,661.407,661.071,660.759,660.456,660.275,660.006,659.705,659.083,658.775,658.700,658.590,658.433,658.147,657.791,657.034,656.622,656.118,655.698,655.315,654.748,653.970,653.671,653.327,653.022,652.618,651.985,651.150,650.280,649.426,648.107,646.796,645.499,644.185,642.917,641.708,640.577,639.432,638.448,637.350,636.467,636.188,635.871,635.079,634.505,633.891,633.216,632.474,631.652,630.792,629.475,628.155,626.834,626.002,624.777,623.977,623.167,621.890,620.585,619.309,618.013],
              'z':[-515.203,-515.114,-515.222,-515.286,-514.847,-514.044,-513.543,-512.974,-512.361,-511.472,-510.543,-509.898,-509.228,-508.809,-508.599,-507.924,-507.458,-507.186,-506.813,-506.414,-506.234,-506.264,-506.627,-506.861,-506.808,-506.880,-506.420,-505.280,-504.376,-503.737,-503.315,-502.825,-502.077,-501.370,-501.098,-501.280,-500.821,-500.592,-499.969,-499.077,-498.473,-497.984,-497.470,-496.483,-495.947,-495.807,-495.333,-494.226,-493.183,-492.563,-492.068,-491.414,-490.490,-490.415,-490.562,-490.472,-489.832,-489.217,-488.562,-487.701,-487.100,-486.535,-485.959,-485.374,-484.863,-483.982,-483.313,-482.653,-482.003,-481.398,-480.965,-480.894,-480.954,-480.904,-480.855,-480.821,-480.710,-480.569,-480.321,-479.913,-479.359,-478.796,-477.986,-477.344,-476.587,-476.699,-476.915,-476.949,-476.653,-476.174,-475.760,-475.474,-475.277,-475.268,-475.278,-475.477,-475.664,-475.569,-475.203,-475.009,-474.788,-474.539,-474.432,-474.400,-474.563],
              'diam':[0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521]
          },

          prefix + 'apic[7]': {
              'x':[-310.789,-310.829,-310.740,-310.659,-310.540,-310.334,-310.215,-310.172,-310.097,-310.154,-310.298,-310.518,-310.699,-310.983,-311.189,-311.542,-313.985,-315.095,-315.557,-315.763,-316.091,-316.493,-316.809,-317.246,-317.499,-317.443,-320.177,-322.209,-323.059,-323.449,-324.102,-324.776,-325.158,-325.605,-326.120,-326.439,-326.791,-327.102,-327.426,-327.778,-328.272,-328.829,-329.357,-330.864,-331.560,-332.989,-333.814,-334.335,-334.877,-335.200,-335.521,-335.963,-336.377,-336.868,-337.419,-337.888,-338.239,-339.643,-341.086,-342.313,-343.391,-344.243,-344.959,-345.747,-347.277,-349.427,-351.494,-353.101,-354.078,-354.720,-355.918,-356.381,-356.704,-357.047,-357.423,-357.703,-358.060,-358.462,-358.863,-359.572,-360.400,-361.346,-361.681,-362.784,-363.938,-365.022,-365.652,-366.504,-368.105,-369.064,-369.518,-369.820,-371.151,-372.111,-373.216,-374.294,-375.871,-377.763,-379.137,-380.170],
              'y':[702.090,701.687,700.862,700.219,700.125,699.941,699.443,698.805,698.578,698.713,698.720,698.483,697.867,697.177,696.694,696.478,696.502,696.433,696.331,696.136,695.871,695.500,695.055,694.282,693.835,693.283,692.933,692.718,692.468,691.958,691.482,690.976,690.150,689.462,688.886,688.535,688.387,687.997,687.888,687.879,687.660,687.322,686.947,686.542,686.226,685.914,685.569,685.044,684.512,684.141,683.761,682.943,682.280,681.838,681.798,681.785,681.800,681.913,681.932,681.972,682.093,682.251,682.794,683.438,683.653,683.807,683.963,684.017,684.151,684.642,685.199,685.420,685.422,685.350,685.038,684.723,684.496,684.437,684.334,684.240,684.244,684.147,683.988,683.920,683.870,683.780,683.667,683.934,684.074,683.831,683.266,682.915,682.534,682.339,681.801,681.572,681.432,681.364,681.308,681.227],
              'z':[-529.674,-530.908,-531.946,-533.090,-534.402,-535.688,-536.919,-538.099,-539.367,-540.720,-542.114,-543.468,-544.715,-545.945,-547.250,-548.661,-549.847,-550.446,-551.449,-552.841,-553.770,-554.685,-555.546,-556.743,-558.080,-559.285,-560.383,-561.015,-561.513,-562.348,-563.254,-564.157,-565.308,-565.970,-566.742,-568.114,-569.549,-570.912,-571.881,-572.863,-573.846,-574.812,-575.758,-576.878,-577.860,-578.961,-579.949,-580.773,-581.587,-582.484,-583.379,-584.547,-585.232,-586.048,-587.052,-588.074,-589.510,-590.620,-591.757,-592.386,-592.998,-593.556,-594.361,-595.030,-595.527,-596.160,-596.827,-597.483,-598.539,-599.399,-600.303,-601.267,-602.238,-603.227,-604.621,-605.536,-606.485,-607.472,-608.469,-609.517,-610.125,-611.214,-612.175,-613.294,-613.961,-615.083,-616.111,-617.099,-618.253,-619.314,-620.647,-621.545,-622.624,-623.224,-624.138,-624.671,-625.328,-626.068,-626.743,-627.864],
              'diam':[0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521]
          },

          prefix + 'apic[2]': {
              'x':[-293.818,-294.634,-296.145,-297.574,-298.728,-299.821,-300.533,-301.889,-303.641,-305.231,-306.238,-307.243],
              'y':[705.859,706.328,706.746,706.767,706.785,707.072,707.393,707.567,707.598,707.653,707.662,707.669],
              'z':[-515.752,-514.700,-513.844,-513.813,-513.706,-513.154,-512.484,-512.026,-512.190,-512.262,-512.343,-512.435],
              'diam':[0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521]
          },

          prefix + 'apic[1]': {
              'x':[-286.857,-288.459,-289.856,-291.712,-292.765,-293.818],
              'y':[704.643,704.992,705.265,705.762,705.807,705.859],
              'z':[-515.203,-515.447,-515.637,-515.513,-515.627,-515.752],
              'diam':[0.521,0.521,0.521,0.521,0.521,0.521]
          },

          prefix + 'soma': {
              'x':[-40.769,-40.932,-41.095],
              'y':[674.207,672.870,671.533],
              'z':[-496.265,-496.010,-495.756],
              'diam':[2.742,2.742,2.742]
          },

          prefix + 'apic[3]': {
              'x':[-307.243,-307.947,-308.696,-309.205,-309.581,-309.855,-310.234,-310.710,-311.323,-311.841,-312.454,-313.011,-313.400,-313.784,-314.318,-315.051,-315.826,-316.841,-317.648,-318.340,-318.899,-319.545,-320.150,-320.831,-321.389,-321.867,-322.162,-322.458,-322.912,-323.568,-324.116,-324.422,-324.748,-325.317,-325.887,-326.359,-326.926,-327.355,-327.771,-328.130,-328.608,-329.088,-329.846,-330.660,-331.389,-332.263,-333.204,-334.009,-334.670,-335.299,-336.055,-337.295,-338.343,-339.215,-340.065,-340.764,-341.506,-342.321,-343.255,-343.960,-344.322,-344.537,-344.690,-344.840,-345.073,-345.420,-345.710,-345.993,-346.180,-346.290,-346.491,-346.736,-347.185,-347.996,-348.610,-349.178,-349.688,-350.277,-350.965,-352.342,-353.403,-354.919,-355.786,-356.267],
              'y':[707.669,708.308,708.948,709.656,710.293,711.235,712.115,713.009,713.750,714.321,715.060,715.269,715.615,715.703,715.752,716.295,716.697,716.998,717.148,717.497,718.021,718.342,718.693,719.120,719.662,720.398,721.311,722.255,723.156,723.687,724.393,725.062,725.565,726.067,726.573,727.101,727.642,728.196,729.080,729.982,730.840,731.776,732.383,732.553,732.631,732.629,732.797,733.306,733.631,733.763,734.457,734.604,734.728,734.938,735.237,735.583,735.844,736.084,736.539,737.232,738.334,739.326,739.584,739.762,740.260,740.694,741.082,741.373,742.164,743.246,744.233,745.053,745.635,746.340,747.084,748.322,749.591,750.791,751.563,752.326,752.684,753.445,754.244,754.942],
              'z':[-512.435,-511.387,-510.394,-509.381,-508.302,-507.427,-506.509,-505.644,-504.689,-503.599,-502.654,-501.486,-500.281,-499.043,-497.812,-496.787,-496.179,-495.602,-494.456,-493.329,-492.224,-491.076,-489.922,-488.809,-487.717,-486.717,-485.830,-484.947,-484.091,-483.016,-482.018,-480.929,-479.747,-478.649,-477.531,-476.398,-475.308,-474.197,-473.314,-472.398,-471.504,-470.677,-469.699,-469.028,-468.301,-467.632,-466.993,-465.948,-464.833,-463.657,-462.696,-462.202,-461.594,-460.937,-460.294,-459.647,-458.977,-457.850,-456.827,-455.870,-455.229,-454.452,-453.196,-451.883,-450.713,-449.521,-448.293,-447.046,-446.041,-445.313,-444.451,-443.468,-442.364,-441.461,-441.171,-440.902,-440.728,-440.342,-440.126,-440.154,-440.279,-440.330,-440.575,-441.186],
              'diam':[0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521]
          },

          prefix + 'apic[5]': {
              'x':[-307.243,-310.358,-312.318,-313.645,-315.464,-317.341,-319.146,-321.161,-323.137,-324.894,-327.120,-329.488,-331.437,-333.254,-335.163,-336.887,-337.833,-338.216,-338.636,-340.643,-341.811,-342.804,-343.599,-343.894,-344.468,-345.531,-347.511,-349.379,-351.853,-354.334,-356.498,-358.253,-359.127,-359.529,-359.981,-360.825,-362.661,-364.195,-364.911,-366.641,-368.256,-369.188,-369.631,-369.946,-370.330,-370.610,-370.838,-370.970,-370.942,-370.922,-370.914,-370.937,-370.927,-370.834,-370.901,-371.473,-372.096,-372.567,-372.968,-375.888,-378.078,-379.016],
              'y':[707.669,707.255,706.988,706.916,706.978,707.110,707.216,707.295,707.361,707.441,707.503,707.615,707.764,707.851,707.885,707.822,707.671,707.251,706.451,705.929,705.629,705.399,705.032,704.260,703.837,703.756,703.601,703.484,703.417,703.402,703.360,703.165,702.895,702.495,701.988,701.861,701.781,701.767,702.092,702.421,702.389,702.229,701.808,701.402,700.878,700.583,699.839,699.092,698.249,697.310,696.272,695.238,694.404,693.804,692.942,691.691,690.846,690.075,688.837,688.302,688.084,687.734],
              'z':[-512.435,-513.545,-514.426,-515.074,-515.720,-516.375,-517.050,-517.738,-518.430,-519.085,-519.778,-520.442,-521.077,-521.748,-522.387,-522.980,-523.516,-524.410,-525.590,-526.640,-527.177,-527.753,-528.745,-529.868,-530.756,-531.880,-533.082,-533.759,-534.367,-534.812,-535.193,-535.681,-536.136,-537.035,-538.388,-538.940,-539.632,-540.320,-541.256,-542.295,-542.977,-543.550,-544.459,-545.328,-546.661,-547.580,-548.764,-549.897,-550.926,-551.875,-552.704,-553.515,-554.558,-555.741,-556.723,-557.255,-557.646,-558.161,-558.701,-559.523,-559.974,-560.061],
              'diam':[0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521,0.521]
          },


        }