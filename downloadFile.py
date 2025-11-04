from huggingface_hub import hf_hub_download
from huggingface_hub import snapshot_download
from pathlib import Path
import requests
from tqdm import tqdm

model_path = hf_hub_download(
    repo_id="mradermacher/NuExtract-2.0-8B-GGUF",
    filename="NuExtract-2.0-8B.IQ4_XS.gguf",
    local_dir="./models"
)
