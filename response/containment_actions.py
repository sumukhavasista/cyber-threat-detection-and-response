# containment_actions.py

def perform_containment_action(action_type, details):
    print(f"[CONTAINMENT] Performing '{action_type}' action with details: {details}")

    # Simulated containment logic
    if action_type == "isolate_system":
        print(f"[SIMULATION] System '{details}' is now isolated from the network.")
    
    elif action_type == "terminate_process":
        print(f"[SIMULATION] Process '{details}' has been terminated.")
    
    elif action_type == "block_ip":
        print(f"[SIMULATION] IP address '{details}' has been blocked.")
    
    elif action_type == "restrict_user":
        print(f"[SIMULATION] User account '{details}' access has been restricted.")
    
    else:
        print(f"[WARNING] Unknown containment action: {action_type}. No action taken.")
