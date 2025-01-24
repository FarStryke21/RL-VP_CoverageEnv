# RL-VP: Coverage Environment and Agent Policy
![Alt Text](/media/architecture.png)

This repository contains the Coverage Environment and Agent Policy Network developed for training agents with the RL-VP algorithm. 

## Install instructions

Navigate into the root directory of the repository and perform a source install

```
pip install -e .
```

## Usage

```
from viewpoint_env.viewpointWorld import CoverageEnv

env = CoverageEnv(**kwargs)
env.reset()
```


## Description

This project is a custom reinforcement learning environment, named `CoverageEnv`, built using the OpenAI Gym interface. The environment represents a 3D space with a mesh surface, and an agent that can move around to observe the mesh. The goal of the agent is to cover as much of the mesh as possible within its sensor range. The project includes methods for computing the coverage mask, reward calculation, checking termination conditions, and rendering the environment for visualization.

The repository also contains the Agent Policy Network used by the Agent. The structure is based on Stable-Baselines3.

We recommend using [RL-Baselines3-Zoo](https://github.com/DLR-RM/rl-baselines3-zoo) for training the agents. An example usage for using the policy with PPO is given below (from /hyperparams/ppo.yml):

```
CoverageEnv-v0:
  n_envs: 64
  n_timesteps: !!float 1e7
  policy: viewpoint_env.coverageAgentPolicy.CoverageAgentPolicy
  n_steps: 1024
  batch_size: 512
  gae_lambda: 0.95
  gamma: 0.99
  n_epochs: 32
  ent_coef: 0.8
  # learning_rate: !!float 1.0e-4
  learning_rate: exp_0.001
  clip_range: 0.5
```

## Contributing
Any improvements to this work are welcome! Please submit a pull request mentioning the changes and reasoning to contribute.

## Citation
Please use the following to cite this repository in publications

```
@misc{rl-vp,
  author = {Chulawala, Aman},
  title = {RL-VP: Coverage Environment},
  year = {2025},
  publisher = {GitHub},
  journal = {GitHub repository},
}
```