import multiprocessing
import time

start = time.perf_counter()


def do(seconds):
    print('Starting')
    time.sleep(seconds)
    print('Done')

processes = []
for _ in range(10):
    p = multiprocessing.Process(target=do, args=[2])
    p.start()
    processes.append(p)

for process in processes:
    process.join()

# p1 = multiprocessing.Process(target=do)
# p2 = multiprocessing.Process(target=do)
#
# p1.start()
# p2.start()
#
# p1.join()
# p2.join()

end = time.perf_counter()

print('Total time: ', end - start)

import concurrent.futures
import time

start = time.perf_counter()

def do(seconds):
    print('Starting')
    time.sleep(seconds)
    return 'done sleep'

with concurrent.futures.ProcessPoolExecutor() as executor:
    # f1 = executor.submit(do, 1)
    # f2 = executor.submit(do, 1)
    results = [executor.submit(do, 1) for _ in range(50)]
    for f in concurrent.futures.as_completed(results):
        print(f.result())



end = time.perf_counter()
print(f'time to run: {end-start}')
