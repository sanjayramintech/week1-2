import tiktoken

filename = input("Enter file name: ")

#introducing exception handling for file not found 
#----------------------------------------------------------
try:
    with open(filename, "r", encoding="utf-8") as f:
        text = f.read()
except FileNotFoundError:
    print(f"File '{filename}' not found,pls check the file name and re-enter it!")
    exit()
#----------------------------------------------------------

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