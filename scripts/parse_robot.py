import sys, mujoco
sys.path.append('../package/helper/')
sys.path.append('../package/mujoco_usage/')
from mujoco_parser import *
from utility import *
print ("MuJoCo:[%s]"%(mujoco.__version__))

xml_path = '../asset/unitree_g1/scene_g1.xml' 

# init MuJoCoParser using parameter (name, xml_path, verbose)
# xml file is transmitted & related info is printed
env = MuJoCoParserClass(name='Floor', rel_xml_path=xml_path, verbose=True)

# reset mjModel & mjData and step() function is called to update the model
env.reset(step=True)
env.init_viewer(transparent=True)
while env.is_viewer_alive():
    env.step()
    if env.loop_every(tick_every=10):
        env.plot_T()
        env.plot_time() # time
        env.plot_contact_info() # contact information
        env.plot_joint_axis(axis_len=0.025,axis_r=0.005) # revolute joints
        env.plot_links_between_bodies(rgba=(0,0,0,1),r=0.001) # link information
        env.render()
print ("Done.")

# xml_path = '../asset/rby/scene_rby.xml'
# env = MuJoCoParserClass(name='RB-Y1',rel_xml_path=xml_path,verbose=True)

# env.reset(step=True)
# env.init_viewer(transparent=True)
# while env.is_viewer_alive():
#     env.step()
#     if env.loop_every(tick_every=10):
#         env.plot_T()
#         env.plot_time() # time
#         env.plot_contact_info() # contact information
#         env.render()
# print ("Done.")
