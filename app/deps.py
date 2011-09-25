'''
Dependency module - contains a simple class for loading the CSS and JS
dependencies on every page based on URL patterns.

@author: This file was originally written by Alexis Michael
'''

import re

class ScriptDeps(object):
    
    def __init__(self):
        self.deps = {}
        
    def registerDep(self, dep):
        '''
        Registers a dependency object. Dependency objects are of the form (id, dir, [deps]). 
        An example of a dependency object:
            css_deps = ("css", "css",
                [
                    ("/login", ["auth"]),
                    ("/signup", ["auth", "facebox"]),
                ])
        Here we are registering a dependency with ID 'css', that can be found in the 'css' dir 
        in the 'static' folder. 'auth' is a dependency for the login page etc. The module takes 
        care of creating the full path and appending the correct extension to the file.
        '''
        type, base_dir, url_script_pairs = dep
        _scripts = []
        for url, scripts in url_script_pairs:
            paths = []
            for script in scripts:
                path = base_dir + "/" + script 
                if "https" in script or "http" in script:
                    path = script
                paths.append(path)
            _scripts.append((re.compile(url), paths))
            paths = []
        self.deps.setdefault(type, []).extend(_scripts)
        return self
    
    def get(self, id, url):
        '''
        Gets a dependency with a given id - the first matched url pattern is returned.
        '''
        for pattern, scripts in self.deps.get(id, []):
            if pattern.match(url):
                return scripts
        return []
