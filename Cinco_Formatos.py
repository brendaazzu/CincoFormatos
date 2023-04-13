
class Pessoa:
    """Representa uma pessoa.
    
    Atributos:
        _nome (str): O nome da pessoa.
    """
    def __init__(self, nome):
        """Inicializa uma instância de Pessoa com um nome."""
        self._nome = nome
    
    def get_nome(self):
        """Retorna o nome da pessoa."""
        return self._nome
    
    def set_nome(self, nome):
        """Define o nome da pessoa."""
        self._nome = nome

class Medidas(Pessoa):
    """Representa um conjunto de medidas corporais de uma pessoa.
    
    Atributos:
        _busto (float): Medida do busto em centímetros.
        _cintura (float): Medida da cintura em centímetros.
        _quadril (float): Medida do quadril em centímetros.
        _coxas (float): Medida das coxas em centímetros.
    """
    def __init__(self, busto, cintura, quadril, coxas):
        """Inicializa uma nova instância da classe Medidas.

        Args:
            busto (float): valor da medida de busto da pessoa.
            cintura (float): valor da medida de cintura da pessoa.
            quadril (float): valor da medida de quadril da pessoa.
            coxas (float): valor da medida de coxas da pessoa.
        """
        self._busto = busto
        self._cintura = cintura
        self._quadril = quadril
        self._coxas = coxas


    def verificar_formato_corpo(self):
        """Verifica o formato do corpo da pessoa com base nas medidas fornecidas.
        
        Retorna:
            str: Uma string que descreve o formato do corpo, que pode ser "triângulo", "diamante",
            "losango", "ampulheta" ou "retângulo".
        """
        if self._busto < self._quadril and self._cintura < self._quadril and self._busto < self._coxas and self._cintura < self._coxas:
            return "triângulo"
        elif self._busto > self._quadril and self._cintura > self._quadril and self._busto > self._coxas and self._cintura > self._coxas:
            return "diamante"
        elif self._busto < self._cintura and (self._cintura - self._busto) <= 10 and (self._cintura - self._quadril) <= 10 and self._quadril > self._coxas:
            return "losango"
        elif (self._busto - self._cintura) <= 10 and (self._busto - self._quadril) <= 10 and (self._busto - self._coxas) <= 10 and self._cintura < self._quadril and self._cintura < self._coxas:
            return "ampulheta"
        elif (self._busto - self._cintura) <= 10 and (self._busto - self._quadril) <= 10 and (self._busto - self._coxas) <= 10 and (self._cintura - self._quadril) <= 10 and (self._cintura - self._coxas) <= 10 and (self._quadril - self._coxas) <= 10:
            return "retângulo"
        else:
            return "Formato de corpo não identificado. Meça-se novamente e certifique-se de inserir os números corretos!"


    def caracteristicas_formato(self, formato_corpo):
        """Retorna as características do formato de corpo especificado.

        Args:
        formato_corpo (str): O formato do corpo da pessoa, que pode ser "triângulo", "diamante",
        "losango", "ampulheta" ou "retângulo".
        
        Returns:
            str: Uma string que descreve as características do formato de corpo.
        """
        if formato_corpo == "triângulo":
            return "As características do seu formato de corpo triângulo são: medidas de quadril e coxas maiores que as medidas de busto e cintura."
        elif formato_corpo == "diamante":
            return "As características do seu formato de corpo diamante são: medidas de quadril e coxas menores que as medidas de busto e cintura."
        elif formato_corpo == "losango":
            return "As características do seu formato de corpo losango são: medidas de cintura e quadril maiores que as medidas de busto."
        elif formato_corpo == "ampulheta":
            return "As características do seu formato de corpo ampulheta são: medidas proporcionais de busto, quadril e coxas. Medida de cintura menor que as demais."
        elif formato_corpo == "retângulo":
            return "As características do seu formato de corpo retângulo são: medidas proporcionais de busto, quadril e coxas."
        else:
            return "Formatos disponíveis: triângulo, diamante, losango, ampulheta ou retângulo."


"""
Recebe as medidas do usuário e registra no banco de dados.

Solicita o nome do usuário e suas medidas de busto, cintura, quadril e coxas. Em seguida, instancia um objeto Medidas com as medidas fornecidas e verifica o formato do corpo utilizando o método verificar_formato_corpo. Em seguida, utiliza o método caracteristicas_formato para obter uma string descrevendo as características do formato do corpo e imprime o resultado.

Por fim, registra as medidas no banco de dados SQLite 'medidas.db'.

Retorna:
None.
"""
"""
Este script calcula as medidas corporais de uma pessoa e determina seu formato corporal com base nessas medidas. Também salva o nome e as medidas da pessoa em um banco de dados SQLite.

Uso:
    Execute o script e siga as instruções.

Requisitos:
    - Python 3.x
    - módulo sqlite3

Autor:
    [Brenda Azzu]

Última atualização:
    [13/04/2023]

"""

import sqlite3

# Pede o nome do usuário
nome = input("Olá! Qual é o seu nome? ")

# Pede as medidas corporais do usuário
try:
    medida01 = float(input("Insira as suas medidas de busto, em centímetros: "))
    medida02 = float(input("Insira as suas medidas de cintura, em centímetros: "))
    medida03 = float(input("Insira as suas medidas de quadril, em centímetros: "))
    medida04 = float(input("Insira as suas medidas de coxas, em centímetros: "))
except ValueError:
    print("Por favor, insira valores numéricos para as medidas.")
else:
    # Calcula o formato corporal com base nas medidas
    pessoa = Medidas(medida01, medida02, medida03, medida04)
    formato_corpo = pessoa.verificar_formato_corpo()
    caracteristicas_formato_corpo = pessoa.caracteristicas_formato(formato_corpo)

# Mostra o resultado do formato corporal e suas características
    print(f"{nome}, de acordo com as suas medidas, o formato do seu corpo é {formato_corpo}.")
    print(caracteristicas_formato_corpo)

# Salva as medidas e o nome da pessoa no banco de dados SQLite
    conn = sqlite3.connect('medidas.db')
    conn.execute('CREATE TABLE IF NOT EXISTS medidas (id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, busto REAL, cintura REAL, quadril REAL, coxas REAL)')
    conn.execute('INSERT INTO medidas (nome, busto, cintura, quadril, coxas) VALUES (?, ?, ?, ?, ?)', (nome, medida01, medida02, medida03, medida04))
    conn.commit()
    conn.close()

#------------------VERSÃO DO TKINTER----------------------------


import tkinter as tk
from tkinter import messagebox

class App:
    """Janela principal da calculadora de formato de corpo."""

    def __init__(self, master):
        """Inicializa a interface gráfica da calculadora.

        Args:
            master (objeto Tk): Representa a janela principal.
        """
        self.master = master
        master.title("Calculadora de formato de corpo")

        self.label_busto = tk.Label(master, text="Busto (cm)")
        self.label_busto.pack()

        self.entry_busto = tk.Entry(master)
        self.entry_busto.pack()

        self.label_cintura = tk.Label(master, text="Cintura (cm)")
        self.label_cintura.pack()

        self.entry_cintura = tk.Entry(master)
        self.entry_cintura.pack()

        self.label_quadril = tk.Label(master, text="Quadril (cm)")
        self.label_quadril.pack()

        self.entry_quadril = tk.Entry(master)
        self.entry_quadril.pack()

        self.label_coxas = tk.Label(master, text="Coxas (cm)")
        self.label_coxas.pack()

        self.entry_coxas = tk.Entry(master)
        self.entry_coxas.pack()

        self.button_calcular = tk.Button(master, text="Calcular", command=self.calcular_formato_corpo)
        self.button_calcular.pack()

    
    def calcular_formato_corpo(self):
        """
        Calcula o formato do corpo e exibe uma caixa de diálogo com o resultado.

        Obtém as medidas de busto, cintura, quadril e coxas a partir das entradas do usuário.
        Usa as medidas para determinar o formato do corpo do usuário com base nas regras definidas.
        Exibe o resultado em uma caixa de diálogo.

        """
        busto = float(self.entry_busto.get())
        cintura = float(self.entry_cintura.get())
        quadril = float(self.entry_quadril.get())
        coxas = float(self.entry_coxas.get())

        if busto < quadril and cintura < quadril and busto < coxas and cintura < coxas:
            formato = "triângulo"
        elif busto > quadril and cintura > quadril and busto > coxas and cintura > coxas:
            formato = "diamante"
        elif busto < cintura and (cintura - busto) <= 10 and (cintura - quadril) <= 10 and quadril > coxas:
            formato = "losango"
        elif (busto - cintura) <= 10 and (busto - quadril) <= 10 and (busto - coxas) <= 10 and cintura < quadril and cintura < coxas:
            formato = "ampulheta"
        elif (busto - cintura) <= 10 and (busto - quadril) <= 10 and (busto - coxas) <= 10 and (cintura - quadril) <= 10 and (cintura - coxas) <= 10 and (quadril - coxas) <= 10:
            formato = "retângulo"
        else:
            formato = "Formato de corpo não identificado. Meça-se novamente e certifique-se de inserir os números corretos!"

        messagebox.showinfo("Formato de corpo", f"Seu formato de corpo é: {formato}")
        self.master.withdraw()  # oculta a janela
        self.master.destroy()  # fecha completamente a janela

root = tk.Tk()
app = App(root)
root.mainloop()


#------------------------FIM DA VERSÃO DO TKINTER------------------


