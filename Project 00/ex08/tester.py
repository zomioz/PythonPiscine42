from time import sleep
from tqdm import tqdm
from Loading import ft_tqdm

for x in ft_tqdm(range(333)):
    sleep(0.05)  # Ajoutez un petit délai pour voir la progression
print()

for x in tqdm(range(333)):
    sleep(0.05)
print()