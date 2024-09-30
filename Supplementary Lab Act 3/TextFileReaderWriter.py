from TextFileReaderWriter import TextFileReaderWriter

file = TextFileReaderWriter()

file.write('text.txt', input("Enter your text : "))

read_txt = file.read('text.txt')
print(read_txt)
