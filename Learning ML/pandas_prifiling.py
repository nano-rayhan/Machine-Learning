from ydata_profiling import ProfileReport
import pandas as pd
df = pd.read_csv("netflix.csv")

prof = ProfileReport(df)
prof.to_file(output_file='output_netflix.html')
