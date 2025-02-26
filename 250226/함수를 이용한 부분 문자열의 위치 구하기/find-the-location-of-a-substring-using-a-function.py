text = input()
pattern = input()

# Please write your code here.

def sol(text, pattern):
    text_len, pat_len = len(text), len(pattern)
    idx = -1
    for i in range(text_len):
        if i + pat_len > text_len:
            break
        if text[i:i+pat_len] == pattern:
            idx = i
            break
    return idx

print(sol(text, pattern))