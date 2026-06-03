import re
import csv
import pandas as pd
import numpy as np

genre_names = ['(no genres listed)','Action','Adventure',
'Animation', "Children", "Comedy", "Crime", "Documentary", "Drama", "Fantasy", "Film-Noir", "Horror", 
"Musical", "Mystery", "Romance", "Sci-Fi", "Thriller" , "War", "Western", "IMAX" ]
num_genre = len(genre_names)

