import gymnasium as gym
import numpy as np
from utils.plot_func import plot_grid_from_list as plot

env = gym.make("FrozenLake-v1", render_mode='human', is_slippery=False)
observation, info = env.reset(seed=42)

Val = np.zeros(16)
policy = [3 for _ in range(16)]
Gamma = 0.9
Theta = 0.1
MAP = ["SFFF", "FHFH", "FFFH", "HFFG"]
MAPCONCAT = "".join(MAP)

def Pol_eval(env_space,Discount):
   while True:
      Del = 0
      for state in range(env_space):
         if MAPCONCAT[state] != "H" and MAPCONCAT[state] != "G":
            v = Val[state]
            Prob,Next_state,Reward,_ = env.P[state][policy[state]][0]
            Val[state] = Prob*(Reward+Discount*Val[Next_state])
            Del = max(Del, int(np.abs(v-Val[state])))
      if Del < Theta:
         print(Del)
         break

def Pol_iter(env_space):
   policy_stable = True
   for state in range(env_space):
    if MAPCONCAT[state] != "H" and MAPCONCAT[state] != "G":
      old_action = policy[state]
      # print("This is an old value",old_action, "for", state)
      temp_act = []
      for action in env.P[state]:
         Prob2 = env.unwrapped.P[state][action][0][0]
         V_N2 = env.unwrapped.P[state][action][0][1]
         R2 = env.unwrapped.P[state][action][0][2]
         is_terminal2 = env.unwrapped.P[state][action][0][3]
         temp_act_val = Prob2*(R2+Gamma*Val[V_N2])
         temp_act.append(temp_act_val)
    else:
       temp_act.append(0)
    max_val = np.where(temp_act == max(temp_act))[0]
    any_argmax = np.random.choice(max_val)
    policy[state] = any_argmax
   #  print("This is a new value",policy[state], "for", state)
    if old_action != policy[state]:
        policy_stable = False
   return policy_stable

for _ in range(100):

   action = policy[observation]  # this is where you would insert your policy
   observation, reward, terminated, truncated, info = env.step(action)

   Pol_eval(env.observation_space.n,Gamma)
   # plot(Val)
   policy_stable = Pol_iter(env.observation_space.n)
   print(policy)
   if policy_stable:
    print('optimal policy achieved')
    break
   
   if terminated or truncated:
      observation, info = env.reset()

env.close()