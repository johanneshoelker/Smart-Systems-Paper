# Implementations of chosen RL methods
## MOMENT
The file impl_moment.ipynb is an extension of the tutorial anomaly_detection.ipynb found in [here](github.com/moment-timeseries-foundation-model/moment/blob/main/tutorials/anomaly\_detection.ipynb)

The evaluation on the model is presented on inverter 0 in impl_moment.ipynb. According to this solution all other inverters are tested the same way.

## MEGA
The main_mutiwave.py script provided by the authors in this [repo](github.com/jingwang2020/MEGA) is used to evaluate on the SMA dataset.
In order to run the script it needs to be added into the cloned repository of MEGA. Additionally, the SMA dataset as well as the smadata.py need to be added into the cloned repo.
Following this a successful forward pass with evaluation can be achieved (see screenshot).

## TS2Vec
A function to preprocess the SMA dataset is provided in impl_ts2vec.py. It needs to be placed in the cloned [repository](https://github.com/zhihanyue/ts2vec) of the authors. Additionally, the SMA dataset as well as the smadata.py need to be added into the cloned repo. Following this way, a successful forward pass was achieved. The output and the learned representations are visible in results_ts2vec.txt.

# SMA Dataset
