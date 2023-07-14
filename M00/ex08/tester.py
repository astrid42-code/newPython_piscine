from time import sleep
from tqdm import tqdm
from Loading import ft_tqdm

# def main():
#     listy = range(420)
#     ret = 0
#     for elem in ft_progress(listy):
#         ret += (elem + 3) % 5
#         time.sleep(0.01)
#     print()
#     print(ret)

# if __name__ == "__main__":
#     main()

for elem in ft_tqdm(range(333)):
    sleep(0.005)
print()
for elem in tqdm(range(333)):
    sleep(0.005)
print()
