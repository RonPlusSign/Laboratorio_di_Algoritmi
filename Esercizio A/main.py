import timeit
import numpy as np
import os, sys
from numpy import ndarray
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
from copy import deepcopy

from queue import Queue
from linked_list import LinkedListQueue
from sorted_linked_list import SortedLinkedListQueue
from max_heap import MaxHeap

n = 1002
tests_per_iteration = 100
step = 50
sys.setrecursionlimit(10000) 


def insert_values(queue: Queue, values: list):
    for v in values:
        queue.insert(v)


def measure_insertion(queue: Queue, values: list | ndarray):
    """ Ritorna il tempo di esecuzione medio (in millisecondi) dell'inserimento dei valori nella coda, eseguendo l'inserimento `test_per_iteration` volte """
    times = []
    for _ in range(tests_per_iteration):
        # Uso la deepcopy altrimenti con insert_values() ripetuto si inseriscono i valori più volte!
        copy_queue = deepcopy(queue)
        # Misuro il tempo di esecuzione di una singola iterazione
        times.append(timeit.timeit(stmt=lambda: insert_values(copy_queue, values), number=1))
    return np.mean(times) * 1000


def measure_find_max(queue: Queue):
    """ Ritorna il tempo di esecuzione medio (in millisecondi) della ricerca del valore massimo nella coda, eseguendo la ricerca `test_per_iteration` volte """
    return timeit.timeit(stmt=lambda: queue.find_max(), number=tests_per_iteration) / tests_per_iteration * 1000


def measure_extract_max(queue: Queue):
    """ Ritorna il tempo di esecuzione medio (in millisecondi) dell'estrazione del valore massimo nella coda, eseguendo l'estrazione `test_per_iteration` volte """
    times = []
    for _ in range(tests_per_iteration):
        # Uso la deepcopy altrimenti con extract_max() ripetuto si estraggono vari valori!
        copy_queue = deepcopy(queue)
        # Misuro il tempo di esecuzione di una singola iterazione
        times.append(timeit.timeit(stmt=lambda: copy_queue.extract_max(), number=1))
    return np.mean(times) * 1000


def draw_approximation(x: list, y: list, degree: int, label: str) -> None:
    """ Disegna l'approssimazione polinomiale di grado `degree` dei punti """
    coefficients = np.polyfit(x, y, degree)
    new_x = np.linspace(1, n, n)
    new_y = np.polyval(coefficients, new_x)
    plt.plot(new_x, new_y, '--', label=label)


def draw_plots(data: list[list[any]], titles: list[str], plot_title: str = None, smooth: bool = False) -> None:
    for index, data_list in enumerate(data):
        x = np.linspace(1, n, len(data_list))

        if smooth:  # Crea la funzione d'interpolazione & genera i valori della curva smooth
            x_smooth = np.linspace(1, n, n)
            data_list = interp1d(x, data_list, kind='cubic')(x_smooth)
            x = x_smooth

        plt.plot(x, data_list, label=titles[index])
        # Aggiungi l'approssimazione polinomiale
        # draw_approximation(x, data_list, 2, label=(titles[index] + " approximation"))

    plt.title(plot_title)
    plt.xlabel('Dimensione della lista (n)')
    plt.ylabel('Tempo di esecuzione (in ms)')
    plt.legend()

    plt.savefig(f"plots/{plot_title}.png")  # Salva il grafico come immagine
    plt.clf()  # Pulisci la figura per il prossimo grafico


def draw_table_data(columns: list, headers: tuple, title: str):
    fig, ax = plt.subplots(figsize=(6, 8))
    # plt.title(title)

    data = np.stack(tuple(columns), axis=1)  # Unisci liste come colonne

    # Stile della tabella
    ax.axis('off')
    table = ax.table(cellText=data, colLabels=headers, loc='center', cellLoc='center')
    table.auto_set_column_width(col=list(range(len(columns))))
    table.scale(1, 1.5)

    for cell in table._cells:
        if table[cell].get_text().get_text() in headers:
            table[cell].set_facecolor("#c1d6ff")
            table[cell].set_text_props(weight='bold')
        elif cell[0] % 2 == 0:  # Colora righe pari
            table[cell].set_facecolor("#deebff")

    fig.savefig(f"tables/{title}.png", dpi=300, bbox_inches='tight')  # Salva la tabella come immagine
    plt.clf()  # Pulisci la figura per il prossimo grafico


if __name__ == '__main__':

    llq_times_insert = []
    sllq_times_insert = []
    mh_times_insert = []

    llq_times_find = []
    sllq_times_find = []
    mh_times_find = []

    llq_times_extract = []
    sllq_times_extract = []
    mh_times_extract = []

    print("Esecuzione dei test...")
    for index in range(1, n, step):
        
        print(f"Test {index}/{n} (" + str(round(index / n * 100, 2)) + "%)")
        
        llq = LinkedListQueue()
        sllq = SortedLinkedListQueue()
        mh = MaxHeap()
        values_to_insert = np.random.randint(1, 100, size=index)  # Genera un array di valori random tra 1 e 99 (estremi inclusi)

        # Test inserimento
        llq_times_insert.append(measure_insertion(llq, values_to_insert))  # Test LinkedListQueue insert
        sllq_times_insert.append(measure_insertion(sllq, values_to_insert))  # Test SortedLinkedListQueue insert
        mh_times_insert.append(measure_insertion(mh, values_to_insert))  # Test MaxHeap insert
        
        # Aggiungi effettivamente i valori alla coda (measure_insertion() lavora su una copia delle code)
        insert_values(llq, values_to_insert)
        insert_values(sllq, values_to_insert)
        insert_values(mh, values_to_insert)

        # Test ricerca del massimo
        llq_times_find.append(measure_find_max(llq))  # Test LinkedListQueue find
        sllq_times_find.append(measure_find_max(sllq))  # Test SortedLinkedListQueue find
        mh_times_find.append(measure_find_max(mh))  # Test MaxHeap find

        # Test estrazione del massimo
        llq_times_extract.append(measure_extract_max(llq))  # Test LinkedListQueue extract
        sllq_times_extract.append(measure_extract_max(sllq))  # Test SortedLinkedListQueue extract
        mh_times_extract.append(measure_extract_max(mh))  # Test MaxHeap extract

    print("Generazione dei grafici...")
    if not os.path.exists("plots"):  # Crea la cartella plots se non esiste
        os.makedirs("plots")

    draw_plots([llq_times_insert, sllq_times_insert, mh_times_insert],
               ["Lista concatenata", "Lista concatenata ordinata", "Max Heap"],
               "Inserimento", smooth=True)

    draw_plots([llq_times_find, sllq_times_find, mh_times_find],
               ["Lista concatenata", "Lista concatenata ordinata", "Max Heap"],
               "Ricerca del massimo", smooth=True)

    draw_plots([llq_times_extract, sllq_times_extract, mh_times_extract],
               ["Lista concatenata", "Lista concatenata ordinata", "Max Heap"],
               "Estrazione del massimo", smooth=True)

    print("Generazione delle tabelle...")
    if not os.path.exists("tables"):  # Crea la cartella tables se non esiste
        os.makedirs("tables")

    draw_table_data([[i for i in range(1, n, step)],
                     ["{:.3e}".format(val) for val in llq_times_insert],
                     ["{:.3e}".format(val) for val in sllq_times_insert],
                     ["{:.3e}".format(val) for val in mh_times_insert]],
                    ("N° elementi", "Lista concatenata", "Lista concatenata ordinata", "Max Heap"),
                    "Tempi inserimento")

    draw_table_data([[i for i in range(1, n, step)],
                     ["{:.3e}".format(val) for val in llq_times_find],
                     ["{:.3e}".format(val) for val in sllq_times_find],
                     ["{:.3e}".format(val) for val in mh_times_find]],
                    ("N° elementi", "Lista concatenata", "Lista concatenata ordinata", "Max Heap"),
                    "Tempi ricerca del del massimo")

    draw_table_data([[i for i in range(1, n, step)],
                     ["{:.3e}".format(val) for val in llq_times_extract],
                     ["{:.3e}".format(val) for val in sllq_times_extract],
                     ["{:.3e}".format(val) for val in mh_times_extract]],
                    ("N° elementi", "Lista concatenata", "Lista concatenata ordinata", "Max Heap"),
                    "Tempi estrazione del massimo")

    print("Fine!")
