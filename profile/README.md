
<!--
<img src="../static/coexistence.png" alt="drawing" width="350"/> 
-->

<p align="center">
  <img src="../static/coexistence.png" alt="drawing" width="500"/> 
</p>

<p align="center">
  <a href="https://github.com/orgs/COeXISTENCE-PROJECT/repositories">
    <img src="https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.github.com%2Forgs%2FCOeXISTENCE-PROJECT&query=%24.public_repos&label=Public%20Repositories&style=flat-square&logo=github&color=0F766E" alt="COeXISTENCE public repositories"/>
  </a>
  <a href="https://github.com/COeXISTENCE-PROJECT/URB/releases">
    <img src="https://img.shields.io/github/v/release/COeXISTENCE-PROJECT/URB?display_name=release&label=URB&style=flat-square" alt="URB GitHub release"/>
  </a>
  <a href="https://pypi.org/project/routerl/">
    <img src="https://img.shields.io/pypi/v/routerl?label=RouteRL%20PyPI&style=flat-square" alt="RouteRL PyPI version"/>
  </a>
  <a href="https://pypi.org/project/janux/">
    <img src="https://img.shields.io/pypi/v/janux?label=JanuX%20PyPI&style=flat-square" alt="JanuX PyPI version"/>
  </a>
</p>

<p align="center">
  <a href="https://github.com/COeXISTENCE-PROJECT/RouteRL/stargazers">
    <img src="https://img.shields.io/github/stars/COeXISTENCE-PROJECT/RouteRL?label=RouteRL%20stars&style=flat-square&color=DAA520" alt="RouteRL stars"/>
  </a>
  <a href="https://github.com/COeXISTENCE-PROJECT/RouteRL/forks">
    <img src="https://img.shields.io/github/forks/COeXISTENCE-PROJECT/RouteRL?label=RouteRL%20forks&style=flat-square&color=F97316" alt="RouteRL forks"/>
  </a>
  <a href="https://github.com/COeXISTENCE-PROJECT/URB/stargazers">
    <img src="https://img.shields.io/github/stars/COeXISTENCE-PROJECT/URB?label=URB%20stars&style=flat-square&color=DAA520" alt="URB stars"/>
  </a>
  <a href="https://github.com/COeXISTENCE-PROJECT/URB/forks">
    <img src="https://img.shields.io/github/forks/COeXISTENCE-PROJECT/URB?label=URB%20forks&style=flat-square&color=F97316" alt="URB forks"/>
  </a>
</p>

**We study the new class of urban routing games, where fleets of collaborative autonomous vehicles (CAVs) learn to make better route choice decisions in mixed urban traffic systems.**

#### The core elements are:

<img src="../static/routerl_modern.png" alt="RouteRL" align="right" width="200">

1. [RouteRL](https://github.com/COeXISTENCE-PROJECT/RouteRL): Multi-Agent Reinforcement Learning framework for modeling and simulating the collective route choices of humans and autonomous vehicles - [SoftwareX](https://doi.org/10.1016/j.softx.2025.102279), [Docs](https://coexistence-project.github.io/RouteRL/)

<img src="../static/urb.png" alt="URB" align="right" width="200">

2. [URB](https://github.com/COeXISTENCE-PROJECT/URB) - Urban Routing Benchmark: Benchmarking MARL algorithms on the fleet routing tasks - [NeurIPS 2025](https://proceedings.neurips.cc/paper_files/paper/2025/file/77e5b98de7d7060bc7c57d7943b53d8f-Paper-Datasets_and_Benchmarks_Track.pdf), [Website](https://www.urbenchmark.com), [Leaderboard](https://coexistence-project.github.io/URB/)

---

#### With which you may run a standard task, such as:

<p align="center">
   <img src="../static/highlight_rounded.png" alt="drawing" width="350"/> 
</p>

> In the town of Nemours inhabited only by human drivers, at some point, a given share of drivers _mutate_ to CAVs and delegate their routing decisions to algorithms.
> Then, for a period of time, the CAV agents develop routing strategies to minimize their delay (e.g. using MARL).
> This process (both learning and new state) affects traffic and all its users (human and autonomous vehicles).



 [RouteRL](https://github.com/COeXISTENCE-PROJECT/RouteRL) can run this task for an arbitrary city with arbitrary demand (most likely from predefined case studies) and configuration. You may use some algorithm (own or from [TorchRL](https://github.com/pytorch/rl)) and analyze results to draw conclusions.
 <p align="center">
  <img src="../static/routerl_overview.png" width="50%"/>
</p>

 Then, you may compete in [URB](https://github.com/COeXISTENCE-PROJECT/URB) to dominate [the official leaderboard](https://coexistence-project.github.io/URB/) with your best-performing algorithm tested across variety of tasks.
 <p align="center">
  <img src="../static/urb_overview.png" width="50%"/>
</p>


🏃‍♀️  In the typical use-case: 

> * You import road network of a given urban areas from [`Open Street Map`](https://www.openstreetmap.org/#map=19/50.030513/19.906586).
> * You generate a demand pattern, where each of agents is specified with own traits and travel demans $(o_i, d_i, \tau_i$).
> * You control your experiment with a `.json` file and specify details of conducted experiment (or set of experiments).
> * You specify your human behaviour models to accurately reproduce how human drivers select routes.
> * You generate choice set of paths for each agent to select from.
> * You connect with `SUMO` traffic simulator to be used as environment to compute travel costs.
> * You run $n$ days of human learning (`SUMO days`), hoping the system will stabilize in proximity of Wardrop User Equilibrium.
> * You introduce mutation and replace some human agents with `CAVs`.
> * You determine `reinforcement learning` algorithm for each agent by defining rewards, observations and hyperparameters.
> * You `train` your algorithms until it finds suitable `policy`.
> * You roll-out the trained policy and observe impact of new routing on the system.
> * You further allow humans to adapt to actions of `CAVs` and allow `CAVs` to refine its policies.

---

### 🧑‍💻 Software

Complete list of available software (work-in-progress, sandboxes, discontinued projects, or side quests) is:

<img src="https://github.com/COeXISTENCE-PROJECT/JanuX/raw/main/graphics/janux_logo.png" alt="JanuX" align="right" width="75">

1\. [JanuX](https://github.com/COeXISTENCE-PROJECT/JanuX) — Tool for generating a set of path options in directed graphs. Designed for efficient routing and creating path options for custom requirements.

<br>

2\. [GenTTP](https://github.com/COeXISTENCE-PROJECT/OptimalAssignment) — Leading to optimal assigment by approximating SUMO with ML methods.

<img src="https://raw.githubusercontent.com/aonurakman/demandify/refs/heads/main/static/demandify.png" alt="demandify" align="right" width="75">

3\. [demandify](https://github.com/COeXISTENCE-PROJECT/demandify) — Reproduce real-world traffic congestion with synthetic demand calibration for agent-based traffic scenarios using genetic algorithms.

<br>

<img src="https://raw.githubusercontent.com/COeXISTENCE-PROJECT/OpenURB/main/docs/openurb.png" alt="OpenURB" align="right" width="75">

4\. [OpenURB](https://github.com/COeXISTENCE-PROJECT/OpenURB) — A benchmark for testing MARL algorithms for CAV route choice under dynamic CAV-HDV changes.

<br>

5\. [Coalition formation](https://github.com/COeXISTENCE-PROJECT/Coalition_formation_in_mixed_traffic_with_AVs_) — We demonstrate (for the first time) that CAVs may form exclusive routing coalitions in traffic.

6\. [General Decision Model](https://github.com/COeXISTENCE-PROJECT/GeneralDecisionModel) — Framework to simulate the decision process of humans that can join CAV fleet.

7\. [RoutingZOO](https://github.com/COeXISTENCE-PROJECT/RoutingZoo) — A simulation platform where virtual drivers experiment with routing strategies to navigate from origins to destinations in dense urban networks.

8\. [Wardropian Cycles](https://github.com/COeXISTENCE-PROJECT/Wardropian_cycles) — A concept bridging between System Optimum and User Equilibrium Assignment in a day-to-day context.

9\. [parcour](https://github.com/COeXISTENCE-PROJECT/parcour) — An early prototype version of _RouteRL_ by Onur Akman.

10\. [BottleCOEX](https://github.com/COeXISTENCE-PROJECT/BottleCOEX) — Lightweight Simulation of coexistence of CAVs and human drivers in two-route bottleneck scenarios with a macroscopic traffic model.


<p align="center">
   <img src="../static/budapest_bottleneck.png" alt="drawing" width="350"/> 
</p>

---

### 🤝 Get in touch

🔖 For the overview of scientific contributions and societal impact see the [COeXISTENCE](https://www.rafalkucharskilab.pl/research/coexistence/) group web page.

🫵 To collaborate [mail us](mailto:coexistence@uj.edu.pl) or see contribution guidelines at repsective repositories.

👩‍🎓 Prospective students, PhDs or visiting scholars welcomed - please mail [Rafał Kucharski](mailto:rafal.kucharski@uj.edu.pl).

---
### Credits

This project is developed within the [COeXISTENCE](https://www.rafalkucharskilab.pl/research/coexistence/) project  
(ERC Starting Grant, grant agreement No. 101075838), based at Jagiellonian University in Kraków, Poland.

#### Project members

<p align="center">
  <a href="https://github.com/aonurakman" title="Onur Akman">
    <img src="../static/contributors/cards/aonurakman.png" width="19%" alt="Onur Akman"/>
  </a>
  <a href="https://github.com/AnastasiaPsarou" title="Anastasia Psarou">
    <img src="../static/contributors/cards/anastasiapsarou.png" width="19%" alt="Anastasia Psarou"/>
  </a>
  <a href="https://github.com/Limexcyan" title="Łukasz Gorczyca">
    <img src="../static/contributors/cards/limexcyan.png" width="19%" alt="Łukasz Gorczyca"/>
  </a>
  <a href="https://github.com/Blato122" title="Błażej Torbus">
    <img src="../static/contributors/cards/blato122.png" width="19%" alt="Błażej Torbus"/>
  </a>
  <a href="https://github.com/L2Space" title="Kacper Drozd">
    <img src="../static/contributors/cards/l2space.png" width="19%" alt="Kacper Drozd"/>
  </a>
</p>

<p align="center">
  <a href="https://github.com/mikolajRams" title="Mikołaj Rams">
    <img src="../static/contributors/cards/mikolajrams.png" width="19%" alt="Mikołaj Rams"/>
  </a>
  <a href="https://github.com/pgora" title="Paweł Gora">
    <img src="../static/contributors/cards/pgora.png" width="19%" alt="Paweł Gora"/>
  </a>
  <a href="https://github.com/michallbujak" title="Michał Bujak">
    <img src="../static/contributors/cards/michallbujak.png" width="19%" alt="Michał Bujak"/>
  </a>
  <a href="https://github.com/GrzegorzJamroz" title="Grzegorz Jamróz">
    <img src="../static/contributors/cards/grzegorzjamroz.png" width="19%" alt="Grzegorz Jamróz"/>
  </a>
  <a href="https://github.com/RafalKucharskiPK" title="Rafał Kucharski">
    <img src="../static/contributors/cards/rafalkucharskipk.png" width="19%" alt="Rafał Kucharski"/>
  </a>
</p>

#### Affiliated contributors and former members

<p align="center">
  <a href="https://github.com/dg7s" title="Dominik Gaweł">
    <img src="../static/contributors/cards/dg7s.png" width="19%" alt="Dominik Gaweł"/>
  </a>
  <a href="https://github.com/msudolm" title="Małgorzata Sudoł">
    <img src="../static/contributors/cards/msudolm.png" width="19%" alt="Małgorzata Sudoł"/>
  </a>
  <a href="https://github.com/Crackhoff" title="Michał Hoffmann">
    <img src="../static/contributors/cards/crackhoff.png" width="19%" alt="Michał Hoffmann"/>
  </a>
  <a href="https://github.com/kistref" title="Zoltán Varga">
    <img src="../static/contributors/cards/kistref.png" width="19%" alt="Zoltán Varga"/>
  </a>
  <a href="https://github.com/natdesc" title="Natello Descormier">
    <img src="../static/contributors/cards/natdesc.png" width="19%" alt="Natello Descormier"/>
  </a>
</p>



### 🔎 Pipeline at glance (from [here](https://www.nature.com/articles/s41598-025-90783-w))
<p align="center">
  <img src="../static/overview.png" width="99%"/>
</p>


<p align="center">
  <img src="https://github.com/COeXISTENCE-PROJECT/URB/raw/main/docs/credits.png" width="70%"/>
</p>
