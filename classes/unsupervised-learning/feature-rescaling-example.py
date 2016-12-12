from matplotlib import pyplot as plt
from sklearn.preprocessing import MinMaxScaler

data = [[175., 5.9], [115., 5.2]]
chris_data = [[140., 6.1]]

def plot_data():
    for d in data:
        plt.scatter(d[0], d[1], color="red")
        print d[0], d[1]

    plt.scatter(chris_data[0][0], chris_data[0][1], color="blue")

    

plt.title('Before rescaling')
plot_data()
plt.show()
plt.close()

# rescale
scaler = MinMaxScaler()
scaler.fit(data)
data = scaler.transform(data)
chris_data = scaler.transform(chris_data)

plt.title("After rescaling")
plot_data()
plt.show()
plt.close()
