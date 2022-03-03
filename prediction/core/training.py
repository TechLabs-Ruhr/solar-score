from tsai.all import *

class dataframe:
    """Provides high level functionality for training on DataFrames."""
    
    def plot_all(df:pd.DataFrame, target_column:string=None):
        """Plots input/output columns of given DataFrame."""
        y = utility.get_column_names(df)

        if target_column is None:
            target_column = y[-1]

        y.remove(target_column)

        fig, [ax1,ax2] = plt.subplots(2, 1)
        df.plot(x='Time', y=y, grid=True, ax=ax1);
        df.plot(x='Time', y=target_column, ax = ax2);

    def plot_batches(df:pd.DataFrame):
        swp = sliding_window_parameter(num_features=4)
        td = swp.create_training_data(df)
        td.plot_batches()

    def prepare(df:pd.DataFrame):
        df = df.drop('Site', axis=1)
        df['unique_id'] = np.ones((df.shape[0]))
        df = df.fillna(0)
        return df

    def train(df:pd.DataFrame):
        """Performs preprocessing and training on given DataFrame. Returns the Learner."""
        td = dataframe.get_train_data(df)
        return td.train_on_batches()

    def get_train_data(df:pd.DataFrame):
        """Returns the training data object from given DataFrame."""
        swp = sliding_window_parameter()
        return swp.create_training_data(df)

class utility:
    """Provides helper functionality without context to other classes."""

    def get_feature_names(num_features:int):
        """Returns the indexed variable names as list."""
        vars = list()
        for f in range(num_features):
            vars.append(f'var{f+1}')
        return vars

    def get_column_names(df:pd.DataFrame):
        return [element for element in list(df.columns) if element not in ['Site', 'Time', 'unique_id']]

    def get_feature_count(df:pd.DataFrame):
        """"""
        return len(df.columns) - 3

    def get_example_dataframe(num_features:int):
        """"""
        edp = example_data_parameter(num_features)
        return edp.create_sample_dataframe()

class train_data:
    """Represents the final data layer before training."""
    X = None
    y = None
    splits = None
    lrs = None
    trained = False
    learn = None

    def __init__(self, X, y, splits):
        """Initializes empty object."""
        self.X = X
        self.y = y
        self.splits = splits

    def train_on_batches(self, autosave:bool=True, iterations:int=100):
        """Performs training on optimal learning rate and returns Learner."""
        if self.check_if_ready is False:
            return
        dls = get_ts_dls(X=self.X, y=self.y, splits=self.splits)
        cbs = [ShowGraph(), 
            SaveModelCallback(monitor='valid_loss', comp=np.less, min_delta=0.001), 
            EarlyStoppingCallback(monitor='valid_loss', comp=np.less, min_delta=0.001, patience=10)]
        self.learn = ts_learner(dls, InceptionTimePlus, cbs=cbs, loss_func=mae, metrics=[mae, mse])
        if self.lrs is None:
            self.lrs = self.learn.lr_find(suggest_funcs=(minimum, steep, valley, slide))
        self.learn.fit_one_cycle(iterations, lr_max=self.lrs.valley)
        self.trained = True

        if autosave:
            self.learn.export(Path('models/core.pkl'))
        return self.learn
    
    def plot_batches(self):
        """Plots the created batches."""
        if self.check_if_ready is False:
            return        
        num_limit = 10
        half_lim = int(num_limit/2)
        num_batches = self.X.shape[0]
        num_features = self.X.shape[1]
        if num_batches > num_limit:
            print(f"Too many batches. Display only the first and last {half_lim}.")
            num_batches = num_limit
        fig, axs = subplots(1, num_batches, sharey=True)
        for c,n in enumerate(range(half_lim)):
            for f in range(num_features):
                axs[c].plot(self.X[n,f,:])#, 'tab:green')
            axs[c].plot(self.y[n])#, 'tab:red')
            axs[c].grid()
        for c,n in enumerate(range(int(self.X.shape[0]-half_lim-1), self.X.shape[0]-1)):
            for f in range(num_features):
                axs[c + half_lim].plot(self.X[n,f,:])#, 'tab:green')
            axs[c + half_lim].plot(self.y[n])#, 'tab:red')
            axs[c + half_lim].grid()

    def check_if_ready(self):
        """Checks whether or not the batches are ready for training."""
        if self.X is None:
            print("X was not yet initialized.")
            return False
        elif self.y is None:
            print("y was not yet initialized.")
            return False
        elif self.splits is None:
            print("splits were not yet initialized.")
            return False
        else:
            return True

class example_data_parameter:
    """Stores parameter for creating example data."""
    num_days = 0
    num_hours_per_day = 24
    num_features = 2
    time = None

    def __init__(self, num_days:int, num_features:int=2):
        """Initialize new parameter object for synthetic data."""
        self.num_days = num_days
        self.num_features = num_features

    def create_sample_data(self, with_unique:bool=False):
        """Returns new array with synthetic data."""
        num_points = self.num_hours_per_day * self.num_days

        data = np.zeros((num_points, self.num_features+2))
        self.time = np.linspace(1, num_points, num_points)
        
        if with_unique:
            data[:int(num_points/2),0] = 1
            data[int(num_points/2):,0] = 2
        else:
            data[:,0] = 1
        for f in range(self.num_features):          
            data[:,f+1] = 2*np.sin(2*np.pi*self.time/self.num_hours_per_day + f)
            data[:,self.num_features+1] += data[:,f+1]
        data[:,self.num_features+1] += np.random.randint(-10,10,(num_points))/10
        return data

    def create_sample_dataframe(self, with_unique:bool=False):
        """Returns new DataFrame with synthetic data."""
        data = self.create_sample_data(with_unique)
        columns = ['unique_id']
        columns.extend(utility.get_feature_names(self.num_features))
        columns.append('target')
        print(columns)
        frame = pd.DataFrame(data, columns=columns)
        frame = frame.reset_index()
        frame.rename(columns={'index': 'Time'}, inplace=True)
        frame = frame.sort_values('Time')
        return frame

class sliding_window_parameter:
    """Stores parameter for creating a sliding window operation."""
    add_padding_feature = False #1 Add an additional feature indicating whether each timestep is padded (1) or not (0).
    ascending = True #2 Used in sorting.
    check_leakage = True #3 Checks if there's leakage in the output between X and y
    copy=True #4 Copy the original object to avoid changes in it.
    get_x = None #5 Indices of columns that contain the independent variable (xs). If None, all data will be used as x.
    get_y = ['target'] #6 Indices of columns that contain the target (ys). If None, all data will be used as y. [] means no y data is created (unlabeled data).
    horizon = 240 #7 Number of future datapoints to predict (y). If get_y == [] horizon will be set to 0.
    output_processor = None #8 (Optional) Function to process the final output (X (and y if available)). This is useful when some values need to be removed.
    padding = 'pre' #9 (Optional) Pad either before or after each sequence. Defaults: 'pre'. If pad_remainder == False, it indicates the starting point to create the sequence ('pre' from the end, and 'post' from the beginning)
    padding_value = np.nan #10 Float that will be used for padding. Default: np.nan.
    pad_remainder = False #11 Allows to pad remainder subsequences when the sliding window is applied and get_y == [] (unlabeled data).
    return_key = False #12 When True, the key corresponsing to unique_id_cols for each sample is returned
    seq_first = True #13 True if input shape (seq_len, n_vars), False if input shape (n_vars, seq_len).
    sort_by = ['Time'] #14 Column/s used for sorting the array in ascending order.
    start = 0 #15 Determines the step where the first window is applied. Default: 0. Previous steps will be discarded. 
    stride = 1 #16 Number of datapoints the window is moved ahead along the sequence. Default: 1. If None, stride=window_len (no overlap).
    unique_id_cols = []#['unique_id'] #17 pd.DataFrame columns that will be used to identify a time series for each entity.
    verbose = True #18 Controls verbosity. True or 1 displays progress bar. 2 or more show records that cannot be created due to its length.
    window_len = 240 #19 Length of lookback.
    y_func = None #20 Optional function to calculate the ys based on the get_y col/s and each y sub-window. y_func must be a function applied to axis=1!.

    def __init__(self, num_features:int=2):
        """Initializes new default parameter."""
        self.get_x = utility.get_feature_names(num_features)

    def create_training_data(self, df:pd.DataFrame, target_column:string=None):
        """Performs sliding window operation on DataFrame and returns train_data object."""         
        self.get_x = utility.get_column_names(df)
        
        if target_column is None:
            target_column = self.get_x[-1]

        self.get_x.remove(target_column)
        self.get_y = [target_column]

        output = [df.groupby(['unique_id']).apply(lambda x: SlidingWindow(
            add_padding_feature=self.add_padding_feature,
            ascending=self.ascending,
            check_leakage=self.check_leakage,
            copy=self.copy, # it's important to set copy to True when used in this way!!!
            get_x=self.get_x,
            get_y=self.get_y,
            horizon=self.horizon,
            #output_processor=output_processor,
            padding=self.padding,
            padding_value=self.padding_value,
            pad_remainder=self.pad_remainder,
            #return_key=return_key, {unexpected keyword}
            seq_first=self.seq_first,
            sort_by=self.sort_by,
            start=self.start,
            stride=self.stride,
            #unique_id_cols=unique_id_cols, {unexpected keyword}
            #verbose=verbose, {unexpected keyword}
            window_len=self.window_len,
            y_func=self.y_func,
        )(x))][0].values

        X = np.concatenate([oi[0] for oi in output])
        y = np.concatenate([oi[1] for oi in output])
        splits = get_splits(o=y, n_splits=1, valid_size=.2, shuffle=False)

        return train_data(X=X, y=y, splits=splits)