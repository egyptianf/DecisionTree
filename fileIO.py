import csv


class FileIO:


    def read_csv(self, filename):
        data = []
        with open(filename) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                data.append(row)
        return data


    def write_csv(self):
        pass
