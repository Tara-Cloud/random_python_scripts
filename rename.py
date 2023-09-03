#!/bin/env python
import os

path = "/Volumes/videos/2005"
month = "August"

for filename in os.listdir(path):
    print(f"Renaming {filename}")
    source_name = f"{path}/{filename}"
    new_name = f'{path}/{filename.replace(" ", "-")}'
    os.rename(source_name, new_name)
    print(f"Successfully renamed {filename} to {new_name}")

# for filename in os.listdir(path):
#     if filename[0] == "E":
#         print(f"Renaming {filename}")
#         filename_clean = filename.split("_504p")
#         prefix_month_day = filename_clean[0].split("-")
#         source_name = f"{path}/{filename}"
#         new_name = f"{path}/{prefix_month_day[0]}_{month}_{prefix_month_day[2]}.mp4"
#         # new_name = f'{path}/{filename.replace("March", "December")}'
#         os.rename(source_name, new_name)
#         print(f"Successfully renamed {filename} to {new_name}")
