import numpy as np

def eval_metric_bucket(labels, preds, log_sold_price_groups = [0,50,100, 500, 1000]):
    labels = np.array(labels).flatten()
    preds = np.array(preds).flatten()
    SE = (labels - preds)**2
    metrics = []
    for i in range(len(log_sold_price_groups)):
        try:
            mask_ = (labels >= log_sold_price_groups[i]) & (labels < log_sold_price_groups[i+1])
            try:
                metrics.append(np.sqrt(SE[mask_].mean()))
            except:
                metrics.append(np.nan)
        except:
            mask_ = (labels >= log_sold_price_groups[i])
            try:
                metrics.append(np.sqrt(SE[mask_].mean()))
            except:
                metrics.append(np.nan)
    
    return np.array(metrics)
    #
