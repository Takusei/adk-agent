from google.adk.models.lite_llm import LiteLlm

AGENT_NAME = "summary_agent"
AGENT_DESCRIPTION = (
    "This agent summarizes the content of a given text or url of a web page."
)
LLM_MODEL_NAME = "ollama_chat/PetrosStav/gemma3-tools:4b"
BASE_URL = "http://localhost:11434"

model_config = LiteLlm(
    model=LLM_MODEL_NAME,
    api_base=BASE_URL)
