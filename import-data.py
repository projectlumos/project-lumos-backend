import csv,sys,os

project_dir = "/Users/JAI MATA DI/Desktop/Related_Resource/project-lumos-backend/backend"
sys.path.append(project_dir)
os.environ['DJANGO_SETTINGS_MODULE']='settings.development'

import django
django.setup() 	

from courses.models import Language,Domain,SoftSkills,SoftSkillsData,KnowledgeBase,RandomData

language_data = csv.reader(open("/Users/JAI MATA DI/Desktop/Related_Resource/project-lumos-backend/Language.csv"),delimiter=",")
domain_data = csv.reader(open("/Users/JAI MATA DI/Desktop/Related_Resource/project-lumos-backend/Domain.csv"),delimiter=",")
softskills_data = csv.reader(open("/Users/JAI MATA DI/Desktop/Related_Resource/project-lumos-backend/Soft Skills.csv",encoding="UTF-8"),delimiter=",")
softskillsdata_data = csv.reader(open("/Users/JAI MATA DI/Desktop/Related_Resource/project-lumos-backend/Soft Skills Data.csv",encoding="UTF-8"),delimiter=",")
knowledge_base_data = csv.reader(open("/Users/JAI MATA DI/Desktop/Related_Resource/project-lumos-backend/KnowledgeBase.csv",encoding="UTF-8"),delimiter=",")
random_data = csv.reader(open("/Users/JAI MATA DI/Desktop/Related_Resource/project-lumos-backend/Random Data.csv",encoding="UTF-8"),delimiter=",")
knowledgebase_header = next(knowledge_base_data)
softskillsdata_header = next(softskillsdata_data)

# for row in language_data:
# 	Language.objects.create(language_name=row[0],site_url=row[1],description=row[2],icon=row[3])

# for row in domain_data:
# 	Domain.objects.create(domain_name=row[0],description=row[1],icon=row[2])

# for row in softskills_data:
# 	SoftSkills.objects.create(soft_skill_category=row[0],description=row[1],icon=row[2])

# for row in softskillsdata_data:
# 	softskillsdata_resource = SoftSkillsData(is_active=row[0],title=row[2],description=row[3],
# 										link_url=row[4],data_type=row[5],paid=row[6])
# 	softskillsdata_resource.save()
# 	soft_skill = SoftSkills.objects.filter(soft_skill_category=row[1])
# 	for soft_skills in soft_skill:
# 		softskillsdata_resource.soft_skill.add(soft_skills)

for row in knowledge_base_data:
	# q=KnowledgeBase.objects.get_or_create(is_active=row[0],title=row[1],description=row[2],
	# 							skill_level=row[3],data_type=row[4],link_url=row[7],paid=row[8],project=row[9])
	knowledgebase_resource = KnowledgeBase(is_active=row[0],title=row[1],description=row[2],skill_level=row[3],
											data_type=row[4],link_url=row[7],paid=row[8],project=row[9])
	knowledgebase_resource.save()

	languages = Language.objects.filter(language_name = row[5])
	domains = Domain.objects.filter(domain_name = row[6])
	for language in languages:
		knowledgebase_resource.languages.add(language)
	for domain in domains:
		knowledgebase_resource.domains.add(domain)



# for row in random_data:
# 	RandomData.objects.create(is_active=row[0],title=row[1],description=row[2],
# 							link_url=row[3],data_type=row[4],paid=row[5])
