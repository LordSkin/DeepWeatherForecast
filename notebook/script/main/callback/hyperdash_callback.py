from hyperdash import Experiment
from tensorflow.keras.callbacks import Callback


class HyperdashCallback(Callback):
    exp = None
    last = 1

    def on_train_begin(self, logs=None):
        self.exp = Experiment("Deep Weather")

    def on_train_end(self, logs=None):
        self.exp.end()

    def on_epoch_end(self, epoch, logs=None):
        self.exp.metric("progress", min(0.1, self.last - logs["loss"]))
        self.last = logs["loss"]
        self.exp.metric("loss", min(0.5, logs["loss"]))
        self.exp.metric("val_loss", min(0.5, logs["val_loss"]))
