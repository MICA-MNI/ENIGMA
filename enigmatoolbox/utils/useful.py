"""
Utility functions for ENIMA-related analyses.
"""

# Author: Sara Lariviere <saratheriver@gmai.com>
# License: BSD 3 clause


import numpy as np
import numpy.matlib as npm

def zscore_matrix(data, group, controlCode):
    """
    Z-score data relative to a given group (author: @saratheriver)

    Parameters
    ----------
    data : pandas.DataFrame
        Data matrix (e.g. thickness data), shape = (n_subject, n_region)
    group : list
        Group assignment (e.g, [0, 0, 0, 1, 1, 1], same length as n_subject.
    controlCode : int
        Value that corresponds to "baseline" group

    Returns
    -------
    Z : pandas.DataFrame
        Z-scored data relative to control code
    """
    C = [i for i, x in enumerate(group) if x == controlCode]
    n = len(group)
    z1 = data - npm.repmat(np.mean(data.iloc[C, ]), n, 1)
    z2 = np.std(data.iloc[C, ], ddof=1)
    return z1 / z2

def reorder_sctx(data):
    """
    Re-order subcortical volume data alphabetically and by hemisphere (left then right; author: @saratheriver)

    Parameters
    ----------
    data : pandas.DataFrame
        Data matrix

    Returns
    -------
    data_r : pandas.DataFrame
        Re-ordered data
    """
    if data.shape[1] == 18:
        new_order = [0, 15, 13, 5, 11, 9, 7, 3, 1, 16, 14, 6, 12, 10, 8, 4, 2, 17]
        return data[data.columns.values[new_order]]
    elif data.shape[1] == 16:
        new_order = [14, 12, 4, 10, 8, 6, 2, 0, 15, 13, 5, 11, 9, 7, 3, 1]
        return data[data.columns.values[new_order]]


