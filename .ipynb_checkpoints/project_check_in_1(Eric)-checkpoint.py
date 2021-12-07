import pandas as pd

def get_major_cat_list():
    """Obtains major category list
    
    Returns:
        [set]: returns a set populated from major category column
    """
    data = pd.read_csv('majors-list.csv')
    data = data[data['Major_Category']]
    
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
    data = pd.read_csv('majors-list.csv')
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
    data = pd.read_csv('majors-list.csv')
    data = data[data['FOD1P']]
    
    df = pd.DataFrame(data)
    major_num_list = df.values.tolist()
    major_num_list = set(major_num_list)
    print(major_num_list)
    return(major_num_list)

get_major_list()
get_major_cat_list()
get_major_num()