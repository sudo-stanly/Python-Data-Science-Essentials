
#! PANDAS
"""
The Pandas library contains several python objects. Here are brief descriptions of the objects we'll be using:


DataFrame: A 2D data structure of rows and columns.
    -Series: A 1D data structure.
    -read_csv( ): A function to load CSV files as dataframes.
    -and more... There are many more features of the pandas library.
    
    The DataFrame class is the star of the show. It is the most common data structure used in the 
    python data science world. Let's create a dataframe and see how it works.
""" 

"""
Let's apply what we learned from the previous intro to 
import
 the pandas library and instantiate a DataFrame. Note that the standard alias for pandas is "pd".

Activity Goals:
    Import pandas.
    Create a DataFrame.Let's apply what we learned from the previous intro to 
"""
import pandas as pd
df = pd.DataFrame

"""
[Empty DataFrame]
0 Rows x 0 Columns

[1]

    We have our first dataframe! But it's rather boring since it's empty. 
    Fortunately, pandas gives us ways to fill dataframes with data.
    For example, consider the following circles as a data source:
"""
#*  These circles have radius values: 2, 4, 3 and 5.

"""
Let's put this data into a dataframe by assigning 'color' and 'radius' columns.

Activity Goals:
    Assign a color column.
    Assign a radius column.
    Show the result.
"""
df = pd.DataFrame()
df['color'] = ['blue','red','yellow','green']
df['radius'] = [2,4,3,5]
print(df) #show result



"""
    Fantastic! Now we have a dataframe populated with 4 rows and 2 columns.
    Verify that this data represents the four circles displayed earlier.
"""



"""
    Column calculations
        We can also calculate new columns.

        For example, let's calculate a 'diameter' column by multiplying the radius by 2.
"""

df['diameter'] = df['radius'] * 2
df #output result
"""
      color	 radius	diameter
    0	blue	2	4
    1	red	4	8
    2	yellow	3	6
    3	green	5	10
    4 Rows x 3 Columns
"""
"""
    We have a diameter column! This shows the power and elegance of dataframes in python.
    Pandas also provides a variety of summary calculations for columns. Here are some examples 
    (click each to show the code):
"""

#! smallest radius
df['radius'].min( ) #* = 2

#! add up all the diameters
df['diameter'].sum( ) #* = 28

#! average radius
df['radius'].mean( ) #* = 3.5