import csv
from faker import Faker


class CreateCsvFile:
    def __init__(self, file_name: str, total_rows: int = 10):
        self.file_name = f'{file_name}.csv'
        self.fields = ['data', 'produto', 'preco', 'quantidade', 'vendedor']
        self.total_rows = total_rows
        self.fake = Faker()

    def execute(self):
        with open(self.file_name, mode='w', newline='') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=self.fields)
            writer.writeheader()

            for i in range(self.total_rows):
                date = self.fake.date()
                product = self.fake.word() + " " + self.fake.color_name()
                price = self.fake.pricetag()
                quantity = self.fake.random_int(min=2, max=20, step=1)
                seller = self.fake.name()

                writer.writerow({
                    'data': date,
                    'produto': product,
                    'preco': price,
                    'quantidade': quantity,
                    'vendedor': seller
                })
