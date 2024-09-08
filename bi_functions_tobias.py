import pandas as pd

def calculate_outliers (data_frame, df, exclude_columns, *columns):


    categorical_columns = data_frame.select_dtypes(include=['object', 'category']).columns
    columns_to_exclude = categorical_columns.tolist()

    
    if exclude_columns == True:
        for col in columns:
            columns_to_exclude.append(col)
    

    column_names = []
    
    dic_of_data_to_return = {}

    df_without_outliers = data_frame.copy()

    total_number_of_outliers = 0

    
    if len(columns) == 0 or exclude_columns == True:
        if len(columns) == 0:
            print("No column arguments chosen. Outliers for all columns with numerical values are calculated")
        if exclude_columns == True: 
            print("No outliers calculated for the column arguments") 

        column_names = list(data_frame.drop(columns = columns_to_exclude).columns)    


    else:
        column_names = columns
        print("Outliers only calculated for the column arguments")

        
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




