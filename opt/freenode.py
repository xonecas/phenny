#!/usr/bin/env python
"""
freenode.py - Freenode Specific Stuff
Copyright 2008, Sean B. Palmer, inamidst.com
Licensed under the Eiffel Forum License 2.

http://inamidst.com/phenny/
"""

def replaced(phenny, input): 
   command = input.group(1)
   response = {
      'cp': '.cp has been replaced by .u', 
      'pc': '.pc has been replaced by .u', 
      'unicode': '.unicode has been replaced by .u', 
      'compare': '.compare has been replaced by .gcs (googlecounts)', 
      'map': 'the .map command has been removed; ask sbp for details', 
      'acronym': 'the .acronym command has been removed; ask sbp for details', 
      'img': 'the .img command has been removed; ask sbp for details', 
      'v': '.v has been replaced by .val', 
      'validate': '.validate has been replaced by .validate', 
      'thesaurus': ".thesaurus hasn't been ported to my new codebase yet", 
      'rate': ".rate hasn't been ported to my new codebase yet, sorry!", 
      'rates': ".rates hasn't been ported to my new codebase yet, sorry!"
   }[command]
   phenny.reply(response)
replaced.commands = [
   'cp', 'pc', 'unicode', 'compare', 'map', 'acronym', 'img', 
   'v', 'validate', 'thesaurus', 'rate', 'rates'
]
replaced.priority = 'low'

if __name__ == '__main__': 
   print __doc__.strip()
