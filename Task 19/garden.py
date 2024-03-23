import spacy

# Find garden path sentences
gardenpathsentences = [
    "The old man the boats.",
    "The complex houses married and single soldiers and their families.",
    # Add more sentences here
]

# Add additional sentences
additional_sentences = [
    "Mary gave the child a Band-Aid.",
    "That Jill is never here hurts.",
    "The cotton clothing is made of grows in Mississippi.",
]

    # add more sentences using .apend()
for sent in additional_sentences:
    gardenpathsentences.append(sent)
print(gardenpathsentences)


# Tokenize and perform named entity recognition

nlp = spacy.load("en_core_web_sm")

for sentence in gardenpathsentences:
    doc = nlp(sentence)
    # Do something with the tokens and entities
    for token in doc:
        print(token.orth_, token.orth, token.text, token.pos_, token.dep_)
        
    for ent in doc.ents:
        print(ent, ent.label_, ent.label)

# Looked up entities

print(spacy.explain("GPE"))
print(spacy.explain("ORG"))
print(spacy.explain("FAC"))
print(spacy.explain("CARDINAL"))

print("YES THE ENTITIES MADE SENSE TO ME")






