def decompress(order, unique):
    final = []
    for word_tag in order:
        final.append(unique[word_tag])
    print(final)
