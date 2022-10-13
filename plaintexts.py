#!/usr/bin/python3

plaintexts = [
    # "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla sem diam, lobortis vitae ligula sed, posuere laoreet dui.",
    # "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque faucibus malesuada purus interdum cursus.",
    # "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras sed fermentum nunc. Curabitur malesuada purusfaucibus elit quis cursus suscipit.",
    # "Lorem ipsum dolor sit camA, donsectetur adipiscing elit. Ut lacinia luctus vulputate.",
    # "Lorem ipsum dolor sit amet, donsectetut adipiscing elit. Aenean posuere arcu quis malesuada purus sem pretium, nec condimentum nunc venenatis.",
    # "Lorem ipsum dolor sit camA, donsectetut adipiscing elit. Maecenas porta nibh pulvinar est auctor malesuada.",
    # "Aenean vulputate condimentum mauris quis ornare. Ut aliquet ac just, bibendum efficitur.",
    # "Vivamus ac sollicitudin justo. Morbi congue risus mi, nec porta sapien vestibulum vitae.",
    # "Pellentesque a erat eu eros suscipit tincidunt. Fusce sodales porttitor tortor, lacinia laoreet urna mattis eget.",
    # "Nulla a felis egestas, ornare diam in, pulvinar mi. Donec tincidunt pharetra augue, sed tincidunt quam posuere et.",

    # "1. Secrets of endless lava have been unlocked to you.",
    # "2. Secrets of Earth's anger have been unlocked to you.",
    # "3. Secrets of otherworldly life have been unlocked to you.",
    # "4. Secrets of utter destruction have been unlocked to you.",
    # "5. Secrets of Undeath have been unlocked to you.",
    # "6. Secrets of fire and brimstone have been unlocked to you.",
    # "Secrets of the Spiral have been unlocked to you.",
    # "Secrets of stormy skies have been unlocked to you.",
    # "Secrets of jubilation have been unlocked to you.",
    # "Secrets of hidden danger have been unlocked to you.",
    # "Secrets of rebuilding have been unlocked to you.",
    # "This secret should not have been available for you.",
    # "Secrets of great undoing have been unlocked to you.",

    "1. Makes a projectile explode powerfully upon collision with creatures covered in slime",
    "2. Makes a projectile explode upon collision with creatures covered in alcohol",
    "3. Makes a projectile turn the creatures it hits into living fireball throwers",
    "4. Makes a projectile turn the creatures it hits into living thunderstorms",
    "5. Makes creatures hit by a projectile gain a temporary gravity well that draws projectiles in",
    "6. Makes creatures hit by a projectile grow tentacles in a chaotic manner",
    "7. Makes four fireballs rotate around a projectile",
    "8. Makes four... nukes(?!) rotate around a projectile",
    "9. Makes four plasma beams rotate around a projectile",
]

plaintexts_lower = [p.lower() for p in plaintexts]
plaintexts_no_space = [p.replace(" ", "") for p in plaintexts_lower]
