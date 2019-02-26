#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 13:50:11 2019
Script to make movies for the gravity machine paper
@author: deepak
"""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  8 11:55:48 2019

@author: deepak
"""
import imp
import GravityMachineTrack 
imp.reload(GravityMachineTrack)
import cv2
import sys
import pims
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
import matplotlib.patches as patches
from matplotlib.lines import Line2D
plt.close("all")
from matplotlib import animation
import matplotlib.ticker as ticker
import pickle


#==============================================================================
#                              Plot Parameters and Functions 
#==============================================================================
from matplotlib import rcParams
from matplotlib import rc
plt.style.use('dark_background')

#rcParams['axes.titlepad'] = 20 
#rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
### for Palatino and other serif fonts use:
##rc('font',**{'family':'serif','serif':['Palatino']})
rc('text', usetex=True)
#plt.rc('font', family='serif')

rc('font', family='sans-serif') 
rc('font', serif='Helvetica') 
rc('text', usetex='false') 
rcParams.update({'font.size': 12})


#path = '/Volumes/GRAVMACH1/HopkinsEmbroyologyCourse_GoodData/2018_06_11/Dendraster_starved_11Days_nofood/Dendraster3'
#path = '/Volumes/GRAVMACH1/HopkinsEmbroyologyCourse_GoodData/2018_06_12/Starfish/StarFish6'

# Volvox
#path = '/Volumes/GRAVMACH1/VolvoxPhotoresponse/vvx25'

# Centric diatom
path = '/Volumes/DEEPAK-SSD/GravityMachine/PuertoRico_2018/GravityMachineData/2018_11_06/Tow_1/Centric_diatom_3_Good' 


rootFolder = '/Volumes/DEEPAK-SSD/GravityMachine/MovieRawFiles'

Folder = 'Centric_Diatom_small_40_240'

savePath= os.path.join(rootFolder, Folder)

if (not os.path.exists(savePath)):
    os.makedirs(savePath)

T_start = 0
T_end = 2700

frame_start = 'IMG_0025604.tif'
frame_end = 'IMG_0025833.tif'

indexing_method = 'time'
#indexing_method = 'frame'

if(indexing_method == 'time'):
    track = GravityMachineTrack.gravMachineTrack(path, Tmin=T_start, Tmax=T_end, indexing = 'time')

elif(indexing_method=='frame'):
    track = GravityMachineTrack.gravMachineTrack(path, frame_min = frame_start, frame_max = frame_end, indexing='frame')

track.correctedDispVelocity(overwrite_flag=False)

peakFile = 'peakLocations.pkl'

savePath_peak = os.path.join(path, peakFile)

if(os.path.exists(savePath_peak)):
    with open(savePath_peak, 'rb') as f:  # Python 3: open(..., 'wb')
        peak_indicator, peak_neg_indicator = pickle.load(f)


###

#Index = track.df.index
#
#Frames =np.array(['IMG_13185.tif', 'IMG_13235.tif', 'IMG_13259.tif'])
#
#indices = np.where(np.in1d(track.df['Image name'], Frames))[0]
#
#print(indices)
#
#
#FM_smooth = track.smoothSignal(track.df['Focus Measure'],1)
#
#plt.figure()
#plt.plot(track.df['Time'],track.smoothSignal(track.df['Focus Measure'],1),'k-')
#plt.show()
#
#plt.figure()
#plt.plot(Index, FM_smooth,'g-')
#plt.scatter(Index[indices],FM_smooth[indices],50,color='r',alpha=0.5) 
#plt.show()
#
#for ii in range(track.trackLen):
#    print(track.df['Time'][ii], track.df['Image name'][ii])
    
    
    


    
##==============================================================================
## Plots for Volvox light response experiments. These are the frames used in Movies
##==============================================================================
#
#RisingEdge = []
#FallingEdge = []
#
#for ii in range(track.trackLen - 1):
#    if(track.df['LED_Intensity'][ii]==0 and track.df['LED_Intensity'][ii+1]>0):
#        RisingEdge.append(ii)
#    elif(track.df['LED_Intensity'][ii]>0 and track.df['LED_Intensity'][ii+1]==0):
#        FallingEdge.append(ii)
#
#    
#    
#custom_line = [Line2D([0], [0], color='y', lw=4), Line2D([0], [0], color='k', lw=4) ]
#
#
#fig, ax1 = plt.subplots(1,figsize=(4.8,3.6), dpi=150)
###
#
#img_index = track.imageIndex
#
#
#for ii in img_index:
#    plt.cla()
#    ax1.fill_between(track.df['Time'],y1=np.max(track.df['ZobjWheel']),y2 = np.min(track.df['ZobjWheel']) ,where = track.df['LED_Intensity']>0,facecolor = 'lemonchiffon',alpha = 0.4)
#    
##    ax1.fill_between(track.df['Time'],y1=np.max(track.df['ZobjWheel']),y2 = np.min(track.df['ZobjWheel']),where = track.df['LED_Intensity']==0,facecolor = 'k',alpha = 0.5)
#    
#    
#    ax1.plot(track.df['Time'], track.df['ZobjWheel'], 'cornflowerblue', linewidth = 2)
#    
#        
#    
#    
#    
#    line = ax1.vlines(x=np.min(track.df['Time'][ii]), ymin = np.min(track.df['ZobjWheel']),ymax = np.max(track.df['ZobjWheel']), color = 'r', linewidth = 2, zorder = 10)
#    
#    scat = ax1.scatter(np.min(track.df['Time'][ii]), np.min(track.df['ZobjWheel'][ii]), 50, color='r', zorder = 10)
#
#    ax1.legend(custom_line, ['Light ON', 'Light OFF'])
#
#    ax1.set_xlabel('Time (s)')
#    ax1.set_ylabel('Z displacement (mm)')
#    ax1.set_xlim([np.min(track.df['Time']), np.max(track.df['Time'])])
#    ax1.set_ylim([np.min(track.df['ZobjWheel']), np.max(track.df['ZobjWheel'])])
#    
#    ax1.xaxis.set_major_formatter(ticker.FormatStrFormatter('%0.0f'))
#    
#    plt.subplots_adjust(left=0.15, bottom=0.15, right=0.95, top=0.95, wspace=0, hspace=0)
#    
#    
#    img_name = 'Plot_'+track.df['Image name'][ii]
#    plt.savefig(os.path.join(savePath,img_name), dpi=150)
#    
#    
#    
#    plt.pause(0.001)
#    plt.show()
#
#
#
##=============================================================================
# Plot of centric diatom displacements
##=============================================================================
Time_loc = track.df['Time'][track.imageIndex_array[:-1]]
##

img_index = track.imageIndex

nData = 500

x_data = track.df['Time'][track.imageIndex[:-2]]
y_data = track.corrected_disp




fig, ax0 = plt.subplots(1,figsize=(4.8,3.6), dpi=150)

ax0.plot(track.df['Time'][track.imageIndex_array], track.V_objFluid , color = 'cornflowerblue', label = 'Residual', linestyle='-', linewidth=2)

for jj in range(0,len(peak_neg_indicator)-1):
    ax0.fill_between(Time_loc[peak_indicator[jj] : peak_neg_indicator[jj+1]], y1 = np.max(track.V_objFluid), y2 = np.min(track.V_objFluid), color = 'r', alpha = 0.45)

ax0.vlines(x = Time_loc[0], ymin = np.min(track.V_objFluid), ymax = np.max(track.V_objFluid),color='w',linewidth=2)


scat = ax0.scatter(Time_loc[0], track.V_objFluid[0], 50, color='r', zorder = 10)

#plt.show()



#ax0.set_ylim(np.min(track.corrected_disp), np.max(track.corrected_disp))

t_low = 40
t_high = 240

Tmin_index = next((i for i,x in enumerate(Time_loc) if x >= t_low), None)
Tmax_index = next((i for i,x in enumerate(Time_loc) if x >= t_high), None)

for ii in range(Tmin_index,Tmax_index):
    
    time = Time_loc[img_index[ii]]

    print(time)
    plt.cla()
    
    ax0.plot(track.df['Time'][track.imageIndex_array], track.V_objFluid , color = 'cornflowerblue', label = 'Residual', linestyle='-', linewidth=2)

    for jj in range(0,len(peak_neg_indicator)-1):
        ax0.fill_between(Time_loc[peak_indicator[jj] : peak_neg_indicator[jj+1]], y1 = np.max(track.V_objFluid), y2 = np.min(track.V_objFluid), color = 'r', alpha = 0.35)
    
    
    ax0.vlines(x = time, ymin = np.min(track.V_objFluid), ymax = np.max(track.V_objFluid),color='w',linewidth=2, zorder = 10)


    scat = ax0.scatter(time, track.V_objFluid[ii], 30, color='w', zorder = 10)

    
    ax0.set_ylabel('z - velocity ($ mm  s^{-1}$)')
    ax0.set_xlim(0, 400)
    ax0.set_ylim(np.min(track.V_objFluid), np.max(track.V_objFluid))
    


    
    ax0.xaxis.set_major_formatter(ticker.FormatStrFormatter('%0.0f'))
    
    plt.subplots_adjust(left=0.2, bottom=0.15, right=0.95, top=0.95, wspace=0, hspace=0)
    
    
    img_name = 'Plot_'+track.df['Image name'][img_index[ii]]
#    print(img_name)
    plt.savefig(os.path.join(savePath,img_name), dpi=150)
    
    
    
    plt.pause(0.001)
    plt.show()