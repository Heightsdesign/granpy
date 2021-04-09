"""This file handles wikipedia requests and data"""
import wikipedia

eiffel_tower = wikipedia.summary("Tour Eiffel", sentences=2)

print(eiffel_tower)