import pandas as pd


class GetCSVInfo:
    def __init__(self, file_name: str):
        self.file_name = file_name
        self.data_frame = pd.read_csv(self.file_name)

    def get_total_sales(self):
        self.data_frame['preco'] = self.data_frame['preco'].str.replace('$', '')
        self.data_frame['preco'] = self.data_frame['preco'].str.replace(',', '')
        self.data_frame['total'] = self.data_frame['quantidade'] * self.data_frame['preco'].astype(float)

        return self.data_frame['total'].sum()

    def get_best_seller(self):
        pass

    def get_best_selling_product(self):
        pass

    def get_average_sells(self):
        pass
