from llama_cpp import Llama
import json
import os
file_path = os.path.expanduser("~/Documents/Projects/local_llm/local_llm_practice")

base_path = os.path.join("/media", "eric", "GASSS")
model_file = os.path.join(base_path, "models", "mistral-7b-instruct-v0.2.Q4_K_M.gguf")


with open(file_path + "/examples/Original3.txt", "r", encoding="utf-8") as f:
    text_variable = f.read()


with open(file_path + "/examples/Truth3.json", "r", encoding="utf-8") as f:
    json_variable = json.load(f)


# Initialize the LLaMA model
llm = Llama(
    model_path= model_file,
    chat_format="chatml",
    n_ctx=32768,
    n_gpu_layers = 12,
    verbose=True
)
