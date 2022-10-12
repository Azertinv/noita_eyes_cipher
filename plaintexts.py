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

    "Secrets of endless lava have been unlocked to you.",
    "Secrets of Earth's anger have been unlocked to you.",
    "Secrets of otherworldly life have been unlocked to you.",
    "Secrets of utter destruction have been unlocked to you.",
    "Secrets of Undeath have been unlocked to you.",
    "Secrets of fire and brimstone have been unlocked to you.",
    "Secrets of the Spiral have been unlocked to you.",
    "Secrets of stormy skies have been unlocked to you.",
    "Secrets of jubilation have been unlocked to you.",
    "Secrets of hidden danger have been unlocked to you.",
    "Secrets of rebuilding have been unlocked to you.",
    "This secret should not have been available for you.",
    "Secrets of great undoing have been unlocked to you.",
]

plaintexts_lower = [p.lower() for p in plaintexts]
plaintexts_no_space = [p.replace(" ", "") for p in plaintexts_lower]
