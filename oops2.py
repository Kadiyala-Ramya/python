#create a class about laptop with 10 instances
class Laptop():
    def __init__(self,type,size,ram,rom,os,processor):
        self.type=type
        self.size=size
        self.ram=ram
        self.rom=rom
        self.os=os
        self.processor=processor
    def about(self):
        return f"This is {self.type} which has properties: Screen Size - {self.size}, RAM - {self.ram}, ROM - {self.rom}, OS - {self.os}, and Processor - {self.processor}"
    
model1=Laptop("Apple MacBook Air (M2, 2023)","13.6 inches","8 GB ","256 GB SSD ","macOS Ventura","Apple M2 chip")
print(model1.about())

model2=Laptop("Dell XPS 13 Plus (2023)","13.4 inches","16 GB","512 GB SSD ","Windows 11","Intel Core i7-1360P")
print(model2.about())

model3=Laptop("HP Spectre x360 14","13.5 inches","16 GB","512 GB ","Windows 11","Intel Core i7-1355U")
print(model3.about())

model4=Laptop("Lenovo ThinkPad X1 Carbon Gen 11","14 inches","16 GB LPDDR5","512 GB SSD","Windows 11 Pro","Intel Core i7-1365U vPro")
print(model4.about())

model5=Laptop("ASUS ROG Zephyrus G14 (Gaming)","14 inches","16 GB DDR5","1 TB SSD","Windows 11","AMD Ryzen 9 7940HS + NVIDIA RTX 4060")
print(model5.about())

model6=Laptop("Acer Swift Go 14 (2024)","14 inches","16 GB LPDDR5","512 GB SSD","Windows 11","Intel Core Ultra 7 155H")
print(model6.about())

model7=Laptop("Microsoft Surface Laptop 5","13.5 or 15 inches","8 GB or 16 GB","256 GB to 1 TB SSD","Windows 11","Intel Core i5 or i7 (12th Gen)")
print(model7.about())

model8=Laptop("Samsung Galaxy Book3 Pro","14 or 16 inches AMOLED","16 GB","512 GB SSD","Windows 11","Intel Core i7-1360P")
print(model8.about())

model9=Laptop("LG Gram 17 (2023)","17 inches (WQXGA)","16 GB LPDDR5","1 TB SSD","Windows 11","Intel Core i7-1360P")
print(model9.about())

model10=Laptop("MSI Creator Z16","16 inches QHD+ Touch","32 GB DDR5","1 TB SSD","Windows 11","Intel Core i9-13900H + NVIDIA RTX 4070")
print(model10.about())