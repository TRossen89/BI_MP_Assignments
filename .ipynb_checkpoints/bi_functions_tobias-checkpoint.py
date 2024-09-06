import pandas as pd

def calculate_outliers (data_frame, df, *column_names):

    dic_of_data_to_return = {}

    df_without_outliers = pd.DataFrame()

    if len(column_names) == 0:
        print("no args")

    else:
        for column_name in column_names:
            
            Q1 = data_frame[f"{column_name}"].quantile(0.25)
            
            Q3 = data_frame[f"{column_name}"].quantile(0.75)
            
            IQR = Q3-Q1
            
            Lower_Fence = Q1 - (1.5*IQR)
            Upper_Fence = Q3 + (1.5*IQR)
            
            outliers_condition = (data_frame[f"{column_name}"]< Lower_Fence) | (data_frame[f"{column_name}"] > Upper_Fence)
    
            df_without_outliers = data_frame[~outliers_condition]
            
            outliers_df = data_frame[(outliers_condition)]
            
            number_of_outliers = outliers_df.shape[0]
            
            dic_of_data_to_return[column_name] = {"number_of_outliers": number_of_outliers, "outliers": outliers_df}


    if df == True:
        return df_without_outliers

    dic_of_data_to_return["df_without_outliers"] = df_without_outliers 

    return dic_of_data_to_return