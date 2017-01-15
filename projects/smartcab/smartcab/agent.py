import random
import math
import sys
from environment import Agent, Environment
from planner import RoutePlanner
from simulator import Simulator

import numpy as np
import pandas as pd
import os
import ast

class LearningAgent(Agent):
    """ An agent that learns to drive in the Smartcab world.
        This is the object you will be modifying. """ 

    def __init__(self, env, learning=False, epsilon=1.0, alpha=0.5):
        super(LearningAgent, self).__init__(env)     # Set the agent in the evironment 
        self.planner = RoutePlanner(self.env, self)  # Create a route planner
        self.valid_actions = self.env.valid_actions  # The set of valid actions

        # Set parameters of the learning agent
        self.learning = learning # Whether the agent is expected to learn
        self.Q = dict()          # Create a Q-table which will be a dictionary of tuples
        self.epsilon = epsilon   # Random exploration factor
        self.alpha = alpha       # Learning factor

        ###########
        ## TO DO ##
        ###########
        # Set any additional class parameters as needed


    def reset(self, destination=None, testing=False):
        """ The reset function is called at the beginning of each trial.
            'testing' is set to True if testing trials are being used
            once training trials have completed. """

        # Select the destination as the new location to route to
        self.planner.route_to(destination)
        
        ########### 
        ## TO DO ##
        ###########
        # Update epsilon using a decay function of your choice
        # Update additional class parameters as needed
        # If 'testing' is True, set epsilon and alpha to 0

        return None

    def build_state(self):
        """ The build_state function is called when the agent requests data from the 
            environment. The next waypoint, the intersection inputs, and the deadline 
            are all features available to the agent. """

        # Collect data about the environment
        waypoint = self.planner.next_waypoint() # The next waypoint 
        inputs = self.env.sense(self)           # Visual input - intersection light and traffic
        deadline = self.env.get_deadline(self)  # Remaining deadline

        ########### 
        ## TO DO ##
        ###########
        # Set 'state' as a tuple of relevant data for the agent        
        state = None

        return state


    def get_maxQ(self, state):
        """ The get_max_Q function is called when the agent is asked to find the
            maximum Q-value of all actions based on the 'state' the smartcab is in. """

        ########### 
        ## TO DO ##
        ###########
        # Calculate the maximum Q-value of all actions for a given state

        maxQ = None

        return maxQ 


    def createQ(self, state):
        """ The createQ function is called when a state is generated by the agent. """

        ########### 
        ## TO DO ##
        ###########
        # When learning, check if the 'state' is not in the Q-table
        # If it is not, create a new dictionary for that state
        #   Then, for each action available, set the initial Q-value to 0.0

        return


    def choose_action(self, state):
        """ The choose_action function is called when the agent is asked to choose
            which action to take, based on the 'state' the smartcab is in. """

        # Set the agent state and default action
        self.state = state
        self.next_waypoint = self.planner.next_waypoint()
        action = None

        ########### 
        ## TO DO ##
        ###########
        # When not learning, choose a random action
        # When learning, choose a random action with 'epsilon' probability
        #   Otherwise, choose an action with the highest Q-value for the current state
 
        return action


    def learn(self, state, action, reward):
        """ The learn function is called after the agent completes an action and
            receives a reward. This function does not consider future rewards 
            when conducting learning. """

        ########### 
        ## TO DO ##
        ###########
        # When learning, implement the value iteration update rule
        #   Use only the learning rate 'alpha' (do not use the discount factor 'gamma')

        return


    def update(self):
        """ The update function is called when a time step is completed in the 
            environment for a given trial. This function will build the agent
            state, choose an action, receive a reward, and learn if enabled. """

        state = self.build_state()          # Get current state
        self.createQ(state)                 # Create 'state' in Q-table
        action = self.choose_action(state)  # Choose an action
        reward = self.env.act(self, action) # Receive a reward
        self.learn(state, action, reward)   # Q-learn

        return
        

class BasicAgent(LearningAgent):
    def choose_action(self, state):
        """ The choose_action function is called when the agent is asked to choose
            which action to take, based on the 'state' the smartcab is in. """

        # Set the agent state and default action
        self.state = state
        self.next_waypoint = self.planner.next_waypoint()
 
        return self.valid_actions[random.randrange(0,len(self.valid_actions))]

class InformedAgent(LearningAgent):
    def __init__(self, env):
        super(InformedAgent, self).__init__(env)
        self.learning = True

    def reset(self, destination=None, testing=False):
        """ The reset function is called at the beginning of each trial.
            'testing' is set to True if testing trials are being used
            once training trials have completed. """

        # Select the destination as the new location to route to
        self.planner.route_to(destination)
        
        ########### 
        ## TO DO ##
        ###########
        # Update epsilon using a decay function of your choice
        # Update additional class parameters as needed
        # If 'testing' is True, set epsilon and alpha to 0

        if testing:
            self.epsilon = 0
            self.alpha = 0
        else:
            self.epsilon = self.epsilon - 0.05

        return None

    def build_state(self):
        """ The build_state function is called when the agent requests data from the 
            environment. The next waypoint, the intersection inputs, and the deadline 
            are all features available to the agent. """

        # Collect data about the environment
        waypoint = self.planner.next_waypoint() # The next waypoint 
        inputs = self.env.sense(self)           # Visual input - intersection light and traffic
        deadline = self.env.get_deadline(self)  # Remaining deadline

        ########### 
        ## TO DO ##
        ###########
        # Set 'state' as a tuple of relevant data for the agent        
        state = (waypoint, inputs['light'], inputs['oncoming'])

        return state

    def get_maxQ(self, state):
        """ The get_max_Q function is called when the agent is asked to find the
            maximum Q-value of all actions based on the 'state' the smartcab is in. """

        ########### 
        ## TO DO ##
        ###########
        # Calculate the maximum Q-value of all actions for a given state
        max_action = None
        maxQ = None
        for k,v in self.Q[state].iteritems():
            if maxQ == None or v > maxQ:
                maxQ = v
                max_action = k

        return maxQ 


    def createQ(self, state):
        """ The createQ function is called when a state is generated by the agent. """

        ########### 
        ## TO DO ##
        ###########
        # When learning, check if the 'state' is not in the Q-table
        # If it is not, create a new dictionary for that state
        #   Then, for each action available, set the initial Q-value to 0.0
        if self.learning:
            if state not in self.Q:
                self.Q[state] = {None: 0., 'forward': 0., 'left': 0., 'right': 0.}

        return

    def choose_action(self, state):
        """ The choose_action function is called when the agent is asked to choose
            which action to take, based on the 'state' the smartcab is in. """

        # Set the agent state and default action
        self.state = state
        self.next_waypoint = self.planner.next_waypoint()
        action = None

        ########### 
        ## TO DO ##
        ###########
        # When not learning, choose a random action
        # When learning, choose a random action with 'epsilon' probability
        #   Otherwise, choose an action with the highest Q-value for the current state

        if not self.learning:
            action = self.valid_actions[random.randrange(0,len(self.valid_actions))]
        else:
            n = random.random()
            if self.epsilon > n:
                action = self.valid_actions[random.randrange(0,len(self.valid_actions))]
            else:
                maxQ = self.get_maxQ(state)
                possible_actions = []
                for k,v in self.Q[state]:
                    if v == maxQ:
                        possible_actions.append(k)

                action = random.choice(possible_actions)
 
        return action

    def learn(self, state, action, reward):
        """ The learn function is called after the agent completes an action and
            receives a reward. This function does not consider future rewards 
            when conducting learning. """

        ########### 
        ## TO DO ##
        ###########
        # When learning, implement the value iteration update rule
        #   Use only the learning rate 'alpha' (do not use the discount factor 'gamma')
        if self.learning: 
            self.Q[state][action] = self.Q[state][action] * (1 - self.alpha) + (self.alpha * reward)

        return

class OptimizedAgent(InformedAgent):
    def __init__(self, env, epsilon=1.0, alpha=0.5):
        super(OptimizedAgent, self).__init__(env)
        self.trial_number = 0
        self.epsilon = epsilon
        self.alpha = alpha


    def reset(self, destination=None, testing=False):
        """ The reset function is called at the beginning of each trial.
            'testing' is set to True if testing trials are being used
            once training trials have completed. """

        # Select the destination as the new location to route to
        self.planner.route_to(destination)
        
        ########### 
        ## TO DO ##
        ###########
        # Update epsilon using a decay function of your choice
        # Update additional class parameters as needed
        # If 'testing' is True, set epsilon and alpha to 0

        self.trial_number += 1

        if testing:
            self.epsilon = 0
            self.alpha = 0
        else:
            # self.epsilon = self.epsilon - 0.01
            self.epsilon = math.e ** -(self.alpha * self.trial_number)
            # self.epsilon = self.alpha ** self.trial_number
            # self.epsilon = 1 / self.trial_number ** 2
            # self.epsilon = math.cos(self.alpha * self.trial_number)

        return None


def run(agent_type, alpha, tolerance, n_test):
    """ Driving function for running the simulation. 
        Press ESC to close the simulation, or [SPACE] to pause the simulation. """

    ##############
    # Create the environment
    # Flags:
    #   verbose     - set to True to display additional output from the simulation
    #   num_dummies - discrete number of dummy agents in the environment, default is 100
    #   grid_size   - discrete number of intersections (columns, rows), default is (8, 6)
    env = Environment()
    
    ##############
    # Create the driving agent
    # Flags:
    #   learning   - set to True to force the driving agent to use Q-learning
    #    * epsilon - continuous value for the exploration factor, default is 1
    #    * alpha   - continuous value for the learning rate, default is 0.5
    optimized = False
    if agent_type == 'basic':
        agent = env.create_agent(BasicAgent)
    elif agent_type == 'informed':
        agent = env.create_agent(InformedAgent)
    else:
        agent = env.create_agent(OptimizedAgent, alpha=alpha)
        optimized = True
    
    ##############
    # Follow the driving agent
    # Flags:
    #   enforce_deadline - set to True to enforce a deadline metric
    env.set_primary_agent(agent, enforce_deadline=True)

    ##############
    # Create the simulation
    # Flags:
    #   update_delay - continuous time (in seconds) between actions, default is 2.0 seconds
    #   display      - set to False to disable the GUI if PyGame is enabled
    #   log_metrics  - set to True to log trial and simulation results to /logs
    #   optimized    - set to True to change the default log file name
    sim = Simulator(env, update_delay=0.01, display=False, log_metrics=True, optimized=optimized)
    
    ##############
    # Run the simulator
    # Flags:
    #   tolerance  - epsilon tolerance before beginning testing, default is 0.05 
    #   n_test     - discrete number of testing trials to perform, default is 0
    return sim.run(n_test=n_test, tolerance=tolerance)


def calculate_safety(data):
	""" Calculates the safety rating of the smartcab during testing. """

	good_ratio = data['good_actions'].sum() * 1.0 / \
	(data['initial_deadline'] - data['final_deadline']).sum()

	if good_ratio == 1: # Perfect driving
		return ("A+", "green")
	else: # Imperfect driving
		if data['actions'].apply(lambda x: ast.literal_eval(x)[4]).sum() > 0: # Major accident
			return ("F", "red")
		elif data['actions'].apply(lambda x: ast.literal_eval(x)[3]).sum() > 0: # Minor accident
			return ("D", "#EEC700")
		elif data['actions'].apply(lambda x: ast.literal_eval(x)[2]).sum() > 0: # Major violation
			return ("C", "#EEC700")
		else: # Minor violation
			minor = data['actions'].apply(lambda x: ast.literal_eval(x)[1]).sum()
			if minor >= len(data)/2: # Minor violation in at least half of the trials
				return ("B", "green")
			else:
				return ("A", "green")


def calculate_reliability(data):
	""" Calculates the reliability rating of the smartcab during testing. """

	success_ratio = data['success'].sum() * 1.0 / len(data)

	if success_ratio == 1: # Always meets deadline
		return ("A+", "green")
	else:
		if success_ratio >= 0.90:
			return ("A", "green")
		elif success_ratio >= 0.80:
			return ("B", "green")
		elif success_ratio >= 0.70:
			return ("C", "#EEC700")
		elif success_ratio >= 0.60:
			return ("D", "#EEC700")
		else:
			return ("F", "red")

if __name__ == '__main__':
    random.seed(42)
    
    # default agent
    agent_type = 'optimized'

    # these params only work for optimized agent
    tolerance = 0.01
    n_test = 100
    results = []

    n = len(sys.argv)
    if n == 2:
        agent_type = sys.argv[1]

    # use this if you want to run a series of trials with varying alpha values
    # alphas = np.arange(1.0, 0, -0.1)
    # alphas = np.append(alphas, 0.05)
    # alphas = np.append(alphas, 0.01)

    # or use this if you want to run the optimal alpha value
    alphas = [0.01]
    for alpha in alphas:
        training_trials = run(agent_type, alpha, tolerance, n_test)
        data = pd.read_csv(os.path.join("logs", "sim_improved-learning.csv"))
        data['good_actions'] = data['actions'].apply(lambda x: ast.literal_eval(x)[0])
        testing_data = data[data['testing'] == True]

        safety_rating, safety_color = calculate_safety(testing_data)
        reliability_rating, reliability_color = calculate_reliability(testing_data)
        print "Safety: {}, Reliability: {}".format(safety_rating, reliability_rating)
        results.append({"trials": training_trials, "alpha": alpha, "tolerance": tolerance, "safety": safety_rating, "reliability": reliability_rating})

    print "Results:"
    for r in results:
        print r
