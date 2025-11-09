from time import sleep
from tqdm import tqdm
from Loading import ft_tqdm

for x in ft_tqdm(range(167)):
    sleep(0.05)
print()

for x in tqdm(range(167)):
    sleep(0.05)
print()
