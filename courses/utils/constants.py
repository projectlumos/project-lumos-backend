# constants used in the courses app

# skill level constants
SKILL_BEGINNER = 'BG'
SKILL_INTERMEDIATE = 'IT'
SKILL_ADVANCED = 'AD'

# external link type constants
EXTERNAL_LINK_BLOG = 'BL'
EXTERNAL_LINK_TUTORIAL = 'TU'
EXTERNAL_LINK_COURSE = 'CO'

# Language choice
LANGUAGE_TECHNICAL_SKILLS = 'TS'
LANGUAGE_SOFT_SKILLS = 'SS'

# Domain choice
DOMAIN_TECHNICAL_SKILLS = 'TS'
DOMAIN_SOFT_SKILLS = 'SS'

# skill_level choices
skill_levels = (
    (SKILL_BEGINNER, 'BEGINNER'),
    (SKILL_INTERMEDIATE, 'INTERMEDIATE'),
    (SKILL_ADVANCED, 'ADVANCED')
)

# external_type choices
external_types = (
    (EXTERNAL_LINK_BLOG, 'BLOG'),
    (EXTERNAL_LINK_TUTORIAL, 'TUTORIAL'),
    (EXTERNAL_LINK_COURSE, 'COURSE')
)

# Language choices
language_for = (
    (LANGUAGE_TECHNICAL_SKILLS, 'TECHNICAL_SKILLS'),
    (LANGUAGE_SOFT_SKILLS, 'SOFT_SKILLS')
)

# domain choices
domain_for = (
    (DOMAIN_TECHNICAL_SKILLS, 'TECHNICAL_SKILLS'),
    (DOMAIN_SOFT_SKILLS, 'SOFT_SKILLS')
)
