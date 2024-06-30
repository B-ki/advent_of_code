import pandas as pd
import numpy as np

def main():
    print("Hello")
    s = pd.Series([1, 3, 5, np.nan, 6, 8])
    print(s)
    
if __name__ == "__main__":
    main()
