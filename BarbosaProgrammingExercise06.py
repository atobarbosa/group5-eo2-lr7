import pandas as pd

def cleanStats(df):
    """
    Cleans the basketball statistics DataFrame by splitting columns with the 'makes-attempts' format.
    """
    def split_makes_attempts(column):
        makes = column.str.split('-').str[0].astype(int)
        attempts = column.str.split('-').str[1].astype(int)
        return makes, attempts

    # Process FG column
    df['FGM'], df['FGA'] = split_makes_attempts(df['FG'])
    df.drop(columns=['FG'], inplace=True)

    # Process 3PT column
    df['3PM'], df['3PA'] = split_makes_attempts(df['3PT'])
    df.drop(columns=['3PT'], inplace=True)

    # Process FT column
    df['FTM'], df['FTA'] = split_makes_attempts(df['FT'])
    df.drop(columns=['FT'], inplace=True)

    return df

# Load the dataset
df = pd.read_csv('rawbrogdonstats.csv')

# Apply the cleaning function to the dataset
df_cleaned = cleanStats(df)

# Display the cleaned dataset
print("Cleaned Data:")
print(df_cleaned.head())

"""
Explanation:
This Python code imports the pandas library for data manipulation and defines a function `cleanStats` to clean basketball statistics data. The function splits columns with a 'makes-attempts' format (such as FG, 3PT, and FT) into separate columns for makes and attempts using the `split_makes_attempts` helper function. Each original column is then removed after the split. The dataset is loaded from 'rawbrogdonstats.csv', cleaned using the `cleanStats` function, and the cleaned DataFrame is displayed, showing the first few rows to verify the output.
"""