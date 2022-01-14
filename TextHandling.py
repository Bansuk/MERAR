import pytesseract as ocr
import Patient
import re
from PIL import Image

ocr.pytesseract.tesseract_cmd = r'P:\Tesseract-OCR\tesseract.exe'


def getfileinfo(filesnameslist, source, patients):
    for i in filesnameslist:
        info = ocr.image_to_string(Image.open(source + "\\" + substitute(i, "pdf", "jpeg")), lang='por')
        getspecificinfo(info, patients)
        print(info)


def getspecificinfo(info, patients):
    #company
    if re.search(r'(?<=Empresa CNPJ\n)(.*)(?= )', info) is None:
        if re.search(r'(?<=Empresa\n)(.*)(?=)', info) is None:
            if re.search(r'(?<=Empresa\n\n)(.*)(?=)', info) is None:
                if re.search(r'(?<=Empresa CNS\n)(.*)(?= )', info) is None:
                    if re.search(r'(?<=Empresa CNPJ\n\n)(.*)(?= )', info) is None:
                        company = ""
                    else:
                        company = re.search(r'(?<=Empresa CNS\n)(.*)(?= )', info).group(0)
                else:
                    company = re.search(r'(?<=Empresa CNPJ\n\n)(.*)(?= )', info).group(0)
            else:
                company = re.search(r'(?<=Empresa\n\n)(.*)(?=)', info).group(0)
        else:
            company = re.search(r'(?<=Empresa\n)(.*)(?=)', info).group(0)
    else:
        company = re.search(r'(?<=Empresa CNPJ\n)(.*)(?= )', info).group(0)

    #patient name
    if re.search(r'(?<=\d\/)(.*)(?= )', info) is None:
        name = ""
    else:
        name = re.search(r'(?<=\d\/)(.*)(?= )', info).group(0)

        print("Nome" + name)

    #tpExam
    #if re.search(r'(?<=Tipo de Exame\n)(.*)(?=)', info) is None:
    #    if re.search(r'(?<=Tipo de Exame Data Ficha\n)(.*)(?= )', info) is None:
    #        tpExam = ""
    #    else:
    #        tpExam = re.search(r'(?<=Tipo de Exame Data Ficha\n)(.*)(?= )', info).group(0)
    #else:
    #    tpExam = re.search(r'(?<=Tipo de Exame\n)(.*)(?=)', info).group(0)

    if re.search(r'Admissional', info) is None:
        if re.search(r'Demissional', info) is None:
            if re.search(r'Periódico', info) is None:
                if re.search(r'Mudança de Função', info) is None:
                    tpExam = ""
                else:
                    tpExam = re.search(r'Mudança de Função', info).group(0)
            else:
                tpExam = re.search(r'Periódico', info).group(0)
        else:
            tpExam = re.search(r'Demissional', info).group(0)
    else:
        tpExam = re.search(r'Admissional', info).group(0)

    #exam date
    if re.search(r'(?<=Tipo de Exame Data Ficha\n)(.*)', info) is None:
        if re.search(r'(?<=Data Ficha\n)(.*)', info) is None:
            temp = ""
        else:
            temp = re.search(r'(?<=Data Ficha\n)(.*)', info).group(0)
    else:
        temp = re.search(r'(?<=Tipo de Exame Data Ficha\n)(.*)', info).group(0)
    if re.search(r'[0123][0-9].[0123][0-9].[0-9][0-9][0-9][0-9]', temp) is None:
        date = ""
    else:
        date = re.search(r'[0123][0-9].[0123][0-9].[0-9][0-9][0-9][0-9]', temp).group(0)


    patients.append(Patient.Patient(company, name, tpExam, date))


def substitute(text, old, new):
    return re.sub(old, new, text)
