# Example code from FastAPI documentation

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def read_root():
    return {"message": "Hello World! You can view the docs at https://potatoapi.ml/docs"}


@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}

@app.get('/piglatin/{text}')
async def pig_latin(text: str):
	sentence = text
	words = sentence.split()
 
	for i, word in enumerate(words):
		if word[0] in 'aeiou':
			words[i] = words[i]+ "ay"
		else:
			has_vowel = False
			for j, letter in enumerate(word):
				if letter in 'aeiou':
					words[i] = word[j:] + word[:j] + "ay"
					has_vowel = True
					break
			if(has_vowel == False):
				words[i] = words[i]+ "ay"
	pig_latin = ' '.join(words)
	pig_latin = pig_latin.translate({ord(i): None for i in ('!', '?', '.')})
	return {'text': pig_latin}