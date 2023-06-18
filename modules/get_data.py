import os

from pathlib import Path
import requests
import zipfile

data_path = Path("test_data/")
image_path = data_path / "pizza_steak_sushi"

if image_path.is_dir():
    print(f"Directory \"{image_path}\" already exists")
else:
    image_path.mkdir(parents=True, exist_ok=True)

    with open(data_path / "pizza_steak_sushi.zip", "wb") as f:
        request = requests.get("https://github.com/mrdbourke/pytorch-deep-learning/raw/main/data/pizza_steak_sushi.zip")
        print("Downloading pizza, stake and sushi data")
        f.write(request.content)

    with zipfile.ZipFile(data_path / "pizza_steak_sushi.zip", "r") as zip_ref:
        print("Unzipping pizza_steak_sushi.zip")
        zip_ref.extractall(image_path)

    os.remove(data_path/"pizza_steak_sushi.zip")
