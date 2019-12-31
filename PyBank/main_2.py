import os, csv
from pathlib import Path

# Declare Path

import_file = Path("Users", "gregp", "Git_Trilogy", "Python_Challenge", "PyBank", "PyBank", "budget_data.csv")
with open(import_file, "r") as text:

    print(text)
    
    lines = text.read()

    print(lines)

# Setup Reader

