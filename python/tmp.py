import os
import numpy as np


def load_sc_sctx_labels():
  root_pth = os.path.dirname(__file__)
  fname = 'structLabels_sctx.csv'
  ipth = os.path.join(root_pth, 'matrices', 'hcp_connectivity', fname)
  return np.loadtxt(ipth, dtype=np.float, delimiter=',')

from enigmatoolbox.datasets import load_sc, load_fc
c, cl, s, sl = load_sc()
c2, cl2, s2, sl2 = load_fc()

"""
class struct():
  pass

sc  = struct()
sc.labels_sctx = ('ACCUMBENS_LEFT',	'AMYGDALA_LEFT',	'CAUDATE_LEFT',	'HIPPOCAMPUS_LEFT')
sc.sctx = np.array([[1, 4, 5], [-5, 8, 9]])
"""


import enigmatoolbox.datasets
from enigmatoolbox.datasets import load_conte69
from enigmatoolbox.plotting import plot_hemispheres
from enigmatoolbox.utils.parcellation import map_to_labels, reduce_by_labels, relabel_consecutive

