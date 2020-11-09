import argparse 
import math 
import numpy as np 
import seaborn as sb
import matplotlib.pyplot as plt
import os.path

def voltage_gen(trial_id, length, cond, curr, dist, len_elec, nseg):
	# INPUTS
	# length: length of axon [cm]
	# cond: conductivity [S/m]
	# curr: current [nA]
	# dist: distance between electrode and axon [cm]
	# len_elec: distance between cathode and anodes
	# nseg: number of segments

	# OUTPUTS
	# One script displaying what parameters were chosen
	# Another script with unit voltages for each axon segment

	seg_length = length / nseg # length of each segment
	points = np.arange(-length / 2 + seg_length / 2, length / 2, seg_length) # generate points at the middle of each segment
	thetas = np.arctan(dist / points) # angles describing how far away the point is to the middle electrode

	# R, R1, R2 are the distances between point and each of the three electrodes
	R = np.sqrt(np.square(dist) + np.square(points))
	R1 = R - len_elec * np.cos(thetas)
	R2 = R + len_elec * np.cos(thetas)
	v_stim = 1 / 4 * cond * math.pi * ((curr[0] * curr[1]) / R1 + (curr[0] * curr[2]) / R + (curr[0] * curr[3]) / R2)
	
	#generate heat map of the unit voltages
	v_stim_heat = v_stim.reshape(1, nseg)
	heat_map_test = sb.heatmap(v_stim_heat, cmap="inferno", yticklabels = False) # like autumn, YlOrRd, inferno, magma, plasma, rocket
	plt.xlabel("Axon Segments")
	plt.show()

	# f is a text file that saves the parameters of each trial
	f = open("/Users/p.bhat/Desktop/parameters_" + str(trial_id) + ".txt", "w+")
	f.write("Trial ")
	f.write("axon length: %d\r\n" % length)
	f.write("conductivity: %d\r\n" % cond)
	f.write("current amplitude: %d\r\n" % curr[0])
	f.write("percentages: %r\r\n" % curr[1:4])
	f.write("distance from electode to nerve: %d\r\n" % dist)
	f.write("distance between cathode and anode: %d\r\n" % len_elec)
	f.write("number of segments: %d\r\n" % nseg)
	f.close()

	# save our unit voltages in a separate text file
	np.savetxt("/Users/p.bhat/Desktop/voltages_" + str(trial_id) + ".txt", v_stim)

if __name__ == "__main__":
	# parser = argparse.ArgumentParser()
	# parser.add_argument("--x", type = int)
	# args = parser.parse_args()
	# print(args)
	# print(tes_fxn(args.x))s
	print(voltage_gen("test", 10, 1/100, [5, 150, -100, 150], 1, 1, 21))

# python saving files to specific folders (save this relative to where I am), save this in current directory: relative reference ..//





