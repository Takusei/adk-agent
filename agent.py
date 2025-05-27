from google.adk.agents import LlmAgent
from .config import model_config, AGENT_NAME, AGENT_DESCRIPTION
from .prompts import INSTRUCTION
from .tools.fetch import get_webpage_text

root_agent = LlmAgent(
    name=AGENT_NAME,
    model=model_config,
    description=AGENT_DESCRIPTION,
    instruction=INSTRUCTION,
    tools=[get_webpage_text],
)