import requests
from config.schema import SCHEMA
from config.prompt import PROMPT_TEMPLATE

API_URL = "https://e274eif4vpzm3j-8000.proxy.runpod.net/v1/chat/completions"
API_KEY = "11056cc3fb10f655cd143de42e689cf2037366bade833f087164878be2278c62"
MODEL_NAME = "qwen3-coder"


def extract_structured_invoice(text: str) -> str:
    prompt = PROMPT_TEMPLATE.format(
        schema=SCHEMA,
        text=text
    )

    payload = {
        "model": MODEL_NAME,
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ],
        "temperature": 0.0,
        "max_tokens": 800
    }

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    response = requests.post(API_URL, json=payload, headers=headers)

    if response.status_code != 200:
        raise Exception(
            f"API call failed: {response.status_code}\n{response.text}"
        )

    result = response.json()

    # OpenAI-style response
    return result["choices"][0]["message"]["content"]




#import requests
#from config.schema import SCHEMA
#from config.prompt import PROMPT_TEMPLATE
#
##API_URL = "https://e274eif4vpzm3j-8000.proxy.runpod.net/v1/generate"
#API_URL = "https://e274eif4vpzm3j-8000.proxy.runpod.net/v1/llm-infer"  # Correct endpoint
#
#API_KEY = "11056cc3fb10f655cd143de42e689cf2037366bade833f087164878be2278c62"
#MODEL_NAME = "qwen3-coder"
#
#def extract_structured_invoice(text: str) -> str:
#    """
#    Sends the invoice text to Qwen3-Coder API and returns structured JSON.
#    """
#    # Prepare prompt
#    prompt = PROMPT_TEMPLATE.format(schema=SCHEMA, text=text)
#
#    payload = {
#        "model": MODEL_NAME,
#        "input": prompt,
#        "temperature": 0.0,
#        "max_output_tokens": 800  # Limit response length
#    }
#
#    headers = {
#        "Authorization": f"Bearer {API_KEY}",
#        "Content-Type": "application/json"
#    }
#
#    response = requests.post(API_URL, json=payload, headers=headers)
#
#    if response.status_code == 200:
#        result = response.json()
#        # Qwen3 API usually returns text in 'output' or 'generated_text' key
#        # adjust if API returns different field
#        output_text = result.get("output") or result.get("generated_text")
#        return output_text
#    else:
#        raise Exception(f"API call failed: {response.status_code} {response.text}")
#