from mlagents_envs.environment import UnityEnvironment
import matplotlib.pyplot as plt
import numpy as np

# S,R = World(A)

def step(a):
    env.set_actions(behavior_name, a)
    env.step()
    decision_steps, terminal_steps = env.get_steps(behavior_name)

    if len(terminal_steps) > 0:
        s = terminal_steps.obs[0][0,:,:,:]
        r = terminal_steps.reward 
        env.reset()
    else: 
        s = decision_steps.obs[0][0,:,:,:]
        r = decision_steps.reward
        
    return s,r




env = UnityEnvironment(file_name="Lab3_1", seed=1, side_channels=[])
env.reset()
behavior_name = list(env.behavior_specs)[0]


N = 3
S = np.zeros((N,84,84,3))   #State
A = np.zeros((N,1,1))       #Action  
R = np.zeros((N,1))         #Reward

for i in range(N):

    a = np.array([[0,0,0]]) ##ML Policy

    S[i],R[i] = step(a)

    print("Reward: ",R[i]) 

    plt.imshow(S[i])
    plt.show()


#Vector Action space: (Discrete) 4 Branches:
#
#    Forward Motion 0 no action, 1 forward, 2 backward
#    Side Motion 0 no action, 1 slide right, 2 slide left
#    Rotation 0 no action, 1 turn left, 2 turn right


























#decision_steps, terminal_steps = env.get_steps(behavior_name)
#
#s = decision_steps.obs[0][0,:,:,:]
#r = decision_steps.reward
#
#a = np.array([[0,0,0,0]]) ##ML Policy
#
#env.set_actions(behavior_name, a)
#





