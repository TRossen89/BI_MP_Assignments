import pandas as pd

def calculate_outliers (data_frame, df = True, exclude_columns = False, remove_outliers=False, multiply_value = 1.5, *columns):

    categorical_columns = data_frame.select_dtypes(include=['object', 'category']).columns
    columns_to_exclude = categorical_columns.tolist()
    
    if exclude_columns == True:
        for col in columns:
            columns_to_exclude.append(col)
    

    column_names = []
    
    dic_of_data_to_return = {}

    #df_without_outliers = data_frame.copy()
    df_to_calculate_on = data_frame.copy()
    
    #df_without_outliers['ID'] = range(1, len(df_without_outliers) + 1)
    df_to_calculate_on['ID'] = range(1, len(df_to_calculate_on) + 1)

    total_number_of_outliers = 0
    total_number_of_rows_deleted_in_data_frame_returned = 0
    

    
    if len(columns) == 0 or exclude_columns == True:
        if len(columns) == 0:
            print("No column arguments chosen. Outliers for all columns with numerical values are calculated")
        if exclude_columns == True: 
            print("No outliers calculated for the column arguments") 

        column_names = list(data_frame.drop(columns = columns_to_exclude).columns)    


    else:
        column_names = columns
        print("Outliers only calculated for the column arguments")


    ids_to_delete = set()
        
    for column_name in column_names:
        
        Q1 = df_to_calculate_on[f"{column_name}"].quantile(0.25)
        
        Q3 = df_to_calculate_on[f"{column_name}"].quantile(0.75)
        
        IQR = Q3-Q1
        
        Lower_Fence = Q1 - (multiply_value*IQR)
        Upper_Fence = Q3 + (multiply_value*IQR)
        
        outliers_condition = (df_to_calculate_on[f"{column_name}"]< Lower_Fence) | (df_to_calculate_on[f"{column_name}"] > Upper_Fence)

        outliers_df = pd.DataFrame(df_to_calculate_on[outliers_condition])
    
        number_of_outliers = outliers_df.shape[0]

        
        for id in outliers_df["ID"].tolist():
            
            ids_to_delete.add(id)

        
            
        total_number_of_outliers += number_of_outliers

        
        print(f"Number of outliers in {column_name}: " + str(number_of_outliers))
        
        dic_of_data_to_return[column_name] = {"number_of_outliers": number_of_outliers, "outliers": outliers_df}
        

    if remove_outliers == True:
        data_frame['ID'] = range(1, len(data_frame) + 1)
        data_frame = data_frame[~data_frame['ID'].isin(ids_to_delete)]
        print("Total number of rows deleted in returned data frame: " + str(len(ids_to_delete)))
    else:
        print("No outliers deleted ")
    
    print("Total number of outliers (if there is more outliers than deleted rows it means that some rows contain outliers in more than one column): " + str(total_number_of_outliers)) 
    
    
    if df == True and remove_outliers == True:
        return data_frame

    dic_of_data_to_return["df_without_outliers"] = data_frame
    dic_of_data_to_return["total_number_of_outliers"] = total_number_of_outliers 

    return dic_of_data_to_return




