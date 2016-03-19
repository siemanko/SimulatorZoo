# Simulator Zoo

This repository stores simulators for reinforcement learning experiments.

# Requirements

Every simulator should provide the following Python interface:

+ simulator = Simulator(settings, record=False, seed=None) [ .__init__(settings, record=False, seed=None) ]
	+ takes settings - a dictionary of key parameters required by the simulator
	+ 'record=True' indicates that the simulator should save the full record of the simulation - for example, in form of images, video, or time series data
	+  a seed to initialize the random number generator, if None - initialized randomly
	+ automatically resets the existing simulator

+ simulator.observe() 
	+ returns STATE of the environment

+ simulator.act(action)
	+ takes ACTION (integer 0:n)
	+ returns REWARD
	+ transitions the environment to the new state

+ simulator.is_terminal()
	+ returns True/False for whether the simulator is in the terminal state

+ simulator.execution_metrics()
	+ returns a dictionary (String keys, Float values) of key metrics describing the simulator run/execution up to that point

+ simulator.execution_record(directory)
	+ takes directory name
	+ returns None
	+ saves a record of the simulator run/execution up to that point in the specified directory
	+ Note: can only be run if 'record=True' at the initialization of the simulator

+ simulator.copy()
	return exact copy of the simulator

# Moderators

Max Egorov (etotheipluspi), Szymon Sidor (nivwusquorum), Yegor Tkachenko (yegortk)

# License

All software in this collection is distributed under the Apache License 2.0
