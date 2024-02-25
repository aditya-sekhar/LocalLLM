from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("google/gemma-2b-it")
model = AutoModelForCausalLM.from_pretrained("google/gemma-2b-it")

chat = [
    { "role": "user", "content": "How does the brain work?" },
]
prompt = tokenizer.apply_chat_template(chat, tokenize=False, add_generation_prompt=True)
input_ids = tokenizer(prompt, return_tensors="pt")
outputs = model.generate(**input_ids, max_length=100)

print("\n" + "-"*50)
print(prompt)
print("\n" + "-"*50)
print(tokenizer.decode(outputs[0]))
print("\n" + "-"*50)
