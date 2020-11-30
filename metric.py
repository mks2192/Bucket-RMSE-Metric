import numpy as np
from sklearn.metrics import mean_squared_error
def eval_metric(labels, preds, bucket = [0,50,100, 500, 1000] ):
    labels = np.array(labels).flatten()
    preds = np.array(preds).flatten()
    metrics = []
    for i in range(len(bucket)):
        try:
            mask_ = (labels >= bucket[i]) & (labels < bucket[i+1])
            print(mask_)
            try:
                metrics.append(mean_squared_error(labels[mask_], preds[mask_]))
            except:
                metrics.append(np.nan)
        except:
            mask_ = (labels >= bucket[i])
            print(mask_)
            try:
                metrics.append(mean_squared_error(labels[mask_], preds[mask_]))
            except:
                metrics.append(np.nan)
    
    return np.array(metrics)
    ##