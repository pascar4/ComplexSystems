import os
os.system('pip install git+https://github.com/mpcrlab/mpcr/BrAIn')
from BrAIn import *

def step(a):
    env.set_actions(behavior_name, a)
    env.step()
    decision_steps, terminal_steps = env.get_steps(behavior_name)

    if len(terminal_steps) > 0:
        s = terminal_steps.obs[1][0,:,:,:]
        r = terminal_steps.reward 
        env.reset()
    else: 
        s = decision_steps.obs[1][0,:,:,:]
        r = decision_steps.reward
        
    return s,r


env = UnityEnvironment(file_name="SimpleBox1", seed=1, side_channels=[])
env.reset()
behavior_name = list(env.behavior_specs)[0]


N = 15
S = np.zeros((N,84,84,3))   #State
A = np.zeros((N,1,1))       #Action  
R = np.zeros((N,1))         #Reward



for i in range(N):

    a = np.array([[2]])

    S[i],R[i] = step(a)

    print("Reward: ",R[i]) 

    plt.imshow(S[i])
    plt.show()



