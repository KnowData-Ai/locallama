#!/usr/bin/env python3

HF_TOKEN = '''Access Llama 2 on Hugging Face
This is a form to enable access to Llama 2 on Hugging Face after you have been granted access from Meta. Please visit the Meta website and accept our license terms and acceptable use policy before submitting this form. Requests will be processed in 1-2 days.

Your Hugging Face account email address MUST match the email you provide on the Meta website, or your request will not be approved.
Meta URL: https://ai.meta.com/resources/models-and-libraries/llama-downloads
'''

# Load model directly
import transformers
from transformers import GenerationConfig, AutoTokenizer, AutoModelForCausalLM

def download_llamas():
    for size in [7, 13, 70]:
        size = str(size)
        tokenizer = AutoTokenizer.from_pretrained("meta-llama/Llama-2-"+size+"b-chat-hf", token=HF_TOKEN)
        model = AutoModelForCausalLM.from_pretrained("meta-llama/Llama-2-"+size+"b-chat-hf", token=HF_TOKEN)

download_llamas()
