from transformers import (
    AutoTokenizer,
    TextDataset,
    DataCollatorForLanguageModeling,
    Trainer,
    TrainingArguments,
    AutoModelWithLMHead,
)


def load_dataset(train_path, test_path, tokenizer):
    train_dataset = TextDataset(
        tokenizer=tokenizer, file_path=train_path, block_size=256
    )

    test_dataset = TextDataset(tokenizer=tokenizer, file_path=test_path, block_size=256)

    data_collator = DataCollatorForLanguageModeling(
        tokenizer=tokenizer,
        mlm=False,
    )

    return train_dataset, test_dataset, data_collator


def freeze_lower_layers():
    for param in model.base_model.parameters():
        param.requires_grad = False

    for param in (
        model.base_model.h[23].parameters() or model.base_model.h[22].parameters()
    ):
        param.requires_grad = True


# load model
model = AutoModelWithLMHead.from_pretrained("bolbolzaban/gpt2-persian")

# freeze lower layers and only train top layers
freeze_lower_layers()

# load dataset
tokenizer = AutoTokenizer.from_pretrained("bolbolzaban/gpt2-persian")
train_dataset, test_dataset, data_collator = load_dataset(
    "./data/train.txt", "./data/test.txt", tokenizer
)

# train
training_args = TrainingArguments(
    output_dir="./model",
    overwrite_output_dir=True,
    num_train_epochs=5,
    per_device_train_batch_size=12,
    per_device_eval_batch_size=12,
    eval_steps=1000,
    save_steps=1000,
    warmup_steps=500,
)

trainer = Trainer(
    model=model,
    args=training_args,
    data_collator=data_collator,
    train_dataset=train_dataset,
    eval_dataset=test_dataset,
)

trainer.train()

# save
trainer.save_model()
