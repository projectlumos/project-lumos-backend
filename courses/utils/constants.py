#constants used in the courses app

#skill level constants
SKILL_BEGINNER = 'BG'
SKILL_INTERMEDIATE = 'IT'
SKILL_ADVANCED = 'AD'
#external link type constants
EXTERNAL_LINK_BLOG = 'BL'
EXTERNAL_LINK_TUTORIAL = 'TU'
EXTERNAL_LINK_COURSE = 'CO'

#skill_level choices
skill_levels = (
    (SKILL_BEGINNER, 'BEGINNER'),
    (SKILL_INTERMEDIATE, 'INTERMEDIATE'),
    (SKILL_ADVANCED, 'ADVANCED')
)

#external_type choices
external_types = (     #indicate which type of external link
    (EXTERNAL_LINK_BLOG, 'BLOG'),
    (EXTERNAL_LINK_TUTORIAL, 'TUTORIAL'),
    (EXTERNAL_LINK_COURSE, 'COURSE')
)
