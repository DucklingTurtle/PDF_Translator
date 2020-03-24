import PyPDF2

print("Welcome to PDF Translator!\nCopy and paste path:\n")
user_path = input().strip('"')
# final_path = Path(user_path)

pdfFileObj = open(user_path, "rb")
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

pageObj = pdfReader.getPage(0)
page0 = pageObj.extractText()
page0_list = list(page0.split(" "))


index = -1
money_list = []
address_list = []
print(page0)
for x in page0_list:
    index += 1
    if "$" in x:
        for y in range(index-5, index+5):
            money_list.append(page0_list[y])
            money_list.append(" ")
        money_list.append("\n")
print(money_list)