from importlib.metadata import version
from .data_fetching import fetch_arrest_data
from .plot_crime_map import plot_crime_map
from .analyze_region_danger import analyze_region_danger, plot_distribution
from .numeric_analysis_of_arrests import numeric_analysis_of_arrests

__all__ = [
    'fetch_arrest_data', 
    'plot_crime_map', 
    'analyze_region_danger', 
    'plot_distribution', 
    'numeric_analysis_of_arrests'
]
__version__ = version("nypdarrestdata")
