
# Parsing identifiers and sequences from a Fasta File
__author__= "Henrique Frajacomo"


'''

                            Functions

'''

def FastaParser(myFile):    # Reads a Fasta File, returns a list
    x=0
    List = []
    ReadData = myFile.readline()
    WriteData = ""
    List.append(ReadData[1:].rstrip())
    ReadData = myFile.readline()


    while(ReadData):
        if(ReadData[0]!='>'):
            WriteData = WriteData + ReadData.rstrip()
        else:
            List.append(WriteData)
            WriteData=""
            List.append(ReadData[1:].rstrip())
        ReadData = myFile.readline()

    if(len(List) != 0):
        List.append(WriteData)

    return List

def FastaWriter(myList, stringFileName):   # Writes a Fasta file
    header = True
    outFile = open(stringFileName + ".fasta", "w")
    for element in myList:
        if(header):
            outFile.write('>' + element + '\n')
            header = False
        else:
            outFile.write(element + '\n')
            header = True
    outFile.close()




