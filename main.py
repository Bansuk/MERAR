import FileHandling
import TextHandling

source = "L:\OneDrive\Suporte a Projetos\Carreira\Profissional\EMPREHMET\Software Input"
patients = []

filesNames = FileHandling.getfilesnames(source)
FileHandling.convertfiles(filesNames, source)
TextHandling.getfileinfo(filesNames, source, patients)
FileHandling.renamefiles(filesNames, source, patients)
