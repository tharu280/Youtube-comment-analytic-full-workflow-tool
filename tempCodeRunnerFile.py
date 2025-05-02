import requests

try:
    requests.get("https://huggingface.co", timeout=5)
    print("✅ Internet is working.")
except requests.exceptions.RequestException:
    print("❌ Internet or connection to Hugging Face is not working.")
