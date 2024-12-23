#=========================================================================
# plot-processor-trends.py
#=========================================================================

import matplotlib.pyplot as plt
import math
import sys
import os.path

import numpy

data = numpy.array([
[ 1971.92,0.0023,1,0.7,0.45,0.000012 ],
[ 1972.33,0.0035,1,0.5,0.42,0.000012 ],
[ 1974.33,0.006,1,2,0.92,0.000149    ],
[ 1979.50,0.029,1,5,1.7,0.000212     ],
[ 1982.17,0.134,1,6,3,0.000560       ],
[ 1985.83,0.275,1,16,1.5,0.006851    ],
[ 1986.08,0.11,1,16,3,0.000000       ],
[ 1988.50,0.12,1,40,4,0.046875       ],
[ 1989.33,1.2,1,25,2.75,0.028226     ],
[ 1990.42,1.2,1,33,3.5,0.031250      ],
[ 1992.25,1.2,1,66,5.8,0.050235      ],
[ 1992.50,1.1,1,100,15,0.099126      ],
[ 1992.50,3.1,1,60,14.2,0.149529     ],
[ 1992.83,1.7,1,200,35,0.178931      ],
[ 1993.25,0.93,1,40,3,0.000000       ],
[ 1993.25,3.1,1,66,13,0.130880       ],
[ 1994.50,1.9,1,150,3,0.191532       ],
[ 1994.50,2.8,1,300,28,0.338541      ],
[ 1995.25,9.67,1,300,50,0.578272     ],
[ 1995.50,3.1,1,90,16,0.226814       ],
[ 1995.92,5.2,1,200,30,0.530650      ],
[ 1995.92,5.5,1,200,32.6,0.551059    ],
[ 1996.08,3.6,1,200,10,0.374176      ],
[ 1996.08,6.8,1,200,30,0.775565      ],
[ 1996.25,4.3,1,90,11,0.000000       ],
[ 1996.58,9.67,1,500,43,1.020480     ],
[ 1997.08,5.4,1,250,25,0.707533      ],
[ 1997.25,3.5,1,533,36,0.972858      ],
[ 1997.33,8.8,1,233,17,0.462618      ],
[ 1997.42,7.5,1,300,32,0.795974      ],
[ 1998.58,15.2,1,500,91,1.990400     ],
[ 1998.92,6.9,1,300,30,1.251789      ],
[ 1998.92,9.3,1,400,14,0.646304      ],
[ 1999.17,9.5,1,500,21,1.491200      ],
[ 1999.17,21.3,1,450,17,1.040890     ],
[ 1999.92,22,1,750,35,1.870880       ],
[ 2000.42,28,1,1000,20,2.624000      ],
[ 2000.42,37,1,1000,49,2.675200      ],
[ 2000.75,29,1,900,70,2.988800       ],
[ 2000.92,42,1,2000,72,3.430400      ],
[ 2001.42,25,1,800,98,2.368000       ],
[ 2001.50,37,1,1400,56,3.545600      ],
[ 2002.08,55,1,2200,48,5.190400      ],
[ 2002.50,37.2,1,1800,62,4.723200    ],
[ 2002.58,221,1,1000,98,5.184000     ],
[ 2003.08,152,1,1150,155,5.612800    ],
[ 2003.17,54.3,1,2160,74,6.368000    ],
[ 2003.33,106,1,1800,89,7.488000     ],
[ 2004.50,106,1,2600,89,11.865600    ],
[ 2004.50,125,1,3600,115,10.080000   ],
[ 2004.50,276,2,1900,100,8.947200    ],
[ 2005.42,230,2,3200,130,9.510400    ],
[ 2005.50,114,1,2800,85,11.916800    ],
[ 2005.58,300,8,1200,72,0.000000     ],
[ 2005.67,114,2,2200,25,0.000000     ],
[ 2006.50,154,2,2600,65,10.400000    ],
[ 2006.50,376,2,3600,130,11.609600   ],
[ 2006.58,243,2,2800,125,11.400000   ],
[ 2006.58,291,2,2800,75,21.000000    ],
[ 2006.58,582,2,2660,65,19.800000    ],
[ 2006.67,152,2,2330,31,13.100000    ],
[ 2007.33,582,4,2930,130,22.100000   ],
[ 2007.42,234,9,4000,100,0.000000    ],
[ 2007.42,790,2,4700,100,17.800000   ],
[ 2007.50,114,2,2000,31,7.700000     ],
[ 2007.58,503,8,1400,84,0.000000     ],
[ 2007.75,450,4,2300,95,0.000000     ],
[ 2007.75,463,4,2000,75,11.200000    ],
[ 2008.08,410,2,3000,65,23.500000    ],
[ 2008.83,450,3,2500,95,0.000000     ],
[ 2008.92,781,4,3200,130,33.600000   ],
[ 2009.08,0,4,3000,125,0.000000      ],
[ 2009.17,0,3,2800,95,0.000000       ],
[ 2009.33,1900,6,2660,130,0.000000   ],
[ 2009.33,2300,8,3200,130,0.000000   ],
[ 2009.50,731,4,3330,130,40.800000   ],
[ 2009.75,410,16,2300,0,0.000000     ],
[ 2009.75,774,4,2800,95,37.900000    ],
[ 2009.75,774,4,2930,95,39.000000    ],
[ 2009.83,731,4,3200,130,38.700000   ],
[ 2010.08,1300,48,0,125,0.000000     ],
[ 2010.17,731,4,2800,130,35.000000   ],
[ 2010.25,1170,6,3330,130,37.200000  ],
[ 2010.42,382,2,3600,73,34.200000    ],
[ 2010.42,774,4,3070,95,40.000000    ],
[ 2010.50,382,2,3200,73,32.200000    ],
[ 2010.50,382,2,3330,73,33.200000    ],
[ 2010.50,382,2,3470,73,34.000000    ],
[ 2011.08,1160,4,2800,95,39.000000   ],
[ 2011.08,1160,4,3100,95,42.000000   ],
[ 2011.08,1160,4,3300,95,45.100000   ],
[ 2011.08,1160,4,3400,95,47.100000   ],
[ 2011.17,1170,6,3470,130,40.600000  ],
[ 2011.42,1160,4,2900,95,42.300000   ],
[ 2011.75,1160,4,3000,95,43.600000   ],
[ 2011.83,1160,4,3400,95,52.800000   ],
[ 2011.83,1160,4,3500,95,52.400000   ],
[ 2011.92,2270,6,3300,130,49.000000  ],
[ 2012.33,1400,4,3100,77,47.600000   ],
[ 2012.33,1400,4,3400,77,51.100000   ],
[ 2012.33,1400,4,3500,77,54.400000   ],
[ 2012.50,1400,4,3200,77,48.800000   ],
[ 2012.50,1400,4,3400,77,51.100000   ],
[ 2012.75,1400,4,3000,77,44.200000   ],
[ 2013.50,1400,4,3200,84,55.700000   ],
[ 2014.50,1400,4,3500,88,60.200000   ],
[ 2014.50,1400,4,3500,84,61.400000   ],
[ 2014.50,1400,4,4000,88,67.600000   ],
[ 2012.50,5000,62,1000,115,0.000000  ],
[ 2014.50,4310,15,0,0,0.000000       ],
[ 2012.50,3100,8,0,0,0.000000        ],
[ 2012.50,2750,6,5500,0,0.000000     ],
[ 2011.50,2600,10,0,0,0.000000       ],
[ 2011.50,2300,8,0,0,0.000000        ],
[ 2011.50,2270,6,0,0,0.000000        ],
[ 2012.50,2100,8,0,0,0.000000        ],
[ 2010.50,2000,4,0,0,0.000000        ],
[ 2008.50,1900,6,0,0,0.000000        ],
[ 2010.50,1200,8,0,0,0.000000        ],
[ 2012.50,1200,8,0,0,0.000000        ],
[ 2010.50,1000,16,1670,0,0.000000    ],
],)

#-------------------------------------------------------------------------
# Calculate figure size
#-------------------------------------------------------------------------
# We determine the fig_width_pt by using \showthe\columnwidth in LaTeX
# and copying the result into the script. Change the aspect ratio as
# necessary.

fig_width_pt  = 700.0
inches_per_pt = 1.0/72.27                     # convert pt to inch
aspect_ratio  = 0.65  # aesthetic golden mean

fig_width     = fig_width_pt * inches_per_pt  # width in inches
fig_height    = fig_width * aspect_ratio      # height in inches
fig_size      = [ fig_width, fig_height ]

#-------------------------------------------------------------------------
# Configure matplotlib
#-------------------------------------------------------------------------

plt.rcParams['pdf.use14corefonts'] = True
plt.rcParams['font.size']          = 9
plt.rcParams['font.family']        = 'serif'
plt.rcParams['font.serif']         = ['Helvetica']
plt.rcParams['figure.figsize']     = fig_size

#-------------------------------------------------------------------------
# Create plot
#-------------------------------------------------------------------------

fig = plt.figure()
ax = fig.add_subplot(1,1,1)

ax.plot( data[:,0], numpy.multiply(data[:,1],1000), marker='o', color='red',
         linestyle='none', markeredgecolor='none', markersize=4 )

ax.plot( data[:,0], numpy.divide(data[:,5],0.000560), marker='s', color='blue',
         linestyle='none', markeredgecolor='none', markersize=4 )

ax.plot( data[:,0], data[:,3], marker='p', color='green',
         linestyle='none', markeredgecolor='none', markersize=5 )

ax.plot( data[:,0], data[:,4], marker='^', color='orange',
         linestyle='none', markeredgecolor='none', markersize=5 )

ax.plot( data[:,0], data[:,2], marker='o', color='black',
         linestyle='none', markeredgecolor='none', markersize=4 )

#ax.set_xlabel('Foo')
#%ax.set_ylabel('Probability')
ax.set_xlim( 1970, 2020 )
ax.set_ylim( 0.25, 10000000 )

# Turn off top and right border

ax.set_yscale('log')
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

#-------------------------------------------------------------------------
# Generate PDF
#-------------------------------------------------------------------------

input_basename = os.path.splitext( os.path.basename(sys.argv[0]) )[0]
output_filename = input_basename + '.py.pdf'
plt.savefig( output_filename, bbox_inches='tight' )

