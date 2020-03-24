import PyPDF2

alphabet_capital = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

while True:
    print("Welcome to PDF Translator!\nCopy and paste path:\n")
    user_path = input().strip('"')
    # final_path = Path(user_path)

    pdfFileObj = open(user_path, "rb")
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

    number_of_pages = pdfReader.getNumPages()
    full_page_string = ""
    for page_number in range(number_of_pages):
        page = pdfReader.getPage(page_number)
        page_content = page.extractText()
        # page_content_list = list(page_content.split(" "))
        full_page_string += page_content

    full_page = list(full_page_string.split(" "))
    print("Path set. Enter number.")

    # pageObj = pdfReader.getPage(1)
    # page0 = pageObj.extractText()
    # page0_list = list(page0.split(" "))

    def money():
        # index starts at -1 because it must start at 0 along with full_page
        index = -1
        money_list = ""
        for x in full_page:
            index += 1
            if "$" in x:
                capital = False
                capital_index = index
                period = False
                period_index = index
                # find the index of the capital letter
                while capital is not True:
                    for letter in alphabet_capital:
                        if letter in full_page[capital_index]:
                            capital = True
                    capital_index -= 1
                while period is not True:
                    if "." in full_page[period_index] and "$" not in full_page[period_index]:
                        period = True
                    else:
                        period_index += 1
                for y in range(capital_index, period_index):
                    money_list += full_page[y]
                    money_list += " "
                    # money_list.append(" ")
                # money_list.append("\n")
                money_list += "\n"
        print(money_list)


    # def addresses():
    #     index = -1
    #     address_list = ""
    #     for x in full_page:
    #         index += 1
    #         for y in street_types:
    #             if y in x:
    #                 address_list += "^"
    #                 for z in range(index-5, index+5):
    #                     address_list += full_page[z]
    #                     address_list += " "
    #                 address_list += "\n"
    #     print(address_list)

    # check if unemployed
    def stats():
        index = -1
        unemployed = False
        insurance_list = ""
        purchase_price = ""
        age = ""
        name = ""
        for word in full_page:
            index += 1
            if unemployed is False and "unemployed" in word:
                unemployed = True
            if "Insurance" in word:
                if "Company" in full_page[index + 1]:
                    for index_ins in range(index-3, index+2):
                        insurance_list += full_page[index_ins]
                        insurance_list += " "
            if "years" in word and "old" in full_page[index + 1]:
                age += full_page[index - 1] + " "
                age += full_page[index] + " "
                age += full_page[index + 1]
                if "is" in full_page[index - 2]:
                    name += full_page[index - 4] + " "
                    name += full_page[index - 3]
        print("Stats:")
        print("Name: " + str(name))
        print("Age: " + str(age))
        print("Insurance: " + str(insurance_list))
        if unemployed is True:
            print("Unemployed: Likely" + "\n")
        else:
            print("Unemployed: Unlikely" + "\n")



    while True:
        print("Options:\n(1)Financial\n(2)Stats\n(3)New Lead")
        hold_input = input()
        if hold_input == "1":
            money()
            hold_input = None
        elif hold_input == "2":
            stats()
            hold_input = None
        elif hold_input == "3":
            break