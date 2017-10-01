import random

challenges = {
    1:"Go for atleast a 30 minute walk.",
    2:"Eat 5 fruits today.",
    3:"Cook your own food today.",
    4:"Pick a sport, and play a game today.",
    5:"Do not complain at all today.",
    6:"Do a mindfulness activity for ten minutes today.",
    7:"Don't eat any foods with artificial sugar today.",
    8:"Research something you know little about.",
    9:"Do something new, something that you have never done before.",
    10:"Wash your clothes today.",
    11:"Spend time with a close friend today.",
    12:"Go out of your way to make a new friend today."
}

daily_quest = random.choice(list(challenges.keys()))

daily_challenge = (challenges[daily_quest])



