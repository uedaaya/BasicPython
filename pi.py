text = "How I want a drink, alcoholic of course, after the heavy chapters involving quantum mechanics. All of thy geometry, Herr Planck, is fairly hard."

# TODO

transformed_texta = text.replace(",","").replace(".","")
words = transformed_texta.split()
wordsa = list(map(len,(words)))
wordsb = list(map(str,(wordsa)))
print("".join(wordsb))
wordsc = "".join(wordsb)
wordsd = wordsc[0]
wordse = wordsc[1:]
wordsf = wordsd +"." + wordse
print(wordsf)