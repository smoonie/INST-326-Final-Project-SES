import pandas as pd
import seaborn as sns

def get_major_cat_list():
    """Obtains major category list
    
    Returns:
        [set]: returns a set populated from major category column
    """
    data = pd.read_csv('all-ages.csv')
    data = data[data['Major_category']]
    
    df = pd.DataFrame(data)
    major_cat_list = df.values.tolist()
    major_cat_list = set(major_cat_list)
    print(major_cat_list)
    return(major_cat_list)

def get_major_list():
    """Obtains major list
    
    Returns:
        [set]: returns a set populated from major list column
    """
    data = pd.read_csv('all-ages.csv')
    data = data[data['Major']]
    
    df = pd.DataFrame(data)
    major_list = df.values.tolist()
    major_list = set(major_list)
    print(major_list)
    return(major_list)

def get_major_num():
    """Obtains major number list
    
    Returns:
        [set]: returns a set populated from major number column
    """
    data = pd.read_csv('all-ages.csv')
    data = data[data['Major_code']]
    
    df = pd.DataFrame(data)
    major_num_list = df.values.tolist()
    major_num_list = set(major_num_list)
    print(major_num_list)
    return(major_num_list)

def pairplot():
    df = pd.read_csv("all-ages.csv")
    sns.pairplot(df)
    
def seaborn():
    df = pd.read_csv("all-ages.csv")
    sns.lmplot(x = "Major_code", y = "Employed", data = df, \
        hue = "Major_category")
    sns.lmplot(x = "Major_code", y = "Unemployed", data = df, \
        hue = "Major_category")
    
def employed_over_unemployed():
    df = pd.read_csv("all-ages.csv")
    employed_greater_unemployed = df[(df["Employed"] > \
        df["Unemployed"]) & (df["Major_category"])]
    print(employed_greater_unemployed)
    
def unemplyed_over_employed():
    df = pd.read_csv("all-ages.csv")
    unemployed_greater_employed = df[(df["Employed"] < \
        df["Unemployed"]) & (df["Major_category"])]
    print(unemployed_greater_employed)
    
get_major_list()
get_major_cat_list()
get_major_num()

