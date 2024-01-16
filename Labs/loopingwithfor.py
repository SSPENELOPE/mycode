def main():
    farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]

    ne_animals = farms[0]["agriculture"]
    
    for farm in farms:
        print(f"{farm['name']}\n")
    choice = input("Choose a farm: ")
    
    for farm in farms: 
        if farm['name'].lower() == choice.lower():
            print(f"{farm['agriculture']}")

if __name__ == "__main__":
    main()
