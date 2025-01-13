class GraphicsCard:
    def __init__(self, name:str , price: int, speed: int):
        self.name = name
        self.price = price
        self.speed = speed
        # Also started_mining: float, it is set to 0 after buying graphics card or collecting crypto

# Name, price, bitcoin/second
GTX950 = GraphicsCard("GTX 950", 560_000, 0.3)
GTX960 = GraphicsCard("GTX 960", 600_000, 0.375)
GTX970 = GraphicsCard("GTX 970", 900_000, 0.6)
GTX980 = GraphicsCard("GTX 980", 1_100_000, 0.75)
GTX980_TI = GraphicsCard("GTX 980 Ti", 1_500_000, 0.975)
GTX1050 = GraphicsCard("GTX 1050", 760_000, 0.3)
GTX1050_TI = GraphicsCard("GTX 1050 Ti", 1_000_000, 0.45)
GTX1060 = GraphicsCard("GTX 1060", 1_500_000, 0.75)
GTX1070 = GraphicsCard("GTX 1070", 2_000_000, 1.05)
GTX1070_TI = GraphicsCard("GTX 1070 Ti", 2_700_000, 1.2)
GTX1080 = GraphicsCard("GTX 1080", 2_700_000, 1.275)
GTX1080_TI = GraphicsCard("GTX 1080 Ti", 3_700_000, 1.5)
RTX2060 = GraphicsCard("RTX 2060", 2_900_000, 1.05)
RTX2070 = GraphicsCard("RTX 2070", 3_500_000, 1.2)
RTX2080 = GraphicsCard("RTX 2080", 4_500_000, 1.5)
RTX2080_TI = GraphicsCard("RTX 2080 Ti", 5_900_000, 1.95)
GTX1650 = GraphicsCard("GTX 1650", 1_400_000, 0.45)
GTX1660 = GraphicsCard("GTX 1660", 1_800_000, 0.75)
GTX1660_TI = GraphicsCard("GTX 1660 Ti", 2_000_000, 0.9)
RTX3050 = GraphicsCard("RTX 3050", 3_000_000, 0.9)
RTX3060 = GraphicsCard("RTX 3060", 4_000_000, 1.2)
RTX3060_TI = GraphicsCard("RTX 3060 Ti", 4_800_000, 1.5)
RTX3070 = GraphicsCard("RTX 3070", 5_800_000, 1.8)
RTX3070_TI = GraphicsCard("RTX 3070 Ti", 7_000_000, 1.95)
RTX3080 = GraphicsCard("RTX 3080", 7_800_000, 2.25)
RTX3080_TI = GraphicsCard("RTX 3080 Ti", 9_400_000, 2.55)
RTX3090 = GraphicsCard("RTX 3090", 11_800_000, 2.625)
RTX3090_TI = GraphicsCard("RTX 3090 Ti", 14_000_000, 2.85)
RTX4060 = GraphicsCard("RTX 4060", 5_400_000, 1.5)
RTX4060_TI = GraphicsCard("RTX 4060 Ti", 7_000_000, 1.8)
RTX4070 = GraphicsCard("RTX 4070", 10_000_000, 2.25)
RTX4070_TI = GraphicsCard("RTX 4070 Ti", 14_000_000, 3)
RTX4080 = GraphicsCard("RTX 4080", 18_400_000, 3.6)
RTX4090 = GraphicsCard("RTX 4090", 33_000_000, 4.5)

GPUS = (
    GTX950, GTX960, GTX970, GTX980, GTX980_TI,
    GTX1050, GTX1050_TI, GTX1060, GTX1070, GTX1070_TI, GTX1080, GTX1080_TI,
    RTX2060, RTX2070, RTX2080, RTX2080_TI, GTX1650, GTX1660, GTX1660_TI,
    RTX3050, RTX3060, RTX3060_TI, RTX3070, RTX3070_TI,
    RTX3080, RTX3080_TI, RTX3090, RTX3090_TI,
    RTX4060, RTX4060_TI, RTX4070, RTX4070_TI, RTX4080, RTX4090
)