from sklearn.metrics import adjusted_rand_score
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from scipy.stats import kruskal
from statsmodels.stats.multitest import multipletests

def kmeans_ari (X,y,n_clusters,n_init,return_vars=True,return_plot=False):
    kmeans = KMeans(n_clusters=n_clusters,random_state=42,n_init=n_init)
    clusters = kmeans.fit_predict(X)
    ari = adjusted_rand_score(y,clusters)
    # print(f"ARI: {ari:.4f} and clusters: {clusters:.4f}")
    
    fig = None

    if return_plot:
        fig = plt.scatter(X,y = clusters,c=clusters,cmap='rainbow')
        plt.title('KMeans Clustering')
        plt.xlabel(X.columns[0])
        plt.ylabel("Predicted Clusters")
        plt.show()
        
    if return_vars and return_plot:
        return ari, clusters, fig
    elif return_vars:
        return ari, clusters
    elif return_plot:
        return fig
    else:
        return None
    

def kruskal_wallis_test(group):
    H,p = kruskal(*group)
    return H,p

def adjust_multipletests(results,method):
    adjusted_results = multipletests(
        results,
        method = method
    )[1]
    return adjusted_results
