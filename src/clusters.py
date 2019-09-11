import pandas as pd
from sklearn.cluster import KMeans,DBSCAN
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import Normalizer,scale


def plot_corr(data_path, target_path):
    data = pd.read_csv(data_path)
    df_corr = data.corr()
    n_names = data.columns.values.tolist()
    n_tick = data.shape[1]
    figure = plt.figure()
    ax = figure.add_subplots(111)
    cax = ax.matshow(df_corr, vmin=-1, vmax=1)
    figure.colorbar(cax)
    ticks = np.arange(0, n_tick, 1)
    ax.set_xticks(ticks)
    ax.set_yticks(ticks)
    ax.set_xticklabels(n_names)
    ax.set_yticklabels(n_names)
    plt.title("the correlation matrix of data")
    plt.show()
    plt.savefig(target_path)


# data mustn't with NaN, infinity or too large for data type('float64)
def use_normalize(data):
    data = data.fillna(0)
    data_normal = Normalizer().fit_transform(data)
    normal_model = Normalizer().fit(data)
    return data_normal, normal_model


def use_scale(data):
    data = data.fillna(0)
    data_scale = scale(data)
    return data_scale


def km_cluster(data_path, center):
    data = pd.read_csv(data_path)
    data_in_use, normal_model = use_normalize(data)
    km = KMeans(n_clusters=center).fit(data_in_use)
    labels = list(km.labels_)
    centers = km.cluster_centers_
    centers = normal_model.inverse_transform(centers)
    res = {"labels": labels, "centers": centers}
    return res


def dbscan_cluster(data_path):
    data = pd.read_csv(data_path)
    data_in_use = use_normalize(data)
    db_model = DBSCAN().fit(data_in_use)
    labels = db_model.labels_
    res = {'labels': labels}
    return res


if __name__ == '__main__':
    file = '../generate_data/file.csv'
    km1 = km_cluster(file, 2)
    db1 = dbscan_cluster(file)
