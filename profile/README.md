
<img src="https://www.rafalkucharskilab.pl/assets/img/logo_COeXISTENCE.jpeg" alt="drawing" width="350"/> 

> Landing page with _tools and frameworks_ for the new class of urban routing games, where fleets of collaborative autonomous vehicles (**CAVs**) learn to make better route choice decisions in urban traffic systems.

#### The core elements are:

1. [RouteRL](https://github.com/COeXISTENCE-PROJECT/RouteRL) Multi-Agent Reinforcement Learning framework for modeling and simulating the collective route choices of humans and autonomous vehicles - [SoftwareX](https://doi.org/10.1016/j.softx.2025.102279)
<p align="center">
  <img src="https://github.com/COeXISTENCE-PROJECT/RouteRL/raw/main/docs/_static/logo.png" alt="drawing" width="150"/> 
</p>

2. [URB](https://github.com/COeXISTENCE-PROJECT/URB) Urban Routing Benchmark: Benchmarking MARL algorithms on the fleet routing tasks - [NIPS 2025](https://arxiv.org/abs/2505.17734)
<p align="center">
   <img src="https://github.com/COeXISTENCE-PROJECT/URB/blob/main/docs/urb.png" alt="drawing" width="150"/> 
</p>

---

#### With which you may run a standard task, such as:

> In the town of Nemours inhabited only by human drivers, at some point, a given share of drivers _mutate_ to CAVs and delegate their routing decisions to algorithms.
> Then, for a period of time, the CAV agents develop routing strategies to minimize their delay (e.g. using MARL).
> This process (both learning and new state) affects traffic and ill its users (human and autonomous vehicles).


<p align="center">
   <img src="https://www.rafalkucharskilab.pl/assets/img/Highlight_fig.jpg" alt="drawing" width="250"/> 
</p>



 [RouteRL](https://github.com/COeXISTENCE-PROJECT/RouteRL) can run this task for an arbitrary city with arbitrary demand (most likely from predefined case studies) and configuration. You may use some algorithm (own or from [torchRL](https://github.com/pytorch/rl)) and analyze results to draw conclusions. 
 Or you may compete in [URB](https://github.com/COeXISTENCE-PROJECT/URB) to dominate the leaderboard with your best-performing algorithm tested across variety of tasks.

 ---

🔖 For the overview of scientific contributions and societal impact see the [COeXISTENCE](https://www.rafalkucharskilab.pl/research/coexistence/) group web page.

🫵 To collaborate [mail us](mailto:coexistence@uj.edu.pl) or see contoribution guidelines at repsective repos.

👩‍🎓 prospective students, PhDs or visiting scholars welcomed - please mail [Rafał Kucharski](mailto:rafal.kucharski@uj.edu.pl)

🏃‍♀️  In the typical use-case: 

> * You import road network of a given urban areas from `Open Street Map`
> * You generate a demand pattern, where each of agents is specified with own traits and travel demans $(o_i, d_i, \tau_i$)
> * You control your experiment with a `.json` file and specify details of conducted experiment (or set of experiments).
> * You specify your human behaviour models to accurately reproduce how human drivers select routes.
> * You generate choice set of paths for each agent to select from.
> * You connect with `SUMO` traffic simulator to be used as environment to compute travel costs.
> * You run $n$ days of human learning (`SUMO days`), hoping the system will stabilize in proximity of Wardrop User Equilibrium
> * You introduce mutation and replace some human agents with `AVs`.
> * You determine `reinforcement learning` algorithm for each agent by defining rewards, observations and hyperparameters
> * You `train` your algorithms until it finds suitable `policy`
> * You roll-out the trained policy and observe impact of new routing on the system.
> * You further allow humans to adapt to actions of `AVs` and allow `AVs` to refine its policies.

📜 Complete list of available software (work-in-progress, sandboxes, discontinued projects or side quests) is:

1. [JanuX](https://github.com/COeXISTENCE-PROJECT/JanuX) tool for generating a set of path options in directed graphs. It is designed for efficient routing or creating path options for custom requirements.
<p align="center">
  <img src="https://github.com/COeXISTENCE-PROJECT/JanuX/raw/main/graphics/janux_logo.png" alt="drawing" width="50"/> 
</p>

2. Coalition formation [repo](https://github.com/COeXISTENCE-PROJECT/Coalition_formation_in_mixed_traffic_with_AVs_) where we demonstrate (for the first time) that CAVs may form exclusive routing coalitions in traffic.
3. [General Decision Model](https://github.com/COeXISTENCE-PROJECT/GeneralDecisionModel) framework to simulate the decision process of humans that can join CAV fleet.
4. [RoutingZOO](https://github.com/COeXISTENCE-PROJECT/RoutingZoo) a simulation platform where virtual drivers experiment with routing strategies to navigate from origins to destinations in dense urban networks.
5. [Wardropian Cycles](https://github.com/COeXISTENCE-PROJECT/Wardropian_cycles) a concept bridging between System Optimum and User Equilibrium Assignment in a day-to-day context.
6. [parcour](https://github.com/COeXISTENCE-PROJECT/parcour) early prototype version of _RouteRL_ by Onur Akman.
7. [BottleCOEX](https://github.com/COeXISTENCE-PROJECT/BottleCOEX) - Lightweight Simulation of Coexistence of CAVs and Human Drivers in Two-route Bottleneck Scenarios with Macroscopic Traffic Model.


<p align="center">
   <img src="https://github.com/COeXISTENCE-PROJECT/BottleCOEX/raw/main/Additional_Information/budapest_two_route_botleneck.png" alt="drawing" width="250"/> 
</p>

---
### Credits

`URB` is part of [COeXISTENCE](https://www.rafalkucharskilab.pl/research/coexistence/) (ERC Starting Grant, grant agreement No 101075838) and is a team work at Jagiellonian University in Kraków, Poland by: [Ahmet Onur Akman](https://github.com/aonurakman), [Anastasia Psarou](https://github.com/AnastasiaPsarou), [Łukasz Gorczyca](https://github.com/Limexcyan), [Michał Hoffmann](https://github.com/Crackhoff), [Lukasz Kowalski](https://github.com/LukaszKowalski2013), [Paweł Gora](https://github.com/pgora), and [Grzegorz Jamróz](https://github.com/GrzegorzJamroz), within the research group of [Rafał Kucharski](https://www.rafalkucharskilab.pl).

<p align="center">
  <img src="https://github.com/COeXISTENCE-PROJECT/URB/raw/main/docs/credits.png" width="50%"/>
</p>



### Pipeline at glance (from [here](https://www.nature.com/articles/s41598-025-90783-w))
<img width="820" alt="image" src="https://github.com/RafalKucharskiPK/rafalkucharskipk.github.io/blob/master/assets/img/scirep.jpg" />

### (Outdated) framework overview


![image](https://github.com/user-attachments/assets/3149b95e-4d7c-428c-9455-84a0cf2483f7)



