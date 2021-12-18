import csv
from classmovie import Movie
from classlink import Link
from classrating import Rating
from classtag import Tag

def metoda_czytaj_film(path) -> str:
    file = open(path, encoding='utf-8')
    csvreader = csv.reader(file)

    header = next(csvreader)
    print(header)
    listafilmow = []

    filereader = csv.reader(file, delimiter=',')
    for row in filereader:
        print(', '.join(row))
        film = Movie(int(row[0]), row[1], row[2])
        listafilmow.append(film.__dict__)
    return listafilmow


def metoda_czytaj_link(path) -> str:
    file = open(path, encoding='utf-8')
    csvreader = csv.reader(file)

    header = next(csvreader)
    print(header)
    listalinkow = []

    filereader = csv.reader(file, delimiter=',')
    for row in filereader:
        print(', '.join(row))
        link = Link(int(row[0]), row[1], row[2])
        listalinkow.append(link.__dict__)
    return listalinkow


def metoda_czytaj_ocene(path) -> str:
    file = open(path, encoding='utf-8')
    csvreader = csv.reader(file)

    header = next(csvreader)
    print(header)
    listaocen = []

    filereader = csv.reader(file, delimiter=',')
    for row in filereader:
        print(', '.join(row))
        ocena = Rating(int(row[0]), row[1], row[2], row[3])
        listaocen.append(ocena.__dict__)
    return listaocen


def metoda_czytaj_tag(path) -> str:
    file = open(path, encoding='utf-8')
    csvreader = csv.reader(file)

    header = next(csvreader)
    print(header)
    listatagow = []

    filereader = csv.reader(file, delimiter=',')
    for row in filereader:
        print(', '.join(row))
        tag = Tag(int(row[0]), row[1], row[2], row[3])
        listatagow.append(tag.__dict__)
    return listatagow


objects =[]
def opens(files, classRef) -> str:
    with open(files,'r', encoding='utf-8') as f:
        csvreader = csv.reader(f, delimiter=',')
        headers = next(csvreader)
        print(headers)
        for line in csvreader:
            if len(line) == len(headers):
                classObj = {}
                for i, header in enumerate(headers):
                    classObj[header] = line[i]

                object = classRef(**classObj)
                objects.append(object.__dict__)
        return objects
