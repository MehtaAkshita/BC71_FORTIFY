import face_recognition
from PIL import Image
import numpy as np
import os
from models import Face
import pickle


def load_faces():
    global all_faces, known_faces, known_faces_id
    all_faces = Face.query.all()
    known_faces = [pickle.loads(face.face_encoding) for face in all_faces]
    known_faces_id = [face.user.id for face in all_faces]

load_faces()


def give_match(image_vector):
    face_locations = face_recognition.face_locations(image_vector)
    unknown_faces = face_recognition.face_encodings(image_vector, face_locations)
    people_found = []
    for face in unknown_faces:
        face_distances = face_recognition.face_distance(known_faces, face)
        face_distances = ['{0:.2f}'.format((1-x) * 100) for x in face_distances]
        if face_distances:
            max_index = face_distances.index(max(face_distances))
            max_match_person = known_faces_id[max_index]
            people_found.append(max_match_person)
    return face_locations, people_found
