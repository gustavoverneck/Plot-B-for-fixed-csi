import matplotlib.pyplot as plt



class PlotFields:
    def __init__(self, data, title, outputfile):
        self.data = data
        self.title = title
        self.outputfile = outputfile
        self.plotting()
        self.plotting_zoomed()
    
    def plotting(self):
        for d in data:
            d.plot()
        plt.legend()
        plt.title(self.title)
        plt.xlim(7,13.5)
        plt.ylim(0.5,2.2)
        plt.xlabel(r"Radius $[km]$")
        plt.ylabel(r"Mass $[M_{\odot}]$")
        plt.savefig(self.outputfile, format="svg", dpi=600)
        plt.show()

    def plotting_zoomed(self):
        plt.clf()
        for d in data:
            d.plot()
        plt.xlim(12.5,13.5)
        plt.ylim(1.4,1.8)
        plt.xticks([])
        plt.yticks([])
        plt.savefig("zoomed_" + self.outputfile, format="svg", dpi=600)
        plt.show()


class Data:
    def __init__(self, filename, title):
        self.filename = filename
        self.title = title
        self.read()

    def read(self):
        with open(f"input/tov_{self.filename}.out", "r") as file:
            self.m = []
            self.r = []
            print()
            for line in file:
                self.m.append(float(line.split()[1]))
                self.r.append(float(line.split()[2]))

    def plot(self):
        plt.plot(self.r, self.m, label=f"{self.title}")


data = []
file_path = "input.dat"
if __name__ == "__main__":
    with open(file_path, "r") as file:
        for line in file:
            data.append(Data(line.split(", ")[0], line.split(", ")[1]))
    PlotFields(data, r"GM1 - Mass-Radius diagram for $\xi =10^{-10}$", outputfile="gm1_csi=10_10.svg")
