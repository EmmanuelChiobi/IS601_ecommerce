from products.models import Product

p = [
  {
    "Name": "Samsung Smart TV",
    "PID": 1,
    "Image": "products/SamsungTV.png",
    "Model": "QN75Q80BAFXZA",
    "Category": "Television",
    "Specifications": "Screen Size: 75 inches\nResolution: 4K UHD\nConnectivity: Wi-Fi, Bluetooth, HDMI\nSmart Features: Alexa Built-in, Streaming Apps",
    "Price": 1499.99,
    "StockAmount": 25
  },
  {
    "Name": "Apple iPad Pro",
    "PID": 2,
    "Image": "products/Ipad.jpg",
    "Model": "MPHH3LL/A",
    "Category": "Tablet",
    "Specifications": "Screen Size: 11 inches\nProcessor: M2 chip\nStorage: 128GB\nConnectivity: Wi-Fi, USB-C",
    "Price": 799.99,
    "StockAmount": 40
  },
  {
    "Name": "Bose Noise Cancelling Headphones",
    "PID": 3,
    "Image":"products/BoseHP.jpg",
    "Model": "700",
    "Category": "Headphones",
    "Specifications": "Type: Over-Ear\nNoise Cancelling: true\nBattery Life: 20 hours\nConnectivity: Bluetooth, Wired",
    "Price": 379.99,
    "StockAmount": 50
  },
  {
    "Name": "Dyson Air Purifier",
    "PID": 4,
    "Image": "products/Dyson.webp",
    "Model": "TP07",
    "Category": "Home Appliance",
    "Specifications": "Type: Tower\nCoverage Area: 400 sq. ft.\nAir Quality Monitor: true\nHEPAFilter: true",
    "Price": 549.99,
    "StockAmount": 30
  },
  {
    "Name": "Sony PlayStation 5",
    "PID": 5,
    "Image": "products/PS5.png",
    "Model": "CFI-1200A01",
    "Category": "Gaming Console",
    "Specifications": "Processor: Custom AMD Ryzen Zen 2\nStorage: 825GB SSD\nResolution: 4K HDR\nConnectivity: Wi-Fi, Bluetooth, USB",
    "Price": 499.99,
    "StockAmount": 15
  },
  {
    "Name": "Canon EOS R5 Camera",
    "PID": 6,
    "Image": "products/CanonCam.webp",
    "Model": "DS126841",
    "Category": "Camera",
    "Specifications": "Type: Mirrorless\nSensor: 45MP Full-Frame\nVideo: 8K UHD\nConnectivity: Wi-Fi, Bluetooth, USB",
    "Price": 3899.99,
    "StockAmount": 10
  },
  {
    "Name": "Fitbit Charge 5",
    "PID": 7,
    "Image": "products/Fitbit.png",
    "Model": "FB421",
    "Category": "Fitness Tracker",
    "Specifications": "Display: AMOLED\nBattery Life: 7 days\nHealth Features: Heart Rate Monitor, Sleep Tracker, ECG App\nConnectivity: Bluetooth, GPS",
    "Price": 149.95,
    "StockAmount": 100
  },
  {
    "Name": "Dell UltraSharp Monitor",
    "PID": 8,
    "Image": "products/DellMonitor.jpg",
    "Model": "U3223QE",
    "Category": "Monitor",
    "Specifications": "Screen Size: 32 inches\nResolution: 4K UHD\nPanel Type: IPS\nPorts: USB-C, HDMI, Display Port",
    "Price": 1099.99,
    "StockAmount": 20
  },
  {
    "Name": "Anker PowerCore Portable Charger",
    "PID": 9,
    "Image": "products/AnkerPB.jpg",
    "Model": "26800mAh",
    "Category": "Portable Charger",
    "Specifications":
      """Capacity: 26800mAh\nOutput Ports: 2 USB-A, 1 USB-C\nRecharge Time: 6 hours\nSafety Features: Temperature Control, Short Circuit Protection
    """,
    "Price": 69.99,
    "StockAmount": 150
  },
  {
    "Name": "iRobot Roomba i7+",
    "PID": 10,
    "Image": "products/Roomba.jpg",
    "Model": "i755020",
    "Category": "Robotic Vacuum",
    "Specifications": 
      """Type: Robotic Vacuum\nBattery Life: 90 minutes\nDust Bin Capacity: 0.5L\nSmart Features: Self-Emptying, Voice Control""",
    "Price": 799.99,
    "StockAmount": 35
  },
    ]

for x in p:
  print(x)
  product = Product(Name=x["Name"], Image = x["Image"],
  PID = x["PID"],
  Model = x["Model"],
  Category = x["Category"],
  Specifications = x["Specifications"],
  Price = x["Price"],
  StockAmount = x["StockAmount"])
  product.save()
    
