import matplotlib.pyplot as plt
import numpy as np
import csv 
from scipy.interpolate import interp2d

##### plot setting for python ####
fs00 = 8
fs0 = 10
fs1 = 13
fs2 = 15
fs3 = 17
lw0 = 0.5
lw1 = 0.8
lw2 = 1.2
lw3 = 2.5
lw4 = 4.2
lw5 = 5











def discrete_cmap(N, base_cmap=None):
    """Create an N-bin discrete colormap from the specified input map"""

    # Note that if base_cmap is a string or None, you can simply do
    #    return plt.cm.get_cmap(base_cmap, N)
    # The following works for string, None, or a colormap instance:

    base = plt.cm.get_cmap(base_cmap)
    #color_list = base(np.linspace(0, 1, N))
    #print color_list
    #color_list[3] = np.array([ 0.87,  1 ,  1,  1.])
    #color_list[3] = np.array([ 102./255,  205./255 ,  170./255,  1.])
    #color_list[3] = np.array([ 224./255,  1 ,  1,  1.])
    #color_list[3] = np.array([ 127./255,  1 ,  212./255,  1.])
    #color_list[3] = np.array([ 64./255,  224./255 ,  208./255,  1.])
    #color_list = np.array([
    #   [ 0.70567316,  0.01555616,  0.15023281,  1.        ],
    #   [ 0.81 ,  0.2,  0.27,  1.        ],
    #   [ 0.9318313 ,  0.51908552,  0.40647961,  1.        ],
    #   #[ 0.9473454 ,  0.7946955 ,  0.71699051,  1.        ],
    #   #[ 0.75361062,  0.83023285,  0.96087116,  1.        ],
    #   [ 0.48385433,  0.62204985,  0.9748082 ,  1.        ],
    #   [ 0.35,  0.46,  0.86 ,  1.        ],
    #   [ 0.2298057 ,  0.29871797,  0.75368315,  1.        ]
    #   ])

    color_list = np.array([
       [ 0.70567316,  0.01555616,  0.15023281,  1.        ],
       [ 0.88464344,  0.4100171 ,  0.32250655,  1.        ],
       [ 0.96731652,  0.65747083,  0.53816015,  1.        ],
       [ 0.60316207,  0.73152748,  0.99956528,  1.        ],
       [ 0.40442129,  0.53464349,  0.93200191,  1.        ],
       [ 0.2298057 ,  0.29871797,  0.75368315,  1.        ]])

    color_list = np.array([
       [0.70567316, 0.01555616, 0.15023281, 1.        ],
       [0.85237814, 0.34649195, 0.28034647, 1.        ],
       [0.94405457, 0.55315348, 0.43554849, 1.        ],
       [0.51082432, 0.64939661, 0.98507878, 1.        ],
       [0.3634608 , 0.48478368, 0.90101889, 1.        ],
       [0.2298057 , 0.29871797, 0.75368315, 1.        ]])
    cmap_name = base.name + str(N)
    return base.from_list(cmap_name, color_list, N)

