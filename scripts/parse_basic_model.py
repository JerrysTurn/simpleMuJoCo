import sys, mujoco
sys.path.append('../package/helper/')
sys.path.append('../package/mujoco_usage/')
from mujoco_parser import *
from utility import *
print ("MuJoCo:[%s]"%(mujoco.__version__))

# init MuJoCoParser using parameter (name, xml_path, verbose)
# xml file is transmitted & related info is printed

xml_path = '../asset/object/floor_isaac_style.xml'
env = MuJoCoParserClass(name='Floor', rel_xml_path=xml_path, verbose=True)

# reset mjModel & mjData and step() function is called to update the model
env.reset(step=True)
env.init_viewer()
while env.is_viewer_alive():
    env.step()
    # Render
    env.plot_T(print_xyz=True)
    env.plot_time()
    env.plot_ellipsoid(p=np.array([0,-2.0,1.0]),rx=0.5,ry=0.2,rz=0.3,rgba=(1,0,1,0.5))
    env.plot_cylinder(p=np.array([0,-1.0,1.0]),r=0.1,h=0.2,rgba=(1,1,0,0.5))
    env.plot_T(p=np.array([0,0,1.0]),axis_len=0.2,axis_width=0.01)
    env.plot_arrow(p=np.array([0,1.0,1.0]),R=np.eye(3),r=0.1,h=0.5,rgba=(1,0,0,0.5))
    env.plot_box(p=np.array([0,2.0,1.0]),R=np.eye(3),xlen=0.2,ylen=0.2,zlen=0.1,rgba=(0,1,0,0.5))
    env.plot_capsule(p=np.array([0,3.0,1.0]),R=np.eye(3),r=0.1,h=0.1,rgba=(0,0,1,0.5))
    env.render()
print("Done")
