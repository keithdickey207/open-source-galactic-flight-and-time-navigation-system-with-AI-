#!/usr/bin/env python3
"""
Galactic Flight and Time Navigation System with AI
Sovereign Local-First Implementation
Keith Alan Dickey - Waterville Software Development Services (WSDS)
04901 Studio - Maine Emergency Contractors
"""

import math
import time
import sys

try:
    import ollama
except ImportError:
    print("[!] Critical Failure: Local AI dependency missing.")
    print("    Resolve via: pip install ollama")
    sys.exit(1)

class GalacticNavSystem:
    def __init__(self, ai_model="llama3.2"):
        self.ai_model = ai_model
        self.current_telemetry = {
            "x": 0.0, 
            "y": 0.0, 
            "z": 0.0, 
            "t_flux": time.time()
        }
        print(f"[*] Navigation Core Initialized. AI Engine: {self.ai_model} (Air-gapped)")
        print("[*] Sovereign Operator: Keith Alan Dickey - 04901 Studio")

    def calculate_jump_vector(self, target_coords):
        """Calculates Euclidean distance and temporal variance for the jump."""
        print(f"[*] Calculating trajectory to {target_coords}...")
        spatial_distance = math.sqrt(
            (target_coords['x'] - self.current_telemetry['x'])**2 +
            (target_coords['y'] - self.current_telemetry['y'])**2 +
            (target_coords['z'] - self.current_telemetry['z'])**2
        )
        temporal_delta = target_coords.get('t_flux', time.time()) - self.current_telemetry['t_flux']
        return {
            "distance": round(spatial_distance, 4),
            "t_delta": round(temporal_delta, 4)
        }

    def consult_onboard_ai(self, query):
        """Processes navigation queries through the local LLM."""
        print(f"\n[*] Bridging query to local {self.ai_model} instance...")
        try:
            response = ollama.chat(model=self.ai_model, messages=[
                {
                    'role': 'system',
                    'content': 'You are the onboard AI for Keith Dickey\'s sovereign, air-gapped galactic navigation system. Provide highly technical, concise trajectory and temporal shielding directives aligned with local-first principles.'
                },
                {
                    'role': 'user',
                    'content': query
                }
            ])
            return response['message']['content']
        except Exception as e:
            return f"[!] AI Core communication failure: {str(e)}"

if __name__ == "__main__":
    nav = GalacticNavSystem(ai_model="llama3.2")
    
    target_vector = {
        "x": 1045.8, 
        "y": -332.1, 
        "z": 890.5, 
        "t_flux": time.time() + 86400
    }
    
    telemetry = nav.calculate_jump_vector(target_vector)
    print(f"[+] Trajectory Locked. Spatial Jump: {telemetry['distance']} units. Temporal Shift: {telemetry['t_delta']}s.")
    
    scenario_query = (
        f"We are initiating a jump spanning {telemetry['distance']} spatial units "
        f"with a {telemetry['t_delta']} second temporal shift. Recommend power distribution "
        f"for the deflector arrays and local network shielding."
    )
    
    ai_directive = nav.consult_onboard_ai(scenario_query)
    
    print("\n--- AI DIRECTIVE ---")
    print(ai_directive)
    print("--------------------\n")
    print("[*] Ready for push to master. Sovereign Operator: Keith Alan Dickey")
