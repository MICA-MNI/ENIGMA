import numpy as np
import os

yeo7_colors = np.array([[0, 0, 0, 255],
                        [0, 118, 14, 255],
                        [230, 148, 34, 255],
                        [205, 62, 78, 255],
                        [120, 18, 134, 255],
                        [220, 248, 164, 255],
                        [70, 130, 180, 255],
                        [196, 58, 250, 255]], dtype=np.uint8)

root_pth = os.path.dirname(__file__)
TealRd_colors = np.loadtxt(os.path.join(root_pth, 'cmaps', 'TealRd.csv'))
GyRd_colors = np.loadtxt(os.path.join(root_pth, 'cmaps', 'GyRd.csv'))
GyRd_r_colors = np.loadtxt(os.path.join(root_pth, 'cmaps', 'GyRd_r.csv'))
GyBu_colors = np.loadtxt(os.path.join(root_pth, 'cmaps', 'GyBu.csv'))
GyBu_r_colors = np.loadtxt(os.path.join(root_pth, 'cmaps', 'GyBu_r.csv'))

colormaps = {'yeo7': yeo7_colors, 'TealRd': TealRd_colors, 'GyRd': GyRd_colors,
             'GyRd_r': GyRd_r_colors, 'GyBu': GyBu_colors, 'GyBu_r': GyBu_r_colors}
