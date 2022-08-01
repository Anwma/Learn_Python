class Course:
    def __init__(self, name, price, url):
        self.name = name
        self.price = price
        self.url = url

    def __str__(self):
        return "{}-{}".format(self.name, self.price)


l = []
c1 = Course("django", 200, "")
c2 = Course("scrapy", 100, "")
c3 = Course("tornado", 300, "")
c4 = Course("sanic", 100, "")
l.append(c1)
l.append(c2)
l.append(c3)
l.append(c4)

# data = [1, 3, 5, 2, 6, 8, 9]
# data.sort()
l.sort(key=lambda x: x.price)
for item in l:
    print(item)
# print(data)
print(l)
