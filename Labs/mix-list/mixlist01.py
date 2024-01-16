def main():
    
    wordbank = ["indentation", "spaces"]

    tlgstudents= ['Albert', 'Anthony', 'Brenden', 'Craig', 'Deja', 'Elihu', 'Eric', 'Giovanni', 'James', 'Joshua', 'Maria', 'Mohamed', 'PJ', 'Philip', 'Sagan', 'Suchit', 'Meka', 'Trey', 'Winton', 'Xiuxiang', 'Yaping']

    wordbank.append(4)

    choice= int(input("Pick a student number!"))
    student_name= tlgstudents[choice]

    print(f"{student_name} always uses 4 spaces to indent")

main();

