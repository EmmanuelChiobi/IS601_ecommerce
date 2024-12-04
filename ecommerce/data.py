from products.models import Product
p = [
  {
    "Name": "Samsung Smart TV",
    "Image": "products/SamsungTV.png",
    "Model": "QN75Q80BAFXZA",
    "Category": "Television",
    "Specifications": {
      "ScreenSize": "75 inches",
      "Resolution": "4K UHD",
      "Connectivity": ["Wi-Fi", "Bluetooth", "HDMI"],
      "SmartFeatures": ["Alexa Built-in", "Streaming Apps"]
    },
    "Price": 1499.99,
    "StockAmount": 25
  },
  {
    "Name": "Apple iPad Pro",
    "Image": "products/Ipad.jpg",
    "Model": "MPHH3LL/A",
    "Category": "Tablet",
    "Specifications": {
      "ScreenSize": "11 inches",
      "Processor": "M2 chip",
      "Storage": "128GB",
      "Connectivity": ["Wi-Fi", "USB-C"]
    },
    "Price": 799.99,
    "StockAmount": 40
  },
  {
    "Name": "Bose Noise Cancelling Headphones",
    "Image":"products/BoseHP.jpg",
    "Model": "700",
    "Category": "Headphones",
    "Specifications": {
      "Type": "Over-Ear",
      "NoiseCancelling": True,
      "BatteryLife": "20 hours",
      "Connectivity": ["Bluetooth", "Wired"]
    },
    "Price": 379.99,
    "StockAmount": 50
  },
  {
    "Name": "Dyson Air Purifier",
    "Image": "products/Dyson.webp",
    "Model": "TP07",
    "Category": "Home Appliance",
    "Specifications": {
      "Type": "Tower",
      "CoverageArea": "400 sq. ft.",
      "AirQualityMonitor": True,
      "HEPAFilter": True
    },
    "Price": 549.99,
    "StockAmount": 30
  },
  {
    "Name": "Sony PlayStation 5",
    "Image": "products/PS5.png",
    "Model": "CFI-1200A01",
    "Category": "Gaming Console",
    "Specifications": {
      "Processor": "Custom AMD Ryzen Zen 2",
      "Storage": "825GB SSD",
      "Resolution": "4K HDR",
      "Connectivity": ["Wi-Fi", "Bluetooth", "USB"]
    },
    "Price": 499.99,
    "StockAmount": 15
  },
  {
    "Name": "Canon EOS R5 Camera",
    "Image": "products/CanonCam.webp",
    "Model": "DS126841",
    "Category": "Camera",
    "Specifications": {
      "Type": "Mirrorless",
      "Sensor": "45MP Full-Frame",
      "Video": "8K UHD",
      "Connectivity": ["Wi-Fi", "Bluetooth", "USB"]
    },
    "Price": 3899.99,
    "StockAmount": 10
  },
  {
    "Name": "Fitbit Charge 5",
    "Image": "products/Fitbit.png",
    "Model": "FB421",
    "Category": "Fitness Tracker",
    "Specifications": {
      "Display": "AMOLED",
      "BatteryLife": "7 days",
      "HealthFeatures": ["Heart Rate Monitor", "Sleep Tracker", "ECG App"],
      "Connectivity": ["Bluetooth", "GPS"]
    },
    "Price": 149.95,
    "StockAmount": 100
  },
  {
    "Name": "Dell UltraSharp Monitor",
    "Image": "products/DellMonitor.jpg",
    "Model": "U3223QE",
    "Category": "Monitor",
    "Specifications": {
      "ScreenSize": "32 inches",
      "Resolution": "4K UHD",
      "PanelType": "IPS",
      "Ports": ["USB-C", "HDMI", "DisplayPort"]
    },
    "Price": 1099.99,
    "StockAmount": 20
  },
  {
    "Name": "Anker PowerCore Portable Charger",
    "Image": "products/AnkerPB.jpg",
    "Model": "26800mAh",
    "Category": "Portable Charger",
    "Specifications": {
      "Capacity": "26800mAh",
      "OutputPorts": ["2 USB-A", "1 USB-C"],
      "RechargeTime": "6 hours",
      "SafetyFeatures": ["Temperature Control", "Short Circuit Protection"]
    },
    "Price": 69.99,
    "StockAmount": 150
  },
  {
    "Name": "iRobot Roomba i7+",
    "Image": "products/Roomba.jpg",
    "Model": "i755020",
    "Category": "Robotic Vacuum",
    "Specifications": {
      "Type": "Robotic Vacuum",
      "BatteryLife": "90 minutes",
      "DustBinCapacity": "0.5L",
      "SmartFeatures": ["Self-Emptying", "Voice Control"]
    },
    "Price": 799.99,
    "StockAmount": 35
  }
 
    ]

for x in p:
    product = Product(Name=x["Name"], Image = x["Image"],
    Model = x["Model"],
    Category = x["Category"],
    Specifications = x["Specifications"],
    Price = x["Price"],
    StockAmount = x["StockAmount"])
    product.save()