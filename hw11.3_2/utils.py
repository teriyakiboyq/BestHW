import json

__data = []


def load_candidates_from_json(path):
    global __data
    with open('candidates.json', 'r', encoding='utf-8') as file:
        __data = json.load(file)
    return __data


def get_candidate(candidate_id):
    for candidate in __data:
        if candidate['id'] == candidate_id:
            return {
                'name': candidate['name'],
                'pos': candidate['position'],
                'picture': candidate['picture'],
                'skills': candidate['skills'],
            }
    return {'not_found': 'Отсутствует'}


def get_candidates_by_name(candidate_name):
    return [candidate for candidate in __data if candidate_name.lower() in candidate['name'].lower()]


def get_candidates_by_skill(skill_name):
    candidates = []
    for candidate in __data:
        skills = candidate['skills'].lower().split(', ')
        if skill_name.lower() in skills:
            candidates.append(candidate)
    return candidates
