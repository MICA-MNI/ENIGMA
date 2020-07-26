import os
import numpy as np


def load_sc_sctx_labels():
  root_pth = os.path.dirname(__file__)
  fname = 'structLabels_sctx.csv'
  ipth = os.path.join(root_pth, 'matrices', 'hcp_connectivity', fname)
  return np.loadtxt(ipth, dtype=np.float, delimiter=',')


"""
class struct():
  pass

sc  = struct()
sc.labels_sctx = ('ACCUMBENS_LEFT',	'AMYGDALA_LEFT',	'CAUDATE_LEFT',	'HIPPOCAMPUS_LEFT')
sc.sctx = np.array([[1, 4, 5], [-5, 8, 9]])
"""