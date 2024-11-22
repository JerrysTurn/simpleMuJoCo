import sys, mujoco
sys.path.append('../package/helper/')
sys.path.append('../package/mujoco_usage/')
from mujoco_parser import *
from utility import *
print ("MuJoCo:[%s]"%(mujoco.__version__))

xml_path = '../asset/object/floor_isaac_style.xml'

# init MuJoCoParser using parameter (name, xml_path, verbose)
# xml file is transmitted & related info is printed
env = MuJoCoParserClass(name='Floor', rel_xml_path=xml_path, verbose=True)

# reset mjModel & mjData and step() function is called to update the model
env.reset(step=True)
env.init_viewer()
while env.is_viewer_alive():
    env.step()
    env.render()
print("Done")