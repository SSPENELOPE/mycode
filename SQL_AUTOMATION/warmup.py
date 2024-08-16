def coolpeeps():
    coolpeeps = {
        "all": [
            {"First": "Aranka", "Last": "Bullen", "Skill Level": "G.O.A.T.", "Spirit Animal": "zebra", "Super Power": "Mind control"},
            {"First": "Chris", "Last": "McIntosh", "Skill Level": "astonishing", "Spirit Animal": "seal", "Super Power": "Technopathy"},
            {"First": "Cortney", "Last": "Babb", "Skill Level": "awe-inspiring", "Spirit Animal": "barracuda", "Super Power": "Prehensile/animated hair"},
            {"First": "DeShon", "Last": "Dixon", "Skill Level": "stunning", "Spirit Animal": "ram", "Super Power": "Levitation"},
            {"First": "Jasmin", "Last": "Ellis", "Skill Level": "wondrous", "Spirit Animal": "otter", "Super Power": "Psychic"},
            {"First": "Jeff", "Last": "Khy", "Skill Level": "breathtaking", "Spirit Animal": "lion", "Super Power": "Portal creation"},
            {"First": "Kea", "Last": "Gray", "Skill Level": "wonderful", "Spirit Animal": "badger", "Super Power": "Immortal"},
            {"First": "Kelvin", "Last": "Lau", "Skill Level": "fearsome", "Spirit Animal": "boar", "Super Power": "Super speed"},
            {"First": "Sherie", "Last": "Chandler", "Skill Level": "formidable", "Spirit Animal": "goat", "Super Power": "Elasticity"},
            {"First": "Tobi", "Last": "Akintola", "Skill Level": "frightening", "Spirit Animal": "shark", "Super Power": "Force fields"},
            {"First": "Tyler", "Last": "Poepping", "Skill Level": "shocking", "Spirit Animal": "penguin", "Super Power": "Resurrection"}
        ]
    }

    for person in coolpeeps["all"]:
        print(f"My name is {person['First']} {person['Last']} and my skill level is {person['Skill Level']}.")


coolpeeps()