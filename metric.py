import numpy as np
def eval_metric(labels, preds, log_sold_price_groups = [0,50,100, 500, 1000] ):
    labels = np.array(labels)
    preds = np.array(preds)
    metrics = []
    for i in range(len(log_sold_price_groups)):
        try:
            Filter = (labels >= log_sold_price_groups[i]) & (labels < log_sold_price_groups[i+1])
            print(Filter)
            try:
                metrics.append(mean_squared_error(labels[Filter], preds[Filter]))
            except:
                metrics.append(np.nan)
        except:
            Filter = (labels >= log_sold_price_groups[i])
            print(Filter)
            try:
                metrics.append(mean_squared_error(labels[Filter], preds[Filter]))
            except:
                metrics.append(np.nan)
    
    return np.array(metrics)
    #