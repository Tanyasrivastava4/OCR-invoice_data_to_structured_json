#from llama_cpp import Llama
#from config.schema import SCHEMA
#from config.prompt import PROMPT_TEMPLATE
#
#MODEL_PATH = "models/qwen2.5-1.5b-instruct-q4.gguf"
#
#llm = Llama(
#    model_path=MODEL_PATH,
#    n_ctx=4096,
#    n_threads=6,     # adjust to your CPU cores
#    n_batch=64,
#    verbose=False
#)
#
#
#def extract_structured_invoice(text: str) -> str:
#    prompt = PROMPT_TEMPLATE.format(
#        schema=SCHEMA,
#        text=text
#    )
#
#    response = llm(
#        prompt,
#        max_tokens=800,
#        temperature=0.0,
#        stop=["</json>", "</output>"]  # optional
#    )
#
#    return response["choices"][0]["text"].strip()
#
#
#
#
#
#
#
#
#from transformers import AutoTokenizer, AutoModelForCausalLM
#import torch
#from config.schema import SCHEMA
#from config.prompt import PROMPT_TEMPLATE
#
##MODEL_ID = "microsoft/phi-3-mini-4k-instruct"
##MODEL_ID = "microsoft/phi-2"
#MODEL_ID = "google/gemma-2b-it"
#
#
#
#tokenizer = AutoTokenizer.from_pretrained(MODEL_ID)
#
#model = AutoModelForCausalLM.from_pretrained(
#    MODEL_ID,
#    device_map="cpu",
#    torch_dtype=torch.float32
#)
#
#def extract_structured_invoice(text: str) -> str:
#    prompt = PROMPT_TEMPLATE.format(
#        schema=SCHEMA,
#        text=text
#    )
#
#    inputs = tokenizer(prompt, return_tensors="pt")
#
#    output = model.generate(
#        **inputs,
#        max_new_tokens=800,
#        do_sample=False,
#        temperature=0.0
#    )
#
#    return tokenizer.decode(output[0], skip_special_tokens=True)
#
#
#from config.schema import SCHEMA
#from config.prompt import PROMPT_TEMPLATE
#
## Your API endpoint (example, replace with actual endpoint)
#API_URL = "https://api.qwen3.ai/v1/llm-infer"  
#
## Your API key
#API_KEY = "YOUR_API_KEY_HERE"
#
## Input prompt you want the model to process
#
#
## Request payload
#payload = {
#    "model": "qwen3-coder",
#    "input": prompt,
#    "max_tokens": 200,        # optional: limit output length
#    "temperature": 0.7        # optional: randomness
#}
#
## Headers
#headers = {
#    "Authorization": f"Bearer {API_KEY}",
#    "Content-Type": "application/json"
#}
#
## Make the POST request
#response = requests.post(API_URL, headers=headers, data=json.dumps(payload))
#
## Get the response
#if response.status_code == 200:
#    result = response.json()
#    print("Model Output:\n", result.get("output_text"))
#else:
#    print("Error:", response.status_code, response.text)
#