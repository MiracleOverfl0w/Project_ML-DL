import sklearn as sk
import matplotlib.pyplot as plt
from sklearn.datasets import load_digits
 

data = load_digits()
print(data.keys())
print(data["target"][6])
plt.imshow(data.images[0])
plt.savefig("mnist.png")