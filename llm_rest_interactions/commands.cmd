# Show logs for the Ollama container
docker logs ollama_ollama_1

# List available models in Ollama
docker exec ollama_ollama_1 ollama list

# Pull the llama3.2 model for Ollama
docker exec -it ollama_ollama_1 ollama pull llama3.2

# Pull the phi4-mini model for Ollama
docker exec -it ollama_ollama_1 ollama pull phi4-mini

# Use /api/generate for single-turn completions
curl http://localhost:11434/api/generate -d '{"model": "llama3.2","prompt": "Why is the sky blue?","stream": false}'

# Use /api/chat for multi-turn conversations that maintain message history
curl http://localhost:11434/api/chat -d '{
  "model": "llama3.2",
  "messages": [
    { "role": "user", "content": "Hello!" },
    { "role": "assistant", "content": "Hi there! How can I help you today?" },
    { "role": "user", "content": "What is the capital of France?" }
  ]
}'