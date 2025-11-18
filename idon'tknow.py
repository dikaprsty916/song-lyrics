import time, sys 

lyrics = [
"im not baby anymore",
"im not as innocent as before",
"i see it the mirror. in my room",
"and i can feel it stronger in my soul",
"but im not so ready for this world",
"now i see things i didn't, see before",
"i need explannation. tell me more",
"why i'm in love now?",
"i don't know",
"how can i live forever?",
"i don't know",
"where can i find heaven?",
"i don't know",
"what is going to happen?",
"i don't know",
"why i'm in love now?",
"i don't know",
]
for line in lyrics:
    for ch in line+"\n":
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(0.05)
    time.sleep(0.6)