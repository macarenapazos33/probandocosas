import random

buzz = ('continuous testing', 'continuous integration',
    'continuous deployment', 'continuous improvement', 'devops')
adjectives = ('completo', 'copado', 'self-service', 'integrado', 'end-to-end')
adverbs = ('notablemente', 'enormemente', 'sustancialmente', 'significativamente',
    'seriamente')
verbs = ('acelera', 'mejora', 'realza', 'modeniza', 'impulsa')

def sample(l, n = 1):
    result = random.sample(l, n)
    if n == 1:
        return result[0]
    return result

def generate_buzz():
    buzz_terms = sample(buzz, 2)
    phrase = ' '.join([sample(adjectives), buzz_terms[0], sample(adverbs),
        sample(verbs), buzz_terms[1]])
    return phrase.title()

if __name__ == "__main__":
    print(generate_buzz())
