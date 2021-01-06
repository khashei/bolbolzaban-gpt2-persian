from transformers import pipeline, AutoTokenizer, GPT2LMHeadModel

tokenizer = AutoTokenizer.from_pretrained("bolbolzaban/gpt2-persian")

def generate_sample(model, input):
    model = GPT2LMHeadModel.from_pretrained(model)
    generator = pipeline(
        "text-generation", model, tokenizer=tokenizer, config={"max_length": 256}
    )
    sample = generator(input)
    return sample

# Test finetuned model
sample = generate_sample("./model", "[CLS]فردوسی[CLS][BOM]")
print(sample[0]["generated_text"])

# Test original model
sample = generate_sample("bolbolzaban/gpt2-persian", "در یک اتفاق شگفت انگیز، پژوهشگران")
print(sample[0]["generated_text"])
