"""
Utility functions for ENIMA-related analyses.
"""

# Author: Sara Lariviere <saratheriver@gmai.com>
# License: BSD 3 clause


import numpy as np
import numpy.matlib as npm

def zscore_matrix(data, group, controlCode):
    """
    z-scores data w.r.t. a specific group

    Parameters:
    -------
      data         = data matrix (e.g. thickness data, #subjects x #parcels)
      group        = vector of values (i.e., grp assignment) same length as #subjects
      controlCode  = value that corresponds to control subjects

    Outputs:
    --------
       Z           = z-scored data relative to control code (e.g., HCs)
    """
    C = [i for i, x in enumerate(group) if x == controlCode]
    n = len(group)
    z1 = data - npm.repmat(np.mean(data.iloc[C, ]), n, 1)
    z2 = np.std(data.iloc[C, ], ddof=1)
    return z1 / z2

def reorder_sctx(data):
    """
    re-orders subcortical volume data alphabetically, and by hemisphere (left, then right)

    Parameters:
    -------
      data         = data matrix (e.g. metr1_SubVol)

    Outputs:
    --------
       data_r      = re-ordered data (L-acc, L-amyg, L-caud, L-hip ... R-thalamus, R-ventricle)
    """
    if data.shape[1] == 18:
        new_order = [0, 15, 13, 5, 11, 9, 7, 3, 1, 16, 14, 6, 12, 10, 8, 4, 2, 17]
        return data[data.columns.values[new_order]]
    elif data.shape[1] == 16:
        new_order = [14, 12, 4, 10, 8, 6, 2, 0, 15, 13, 5, 11, 9, 7, 3, 1]
        return data[data.columns.values[new_order]]


