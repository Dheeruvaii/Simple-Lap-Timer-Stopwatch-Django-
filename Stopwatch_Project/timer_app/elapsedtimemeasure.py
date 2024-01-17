# https://www.programiz.com/python-programming/examples/elapsed-time
from timeit import default_timer as timer

start=timer()
print(23*2.3)
end=timer()
print(start-end)