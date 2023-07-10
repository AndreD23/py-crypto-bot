class Carro:
    def __init__(self, cor, marca, modelo):
        self.cor = cor
        self.marca = marca
        self.modelo = modelo

    def get_values(self):
        print(f"Cor: {self.cor} | Marca: {self.marca} | Modelo: {self.modelo}")


    def drive(self):
        print('Estou dirigindo')

    def stop(self):
        print('Freei')