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
    "StockAmount": 25,
    "Description": "The Samsung Smart TV QN75Q80BAFXZA brings the cinema experience to your home with its 75-inch 4K UHD display. With vibrant colors and sharp details, it provides an unparalleled viewing experience. Built-in Alexa allows you to control your TV effortlessly, while the wide array of streaming apps gives you access to all your favorite entertainment. It features Wi-Fi and Bluetooth connectivity, ensuring seamless integration with your other devices for a fully immersive smart home experience."
  },
  {
    "Name": "Apple iPad Pro",
    "PID": 2,
    "Image": "products/Ipad.jpg",
    "Model": "MPHH3LL/A",
    "Category": "Tablet",
    "Specifications": "Screen Size: 11 inches\nProcessor: M2 chip\nStorage: 128GB\nConnectivity: Wi-Fi, USB-C",
    "Price": 799.99,
    "StockAmount": 40,
    "Description": "The Apple iPad Pro MPHH3LL/A is designed for users who demand the best in performance and portability. Powered by the M2 chip, this tablet provides exceptional processing speed and power efficiency, making multitasking and high-performance tasks like video editing a breeze. With 128GB of storage and a stunning 11-inch Liquid Retina display, it’s perfect for both work and play. The iPad Pro also features Wi-Fi and USB-C connectivity for faster data transfer and seamless integration with your devices."
  },
  {
    "Name": "Bose Noise Cancelling Headphones",
    "PID": 3,
    "Image": "products/BoseHP.jpg",
    "Model": "700",
    "Category": "Headphones",
    "Specifications": "Type: Over-Ear\nNoise Cancelling: true\nBattery Life: 20 hours\nConnectivity: Bluetooth, Wired",
    "Price": 379.99,
    "StockAmount": 50,
    "Description": "The Bose Noise Cancelling Headphones 700 deliver an unparalleled audio experience with cutting-edge noise-canceling technology. Whether you're traveling or working, these over-ear headphones create an immersive soundscape, allowing you to focus on what matters most. With a long battery life of up to 20 hours and seamless Bluetooth or wired connectivity, they are perfect for all-day use. Additionally, the built-in microphone and touch-sensitive controls provide easy access to calls and volume adjustments."
  },
  {
    "Name": "Dyson Air Purifier",
    "PID": 4,
    "Image": "products/Dyson.webp",
    "Model": "TP07",
    "Category": "Home Appliance",
    "Specifications": "Type: Tower\nCoverage Area: 400 sq. ft.\nAir Quality Monitor: true\nHEPA Filter: true",
    "Price": 549.99,
    "StockAmount": 30,
    "Description": "The Dyson TP07 Air Purifier is a top-of-the-line home appliance designed to improve air quality in medium to large rooms. With its HEPA filter, it captures 99.97% of particles as small as 0.3 microns, ensuring clean and fresh air. The built-in air quality monitor adjusts the purifier's performance to match the current air quality in your room. The tower design ensures that air is purified efficiently, and its smart features include Wi-Fi connectivity for control via your smartphone or voice assistant."
  },
  {
    "Name": "Sony PlayStation 5",
    "PID": 5,
    "Image": "products/PS5.png",
    "Model": "CFI-1200A01",
    "Category": "Gaming Console",
    "Specifications": "Processor: Custom AMD Ryzen Zen 2\nStorage: 825GB SSD\nResolution: 4K HDR\nConnectivity: Wi-Fi, Bluetooth, USB",
    "Price": 499.99,
    "StockAmount": 15,
    "Description": "The Sony PlayStation 5 is a revolutionary gaming console, designed to offer incredible speed, 4K HDR gaming, and the latest in gaming technology. Powered by a custom AMD Ryzen Zen 2 processor and an ultra-fast 825GB SSD, the PS5 delivers instant load times and a smoother, more responsive gaming experience. With Wi-Fi, Bluetooth, and USB connectivity, it supports a wide range of accessories and allows you to connect seamlessly to your favorite gaming network."
  },
  {
    "Name": "Canon EOS R5 Camera",
    "PID": 6,
    "Image": "products/CanonCam.webp",
    "Model": "DS126841",
    "Category": "Camera",
    "Specifications": "Type: Mirrorless\nSensor: 45MP Full-Frame\nVideo: 8K UHD\nConnectivity: Wi-Fi, Bluetooth, USB",
    "Price": 3899.99,
    "StockAmount": 10,
    "Description": "The Canon EOS R5 is a professional-grade mirrorless camera designed for both photographers and videographers. Equipped with a 45MP full-frame sensor, it captures stunning high-resolution images with exceptional detail. The R5 supports 8K UHD video recording, making it perfect for filmmakers and content creators who demand top-tier video quality. Built-in Wi-Fi and Bluetooth make sharing and transferring your media easier than ever."
  },
  {
    "Name": "Fitbit Charge 5",
    "PID": 7,
    "Image": "products/Fitbit.png",
    "Model": "FB421",
    "Category": "Fitness Tracker",
    "Specifications": "Display: AMOLED\nBattery Life: 7 days\nHealth Features: Heart Rate Monitor, Sleep Tracker, ECG App\nConnectivity: Bluetooth, GPS",
    "Price": 149.95,
    "StockAmount": 100,
    "Description": "The Fitbit Charge 5 is a versatile fitness tracker designed to help you stay active and healthy. It features a vibrant AMOLED display, which allows you to track your heart rate, sleep patterns, and even ECG data with ease. With a battery life of up to 7 days, you can rely on it for continuous monitoring. The built-in GPS tracks your outdoor activities, while Bluetooth connectivity enables you to sync your data with the Fitbit app for detailed insights."
  },
  {
    "Name": "Dell UltraSharp Monitor",
    "PID": 8,
    "Image": "products/DellMonitor.jpg",
    "Model": "U3223QE",
    "Category": "Monitor",
    "Specifications": "Screen Size: 32 inches\nResolution: 4K UHD\nPanel Type: IPS\nPorts: USB-C, HDMI, Display Port",
    "Price": 1099.99,
    "StockAmount": 20,
    "Description": "The Dell UltraSharp U3223QE Monitor is a premium display that offers crisp 4K UHD resolution on a large 32-inch screen. Featuring an IPS panel for superior color accuracy, it’s ideal for professionals in fields such as design, video editing, and photography. The monitor’s thin bezels and wide color gamut make it perfect for multi-display setups. It also includes versatile connectivity options such as USB-C, HDMI, and DisplayPort."
  },
  {
    "Name": "Anker PowerCore Portable Charger",
    "PID": 9,
    "Image": "products/AnkerPB.jpg",
    "Model": "26800mAh",
    "Category": "Portable Charger",
    "Specifications": "Capacity: 26800mAh\nOutput Ports: 2 USB-A, 1 USB-C\nRecharge Time: 6 hours\nSafety Features: Temperature Control, Short Circuit Protection",
    "Price": 69.99,
    "StockAmount": 150,
    "Description": "The Anker PowerCore 26800mAh Portable Charger is a powerful and reliable external battery pack. With a massive 26800mAh capacity, it can charge your devices multiple times, making it perfect for long trips or emergency power needs. Equipped with two USB-A ports and one USB-C port, it supports fast charging for multiple devices simultaneously. Safety features like temperature control and short circuit protection ensure your devices stay safe while charging."
  },
  {
    "Name": "iRobot Roomba i7+",
    "PID": 10,
    "Image": "products/Roomba.jpg",
    "Model": "i755020",
    "Category": "Robotic Vacuum",
    "Specifications": "Type: Robotic Vacuum\nBattery Life: 90 minutes\nDust Bin Capacity: 0.5L\nSmart Features: Self-Emptying, Voice Control",
    "Price": 799.99,
    "StockAmount": 35,
    "Description": "The iRobot Roomba i7+ is an advanced robotic vacuum designed to handle cleaning tasks with minimal intervention. Its powerful suction and smart navigation system ensure thorough cleaning of your floors. The self-emptying feature means you never have to worry about emptying the dustbin, while voice control via Alexa or Google Assistant makes operation easier than ever."
  },
  {
    "Name": "LG 65-inch OLED TV",
    "PID": 11,
    "Image": "products/LG_OLED.jpg",
    "Model": "OLED65CXPUA",
    "Category": "Television",
    "Specifications": "Screen Size: 65 inches\nResolution: 4K OLED\nHDR: Dolby Vision\nConnectivity: Wi-Fi, Bluetooth, HDMI",
    "Price": 1999.99,
    "StockAmount": 10,
    "Description": "The LG 65-inch OLED TV OLED65CXPUA delivers stunning visuals with its 4K OLED display. The perfect combination of deep blacks and vibrant colors brings every scene to life. Supporting Dolby Vision HDR for enhanced color and detail, it also features built-in smart features, including access to popular streaming services. With Wi-Fi, Bluetooth, and HDMI ports, this TV fits seamlessly into your home entertainment setup."
  },
  {
    "Name": "GoPro HERO10 Black",
    "PID": 12,
    "Image": "products/GoPro.jpg",
    "Model": "CHDHX-101",
    "Category": "Action Camera",
    "Specifications": "Resolution: 5.3K Video\nLens: Wide-Angle\nWaterproof: Up to 33ft\nConnectivity: Wi-Fi, Bluetooth, USB-C",
    "Price": 399.99,
    "StockAmount": 60,
    "Description": "The GoPro HERO10 Black is a rugged, high-performance action camera designed for adventurers and content creators. It captures 5.3K video for stunning clarity and ultra-smooth footage with its HyperSmooth 4.0 stabilization. Waterproof up to 33 feet, it’s perfect for all kinds of outdoor activities. With Wi-Fi and Bluetooth connectivity, you can easily transfer your footage or control the camera remotely."
  },
  {
    "Name": "Apple MacBook Air",
    "PID": 13,
    "Image": "products/MacBookAir.jpg",
    "Model": "M2 Chip, 13-inch",
    "Category": "Laptop",
    "Specifications": "Processor: Apple M2 Chip\nScreen Size: 13 inches\nStorage: 256GB SSD\nBattery Life: 15 hours",
    "Price": 999.99,
    "StockAmount": 25,
    "Description": "The Apple MacBook Air with the M2 chip offers a lightweight yet powerful laptop experience. Featuring a 13-inch Retina display, 256GB SSD storage, and 15 hours of battery life, it’s designed to keep up with both work and entertainment. The M2 chip delivers impressive performance for tasks like photo editing, programming, and everyday use. With Wi-Fi 6 and Thunderbolt connectivity, it provides seamless integration with other devices."
  }
    ]

for x in p:
  print(x)
  product = Product(Name=x["Name"], Image = x["Image"],
  PID = x["PID"],
  Model = x["Model"],
  Category = x["Category"],
  Specifications = x["Specifications"],
  Description= x["Description"],
  Price = x["Price"],
  StockAmount = x["StockAmount"])
  product.save()
    
