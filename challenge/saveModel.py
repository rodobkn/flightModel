from model import DelayModel
import pandas as pd

data = pd.read_csv(filepath_or_buffer="../data/data.csv")
model = DelayModel()
features, target = model.preprocess(
    data=data,
    target_column="delay"
)
target = target["delay"]
model.fit(
    features=features,
    target=target
)
model.saveModel()

