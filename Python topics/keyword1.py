import keyword
print(keyword.kwlist)

# Get the list of all Python keywords
all_keywords = keyword.kwlist

# Print each keyword with its position (starting from 1)
for i, keyword_str in enumerate(all_keywords, start=1):
    print(f"{i}. {keyword_str}")

    import builtins

for i, func_name in enumerate(dir(builtins), start=1):
    print(f"{i}. {func_name}")