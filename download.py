#!/usr/bin/env python3

HF_TOKEN = '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'

# Load model directly
import transformers
from transformers import GenerationConfig, AutoTokenizer, AutoModelForCausalLM

def download_llamas():
    for size in [7, 13, 70]:
        size = str(size)
        tokenizer = AutoTokenizer.from_pretrained("meta-llama/Llama-2-"+size+"b-chat-hf", token=HF_TOKEN)
        model = AutoModelForCausalLM.from_pretrained("meta-llama/Llama-2-"+size+"b-chat-hf", token=HF_TOKEN)

download_llamas()
