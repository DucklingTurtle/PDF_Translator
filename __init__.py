import PyPDF2

alphabet_capital = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
numbers_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

# while loop so the program re-runs when we finish
while True:
    print("Welcome to PDF Translator!\nCopy and paste path:\n")
    user_path = input().strip('"')
    pdfFileObj = open(user_path, "rb")
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    # open necessary stuff and get num of pages
    number_of_pages = pdfReader.getNumPages()
    full_page_string = ""
    # open all pages into one temp page
    for page_number in range(number_of_pages):
        page = pdfReader.getPage(page_number)
        page_content = page.extractText()
        # page_content_list = list(page_content.split(" "))
        full_page_string += page_content
    # turn temp full page into real full page by turning into list
    full_page = list(full_page_string.split(" "))
    print("Path set. Enter number.")

    # calculate finances
    def money():
        # index starts at -1 because it must start at 0 along with full_page
        index = -1
        money_list = ""
        # blacklist of indexes that have already been used so duplicates dont occur
        index_blacklist = []
        for x in full_page:
            # start increasing index var so we can keep track of where we are
            index += 1
            # parameters for grabbing text
            if "$" in x or "Lump" in x or "lump" in x or "Monthly" in x or "monthly" in x:
                # capital goes to the left until it satisfies parameters and becomes true,
                capital = False
                capital_index = index
                c_index_counter = 0
                period = False
                period_index = index
                p_index_counter = 0
                # find the index of the capital letter
                while capital is not True:
                    for letter in alphabet_capital:
                        if letter in full_page[capital_index] or c_index_counter >= 3:
                            capital = True
                    if capital is not True:
                        capital_index -= 1
                        c_index_counter += 1
                while period is not True:
                    if "." in full_page[period_index] and "$" not in full_page[period_index] or p_index_counter >= 25:
                        # print("Period Index: " + str(period_index))
                        # print("Word: " + str(full_page[period_index]))
                        period = True
                    else:
                        period_index += 1
                        p_index_counter += 1
                    if "$" in full_page[period_index]:
                        period_index -= 1
                        period = True
                money_list_hold = ""
                for y in range(capital_index, period_index + 1):
                    if y not in index_blacklist:
                        money_list_hold += full_page[y]
                        money_list_hold += " "
                        index_blacklist.append(y)
                if money_list_hold and any(x in money_list_hold for x in numbers_list):
                    money_list += "^"
                    money_list += money_list_hold
                    money_list += "\n"
                        # if y == period_index:
                        #     money_list += "\n"
                    # money_list.append("\n")
                    # money_list += "\n"
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
        annuity_number = ""
        for word in full_page:
            index += 1
            if unemployed is False and "unemployed" in word:
                unemployed = True
            if "Annuity" in word or "annuity" in word or "ANNUITY" in word:
                if "number" in full_page[index + 1] or "NUMBER" in full_page[index + 1] or "Number" in full_page[index + 1]:
                    annuity_number = full_page[index + 2]
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
        print("Annuity Number:  " + str(annuity_number))
        if unemployed is True:
            print("Unemployed: Likely" + "\n")
        else:
            print("Unemployed: Unlikely" + "\n")

    def percentages():
        index = -1
        percentages_list = []
        for word in full_page:
            index += 1
            if "%" in word:
                for index_per in range(index-3, index+3):
                    percentages_list.append(index_per)
                    percentages_list.append(" ")
                percentages_list.append("\n")
                print(percentages_list)


    while True:
        print("Options:\n(1)All Monetary References\n(2)Stats\n(3)Percentages\n(4)New Lead")
        hold_input = input()
        if hold_input == "1":
            money()
            hold_input = None
        elif hold_input == "2":
            stats()
            hold_input = None
        elif hold_input == "3":
            percentages()
            hold_input = None
        elif hold_input == "4":
            break