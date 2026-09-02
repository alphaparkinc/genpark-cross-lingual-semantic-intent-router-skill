from client import CrossLingualSemanticIntentRouterClient

def main():
    client = CrossLingualSemanticIntentRouterClient()
    res = client.route_user_query('Comment mettre a jour mon adresse de livraison?')
    print('Cross-Lingual Intent Router: ' + res['intent_routing_id'] + ' (' + res['detected_source_language_iso'] + ')')
    print('Intent: ' + res['predicted_canonical_intent'] + ' (Score: ' + str(res['intent_confidence_score']) + ')')
    print('Normalized: ' + res['english_normalized_representation'])
    print('Queue: ' + res['target_agent_specialist_queue'])
    print('Telemetry URL: ' + res['routing_decision_telemetry_url'])

if __name__ == '__main__':
    main()
