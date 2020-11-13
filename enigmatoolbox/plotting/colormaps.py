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

eco_kos_colors = np.array([[0, 0, 0, 255],
                           [126, 40, 127, 255],
                           [51, 104, 156, 255],
                           [167, 210, 140, 255],
                           [254, 205, 8, 255],
                           [255, 253, 25, 255]], dtype=np.uint8)

spec_5_colors = np.array([[0, 0, 0, 255],
                         [50, 136, 189, 255],
                         [171, 221, 164, 255],
                         [235, 235, 181, 255],
                         [253, 174, 97, 255],
                         [213, 62, 79, 255]], dtype=np.uint8)

root_pth = os.path.dirname(__file__)
TealRd_colors = np.loadtxt(os.path.join(root_pth, 'cmaps', 'TealRd.csv'))
GyRd_colors = np.loadtxt(os.path.join(root_pth, 'cmaps', 'GyRd.csv'))
GyRd_r_colors = np.loadtxt(os.path.join(root_pth, 'cmaps', 'GyRd_r.csv'))
GyBu_colors = np.loadtxt(os.path.join(root_pth, 'cmaps', 'GyBu.csv'))
GyBu_r_colors = np.loadtxt(os.path.join(root_pth, 'cmaps', 'GyBu_r.csv'))

bb_r_colors = np.loadtxt(os.path.join(root_pth, 'cmaps', 'bb_r.csv'))
bb_o_colors = np.loadtxt(os.path.join(root_pth, 'cmaps', 'bb_o.csv'))
bb_g_colors = np.loadtxt(os.path.join(root_pth, 'cmaps', 'bb_g.csv'))
bb_p_colors = np.loadtxt(os.path.join(root_pth, 'cmaps', 'bb_p.csv'))

bb_r_r_colors = np.flipud(np.loadtxt(os.path.join(root_pth, 'cmaps', 'bb_r.csv')))
bb_o_r_colors = np.flipud(np.loadtxt(os.path.join(root_pth, 'cmaps', 'bb_o.csv')))
bb_g_r_colors = np.flipud(np.loadtxt(os.path.join(root_pth, 'cmaps', 'bb_g.csv')))
bb_p_r_colors = np.flipud(np.loadtxt(os.path.join(root_pth, 'cmaps', 'bb_p.csv')))

colormaps = {'yeo7': yeo7_colors, 'TealRd': TealRd_colors, 'GyRd': GyRd_colors,
             'GyRd_r': GyRd_r_colors, 'GyBu': GyBu_colors, 'GyBu_r': GyBu_r_colors,
             'eco_kos': eco_kos_colors, 'bb_r': bb_r_colors, 'bb_o': bb_o_colors,
             'bb_g': bb_g_colors, 'bb_p': bb_p_colors, 'bb_r_r': bb_r_r_colors, 'bb_o_r': bb_o_r_colors,
             'bb_g_r': bb_g_r_colors, 'bb_p_r': bb_p_r_colors, 'spec_5': spec_5_colors}
