try:
    import pandas as pd
    print("Pandas is installed. Version:", pd.__version__)
except ImportError:
    print("Pandas is not installed.")
