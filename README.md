# yaml2urdf_jinja2
This is a very powerful tool in order to introduce some dynamics in the urdf models. The concept is the same that is implemented in "Xacros" from ros. It can be very useful also for building very [complex urdf files](https://answers.ros.org/question/328289/complex-urdf-files/).

The idea is to define a function that takes the parameters from a yaml file and create the desired urdf file from a pre-defined template. The Jinja documentation and installation guide can be found [here](https://jinja.palletsprojects.com/en/3.1.x/).

The repository contains an example with an acrobot urdf in order to make the use of this tool more clear. Another example can be found [here](https://kraby.readthedocs.io/en/latest/urdf_description/).
