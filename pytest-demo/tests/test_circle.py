import pytest
import math
import app.shapes as shapes

class TestCircle:

    def setup_method(self, method):
        print(f"setting up {method}")
        self.circle = shapes.Circle(5)

    def teardown_method(self, method):
        print(f"Tearing down{method}")
    
    def test_area(self):
        self.circle.area() == math.pi * self.circle.radius ** 2

    def test_perimeter(self):
        result = self.circle.perimeter()
        expected = 2 * math.pi * self.circle.radius

        assert result == expected