import numpy as np
import json

class Insight:
    
    @staticmethod
    def personality_distance(insight_u, insight_v):
        weights = [0.5, 0.3, 0.2]

        data_u = open(insight_u)
        data_v = open(insight_v)
        
        json_u = json.load(data_u)
        json_v = json.load(data_v)
        
        tree_u = json_u['tree']['children']
        tree_v = json_v['tree']['children']

        personality_u = tree_u[0]['children'][0]['children']
        consumer_needs_u = tree_u[1]['children'][0]['children']
        values_u = tree_u[2]['children'][0]['children']

        personality_v = tree_v[0]['children'][0]['children']
        consumer_needs_v = tree_v[1]['children'][0]['children']
        values_v = tree_v[2]['children'][0]['children']

        personality_vector_u = np.array([i['percentage'] for i in personality_u])
        consumer_needs_vector_u = np.array([i['percentage'] for i in consumer_needs_u])
        values_vevtor_u = np.array([i['percentage'] for i in values_u])

        personality_vector_v = np.array([i['percentage'] for i in personality_v])
        consumer_needs_vector_v = np.array([i['percentage'] for i in consumer_needs_v])
        values_vevtor_v = np.array([i['percentage'] for i in values_v])

        personality_dist = np.linalg.norm(personality_vector_u-personality_vector_v)
        consumer_needs_dist = np.linalg.norm(consumer_needs_vector_u-consumer_needs_vector_v)
        values_dist = np.linalg.norm(values_vevtor_u-values_vevtor_v)

        factors = np.array([personality_dist, consumer_needs_dist, values_dist])
        weighted_distance = sum(np.multiply(factors, weights))

        return weighted_distance