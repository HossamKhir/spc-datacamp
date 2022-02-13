#! /usr/bin/python3
"""
"""
import matplotlib.pyplot as plt
import seaborn as sns

nan = float("nan")

gdp = [
    700.0,
    4500.0,
    6000.0,
    8000.0,
    19000.0,
    1900.0,
    8600.0,
    11000.0,
    11200.0,
    3500.0,
    28000.0,
    29000.0,
    30000.0,
    3400.0,
    16700.0,
    16900.0,
    1900.0,
    15700.0,
    6100.0,
    29100.0,
    4900.0,
    1100.0,
    36000.0,
    1300.0,
    2400.0,
    6100.0,
    9000.0,
    7600.0,
    16000.0,
    18600.0,
    7600.0,
    1100.0,
    1800.0,
    600.0,
    1900.0,
    1800.0,
    29800.0,
    1400.0,
    35000.0,
    1100.0,
    1200.0,
    9900.0,
    5000.0,
    6300.0,
    700.0,
    700.0,
    700.0,
    5000.0,
    9100.0,
    1400.0,
    10600.0,
    2900.0,
    19200.0,
    15700.0,
    31100.0,
    1300.0,
    5400.0,
    6000.0,
    500.0,
    3300.0,
    4000.0,
    4800.0,
    2700.0,
    700.0,
    12300.0,
    700.0,
    22000.0,
    5800.0,
    27400.0,
    27600.0,
    8300.0,
    17500.0,
    5500.0,
    1700.0,
    600.0,
    2500.0,
    27600.0,
    2200.0,
    17500.0,
    20000.0,
    20000.0,
    5000.0,
    8000.0,
    21000.0,
    4100.0,
    20000.0,
    2100.0,
    800.0,
    4000.0,
    1600.0,
    2600.0,
    28800.0,
    13900.0,
    30900.0,
    2900.0,
    3200.0,
    7000.0,
    1500.0,
    29600.0,
    21000.0,
    19800.0,
    26700.0,
    3900.0,
    28200.0,
    24800.0,
    4300.0,
    6300.0,
    1000.0,
    800.0,
    1300.0,
    17800.0,
    19000.0,
    1600.0,
    1700.0,
    10200.0,
    4800.0,
    3000.0,
    1000.0,
    6400.0,
    25000.0,
    11400.0,
    55100.0,
    19400.0,
    6700.0,
    800.0,
    600.0,
    9000.0,
    3900.0,
    900.0,
    17700.0,
    1600.0,
    14400.0,
    1800.0,
    11400.0,
    2600.0,
    9000.0,
    2000.0,
    1800.0,
    27000.0,
    1800.0,
    3400.0,
    4000.0,
    1200.0,
    7200.0,
    5000.0,
    1400.0,
    28600.0,
    11400.0,
    15000.0,
    21600.0,
    2300.0,
    800.0,
    900.0,
    12500.0,
    37800.0,
    13100.0,
    2100.0,
    9000.0,
    6300.0,
    2200.0,
    4700.0,
    5100.0,
    4600.0,
    11100.0,
    18000.0,
    16800.0,
    21500.0,
    5800.0,
    7000.0,
    8900.0,
    1300.0,
    2500.0,
    8800.0,
    5400.0,
    6900.0,
    2900.0,
    5600.0,
    34600.0,
    1200.0,
    11800.0,
    1600.0,
    2200.0,
    7800.0,
    500.0,
    23700.0,
    13300.0,
    19000.0,
    1700.0,
    500.0,
    10700.0,
    22000.0,
    3700.0,
    1900.0,
    4000.0,
    4900.0,
    26800.0,
    32700.0,
    3300.0,
    23400.0,
    1000.0,
    600.0,
    7400.0,
    1500.0,
    2200.0,
    9500.0,
    6900.0,
    6700.0,
    5800.0,
    9600.0,
    1100.0,
    1400.0,
    5400.0,
    23200.0,
    27700.0,
    37800.0,
    12800.0,
    1700.0,
    2900.0,
    4800.0,
    2500.0,
    17200.0,
    3700.0,
    800.0,
    nan,
    800.0,
    800.0,
    1900.0,
]

phones = [
    3.2,
    71.2,
    78.1,
    259.5,
    497.2,
    7.8,
    460.0,
    549.9,
    220.4,
    195.7,
    516.1,
    565.5,
    452.2,
    137.1,
    460.6,
    281.3,
    7.3,
    481.9,
    319.1,
    462.6,
    115.7,
    9.7,
    851.4,
    14.3,
    71.9,
    215.4,
    80.5,
    225.3,
    506.5,
    237.2,
    336.3,
    7.0,
    10.1,
    3.4,
    2.6,
    5.7,
    552.2,
    169.6,
    836.3,
    2.3,
    1.3,
    213.0,
    266.7,
    176.2,
    24.5,
    0.2,
    3.7,
    289.9,
    340.7,
    14.6,
    420.4,
    74.7,
    nan,
    314.3,
    614.6,
    22.8,
    304.8,
    97.4,
    nan,
    125.6,
    131.8,
    142.4,
    18.5,
    7.9,
    333.8,
    8.2,
    503.8,
    112.6,
    405.3,
    586.4,
    255.6,
    194.5,
    27.4,
    26.8,
    244.3,
    146.6,
    667.9,
    14.4,
    877.7,
    589.7,
    448.9,
    364.5,
    463.8,
    492.0,
    92.1,
    842.4,
    2.7,
    7.4,
    143.5,
    16.9,
    67.5,
    546.7,
    336.2,
    647.7,
    45.4,
    52.0,
    276.4,
    38.6,
    500.5,
    676.0,
    462.3,
    430.9,
    124.0,
    461.2,
    811.3,
    104.5,
    164.1,
    8.1,
    42.7,
    42.4,
    486.1,
    211.0,
    84.0,
    14.1,
    321.4,
    255.6,
    23.7,
    2.3,
    127.1,
    585.5,
    223.4,
    515.4,
    384.9,
    260.0,
    3.6,
    7.9,
    179.0,
    90.0,
    6.4,
    505.0,
    91.2,
    394.4,
    12.9,
    289.3,
    49.7,
    181.6,
    114.8,
    208.1,
    1035.6,
    55.1,
    nan,
    40.4,
    3.5,
    62.6,
    143.0,
    15.9,
    460.8,
    365.3,
    252.2,
    441.7,
    39.7,
    1.9,
    9.3,
    254.7,
    461.7,
    85.5,
    31.8,
    325.6,
    137.9,
    10.9,
    49.2,
    79.5,
    38.4,
    306.3,
    399.2,
    283.1,
    232.0,
    380.9,
    196.9,
    280.6,
    2.7,
    293.3,
    638.9,
    303.3,
    683.2,
    190.9,
    75.2,
    704.3,
    36.2,
    140.6,
    22.2,
    285.8,
    262.4,
    4.0,
    411.4,
    220.1,
    406.1,
    13.4,
    11.3,
    107.0,
    453.5,
    61.5,
    16.3,
    184.7,
    30.8,
    715.0,
    680.9,
    153.8,
    591.0,
    33.5,
    4.0,
    108.9,
    10.6,
    97.7,
    303.5,
    123.6,
    269.5,
    74.6,
    269.5,
    59.3,
    3.6,
    259.9,
    475.3,
    543.5,
    898.0,
    291.4,
    62.9,
    32.6,
    140.1,
    187.7,
    652.8,
    118.6,
    145.2,
    nan,
    37.2,
    8.2,
    26.8,
]
percent_literate = [
    36.0,
    86.5,
    70.0,
    97.0,
    100.0,
    42.0,
    95.0,
    89.0,
    97.1,
    98.6,
    97.0,
    100.0,
    98.0,
    97.0,
    95.6,
    89.1,
    43.1,
    97.4,
    99.6,
    98.0,
    94.1,
    40.9,
    98.0,
    42.2,
    87.2,
    nan,
    79.8,
    86.4,
    97.8,
    93.9,
    98.6,
    26.6,
    85.3,
    51.6,
    69.4,
    79.0,
    97.0,
    76.6,
    98.0,
    51.0,
    47.5,
    96.2,
    90.9,
    92.5,
    56.5,
    65.5,
    83.8,
    95.0,
    96.0,
    50.9,
    98.5,
    97.0,
    97.6,
    99.9,
    100.0,
    67.9,
    94.0,
    84.7,
    58.6,
    92.5,
    57.7,
    80.2,
    85.7,
    58.6,
    99.8,
    42.7,
    nan,
    93.7,
    100.0,
    99.0,
    83.0,
    98.0,
    63.2,
    40.1,
    nan,
    99.0,
    99.0,
    74.8,
    nan,
    97.5,
    nan,
    98.0,
    90.0,
    99.0,
    70.6,
    nan,
    35.9,
    42.4,
    98.8,
    52.9,
    76.2,
    93.5,
    99.4,
    99.9,
    59.5,
    87.9,
    79.4,
    40.4,
    98.0,
    nan,
    95.4,
    98.6,
    87.9,
    99.0,
    nan,
    91.3,
    98.4,
    85.1,
    nan,
    99.0,
    97.9,
    83.5,
    97.0,
    66.4,
    99.8,
    87.4,
    84.8,
    57.5,
    82.6,
    100.0,
    99.6,
    100.0,
    94.5,
    nan,
    68.9,
    62.7,
    88.7,
    97.2,
    46.4,
    92.8,
    93.7,
    97.7,
    41.7,
    85.6,
    nan,
    92.2,
    89.0,
    99.1,
    99.0,
    97.8,
    97.0,
    51.7,
    47.8,
    84.0,
    nan,
    45.2,
    99.0,
    96.7,
    91.0,
    99.0,
    67.5,
    17.6,
    68.0,
    97.0,
    100.0,
    75.8,
    45.7,
    92.0,
    92.6,
    64.6,
    94.0,
    90.9,
    92.6,
    99.8,
    93.3,
    94.1,
    82.5,
    88.9,
    98.4,
    99.6,
    70.4,
    97.0,
    97.0,
    67.0,
    99.0,
    96.0,
    99.7,
    96.0,
    79.3,
    78.8,
    40.2,
    93.0,
    58.0,
    31.4,
    92.5,
    nan,
    99.7,
    nan,
    37.8,
    86.4,
    97.9,
    92.3,
    61.1,
    93.0,
    81.6,
    99.0,
    99.0,
    76.9,
    96.1,
    99.4,
    78.2,
    92.6,
    60.9,
    98.5,
    98.6,
    74.2,
    86.5,
    98.0,
    98.0,
    nan,
    69.9,
    99.7,
    77.9,
    99.0,
    97.0,
    98.0,
    99.3,
    53.0,
    93.4,
    90.3,
    nan,
    50.0,
    nan,
    nan,
    50.2,
    80.6,
    90.7,
]

if __name__ == "__main__":
    # Create scatter plot with GDP on the x-axis and number of phones on the y-axis
    sns.scatterplot(x=gdp, y=phones)

    # Show plot
    plt.show()

    # Change this scatter plot to have percent literate on the y-axis
    sns.scatterplot(x=gdp, y=percent_literate)

    # Show plot
    plt.show()
