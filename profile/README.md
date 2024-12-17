

![logo](https://github.com/COeXISTENCE-PROJECT/shared/blob/main/graphical/COeXISTENCE/COeXISTENCE_logo/LOGO/COLOR/horizontal/COeXISTENCE_logo_color_horizontal_blue-gray.jpg)

> COeXISTENCE is an ecosystem to experiment with future Urban Traffic Systems, where routing decisions are simulatenously made by humans and autonomous vehicles.
>

## The following use-case synthesize main features of an ecosystem:

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

Each of above handled with specific packages/modules/workflows of `COeXISTENCE`:

![image](https://github.com/user-attachments/assets/3149b95e-4d7c-428c-9455-84a0cf2483f7)




