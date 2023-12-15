# nypdarrestdata

This Python package `nypdarrestdata` is designed to facilitate the analysis of arrest data in New York. It includes functions for fetching arrest data, plotting crime maps, analyzing regional dangers, and more. This tool is particularly useful for researchers, data analysts, and anyone interested in crime statistics and patterns in New York City.

## Installation

```bash
$ pip install nypdarrestdata
```
## Functions
fetch_arrest_data
This function fetches arrest data between specified start and end dates. It returns a pandas DataFrame containing detailed information about each arrest made in New York City within the given time frame.

plot_crime_map
Generates an interactive map displaying crime locations. Users can visually explore crime data with details such as race, age group, and charges of each incident.

analyze_region_danger
Analyzes the danger level of different regions based on the arrest data. It provides insights into the number of arrests in each NYC borough and further breaks down the data by age group, gender, race, and charges.

plot_distribution
A utility function used within analyze_region_danger to create distribution plots for various categories such as age group, sex, and race.

## Usage Example

```python
from nypdarrestdata import fetch_arrest_data, plot_crime_map
```
## Fetch arrest data
```python
start_date = '2023-01-01'
end_date = '2023-01-10'
arrest_data = fetch_arrest_data(start_date, end_date)
```
## Plot the crime map with the fetched data
```python
crime_map = plot_crime_map(arrest_data)
crime_map
```
## Contributing

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## License

`nypdarrestdata` was created by Benny Ha. It is licensed under the terms of the MIT license.

## Credits

`nypdarrestdata` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).
