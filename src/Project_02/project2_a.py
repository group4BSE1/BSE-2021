try:
    handle = open("measles.txt", "r")
    year = input("Enter year :")
    if year == "" or year == "all" or year == "ALL":
      pass
    elif int(year):
        if len(year) < 5:
            pass
        else:
            print("Invalid year")
            exit()
    output_file = input("Enter the output file: ")
    if not ".txt" in output_file:
        print("Invalid entry")
        print("Output_file must have a .txt extension ")
        exit()

    save = open(output_file, "w")
    for line in handle:
        if year in line[88:92]:
            if line[88:92].startswith(year):
                save.write(line)
    save.close()
    handle.close()
except:
    print("Invalid input")
