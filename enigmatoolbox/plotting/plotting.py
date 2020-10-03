"""
Plotting functions.
"""

import numpy as np

def enigma_scatter(ax, x, y, scatter_color='#000000', linear_fit=False, fit_color=None,
            xlim=None, ylim=None, xlabel=None, ylabel=None, corr_value=None, p_value=None, p_type='spin'):
    """
    Scatter plot.

    Parameters
    ----------
    ax : figure axis
    x, y : two maps (ndarray)
    scatter_color : color of data in scatter plot, default is black
    linear_fit : add linear fit on top of scatter, default is no!
    fit_color : color of line fit if linear_fit is True
    xlim : x-axis limit (tuple), default is xmin-xmax
    ylim : y-axis limit (tuple), default is ymin-ymax
    xlabel : label of x axis (string), default is None
    ylabel : label of y axis (string), default is None
    corr_value : add r=correlation value if provided (number), default is None
    p_value : add p_spin=p-value if provided (number), default is None
    p_type : spin (default), shuf

    Sara Lariviere | Sunny September day 2020
    """

    ax.scatter(x, y, color=scatter_color)                    # Plot scatter
    if linear_fit is True and fit_color is None:
        fit_color = '#000000'
        m, b = np.polyfit(x, y, 1)                           # Compute linear fit
        ax.plot(x, m*x + b, color=fit_color)                 # Plot linear fit
    elif linear_fit is True and fit_color is not None:
        m, b = np.polyfit(x, y, 1)
        ax.plot(x, m * x + b, color=fit_color)

    if xlim is None:
        ax.set_xlim(np.min(x), np.max(x))
    else:
        ax.set_xlim(xlim)

    if ylim is None:
        ax.set_ylim(np.min(y), np.max(y))
    else:
        ax.set_ylim(ylim)

    if xlabel is not None:
        ax.set_xlabel(xlabel)       # Add x-axis label

    if ylabel is not None:
        ax.set_ylabel(ylabel)       # Add y-axis label

    if corr_value is not None and p_value is not None:                                        # Add correlation and p values
        ax.text(ax.get_xlim()[0] + (((ax.get_xlim()[1] - ax.get_xlim()[0]) / 100) * 5),
                ax.get_ylim()[0] + (((ax.get_ylim()[1] - ax.get_ylim()[0]) / 100) * 5),
                '$r$=' + str(round(corr_value, 2)) + ', $p$$_{{{}}}$='.format(p_type) + str(round(p_value, 4)))
    elif corr_value is not None and p_value is None:                                         # Add correlation value only
        ax.text(ax.get_xlim()[0] + (((ax.get_xlim()[1] - ax.get_xlim()[0]) / 100) * 5),
                ax.get_ylim()[0] + (((ax.get_ylim()[1] - ax.get_ylim()[0]) / 100) * 5),
                '$r$=' + str(round(corr_value, 2)))
    elif corr_value is None and p_value is not None:                                          # Add p-value only
        ax.text(ax.get_xlim()[0] + (((ax.get_xlim()[1] - ax.get_xlim()[0]) / 100) * 5),
                ax.get_ylim()[0] + (((ax.get_ylim()[1] - ax.get_ylim()[0]) / 100) * 5),
                '$p$$_{{{}}}$='.format(p_type) + str(round(p_value, 4)))

    # hide the right and top spines
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)