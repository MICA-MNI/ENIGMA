import matplotlib.pyplot as plt
from math import pi
import numpy as np
import pandas as pd
from ..utils.parcellation import parcel_to_surface
import os
import matplotlib.patches as pat
import random
import seaborn as sns
from scipy.stats import median_absolute_deviation

def economo_koskinas_spider(parcel_data=None, parcellation='aparc_fsa5', fill=0, title='',
                           axis_range=None, label=None, color=(0, 0, 0)):
    """Stratify parcellated data according to von Economo-Koskinas
        cytoarchitectonic classes (authors: @caseypaquola, @saratheriver)

        Parameters
        ----------
        parcel_data : ndarray, shape = (n_val,)
            Parcellated data.
        parcellation : string (e.g., aparc_fsa5), optional
            Parcellation to go from parcel_data to surface
        fill : float, optional
            Value used to fill elements outside the mask. Default is 0.
        title : string, optional
            Title of spider plot. Default is empty.
        axis_range : tuple, optional
            Range of spider plot axes. Default is (min, max).
        label : list, optional
            List of axis labels. Length = 5. Default is names of von Economo-Koskinas cytoarchitectonic classes.
        color : tuple, optional
            Color of line. Default is (0, 0, 0).

        Returns
        -------
        class_mean : ndarray, shape = (5,)
            Mean values within each von Economo-Koskinas cytoarchitectonic class.
        figure
            Spider plot.
        """
    # Data check
    if parcel_data is None:
        print("Need data to plot")

    # Map parcellated data to the surface
    surf_data = parcel_to_surface(parcel_data, parcellation, fill=fill)

    # Average within ve classes
    if 'fsa5' in parcellation:
        parc_pth = os.path.dirname(os.path.dirname(__file__)) + '/datasets/parcellations/economo_koskinas_fsa5.csv'
        ve = np.loadtxt(parc_pth, dtype=np.int)
    elif 'conte69' in parcellation:
        parc_pth = os.path.dirname(os.path.dirname(__file__)) + '/datasets/parcellations/economo_koskinas_conte69.csv'
        ve = np.loadtxt(parc_pth, dtype=np.int)

    ve_class = np.zeros((5, 1))
    for ii in range(5):
        jj = ii + 1
        ido = np.where(ve == jj)
        ve_class[ii] = np.nanmean(surf_data[ido])

    # Create dataframe
    class_mean = pd.DataFrame(data=np.transpose(ve_class), columns=['Agranular', 'Frontal', 'Parietal', 'Polar',
                                                                    'Granular'])

    # Number of variable
    categories = list(class_mean)
    N = len(categories)

    # We are going to plot the first line of the data frame.
    # But we need to repeat the first value to close the circular graph:
    values = class_mean.loc[0].values.flatten().tolist()
    values += values[:1]

    # What will be the angle of each axis in the plot? (we divide the plot / number of variable)
    angles = [n / float(N) * 2 * pi for n in range(N)]
    angles += angles[:1]

    # Initialise the spider plot
    ax = plt.subplot(111, polar=True)
    ax.spines['polar'].set_visible(False)

    # Draw one axe per variable + add labels labels yet
    if label is None:
        label = list(class_mean)

    plt.xticks(angles[:-1], label, color='black', size=12)
    ax.xaxis.get_majorticklabels()[0].set_horizontalalignment("left")
    ax.xaxis.get_majorticklabels()[2].set_verticalalignment("bottom")
    ax.xaxis.get_majorticklabels()[3].set_verticalalignment("top")

    # Draw ylabels
    ax.set_rlabel_position(0)
    if axis_range is None:
        axis_range = (np.min(values), np.max(values))

    inc = (axis_range[1] - axis_range[0]) / 4
    newinc = [axis_range[0] + inc, axis_range[0] + (inc * 2), axis_range[0] + (inc * 3),
              axis_range[0]]
    plt.yticks(newinc, [str("{:.2f}".format(elem)) for elem in newinc], color="grey", size=10)
    plt.ylim(axis_range)

    # add title
    if title:
        plt.title(title)

    # Plot data
    ax.plot(angles, values, linewidth=3, linestyle='solid', color=color)

    return class_mean


def bb_moments_raincloud(region_idx=None, parcellation='aparc', title=''):
    """Stratify regional data according to BigBrain statistical moments (authors: @caseypaquola, @saratheriver)

        Parameters
        ----------
        region_idx : ndarray, shape = (n_val,)
            Indices of regions to be included in analysis.
        parcellation : string, optional
                Name of parcellation. Options are 'aparc', 'schaefer_100', 'schaefer_200', 'schaefer_300',
                'schaefer_400', 'glasser_360'. Default is 'aparc'.
        title : string, optional
            Title of raincloud plot. Default is empty.

        Returns
        -------
        figure
            Raincloud plot.
        """
    def prctile(x, p):
        """Matlab-like percentile function (author: someone from the internet)"""
        p = np.asarray(p, dtype=float)
        n = len(x)
        p = (p - 50) * n / (n - 1) + 50
        p = np.clip(p, 0, 100)
        return np.percentile(x, p)

    # Load BigBrain statistical moments (mean, skewness)
    bb_pth = os.path.dirname(os.path.dirname(__file__)) + '/histology/bb_moments_' + parcellation + '.csv'
    bb_moments_aparc = np.loadtxt(bb_pth, delimiter=',', dtype=float)

    # Initiate figure and axes
    fig, axs = plt.subplots(1, 1, figsize=(15, 5))
    axs2 = [axs.twinx(), axs.twinx()]

    # Plot first moment at the top
    inv = [(ii + 1) * 2 for ii in reversed(range(bb_moments_aparc.shape[0]))]

    # Moments colors
    spec = ['#9e0142', '#66c2a5']

    # Loop over BigBrain moments
    for ii in range(bb_moments_aparc.shape[0]):
        # for ii in range(1):
        jj = inv[ii]

        # Random numbers to scatter points
        rando = [(random.random() * .3) + (jj - 0.15) for rr in range(bb_moments_aparc[ii, region_idx].shape[1])]

        # Scatter plot
        axs2[ii].scatter(bb_moments_aparc[ii, region_idx], rando, c=spec[ii], alpha=0.88,
                         linewidth=0.88, edgecolors='w', s=122)

        # Density distribution
        data = sns.distplot(bb_moments_aparc[ii, region_idx], hist=False, kde=True, ax=axs2[ii]).get_lines()[0].get_data()
        axs2[ii].fill_between(data[0], (jj + 0.3), data[1] + (jj + 0.3), facecolor=spec[ii])

        # In-house box plot
        qr = prctile(bb_moments_aparc[ii, region_idx].flatten(), [25, 75])
        rect = pat.FancyBboxPatch((qr[0] + 0.01, jj - 0.1), qr[1] - qr[0] - 0.02, 0.2, fc=spec[ii], alpha=0.41,
                                  ec=None, boxstyle="round,pad=0.01")
        rectout = pat.FancyBboxPatch((qr[0] + 0.01, jj - 0.1), qr[1] - qr[0] - 0.02, 0.2, alpha=.88,
                                     ec='k', boxstyle="round,pad=0.01", fill=False, lw=1.5)
        axs2[ii].add_patch(rect)
        axs2[ii].add_patch(rectout)

        # Median line
        axs2[ii].plot([np.median(bb_moments_aparc[ii, region_idx]), np.median(bb_moments_aparc[ii, region_idx])],
                      [jj - 0.1, jj + 0.1], lw=3, color='k')

        # Detect outliers, and if any, excluse them from the whiskers
        mad = 3 * median_absolute_deviation(bb_moments_aparc[ii, region_idx], axis=1)
        if np.argwhere(np.abs(bb_moments_aparc[ii, region_idx]) > mad).shape[0] == 0:
            mini = np.nanmin(bb_moments_aparc[ii, region_idx])
            maxi = np.nanmax(bb_moments_aparc[ii, region_idx])
        else:
            mat = np.abs(bb_moments_aparc[ii, region_idx])
            np.where(np.abs(mat) > mad, np.nan, mat)
            mini = np.nanmin(mat)
            maxi = np.nanmax(mat)

        axs2[ii].plot([mini, qr[0]], [jj, jj], lw=1.5, color='k')
        axs2[ii].plot([qr[1], maxi], [jj, jj], lw=1.5, color='k')

        # Figure axes and other things to prettify
        axs2[ii].set_ylim([1.5, 5.5])
        axs2[ii].set_xlim([-1.6, 1.6])
        fig.tight_layout()
        sns.despine(fig=fig, ax=axs2[ii])
        axs2[ii].axes.get_yaxis().set_ticks([])
        axs2[ii].set_ylabel('')
        axs.set_ylim([1.5, 5.5])
        axs.tick_params(axis='y', length=0, rotation=90, labelsize=16)
        axs.tick_params(axis='x', length=0, labelsize=16)
        axs.set_yticks((2.75, 4.75))
        axs.set_yticklabels(('Skewness', 'Mean'))

        # Add title
        if title:
            plt.title(title)

    return fig, axs, axs2


def bb_gradient_plot(data=None, parcellation='aparc', axis_range=None, title='', yaxis_label='', xaxis_label=''):
    """Stratify parcellated data according to the BigBrain gradient (authors: @caseypaquola, @saratheriver)

        Parameters
        ----------
        data : ndarray, shape = (n_val,)
            Parcellated data.
        parcellation : string, optional
                Name of parcellation. Options are 'aparc', 'schaefer_100', 'schaefer_200', 'schaefer_300',
                'schaefer_400', 'glasser_360'. Default is 'aparc'.
        axis_range : tuple, optional
            Range of spider plot axes. Default is (min, max).
        title : string, optional
            Title of spider plot. Default is empty.
        yaxis_label : list, optional
            Label for y-axis. Default is empty.
        xaxis_label : list, optional
            Label for x-axis. Default is empty.

        Returns
        -------
        figure
            Gradient plot.
        """
    # Check data
    if not isinstance(data, pd.Series):
        data = pd.Series(data)

    # Load BigBrain gradient
    bb_pth = os.path.dirname(os.path.dirname(__file__)) + '/histology/bb_gradient_' + parcellation + '.csv'
    g = np.loadtxt(bb_pth, delimiter=',', dtype=float)

    # Define number of bins
    numbin = 5
    p = np.arange(100 / numbin, 101, 100 / numbin)
    newg = np.zeros((0, round(g.shape[0] / numbin)))

    # Initiate figure and axes
    fig, axs = plt.subplots(1, 1, figsize=(15, 5))

    # Store means
    means = []

    # Bin colors
    spec = ['#3288bd', '#abdda4', '#ebebb5', '#fdae61', '#d53e4f']

    # Loop over bins
    for ii in range(numbin):

        def prctile(x, pp):
            """
            Matlab-like percentile function (author: someone from the internet)
            """
            pp = np.asarray(pp, dtype=float)
            n = len(x)
            pp = (pp - 50) * n / (n - 1) + 50
            pp = np.clip(pp, 0, 100)
            return np.percentile(x, pp)

        # Split gradients into bins
        if ii == 0:
            tmp_o = np.argwhere(g <= prctile(g, p[ii]))
        else:
            tmp_o = np.argwhere((g <= prctile(g, p[ii])) & (g > prctile(g, p[ii - 1])))

        if len(tmp_o) < round(g.shape[0] / numbin):
            tmp = np.expand_dims(np.append(tmp_o, np.nan), axis=0)
        else:
            tmp = np.transpose(tmp_o)

        newg = np.append(newg, tmp, axis=0)

        # Random numbers to scatter points
        rando = [(random.random() * .3) + (ii - 0.15) for rr in range(len(tmp_o))]

        # Scatter bins
        axs.scatter(rando, data[newg[ii, :len(tmp_o)]], c=spec[ii], alpha=0.88,
                    linewidth=0.88, edgecolors='w', s=222)

        # Plot mean line (so long as they are not nans)
        if data[newg[ii, :len(tmp_o)]].isnull().all():
            means = np.append(means, np.nan)

        else:
            axs.plot([ii - 0.17, ii + 0.17],
                     [np.nanmean(data[newg[ii, :len(tmp_o)]]), np.nanmean(data[newg[ii, :len(tmp_o)]])],
                     lw=10, color='k')
            axs.plot([ii - 0.17, ii + 0.17],
                     [np.nanmean(data[newg[ii, :len(tmp_o)]]), np.nanmean(data[newg[ii, :len(tmp_o)]])],
                     lw=6, color=spec[ii])
            # Store means
            means = np.append(means, np.nanmean(data[newg[ii, :len(tmp_o)]]))

    if not np.isnan(means).any():
        jj = np.vstack((np.arange(0, numbin - 1, 1), np.arange(1, numbin, 1)))
        for ii in range(jj.shape[1]):
            axs.plot([jj[0, ii] + 0.23, jj[1, ii] - 0.23],
                     [means[jj[0, ii]], means[jj[1, ii]]],
                     lw=2.5, color='k', alpha=0.88)
    else:
        print('Some empty bins, not plotting connecting lines')

    # Figure axes and other things to prettify
    if axis_range is None:
        axis_range = (np.nanmin(data), np.nanmax(data))

    #fig.tight_layout()
    axs.set_ylim(axis_range[0], axis_range[1])
    axs.set_xlim(-0.5, 4.5)
    axs.tick_params(axis='y', length=0, labelsize=14)
    axs.tick_params(axis='x', length=0, labelsize=14)
    axs.set_yticks((axis_range[0], axis_range[1]))
    axs.set_xticks((0, 1, 2, 3, 4))
    axs.set_xticklabels(('Bin1', 'Bin2', 'Bin3', 'Bin4', 'Bin5'))
    axs.spines['right'].set_visible(False)
    axs.spines['top'].set_visible(False)

    # Add title
    if title:
        plt.title(title)

    # Add y-axis label
    if yaxis_label:
        plt.ylabel(yaxis_label, fontsize=16)

    # Add x-axis label
    if xaxis_label:
        plt.xlabel(xaxis_label, fontsize=16)

    return axs