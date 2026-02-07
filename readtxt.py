with open('input.txt', 'r', encoding='utf-8') as file:
    text = file.read()

#print(len(text))
#print(text[:1000])
chars = sorted(list(set(text)))
vocab_size = len(chars)
stoi = { ch:i for i, ch in enumerate(chars) }
itos = { i:ch for i, ch in enumerate(chars) }
encode = lambda s: [stoi[c] for c in s]
decode = lambda l: ''.join([itos[i] for i in l])


n = int(0.8*len(text))
train_data = text[:n]
val_data = text[n:]

block_size = 8
x = train_data[:block_size]
y = train_data[1:block_size+1]
for t in range(block_size):
    context = train_data[:t+1]
    target = train_data[t+1:t+2]
    print(f"when input is {context} the target is {target}")

