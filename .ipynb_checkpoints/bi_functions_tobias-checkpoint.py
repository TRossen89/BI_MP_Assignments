import pandas as pd

def calculate_outliers (data_frame, df, *columns):


    categorical_columns = data_frame.select_dtypes(include=['object', 'category']).columns
    categorical_columns_list = categorical_columns.tolist()
    

    column_names = []
    
    dic_of_data_to_return = {}

    df_without_outliers = data_frame.copy()

    total_number_of_outliers = 0

    
    if len(columns) == 0:
        print("no column args chosen")

        column_names = list(data_frame.drop(columns = categorical_columns).columns)    


    else:
        column_names = columns

        
    for column_name in column_names:
        
        Q1 = df_without_outliers[f"{column_name}"].quantile(0.25)
        
        Q3 = df_without_outliers[f"{column_name}"].quantile(0.75)
        
        IQR = Q3-Q1
        
        Lower_Fence = Q1 - (1.5*IQR)
        Upper_Fence = Q3 + (1.5*IQR)
        
        outliers_condition = (df_without_outliers[f"{column_name}"]< Lower_Fence) | (df_without_outliers[f"{column_name}"] > Upper_Fence)

        outliers_df = pd.DataFrame(df_without_outliers[outliers_condition])
        
        df_without_outliers = df_without_outliers[~outliers_condition]
        
        
        
        number_of_outliers = outliers_df.shape[0]

        total_number_of_outliers += number_of_outliers
        
        print(f"Number of outliers in {column_name}: " + str(number_of_outliers))
        
        dic_of_data_to_return[column_name] = {"number_of_outliers": number_of_outliers, "outliers": outliers_df}


    print("Total number of outliers: " + str(total_number_of_outliers)) 
    
    if df == True:
        return df_without_outliers

    dic_of_data_to_return["df_without_outliers"] = df_without_outliers 
    dic_of_data_to_return["total_number_of_outliers"] = total_number_of_outliers 

    return dic_of_data_to_return