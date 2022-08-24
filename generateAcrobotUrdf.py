from jinja2 import Environment, FileSystemLoader
import yaml

## Retrieving data from yaml file
model_par_path = "CMA-ES_design1st.yml"
mpar = yaml.load(open(model_par_path), Loader=yaml.FullLoader)

## Compile templates into URDF robot description
loader = FileSystemLoader(searchpath="template/")
env = Environment(loader=loader, autoescape=True)

t = "acrobot.urdf"
template = env.get_template("acrobotTemplate.j2")
f = open(t, "w")
f.write(template.render(m1 = mpar['m1'], 
                        m2 = mpar['m2'],
                        l1 = mpar['l1'],
                        l2 = mpar['l2'], 
                        I1 = mpar['I1'], 
                        I2 = mpar['I2'], 
                        b1 = mpar['b1'], 
                        b2 = mpar['b2'], 
                        cf1 = mpar['cf1'], 
                        cf2 = mpar['cf2']))