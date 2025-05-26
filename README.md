## Run the LLM locally
```
# Need to use the one supported tools
ollama run PetrosStav/gemma3-tools:4b

# Make sure the `Capabilities` includes `tools`
ollama show PetrosStav/gemma3-tools:4b 
```

## Use command `uv` to active venv
```
uv venv

source .venv/bin/activate 
```