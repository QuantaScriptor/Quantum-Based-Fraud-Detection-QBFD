
import unittest
import numpy as np
import pandas as pd
from qbfd import QuantumFraudDetection

class TestQBFD(unittest.TestCase):
    def setUp(self):
        self.transactions = pd.DataFrame({
            'amount': [100, 200, 300, 400, 500],
            'location': [1, 2, 3, 4, 5],
            'merchant': [1, 1, 2, 2, 3],
            'time': [1, 2, 3, 4, 5]
        }, index=pd.date_range(start='2022-01-01', periods=5))
        self.qbfd = QuantumFraudDetection(self.transactions)

    def test_detect_fraud(self):
        result = self.qbfd.detect_fraud()
        self.assertIsNotNone(result)

if __name__ == '__main__':
    unittest.main()
