class Image:
    def __init__(self, resolution, title, extension):
        self.resolution = resolution
        self.title = title
        self.extension = extension

    def resize(self):
        self.resolution = input("Введите разрешение изображения: ")

    def title_upper(self):
        self.title = self.title.upper()


img1 = Image("257x638", "photo1", "png")
print(img1.__dict__)

img1.resize()
img1.title_upper()

print(img1.__dict__)
