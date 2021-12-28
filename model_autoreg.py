import os
import tensorflow as tf
import numpy as np
import random
import pandas as pd
import seaborn as sns

reg_telescope = 864
telescope = 1
window = 200

class model:
    def __init__(self, path):
        self.model = tf.keras.models.load_model(os.path.join(path, 'SubmissionModel'))

    def predict(self, X):
        # Insert your preprocessing here

        X = X.numpy()
        X_min = X.min(axis=0)
        X_max = X.max(axis=0)

        future = X[-window:]
        future = (future - X_min) / (X_max - X_min)
        future = np.expand_dims(future, axis=0)


        # Autoregressive Forecasting
        reg_predictions = np.array([])
        X_temp = future
        for reg in range(0,reg_telescope,telescope):
            pred_temp = self.model.predict(X_temp)
            if(len(reg_predictions)==0):
                reg_predictions = pred_temp
            else:
                reg_predictions = np.concatenate((reg_predictions,pred_temp),axis=1)
            X_temp = np.concatenate((X_temp[:,telescope:,:],pred_temp), axis=1)

        # Insert your postprocessing here
        out = reg_predictions * (X_max - X_min) + X_min  # denormalize
        out = np.reshape(out, (864, 7))
        out = tf.convert_to_tensor(out)

        # check for NaN predictions
        assert not np.isnan(out).any()

        return out
