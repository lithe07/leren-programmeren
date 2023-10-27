import re

def extract_sub_sentences(text):
    marked_text = re.sub(r"\.|,|!|\?| en |omdat |zodat |want |wanneer |dat ", "|", text)
    sub_sentences = marked_text.split("|")
    return sub_sentences

def calculate_ego_score(sub_sentences):
    ego_score = 0
    for sentence in sub_sentences:
        sentence = sentence.strip()
        sentence = sentence.lower()
        if len(sentence) > 0:
            words = sentence.split(' ')
            if len(words) >= 2 and (words[0] in ('ik', 'mijn') or words[1] in ('ik', 'mijn')):
                ego_score += 1
    return ego_score

# Voorbeeldtekst om de functies te testen
sample_text = "Ik hou van pizza. Omdat pizza heerlijk is, eet ik het vaak. Maar soms wil ik gezonder eten, zodat ik me beter voel."

sub_sentences = extract_sub_sentences(sample_text)
ego_score = calculate_ego_score(sub_sentences)

# Druk de resultaten af
print("Deelzinnen in de tekst:")
for sentence in sub_sentences:
    print(sentence)
print("Ego-score:", ego_score)
