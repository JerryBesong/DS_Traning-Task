import spacy  # importing spacy
nlp = spacy.load('en_core_web_md')

word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")

print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

      

# (NOTEs ON THE SIMILARITIES)
# All three entities: Cat, Monkeys and Banana are nouns representing objects in a pysical world    
# Cat and monkey seem to be similar because they are both animals;
# Cats and monkey are both similar because they can be classified as both animals that fancy jumping
# Cats and Monkey can be classifed as both pets
# Interestingly, monkey and banana have a higher similarity than monkey and apple.


# My example
# Imagine a tropical forest where a mischievous monkey named Milo swings from tree to tree,
# occasionally stealing bananas from a nearby plantation. Meanwhile, a vigilant cat named Whiskers prowls
# beneath, eagerly watching for any fallen fruit or perhaps even eyeing Milo as a potential playmate or
# rival in the hunt for food."


# USING 'en_core_web_sm'
print("USING 'en_core_web_sm' ")
nlp = spacy.load('en_core_web_sm')

sentence_to_compare = "Why is my cat on the car"
sentences = ["where did my dog go", "Hello, there is my car", "I\'ve lost my car in my car", "I\'d like my boat back", "I will name my dog Diana"]
model_sentence = nlp(sentence_to_compare)
for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + "-" + str(similarity))
    

# So we can assume that the model already puts together that monkey seat bananas and that is why there is a significant similarity.
# Another interesting fact is that cat does not have any significant similarity with any of the fruits although monkey does.
# So, the model does not explicitly seem to recognise transitive relationships in its calculation.