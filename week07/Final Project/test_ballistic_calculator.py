import pytest
import ballistic_calculator as bc

class TestBallisticCalculator:
    """Test class for BallisticCalculator."""

    @pytest.fixture
    def calculator(self):
        """calculator method to create a BallisticCalculator instance."""
        return bc.BallisticCalculator()
    
    def test_get_distance_feet(self, calculator):
        """Test the get_distance_feet method."""
        assert calculator.get_distance_feet(100) == pytest.approx(300)
        assert calculator.get_distance_feet(200) == pytest.approx(600)
        assert calculator.get_distance_feet(300) == pytest.approx(900)
        assert calculator.get_distance_feet(500) == pytest.approx(1500)
        assert calculator.get_distance_feet(800) == pytest.approx(2400)

    def test_get_wind_speed_fps(self, calculator):
        """Test the get_wind_speed_fps method."""
        assert calculator.get_wind_speed_fps(3) == pytest.approx(4.4, .1)
        assert calculator.get_wind_speed_fps(5) == pytest.approx(7.3, .1)
        assert calculator.get_wind_speed_fps(10) == pytest.approx(14.7, .1)
        assert calculator.get_wind_speed_fps(15) == pytest.approx(22.0, .1)
        assert calculator.get_wind_speed_fps(20) == pytest.approx(29.3, .1)
        
    def test_get_weight_lbs(self, calculator):
        """Test the get_weight_lbs method."""
        assert round(calculator.get_weight_lbs(25), 5) == pytest.approx(0.00357, .00001)
        assert round(calculator.get_weight_lbs(95), 5) == pytest.approx(0.01357, .00001)
        assert round(calculator.get_weight_lbs(115), 5) == pytest.approx(0.01643, .00001)
        assert round(calculator.get_weight_lbs(150), 5) == pytest.approx(0.02143, .00001)
        assert round(calculator.get_weight_lbs(175), 5) == pytest.approx(0.02500, .00001)

    def test_get_drag_factor(self, calculator):
        """Test the get_drag_factor method."""
        assert round(calculator.get_drag_factor(0.45), 3) == pytest.approx(0.001, .001)
        assert round(calculator.get_drag_factor(0.55), 4) == pytest.approx(0.0009, .0001)
        assert round(calculator.get_drag_factor(0.65), 4) == pytest.approx(0.0008, .0001)
        assert round(calculator.get_drag_factor(0.75), 4) == pytest.approx(0.0007, .0001)
        assert round(calculator.get_drag_factor(0.95), 4) == pytest.approx(0.0005, .0001)

    def test_velocity_at_target(self, calculator):
        """Test the velocity_at_target method."""

        assert round(calculator.get_velocity_at_target(3000, 300, 0.001), 5) == pytest.approx(2222.45466, .00001)
        assert round(calculator.get_velocity_at_target(2800, 500, 0.001), 5) == pytest.approx(1698.28585, .00001)
        assert round(calculator.get_velocity_at_target(2150, 300, 0.007), 5) == pytest.approx(263.28132, .00001)
        assert round(calculator.get_velocity_at_target(3200, 100, 0.001), 5) == pytest.approx(2895.47974, .00001)
        assert round(calculator.get_velocity_at_target(2700, 200, 0.009), 5) == pytest.approx(446.30700, .00001)

    def test_get_flight_time(self, calculator):
        """Test the get_flight_time method."""
        
        assert round(calculator.get_flight_time(300, 3000, 2222.454662045154), 5) == pytest.approx(0.11489, .00001)
        assert round(calculator.get_flight_time(500, 2800, 1698.2858471953737), 5) == pytest.approx(0.22231, .00001)
        assert round(calculator.get_flight_time(300, 2150, 263.2813207439111), 5) == pytest.approx(0.24862, .00001)
        assert round(calculator.get_flight_time(100, 3200, 2895.4797377150703), 5) == pytest.approx(0.03281, .00001)
        assert round(calculator.get_flight_time(200, 2700, 446.30699819828374), 5) == pytest.approx(0.12713, .00001)               
       
    def test_bullet_drop(self, calculator):

        assert calculator.get_bullet_drop(0.11488850336233179, 1.5) == pytest.approx(1.04806, .00001)
        assert calculator.get_bullet_drop(0.22230690400066236, 1.75) == pytest.approx(7.79030, .00001)
        assert calculator.get_bullet_drop(0.2486241429221545, 1.25) == pytest.approx(10.68281, .00001)
        assert calculator.get_bullet_drop(0.03281119921743375, 2) == pytest.approx(-1.79217, .00001)
        assert calculator.get_bullet_drop(0.1271331755702981, 1.5) == pytest.approx(1.62014, .00001)

    def test_get_wind_drift(self, calculator):
        """Test the get_wind_drift method."""

        assert calculator.get_wind_drift(4.4, 10, 0.11488850336233179) == pytest.approx(1.05337, .00001)
        assert calculator.get_wind_drift(7.3, 15, 0.22230690400066236) == pytest.approx(5.04026, .00001)
        assert calculator.get_wind_drift(14.7, 20, 0.2486241429221545) == pytest.approx(15.00008, .00001)
        assert calculator.get_wind_drift(22.0, 25, 0.03281119921743375) == pytest.approx(3.66079, .00001)
        assert calculator.get_wind_drift(29.3, 30, 0.1271331755702981) == pytest.approx(22.35001, .00001)

    def test_get_muzzle_energy(self, calculator):
        """Test the get_muzzle_energy method."""

        assert calculator.get_muzzle_energy(3000, 0.00357) == pytest.approx(499.31622, .00001)
        assert calculator.get_muzzle_energy(2800, 0.01357) == pytest.approx(1653.33499, .00001)
        assert calculator.get_muzzle_energy(2150, 0.01643) == pytest.approx(1180.26473, .00001)
        assert calculator.get_muzzle_energy(3200, 0.02143) == pytest.approx(3410.25673, .00001)
        assert calculator.get_muzzle_energy(2700, 0.02500) == pytest.approx(2832.25586, .00001)

    def test_get_target_energy(self, calculator):
        """Test the get_target_energy method."""

        assert calculator.get_target_energy(2222.454662045154, 0.00357) == pytest.approx(274.030551, .00001)
        assert calculator.get_target_energy(1698.2858471953737, 0.01357) == pytest.approx(608.22795, .00001)   
        assert calculator.get_target_energy(263.2813207439111, 0.01643) == pytest.approx(17.69875, .00001)
        assert calculator.get_target_energy(2895.4797377150703, 0.02143) == pytest.approx(2792.08206, .00001)
        assert calculator.get_target_energy(446.30699819828374, 0.02500) == pytest.approx(77.38777, .00001)

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])

