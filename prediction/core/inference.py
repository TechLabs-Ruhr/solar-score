from tsai.all import *
from core import training

class dataframe:
    """Provides high level functionality for inference with DataFrames."""

    def predict(df:pd.DataFrame, model:Path=Path('models/core.pkl'), target_column:string=None):
        """Creates a new forecast based on given DataFrame."""
        learn = load_learner(model)
        
        source_column = training.utility.get_column_names(df)
        if target_column is None:
            target_column = source_column[-1]
        
        source_column.remove(target_column)

        X = np.expand_dims(np.swapaxes(df[source_column].to_numpy(),1,0), 0)
        y = np.expand_dims(df[target_column].to_numpy(), 0)

        probas, targets, preds = learn.get_X_preds(X)
        return infer_data(probas=probas, targets=targets, preds=preds, X=X, y=y)

    def test(model:Path=Path('models/core.pkl')):
        learn = load_learner(model)

        X = np.expand_dims(np.ones((4,240)), 0)
        y = np.expand_dims(np.ones((1,240)), 0)
        probas, targets, preds = learn.get_X_preds(X)
        return infer_data(probas=probas, targets=targets, preds=preds, X=X, y=y)

    def validate(df:pd.DataFrame):
        """"""
        df = df.iloc[-240:]
        id = dataframe.predict(df)
        preds = np.array(id.preds[0])
        preds[preds<0] = 0

        plt.figure(figsize=(20, 6))
        plt.plot(id.y[0]);
        plt.plot(preds);


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