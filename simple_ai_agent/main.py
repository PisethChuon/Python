class TemperatureAgent:
    def __init__(self, desired_temp):
        self.desired_temp = desired_temp

    def perceive(self, current_temp):
        if current_temp < self.desired_temp - 2:
            return "Turn on heater"
        elif current_temp > self.desired_temp + 2:
            return "Turn on AC"
        else:
            return "Do nothing"
            
    def act(self, action):
        print(f"Action taken: {action}")

# --- Simulation ---
agent = TemperatureAgent(desired_temp=24)  # 24°C is our comfy goal

current_temp = 26  # pretend this is from a sensor
action = agent.perceive(current_temp)
agent.act(action)