# Data Wrangling exercice

## ABOUT

Project to get a nice CSV file of natural gas prices for each granularity.  
The resulting CSV files should have two columns: Date and Price

## INPUT DATA

Input data can be found at  http://www.eia.gov/dnav/ng/hist/rngwhhdm.htm
  
## LOGIC

  - Extracting natural gas data prices:
    - Extracting data using an open data api whose endpoint is : https://www.eia.gov/dnav/ng/hist_xls/
    - Extracting data for every granularity
  
  - Transforming the data:
    - Renaming the columns
    - Formating Date column
    - Dealing with price missing values:
      - drop records with price missing values if PRICE_MISSING_VALUES environment variable is set to drop (It could 
        be the case if we want to make price predictions and therefore records with missing prices are useless to train a model to predict prices)
      - fill price missing values if PRICE_MISSING_VALUES environment variable is set to fill:
        - for daily prices fill with the weekly mean price (ie: compute the mean over the week the date of the 
          missing price belongs to)
        - for weekly prices fill with the monthly mean price (ie: compute the mean over the month the week of the 
          missing price belongs to)
        - for monthly prices fill with the annual mean price (ie: compute the mean over the year the month of the 
          missing price belongs to)
        - Finally for annual prices fill with mean price accross all years (ie: acrross thhe entire annual dataset)  
        
        The default behaviour is to drop records with price missing values but can be changed to fill price missing values by setting PRICE_MISSING_VALUES environment variable to fill.
  
  - Loading data:
    - Exporting data into csv files by default (could be exported into different formats by setting the OUTPUT_EXTENSION environment variable to another value than csv)
    - Looping through the different granularities to export an output file for every granularity

## HOW TO RUN

  - Set HENRY_HUB_GAS_DATA_SOURCE environment variable if different than default value in settings
  - Set PRICE_MISSING_VALUES environment variable to value fill to fill price missing values (default value set to drop   
    to drop records with price missing value)
  - Set OUTPUT_DIR environment variable to indicate the directory where to export output files if different than default 
    value
  - Set OUTPUT_EXTENSION environment variable to indicate in which format we want to export the output files if different 
    than defaul value (csv by default)
  - The output directory is automatically created to store output files using the OUTPUT_DIR environement variable
  - Run python3 data_wrangling.py

