class SaurabhWeek13():
    def extract(self):
        file1 = open("1950.txt", "r")
        file2 = open("extracted_file.txt", "w")
        print("Reading values from the file and printing them")
        for pointer in file1:
            longitude = pointer[34:41]
            qualitycode = pointer[63]
            temperature = pointer[87:92]
            print("Row inserted")
            file2.write(longitude + "\t" + temperature + "\t" + qualitycode + "\n")

if __name__ == '__main__':
    SaurabhWeek13.run()

