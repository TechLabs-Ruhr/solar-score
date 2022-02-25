from tsai.all import *
from core import training

class dataframe:
    """Provides high level functionality for inference with DataFrames."""

    def predict(df:pd.DataFrame, model:Path=Path('models/core.pkl')):
        """Creates a new forecast based on given DataFrame."""
        learn = load_learner(model)
        
        X = np.expand_dims(np.swapaxes(df[training.utility.get_feature_names(training.utility.get_feature_count(df))].to_numpy(),1,0), 0)
        y = np.expand_dims(df['target'].to_numpy(), 0)

        probas, targets, preds = learn.get_X_preds(X)
        return infer_data(probas=probas, targets=targets, preds=preds, X=X, y=y)

    def validate(df:pd.DataFrame):
        """"""
        id = dataframe.predict(df)
        plt.plot(id.y[0]);
        plt.plot(id.preds[0]);


class infer_data:
    """"""
    probas = None
    targets = None
    preds = None
    X = None
    y = None

    def __init__(self, probas, targets, preds, X, y):
        self.probas = probas
        self.targets = targets
        self.preds = preds
        self.X = X
        self.y = y