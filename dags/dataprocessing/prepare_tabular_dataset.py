import argparse
import re
import pandas as pd

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-d", "--dataset", required=True, help="path to the tabular dataset")
ap.add_argument("-o", "--output", required=True, help="path to output file for use on HDFS")
args = vars(ap.parse_args())

# load the dataset
df_raw = pd.read_json(args["dataset"])

# Fix th nested list in images column
new_df = pd.concat([pd.DataFrame(pd.json_normalize(x)) for x in df_raw['images']],ignore_index=True)
new_df = new_df.drop(['url'], axis=1)

# concat the dataset again in tabular format
df_final = pd.concat([df_raw.drop(['images'], axis=1), new_df], axis=1)

df_final["title"] = df_final["title"].apply(lambda x: re.sub(r'\W+', ' ', x[0]).lower() if isinstance(x, list) else x)
df_final["url"] = df_final["url"].apply(lambda x: x[0] if isinstance(x, list) else x).astype(str)
df_final["views"] = df_final["views"].apply(lambda x: x[0] if isinstance(x, list) else x)
df_final["duration"] = df_final["duration"].apply(lambda x: x[0] if isinstance(x, list) else x)
df_final["likes"] = df_final["likes"].apply(lambda x: x[0] if isinstance(x, list) else x)
df_final["dislikes"] = df_final["dislikes"].apply(lambda x: x[0] if isinstance(x, list) else x)
df_final["channelName"] = df_final["channelName"].apply(lambda x: x[0] if isinstance(x, list) else x)
df_final["subscribers"] = df_final["subscribers"].apply(lambda x: x[0] if isinstance(x, list) else x)
df_final["description"] = df_final["description"].apply(lambda x: re.sub(r'\W+', ' ', x[0]).lower() if isinstance(x, list) else x)
df_final["keywords"] = df_final["keywords"].apply(lambda x: re.sub(r'\W+', ' ', x[0]).lower() if isinstance(x, list) else x)
df_final["date_published"] = pd.to_datetime(df_final["date_published"].apply(lambda x: x[0] if isinstance(x, list) else x))
df_final["date_scraped"] = pd.to_datetime(df_final["date_scraped"].apply(lambda x: x[0] if isinstance(x, list) else x))
df_final["tags"] = df_final["tags"].apply(lambda x: re.sub(r'\W+', ' ', ', '.join(map(str, x))).lower() if isinstance(x, list) else x)
df_final["comments"] = df_final["comments"].apply(lambda x: re.sub(r'\W+', ' ', x[0]).lower() if isinstance(x, list) else x)
df_final["image_urls"] = df_final["image_urls"].apply(lambda x: x[0] if isinstance(x, list) else x)
df_final["path"] = df_final["path"].apply(lambda x: x[0] if isinstance(x, list) else x)
df_final["checksum"] = df_final["checksum"].apply(lambda x: x[0] if isinstance(x, list) else x)
df_final["status"] = df_final["status"].apply(lambda x: x[0] if isinstance(x, list) else x)

# save as csv
df_final.to_csv(args["output"], index=False)
