import random

name_adj = ["dark", "cold", "warm", "bright", "damp", "smelly", "dry"]

place_noun = ["corridor", "room", "cave", "nook", "ampitheater", "alcove", "passageway"]

desc_verb = ["enter", "cross the threshold of", "gain access to", "set foot in", "crawl into", "approach", "run into", "pass into"]
desc_sight = ["a panda", "a pile of gold", "a pot roast", "Darth Vader", "a velociraptor", "Dora the Explorer"]
desc_sense = ["see", "hear", "smell", "feel", "sense the presence of"]
desc_location = ["Overhead", "Beneath your feet", "To the right", "To the left", "Behind you", "Ahead of you"]
#so you get the same location in both the title and the description
noun = random.choice(place_noun)

#title
adjective = random.choice(name_adj)
print(f"{adjective} {noun}")

#description
movement_verb = random.choice(desc_verb)
location = random.choice(desc_location)
sense = random.choice(desc_sense)
sight = random.choice(desc_sight)


#####verb######place###where##########sense####thing
#You _enter_ a _room_. _Overhead_, you _see_ a _thing_.""
print(f"You {movement_verb} a {noun}. {location}, you {sense} {sight}")