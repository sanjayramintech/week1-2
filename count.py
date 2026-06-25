import tiktoken

filename = input("Enter file name: ")

with open(filename, "r", encoding="utf-8") as f:
    text = f.read()

encoding = tiktoken.get_encoding("cl100k_base")



tokens = encoding.encode(text)
print(tokens)
for token in tokens:
    print(encoding.decode([token]))
token_count = len(tokens)

cost_per_million = 500

estimated_cost = (token_count / 1000000) * cost_per_million

print("Token Count:", token_count)
print("Estimated Cost: $", estimated_cost)