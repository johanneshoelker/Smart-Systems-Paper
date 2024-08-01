### Implementation Steps

To implement the proposed method (INRAD), follow these steps:

1. **Data Preparation**:
   
   - Gather and preprocess your time-series data. Ensure it is in a format suitable for input into a neural network (e.g., normalized).

2. **Model Design**:
   
   - Define a simple MLP with input as the time value and output as the corresponding time-series value. The MLP should have several hidden layers with non-linear activation functions.
3- **Training**:
   - Train the MLP on your time-series data. Use the mean squared error (MSE) between the predicted and actual values as the loss function.
4- **Anomaly Detection**:
   - After training, calculate the representation error for each data point in your test set. Use these errors as anomaly scores.
5- **Evaluation**:
   - Determine a threshold for anomaly detection based on the distribution of anomaly scores. Data points with scores above this threshold can be classified as anomalies.



### Conclusion

Jeong et al.'s method simplifies the model design and reduces training time while improving anomaly detection performance. The implicit neural representation allows for efficient and robust detection of anomalies in multivariate time-series data.
