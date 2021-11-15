# Known bug: For some reason, the first item in each reiterated loop cycle (csv rows 2+)
#            always applies the quote strip to the 0th item
import csv

class StripQuotes():
    def readWriteFile(file, quoteColumn):

        try:
            noApostrophe = []
            stripAll = False

            # Convert letters to digits
            if quoteColumn.isdigit():
                quoteColumn = int(quoteColumn)
            elif quoteColumn.lower() == "all" or quoteColumn.lower() == "\"all\"":
                stripAll = True
                quoteColumn = -1
            elif quoteColumn.isalpha():
                quoteColumn = int(ord(quoteColumn) - 96)
            else:
                return "Please enter a column value.\n"

            with open(file, newline='') as f:
                reader = csv.reader(f)

                # Remove quotes
                for row in reader:
                    rowList = []
                    i = 0
                    lyst = list(row)

                    # Ensures input is within valid column range
                    if quoteColumn >= len(lyst)+1:
                        return "Please choose a column that is within A and " + str(chr(len(lyst)+96).upper()) + ".\n"
                        break

                    # For each item per row...
                    for item in lyst:
                        word = item

                        # Strip all columns
                        if (stripAll == True):
                            word = word.replace("'", "")
                            word = word.replace('"', "")
                            word = word.strip()
                        else:
                            # Strip only one column
                            # letters = list(word)
                            if word == lyst[quoteColumn - 1] and (word[0] == word[-0]):
                                word = word.replace("'", "")
                                word = word.replace('"', "")
                                word = word.strip()

                        # and (letters[0] == letters[-1]) and ((letters[0] == "'") or (letters[0] == '"'))
                            # letters = letters[1:-1]

                        # Re-form words
                        letters = ''.join(word)
                        word = letters
                        #word.strip()

                        # Create list of words in row
                        rowList.append(word)
                        i += 1

                    noApostrophe.append(rowList)

            # Write new list to file
            file2 = str(file[0:-4] + "_noquotes.csv");
            with open(file2, "w", newline='') as f:
                writer = csv.writer(f, delimiter=',', quotechar="", escapechar="\n", quoting=csv.QUOTE_NONE)

                for row in noApostrophe:
                    writer.writerow(row)

            return 'Formatted column: ' + str(quoteColumn) + ' in '+ file + '\nCSV: '+ str(noApostrophe) + \
                   "\nFile output to: " + str(file2) + "\n"

        # Error handling
        except (FileNotFoundError, IOError):
            return "Please enter a valid filename.\n "

def main():
    column = 0
    print("Type in a column that you want to remove the surrounding quotes or type \"all\". (Type -1 to exit.)")
    while (column != "-1"):
        file = str(input("Which file? (enter a .csv filename in this directory): "))
        column = input("Which column? (enter a letter or number): ")
        print(StripQuotes.readWriteFile(file, column))

if __name__ == "__main__":
    main()