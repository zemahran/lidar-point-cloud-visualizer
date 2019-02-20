import pykitti
import os
import numpy as np
import mayavi.mlab

# Path to point cloud binaries
basedir = './sample_scene/'
date = 'dir'
drive = '0048'

for velo in pykitti.raw(basedir, date, drive).velo:
        x = velo[:, 0]
        y = velo[:, 1]
        z = velo[:, 2]
        c = velo[:, 2]

        fig = mayavi.mlab.figure(bgcolor=(0, 0, 0), size=(850, 700))
        mayavi.mlab.points3d(
            x, y, z, c,
            mode="point", # 'point', 'sphere' , 'cube' }
            colormap='spectral',
            # color=(1, 1, 1),      # using a fixed (r,g,b) color instead of colormap
            scale_factor=100,     # scale of the points
            line_width=10,        # scale of the line, if any
            figure=fig,
        )
        mayavi.mlab.show()
