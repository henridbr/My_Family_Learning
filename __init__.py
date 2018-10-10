# Copyright 2016 Mycroft AI, Inc.
#
# This file is part of Mycroft Core.
#
# Mycroft Core is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Mycroft Core is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Mycroft Core.  If not, see <http://www.gnu.org/licenses/>.

# Mycroft_family_learning
# 
# 
# 
# 
# 


# Mycroft libraries

from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill
from mycroft.util.log import getLogger
from mycroft import intent_handler

import requests
import json

__author__ = 'henridbr' # hd@uip

LOGGER = getLogger(__name__)


class FamilyLearningSkill(MycroftSkill):

    def __init__(self):
        super(FamilyLearningSkill, self).__init__(name="FamilyLearningSkill")
        
        
    @intent_handler(IntentBuilder("FamilyLearningIntent").require("FamilyLearningKeyword"))
    def handle_family_learning_intent(self, message):
        self.speak_dialog("save.it.memory")

##### Son
    @intent_handler(IntentBuilder("SonIntent").require("SonKeyword"))
    def handle_son_intent(self, message):

        with open("./opt/mycroft/skills/skill_family_learning.henridbr/familybook.json", "r") as read_file:
            family = json.load(read_file)
        #print(family)

        membersname = family['family_dictionary']['members']
        #print(membersname)    
        #print("members :",len(membersname)) 

        i=0
        while i< len(membersname):
            if (membersname[i]['rank']=="son"):
                name = membersname[i]['first_name']
#               print (i,name)
                self.speak_dialog('{} is my son'.format(name))
            i = i +1
        
        
##### Daughter
    @intent_handler(IntentBuilder("GrandDaughterIntent").require("DaughterKeyword"))
    def handledaughter_intent(self, message):

        with open("./opt/mycroft/skills/skill_family_learning.henridbr/familybook.json", "r") as read_file:
            family = json.load(read_file)
        #print(family)

        membersname = family['family_dictionary']['members']
        #print(membersname)    
        #print("members :",len(membersname)) 

        i=0
        while i< len(membersname):
            if (membersname[i]['rank']=="daughter"):
                name = membersname[i]['first_name']
#               print (i,name)
                self.speak_dialog('{} is my daughter'.format(name))
            i = i +1
        
        
##### Grand Son
    @intent_handler(IntentBuilder("GrandSonIntent").require("GrandSonKeyword"))
    def handle_grand_son_intent(self, message):

        with open("./opt/mycroft/skills/skill_family_learning.henridbr/familybook.json", "r") as read_file:
            family = json.load(read_file)
        #print(family)

        membersname = family['family_dictionary']['members']
        #print(membersname)    
        #print("members :",len(membersname)) 

        i=0
        while i< len(membersname):
            if (membersname[i]['rank']=="grand_son"):
                name = membersname[i]['first_name']
#               print (i,name)
                self.speak_dialog('{} is my grand-son'.format(name))
            i = i +1
        
##### Grand Daughter
    @intent_handler(IntentBuilder("GrandDaughterIntent").require("GrandDaughterKeyword"))
    def handle_grand_daughter_intent(self, message):

        with open("./opt/mycroft/skills/skill_family_learning.henridbr/familybook.json", "r") as read_file:
            family = json.load(read_file)
        #print(family)

        membersname = family['family_dictionary']['members']
        #print(membersname)    
        #print("members :",len(membersname)) 

        i=0
        while i< len(membersname):
            if (membersname[i]['rank']=="grand_daughter"):
                name = membersname[i]['first_name']
#               print (i,name)
                self.speak_dialog('{} is my grand-daughter'.format(name))
            i = i +1

##### Location
    @intent_handler(IntentBuilder("MemberLocationIntent").require("MemberLocationKeyword"))
    def handle_member_location_intent(self, message):

        with open("./opt/mycroft/skills/skill_family_learning.henridbr/familybook.json", "r") as read_file:
            family = json.load(read_file)
        #print(family)

        membersname = family['family_dictionary']['members']
        #print(membersname)    
        #print("members :",len(membersname)) 

        i=0
        while i< len(membersname):
            if (membersname[i]['rank']=="grand_daughter"):
                name = membersname[i]['first_name']
#               print (i,name)
                self.speak_dialog('{} is my grand-daughter'.format(name))
            i = i +1

    
    def stop(self):
        pass

def create_skill():
    return FamilyLearningSkill()
