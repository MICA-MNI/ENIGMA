import numpy as np
from nilearn import plotting
from nilearn.connectome import ConnectivityMeasure
from sklearn.decomposition import PCA

from enigmatoolbox.plotting import plot_cortical
from enigmatoolbox.utils import parcel_to_surface

from enigmatoolbox.datasets.base import load_summary_stats


def cross_disorder_effect(disorder='all_disorder', measure=['CortThick', 'CortSurf'], additional_data=None,
                          additional_name=None, ignore=['mega'], method='pca', figure=True):
    """ Cross-disorder effect (authors: @boyongpark, @saratheriver)

        Parameters
        ----------
        disorder : list, optional
            Any combination of disorder name. Default is all available disorders
            {'22q', 'adhd', 'asd', 'bipolar', 'depression', 'epilepsy', 'ocd', 'schizophrenia'}.
        measure : list, optional
            Any combination of measure names. Default is {'CortThick', 'CortSurf'}.
        additional_data : ndarray, optional
            Name for additional ENIGMA-type data. Must also provide 'additional_name'.
        additional_name : list, optional
            Additional ENIGMA-type data (n, 68). Must also provide 'additional_name'.
        ignore : list, optional
            Ignore summary statistics with these expressions. Default is ('mega') as it contains NaNs.
        method : string, optional
            Analysis method {'pca', 'correlation'}. Default is 'pca'.
        figure : string, optional
            Whether to output figures {'True', 'False'}. Default is 'True'.

        Returns
        -------
        components : ndarray
            Principal components of shared effects in descending order in terms of component variance.
            Only is method is 'pca'.
        variance : ndarray
            Variance of components. Only is method is 'pca'.
        correlation_matrix : ndarray
            Correlation matrix of for every pair of shared effect maps. Only is method is 'correlation'.
        names - list
            Name of disorder and case-control effect maps included in analysis.
    """

    if disorder is 'all_disorder':
        disorder = ['22q', 'adhd', 'asd', 'bipolar', 'depression', 'epilepsy', 'ocd', 'schizophrenia']

    mat_d = []
    names = []
    for ii in range(len(disorder)):
        # Load summary statistics
        sum_stats = load_summary_stats(disorder[ii])
        fieldos = list(sum_stats.keys())

        # Loop through structure fields (case-control options)
        for jj in range(len(fieldos)):
            if not any(ig in fieldos[jj] for ig in ignore) and any(meas in fieldos[jj] for meas in measure):
                mat_d.append(sum_stats[fieldos[jj]].iloc[:, 2])
                names.append(disorder[jj] + ': ' + fieldos[jj])

    mat_d = (np.asarray(mat_d))

    # If additional data and name
    if additional_data is not None and additional_name is not None:
        mat_d = np.append(mat_d, additional_data)
        names.append(names, additional_name)

    if method is 'pca':
        pca = PCA()
        components = pca.fit_transform(np.transpose(mat_d))
        variance = pca.explained_variance_ratio_

        if figure:
            plot_cortical(parcel_to_surface(components[:, 0], 'aparc_fsa5'), color_range=(-0.5, 0.5),
                          cmap='RdBu_r', color_bar=True, size=(800, 400))

        return components, variance, names

    elif method is 'correlation':
        correlation_measure = ConnectivityMeasure(kind='correlation')
        correlation_matrix = correlation_measure.fit_transform([np.transpose(mat_d)])[0]

        if figure:
            plotting.plot_matrix(correlation_matrix, figure=(12, 8), labels=names, vmax=1,
                                 vmin=-1, cmap='RdBu_r', auto_fit=False)

        return correlation_matrix, names

