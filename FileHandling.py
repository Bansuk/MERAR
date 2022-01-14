import cv2 as cv
import numpy as np
import os
import TextHandling
import re
from wand.image import Image as Wi
k = 0

def getfilesnames(source):
    return os.listdir(source)


def convertfiles(filesnameslist, source):
    for i in filesnameslist:
        pdf = Wi(filename=source + "\\" + i + '[0]', resolution=300)
        page = Wi(image=pdf.convert("jpeg"))
        page.save(filename=source + "\\" + TextHandling.substitute(i, "pdf", "jpeg"))
        imagetreatment(source + "\\" + TextHandling.substitute(i, "pdf", "jpeg"), source, i)


def renamefiles(filesnameslist, source, patientslist):
    for i, j in zip(filesnameslist, patientslist):
        os.rename(source + "\\" + i, source + "\\" + correctformat(i, j))


def correctformat(patientlist, patient):
    global k
    k += 1;
    hyphen = " - "
    if patient.tpExam == "Demissional":
        tpExam = "DEM"
    elif patient.tpExam == "Admissional":
        tpExam = "ADM"
    elif patient.tpExam == "Mudança de Função":
        tpExam = "MDF"
    elif patient.tpExam == "Retorno ao Trabalho":
        tpExam = "RAT"
    else:
        tpExam = ""
    patient.name = re.sub(r'[\\/\:*"<>\|\.%\$\^&£?]', '', patient.name)
    if patient.name == "RJ":
        return str(k) + ".pdf"
    if patient.name == "" and patient.tpExam == "" and patient.date == "":
        return str(k) + ".pdf"
    elif patient.name == "" and patient.tpExam != "" and patient.date != "":
        return str(k) + hyphen + tpExam + hyphen + TextHandling.substitute(patient.date, "/", "-") + ".pdf"
    return patient.company + hyphen + patient.name.upper() + hyphen + tpExam + hyphen + TextHandling.substitute(patient.date, "/", "-") + ".pdf"


def imagetreatment(imageName, source, i):
    img = cv.imread(imageName)
    save_path = os.path.join(source + "\\" + TextHandling.substitute(i, "pdf", "jpeg"))
    cv.imwrite(save_path, img)

