import argparse
import pandas as pd
from pandas_profiling import ProfileReport
import imgkit

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-d", "--dataset", required=True, help="path to the tabular dataset")
ap.add_argument("-o", "--output", required=True, help="path to output html file")
args = vars(ap.parse_args())

df = pd.read_csv(args["dataset"])

profile = ProfileReport(df, title="Pandas Profiling Report")
profile.to_file(args["output"])

imgkit.from_file(args["output"], '/mnt/d/BigDataLifeCycle/img/out.png', options={"xvfb": "", "format": "png"})
