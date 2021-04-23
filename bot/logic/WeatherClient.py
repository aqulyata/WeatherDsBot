from pyowm import OWM


class WeatherClient:
    def __init__(self, token="0daf1e3463914472f26d510ae197bd02"):
        self.token = token
        self.client = None

    def get_observation(self, place):
        if self.client is None:
            owm = OWM(self.token)
            self.client = owm.weather_manager()
        observation = self.client.weather_at_place(place)

        return observation

    def get_detailed_status(self, place):
        observation = self.get_observation(place)
        w = observation.weather
        return w.detailed_status

    def get_humidity(self, place):
        observation = self.get_observation(place)
        w = observation.weather
        return w.humidity

    def get_temperature(self, place):
        observation = self.get_observation(place)
        w = observation.weather
        return w.temperature('celsius')["temp"]

    def get_reference(self, place):
        observation = self.get_observation(place)
        w = observation.weather
        return w.reference_time("iso")


    def get_pressure(self, place):
        observation = self.get_observation(place)
        w = observation.weather
        return w.pressure["press"]
