import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def countplot(df : pd.DataFrame,x_col:str,title : str) -> None:
    sns.countplot(x=x_col,data=df)
    plt.title(title)
    plt.show()
    
