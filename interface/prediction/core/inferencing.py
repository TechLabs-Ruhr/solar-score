from tsai.all import *

def get_prediction_dataframe(df:pd.DataFrame, p_max:float=1) -> pd.DataFrame:
    """"""
    preds = p_max * np.array(torch.squeeze(dataframe.predict(df).preds))
    preds[preds < 0] = 0
    pdf = df.copy()
    pdf['P_gen [kW]'] = pd.Series(preds)
    return pdf

class dataframe:
    """Provides high level functionality for inference with DataFrames."""

    def predict(df:pd.DataFrame, model:Path=Path(__file__).parent / "model.pkl"):
        """Creates a new forecast based on given DataFrame."""
        learn = load_learner(model)       
        source_columns = list(utility.get_column_names())

        X = np.expand_dims(np.swapaxes(df[source_columns].to_numpy(),1,0), 0)

        probas, targets, preds = learn.get_X_preds(X)
        return infer_data(probas=probas, targets=targets, preds=preds, X=X)

    def validate(df:pd.DataFrame):
        """"""
        if len(df.index) < 240:
            print("DataFrame needs to have exactly 240 steps/rows.")
            return
        df = df[utility.get_column_names()].iloc[-240:]
        id = dataframe.predict(df)
        preds = np.array(id.preds[0])
        preds[preds<0] = 0

        plt.figure(figsize=(20, 6))
        plt.plot(id.y[0]);
        plt.plot(preds);

class utility:
    def get_column_names():
        with open(Path(__file__).parent / "weather parameter mapping.pkl", 'rb') as f:
            mapping:dict = pickle.load(f)
        return mapping.values()

class infer_data:
    """Storage for inferencing output."""
    probas = None
    targets = None
    preds = None
    X = None
    y = None

    def __init__(self, probas, targets, preds, X, y=None):
        self.probas = probas
        self.targets = targets
        self.preds = preds
        self.X = X
        self.y = y