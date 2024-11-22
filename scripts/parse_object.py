import sys, mujoco
sys.path.append('../package/helper/')
sys.path.append('../package/mujoco_usage/')
from mujoco_parser import *
from utility import *
print ("MuJoCo:[%s]"%(mujoco.__version__))

xml_path = '../asset/scanned_objects/scene_objects.xml'

# init MuJoCoParser using parameter (name, xml_path, verbose)
# xml file is transmitted & related info is printed
env = MuJoCoParserClass(name='Scanned Objects',rel_xml_path=xml_path,verbose=True)

env.reset(step=True)
# Set object positions
obj_names = env.get_body_names(excluding='world') # object names
n_obj = len(obj_names)
obj_xyzs = sample_xyzs(
    n_obj,
    x_range   = [-0.45,+0.45],
    y_range   = [-0.45,+0.45],
    z_range   = [0.51,0.51],
    min_dist  = 0.2,
    xy_margin = 0.0
)

for obj_idx in range(n_obj):
    env.set_p_base_body(body_name=obj_names[obj_idx],p=obj_xyzs[obj_idx,:])
    env.set_R_base_body(body_name=obj_names[obj_idx],R=np.eye(3,3))
    
# Loop
env.init_viewer(transparent=False)
while env.is_viewer_alive():
    env.step()
    if env.loop_every(tick_every=10):
        env.plot_T()
        env.plot_time() # time
        env.plot_contact_info() # contact information
        env.render()
print ("Done.")

