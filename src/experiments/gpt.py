import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("h2oai/h2ogpt-oasst1-512-12b", padding_side="left")
model = AutoModelForCausalLM.from_pretrained("h2oai/h2ogpt-oasst1-512-12b", torch_dtype=torch.bfloat16, device_map="auto")

input_text = "Why is drinking water so healthy?"
input_ids = tokenizer.encode(input_text, return_tensors="pt").to(model.device)

output = model.generate(input_ids, max_length=100)
generated_text = tokenizer.decode(output[0], skip_special_tokens=True)

print(generated_text)
