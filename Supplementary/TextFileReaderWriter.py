class TextFileReaderWriter:
    def read(self, file):
        with open(file, 'r') as file:
            content = file.read()
        return content
    
    def write(self, file, data):
        with open(file, 'w') as file:
            file.write(data)
        return file.write
    
