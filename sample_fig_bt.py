#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as tk
from mpl_toolkits.basemap import Basemap
import matplotlib.gridspec as gridspec
import datetime
from matplotlib.colors import LinearSegmentedColormap as LSC

## parameters
ch_fig =  # the channel you want to plot
ch_list =  # list of channels you calculated with CRTM
dom = # WRF domain number
xmax =  # domain size in x-direction
ymax =  # domain size in y-direction
time = datetime.datetime(,,,,,) # (YYYY,MM,DD,HH,mm,ss)
FILE_DIR = 'path to CRTM output directory'
filename = FILE_DIR + '/Radiance_d0'+str(dom)+'_'+time.strftime('%Y-%m-%d_%H:%M')+'.bin'

###### functions ###################################################
def ir_colormap():
    ## for 173.15 K ~ 333.15 K
    vmin = 173.15
    vmax = 333.15
    clevs = 0.5
    interval = np.arange(vmin,vmax+clevs,clevs)
    ticks = np.arange(180,340,20)
    cdict = {'red':  ((0.0,    0.9297, 0.9297), # violet
                      (0.09375,0.1   , 0.1   ), # black red
                      (0.125,  0.4844, 0.4844), # Barn red
                      (0.1875, 1.0   , 1.0   ), # red
                      (0.25,   1.0   , 1.0   ), # yellow
                      (0.3125, 0.0   , 0.0   ), # green
                      (0.34375,0.0977, 0.0977), # midnight blue
                      (0.375,  0.0   , 0.0   ), # blue
                      (0.4375, 1.0   , 1.0   ), # white
                      (1.0,    0.0   , 0.0   )),# black
             'green':((0.0000, 0.5078, 0.5078),
                      (0.09375,0.0   , 0.0   ),
                      (0.125,  0.0391, 0.0391),
                      (0.1875, 0.0   , 0.0   ),
                      (0.25,   1.0   , 1.0   ),
                      (0.3125, 1.0   , 1.0   ),
                      (0.34375,0.0977, 0.0977),
                      (0.375,  0.0   , 0.0   ),
                      (0.4375, 1.0   , 1.0   ),
                      (1.0,    0.0   , 0.0   )),
             'blue': ((0.0000, 0.9297, 0.9297),
                      (0.09375,0.0   , 0.0   ),
                      (0.125,  0.0078, 0.0078),
                      (0.1875, 0.0   , 0.0   ),
                      (0.25,   0.0   , 0.0   ),
                      (0.3125, 0.0   , 0.0   ),
                      (0.34375,0.4375, 0.4375),
                      (0.375,  1.0   , 1.0   ),
                      (0.4375, 1.0   , 1.0   ),
                      (1.0,    0.0   , 0.0   ))
            }
    ircmap = LSC('ircmap',cdict)
    return ircmap, interval, ticks

def read_crtm(filename,xmax,ymax,ch_list):
    print 'reading... '+filename
    data = np.fromfile(filename,dtype='>f4')
    n_ch = len(data)/(xmax*ymax)-2
    if n_ch != len(ch_list):
       print 'Error!! # of channels in data is '+str(n_ch)
    sim = data[:].reshape(n_ch+2,ymax,xmax)
    Tb_dict = {}
    Tb_dict['lons'] = sim[0,:,:]
    Tb_dict['lats'] = sim[1,:,:]
    for rec in range(n_ch):
       Tb_dict[ch_list[rec]] = sim[rec+2,:,:]
    return Tb_dict
####################################################################


## reading data
data = read_crtm(filename,xmax,ymax,ch_list)
lons = data['lons']
lats = data['lats']
Tb = data[ch_fig]

## plot
ircmap, ir_interval, ir_ticks = ir_colormap()
plt.figure(figsize=(10,11))
map = Basemap(projection='merc',llcrnrlat=np.amin(lats),urcrnrlat=np.amax(lats),llcrnrlon=np.amin(lons), urcrnrlon=np.amax(lons), resolution='l')
map.drawcoastlines(linewidth=0.8)
map.drawparallels(range(int(np.amin(lats)),int(np.amax(lats))+1,1),color='white',linewidth=0.2,labels=[1,0,0,1])
map.drawmeridians(range(int(np.amin(lons)),int(np.amax(lons))+1,1),color='white',linewidth=0.2,labels=[1,0,0,1])
x, y = map(lons, lats)
cs = map.contourf(x, y, Tb, ir_interval, cmap=ircmap, extend='both')
plt.title('Simulated brightness temperature (K)')
cbar = plt.colorbar(orientation='horizontal')
cbar.set_ticks(ir_ticks)

plt.savefig('sample.png')
plt.show()


