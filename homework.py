###### Have you seen this number before?
before = set()
for i in [1,3,8,35,4,2,3]:
    if i in before:
        print("YES")
    else:
        print("NO")
    before.add(i)

###### Special Words
words = set(input().lower().split())
print(len(words))
times_of_a_appears = 0
for w in words:
    if "a" in w:
        times_of_a_appears += 1

print(times_of_a_appears)

###### Special Numbers
listA = [18, 2, 90, 3, 5]
listB = [2, 86, 42, 5, 7]

setA = set(listA)
setB = set(listB)
intersection = list(setA.intersection(setB))
intersection.sort()
for i in intersection:
    print(i)

###### Multilingual
number_of_people = int(input("How many people are there?"))
languages: "list[set]" = []

for i in range(number_of_people):
    number_of_languages = int(input(f"(To person {i+1}) How many languages can you speak?"))
    print("What languages can you speak in?")
    langs_can_each_person_speak = set()
    for _ in range(number_of_languages):
        langs_can_each_person_speak.add(input())
    languages.append(langs_can_each_person_speak)

languages_everyone_speak = []
for each_lang in languages[0]:
    the_lang_is_speakable_by_other = True
    for other in languages[1:]:
        if each_lang not in other:
            the_lang_is_speakable_by_other = False
            break
    
    if the_lang_is_speakable_by_other:
        languages_everyone_speak.append(each_lang)

print(f"Number of languages everyone speaks: {len(languages_everyone_speak)}")
print(f"Spoken language(s) everyone speaks: {', '.join(languages_everyone_speak)}")

total_languages = set()
for each_person in languages:
    for each_lang in each_person:
        total_languages.add(each_lang)

print(f"Total languages spoken in the group: {len(total_languages)}")
print(f"Languages spoken: {', '.join(total_languages)}")
