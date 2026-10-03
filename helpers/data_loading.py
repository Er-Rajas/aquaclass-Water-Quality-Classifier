"""
Helper script for loading and giving you small info about your dataframe.
num_cat () -> returns numerical and categorical columns list of your dataframe
describe() -> describes your numerical columns and categorical columns
data_type() -> returns data type of your dataframe
null_count() -> returns null count of your dataframe
load_data() -> loads your dataframe from csv file and executes all the above functions

"""

import pandas as pd
import numpy as np

def num_cat(df : pd.DataFrame) -> tuple[list[str],list[str]]:
    numerical_col = df.select_dtypes(include=["int64", "float64"]).columns.tolist()
    categorical_col = df.select_dtypes(include=["object"]).columns.tolist()
    return numerical_col, categorical_col

        
def describe (df : pd.DataFrame, numerical_col, categorical_col ) -> None:
    if numerical_col != []:
        print(f"Numerical column description: \n {df[numerical_col].describe()}")
    else :
        pass
    if categorical_col !=[]:
        print(f"categorical columns description: \n {df[categorical_col].describe()}")
    else :
        pass
    
def data_type (df :pd.DataFrame) -> pd.Series:
    return df.dtypes

def null_count (df :pd.DataFrame) -> pd.Series:
    return df.isnull().sum()


def load_data(df:pd.DataFrame) -> None:
    print("="*20, "\n")
    print("Data Loading... \n")
    print("="*20, "\n")
    print("categorizing columns... \n")
    num_col, cat_col = num_cat(df)
    if num_col != []:
        print(f"Numerical columns : \n {num_col} \n")
    else : print("No Numerical Columns Found \n")
    if cat_col != []:
        print(f"Categorical columns : \n {cat_col} \n")
    else : print("No Categorical Columns Found \n")
    print("="*20, "\n")
    print("detecting data types... \n")
    print(data_type(df),"\n")
    print("="*20, "\n")
    print("Describing  data ... \n")
    describe(df,num_col,cat_col)
    print("="*20, "\n")
    print("Detecting Nulls in data ... \n")
    print(null_count(df))
    print("="*20, "\n")
    print("Data Loading completed \n")
    print("="*20, "\n")

    
