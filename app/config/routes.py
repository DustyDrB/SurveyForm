"""
    Routes Configuration File

    Put Routing rules here
"""
from system.core.router import routes

routes['default_controller'] = 'Surveys'
routes['POST']['/survey'] = 'Surveys#process'
routes['GET']['/result'] = 'Surveys#result'
