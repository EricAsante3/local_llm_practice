from huggingface_hub import hf_hub_download
from huggingface_hub import snapshot_download
from pathlib import Path
import requests
from tqdm import tqdm

# model_path = hf_hub_download(
#     repo_id="TheBloke/Mistral-7B-Instruct-v0.2-GGUF",
#     filename="mistral-7b-instruct-v0.2.Q4_K_M.gguf",
#     local_dir="./models"
# )


# model_path = hf_hub_download(
#    repo_id="TheBloke/based-13b-GGUF",
#    filename="based-13b.Q4_K_M.gguf",
#    local_dir="./models"
#)

# Define the path for the new folder in the current directory
# current_folder = Path.cwd()
# model_folder = current_folder.joinpath("mistral_models", "7B-Instruct-v0.3")
# model_folder.mkdir(parents=True, exist_ok=True)

# Download the GGUF model file
# model_file = hf_hub_download(
#    repo_id="bartowski/Mistral-7B-Instruct-v0.3-GGUF",
#     filename="Mistral-7B-Instruct-v0.3-Q4_K_M.gguf",
#     local_dir=model_folder
# )

# print(f"Model downloaded to: {model_file}")



# URL of the model file on Hugging Face (Q4_K_M is best for most setups)
model_url = "https://huggingface.co/NousResearch/Nous-Hermes-2-Mistral-12B-GGUF/resolve/main/nous-hermes-2-mistral-12b.Q4_K_M.gguf"

# Output file name
output_path = "./nous-hermes-2-mistral-12b.Q4_K_M.gguf"

# Stream download with progress bar
response = requests.get(model_url, stream=True)
total_size = int(response.headers.get("content-length", 0))

print(f"Downloading {output_path} ({total_size / 1e9:.2f} GB)...")

with open(output_path, "wb") as file, tqdm(
    desc=output_path,
    total=total_size,
    unit="B",
    unit_scale=True,
    unit_divisor=1024,
) as bar:
    for data in response.iter_content(chunk_size=1024 * 1024):  # 1 MB chunks
        size = file.write(data)
        bar.update(size)

print("\n✅ Download complete!")
