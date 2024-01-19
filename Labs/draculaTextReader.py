def main():
    count = 0
    with open("dracula.txt", "r") as txt:
        for line in txt:
            if 'vampire' in line.lower():
                count += 1
                print(line)

    # Move the print(count) outside the for loop
    print(count)

    # ADD THE FILE CONVERTER LATER

if __name__ == "__main__":
    main()
