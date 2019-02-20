import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Path to point cloud binaries
basedir = './sample_scene/'
date = 'dir'
drive = '0002'

skip = 100 # plot one point in every `skip` points
for velo in pykitti.raw(basedir, date, drive).velo:
        x = velo[:, 0]
        y = velo[:, 1]
        z = velo[:, 2]
        c = velo[:, 3]

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
velo_range = range(0, velo.shape[0], skip) # skip points to prevent crash
ax.scatter(
        x, y, z, c,
        cmap='gray')

ax.set_title('Subsampled LiDAR Points')
plt.show()
