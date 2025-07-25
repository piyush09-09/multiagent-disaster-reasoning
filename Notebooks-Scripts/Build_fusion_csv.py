import os
import pandas as pd
import json
from tqdm import tqdm

BASE_DIR ="d:/multiagent-disaster-reasoning/data/CrisisMMD_v2.0"
DATASPLIT_DIR = os.path.join(BASE_DIR,"crisismmd_datasplit_all")
IMAGE_DIR = os.path.join(BASE_DIR,"data_image")
JSON_DIR = os.path.join(BASE_DIR,"json")
OUTPUT_CSV =os.path.join(BASE_DIR, "fusion.csv")

def load_split(file_name,split_name):
    path=os.path.join(DATASPLIT_DIR,file_name)
    df=pd.read_csv(path,sep="\t")
    df['split']=split_name
    return df

print("Loading Split files...")
df_train =load_split("task_informative_text_img_train.tsv","train")
df_dev = load_split("task_informative_text_img_dev.tsv","dev")
df_test =load_split("task_informative_text_img_test.tsv","test")
df =pd.concat([df_train,df_dev,df_test],ignore_index=True)

df.rename(columns={
    "tweet_id": "tweet_id",
    "image_id": "image_id",
    "text": "tweet_text",
    "label": "disaster_type"
},inplace =True)

print("matching image paths...")
image_paths=[]
missing_images =0

for image_id in tqdm(df['image_id']):
    img_path = os.path.join(IMAGE_DIR,image_id  + ".jpg")
    if os.path.exists(img_path):
        image_paths.append(img_path)
    else:
        image_paths.append(None)
        missing_images+=1

RELEVANT_LABELS=[
    "infrastructure_damage", "affected_individuals",
    "rescue_volunteering", "vehicle_damage",
    "building_damage", "injured_or_dead_people",
    "fire","flood"
]
df=df[df["disaster_type"].isin(RELEVANT_LABELS)]
df["image_path"]=image_paths
df=df[df["image_path"].notnull()].reset_index(drop=True)
print(f"skipped {missing_images} rows due to missing images.")
 
print("extracting location of JSON metadata...")
locations =[]

for tweet_id in tqdm(df["tweet_id"]):
    json_path =os.path.join(JSON_DIR,f"{tweet_id}.json")
    loc=""
    if os.path.exists(json_path):
        try:
            with open(json_path, "r",encoding ="utf-8") as f:
                data =json.load(f)
                user_loc =data.get("user",{}).get("location","")
                geo =data.get("geo",{}).get("coordinates","")
                if user_loc:
                    loc =user_loc
                elif geo:
                    loc =str(geo)
        except Exception as e:
            loc =""
    locations.append(loc)
df['location']=locations

df_final =df[["image_id","image_path","tweet_text","disaster_type","tweet_id","location","split"]]
df_final.to_csv(OUTPUT_CSV,index=False,encoding= "utf-8")
print(f"fusion.csv saved at: {OUTPUT_CSV}")
print(f" Total usable rows: {len(df_final)}")

print(df["disaster_type"].value_counts())
