import requests

url = 'http://127.0.0.1:8000/trading-formula'
data = [
    {
        "name": "test1",
        "formula": "Fee = \\text{TradeAmount} \\times \\text{BrokerageRate} + \\text{FixedCharge}",
        "variables": {
            "TradeAmount": 10000.0,
            "BrokerageRate": 0.0025,
            "FixedCharge": 10.0
        },
        "type": "compute"
    },
    {
        "name": "test2",
        "formula": "Fee = \\max(\\text{TradeAmount} \\times \\text{BrokerageRate}, \\text{MinimumFee})",
        "variables": {
            "TradeAmount": 1000.0,
            "BrokerageRate": 0.003,
            "MinimumFee": 15.0
        },
        "type": "compute"
    },
    {
        "name": "test3",
        "formula": "Fee = \\frac{\\text{TradeAmount} - \\text{Discount}}{\\text{ConversionRate}}",
        "variables": {
            "TradeAmount": 11300.0,
            "Discount": 500.0,
            "ConversionRate": 1.2
        },
        "type": "compute"
    },
    # Add other test cases here as needed
    {
        "name": "test15",
        "formula": "$$E[R_i] = R_f + \\beta_i (E[R_m] - R_f)$$",
        "variables": {"R_f": 0.02, "beta_i": 1.2, "E_R_m": 0.08},
        "type": "compute"
    },
    {
        "name": "test16",
        "formula": "$$VaR = Z_\\alpha \\cdot \\sigma_p \\cdot V$$",
        "variables": {"Z_alpha": 1.65, "sigma_p": 0.15, "V": 100000.0},
        "type": "compute"
    },
    {
        "name": "test17",
        "formula": "$$SR = \\frac{E[R_p]-R_f}{\\sigma_p}$$",
        "variables": {"E_R_p": 0.1, "R_f": 0.02, "sigma_p": 0.15},
        "type": "compute"
    },
]

response = requests.post(url, json=data)
print(response.json())
