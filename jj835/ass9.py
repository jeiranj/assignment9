# 
# Python ass9.py 
# 

import numpy as np
import matplotlib.pyplot as plt
import pandas as p
from checks import *

def main():
#Question 1: reads countries.csv and excel GDP.xlsx files.
    print '****Starting question 1****'
    try:
        print 'countries data loading...'
        countries = p.read_csv('countries.csv',index_col=0)
        print 'countries data loaded.'
        print 'income data loading...'
        income = p.read_excel('GDP.xlsx',index_col=0);
        if income.index.name != None:
            income.index.names = ['Country']
        elif income.columns.name == None:
            income.columns.names = ['Country']
        income = income.dropna(axis=0, how='all')
        income = income.dropna(axis=1, how='all')
        max_income = income.max(axis=1).max(axis=0)
        print 'income data loaded.'
    except:
        print 'Unexpected error:', sys.exc_info()[0]
        sys.exit()
    
#Question 2: transforms income data to have countries as column names and years as indices.
    print '****Starting question 2****'
    income = income.T  #YearsxCountry
    print income.head()
        
#Question 3: plot histogram of GDP per capita across countries for a user-supplied year.
    print '****Starting question 3****'
    years = list(income.index[0:])
    try:
        year = raw_input('Enter a year to plot GDP histogram between {} and {}: '.format(years[0],years[-1]))
    except (KeyboardInterrupt, EOFError):
        print '\nAs you wish! \n'
        sys.exit()
    # check validity of user-supplied year:
    if (check_type(year) == False):
        raise IncorrectType('User-suplied year should be an integer %s'%year)
    if (check_range(year,income.index[1],income.index[-1]) == False):
        raise OutOfRange('User-suplied year should be in the given range %s'%year)
    gdp_data = get_gdp_for_year(year,income)
    # plot histogram of GDP per capita for the user-supplied year:
    gdp_data.T.hist(bins=50)
    plt.xlabel('GDP per capita', fontsize=18)
    plt.ylabel('Number of countries', fontsize=18)
    plt.title(year, fontsize=20)
    plt.savefig('question3.eps')
    print 'Saved GDP per capita histogram for year {}'.format(year)

# Question 5:
    print '****Starting question 5****'
    year1 = years[-1]-10
    year2 = years[-1]
    max_income_in_range = income.T[range(year1,year2+1)].max(axis=0).max(axis=1)
    for year in range(year1,year2+1):
        gdp_data = get_gdp_for_year(year,income)
        result = merge_by_year(year,gdp_data,countries)
        plt.figure()
        result.boxplot('Income', by='Region',sym='go')
        plt.suptitle('')
        plt.xlabel('Region', fontsize=18)
        plt.xticks(rotation=30)        
        plt.ylabel('GDP per capita', fontsize=18)
        plt.ylim(ymax=max_income)
        plt.title(year, fontsize=20)
        plt.savefig('question5bp_{}.png'.format(year), bbox_inches='tight')
        print 'Saved regional GDP per capita boxplot for year {}'.format(year)
        # subplot of histograms for GDP per region
        plt.figure()
        result.Income.hist(by=result.Region,bins = 30,figsize = (10,10),xrot= 30, xlabelsize = 12, ylabelsize = 12,grid=True)
        plt.savefig('question5h_{}.png'.format(year))
        print 'Saved regional GDP per capita histogram for year {}'.format(year)
        grouped_result=result['Income'].groupby(result.Region)
        plt.figure()
        grouped_result.plot(kind='hist',legend=True)
        plt.xlim(xmax=max_income_in_range)
        plt.xlabel('GDP per capita', fontsize=18)
        plt.ylabel('Number of countries', fontsize=18)
        plt.title(year, fontsize=20)
        plt.savefig('question5all_{}.png'.format(year))
        print 'Saved combined regional GDP per capita histogram for year {}'.format(year)
        plt.close("all")
    
    
def get_gdp_for_year(year,income):
    """Extracts GDP per capita of all countries for the year "year" using the "income" dataframe.
    Args:
        -- year: user-supplied year, a string.
        -- income: dataframe consisting of Country and annual GDP per capita data.
    Returns:
        -- gdp_data: a dataframe consisting of 2 columns: Country and Year for which GDP is listed."""
    # If required, transform dataframe so that year is the index value.
    if income.index.name == 'Country':
        income = income.T
    year = int(year)
    gdp_data = income.ix[[year]] 
    gdp_data = gdp_data.dropna(axis=1)
    return gdp_data
    

# Question 4: 
def merge_by_year(year,income,countries):    
    """Merges countries and income data frames for the year "year".
    Args:
        -- year: user-supplied year, a string.
        -- income: GDP per capita dataframe.
        -- countries: Countries dataframe.
    Returns:
        -- result: a data frame consisting of 3 columns: Country, Region and Income."""
    year = int(year)
    gdp_data = get_gdp_for_year(year,income)
    if gdp_data.index.name != 'Country':
        gdp_data = gdp_data.T
    if countries.index.name != 'Country':
        countries = countries.T
    result = countries.join(gdp_data,how='inner')
    result.reset_index(drop=False,inplace=True)
    result.rename(columns={year: 'Income'},inplace=True)
    return result
    

if __name__ == '__main__':
    main()
    
    
    