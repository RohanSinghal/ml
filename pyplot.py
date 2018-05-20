import matplotlib.pyplot as plt

x=[4,6]
x1=[3,0]
y=[2,3]
y1=[7,2]
plt.title("jupy")
plt.xlabel("time")
plt.ylabel("distance")
#plt.scatter(x,y,label="bombs")#plot,pie
#plt.scatter(x1,y1)#plot,pie
plt.bar(x,y,label="money")
plt.bar(x1,y1,label="dhokha")
plt.grid(True,color="cyan")
plt.legend()
plt.show()
